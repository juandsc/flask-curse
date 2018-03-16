''' Example of own validations. '''
from flask import Flask
from flask import render_template as rt
from flask import request
import forms

app = Flask(__name__)

@app.route('/')
def index():
    my_title = 'Flask Curse'
    return rt('index_form.html', title=my_title)


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    my_comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and my_comment_form.validate():
        print('Username: {}\nE-mail: {}\nComment: {}'.format(
            my_comment_form.username.data, my_comment_form.email.data,
            my_comment_form.comment.data))
    else:
        print('Error en el formulario.')
    my_title = 'Flask Curse'
    return rt('comment.html', title=my_title, comment_form=my_comment_form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
