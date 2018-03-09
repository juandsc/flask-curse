''' Example of sending and validation parameters with form.  '''
from flask import Flask
from flask import render_template as rt
from flask import request
import forms

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    my_comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and my_comment_form.validate():
        print('Username: {}\nE-mail: {}\nComment: {}'.format(my_comment_form.username.data,
            my_comment_form.email.data, my_comment_form.comment.data))
    my_title = 'Flask Curse'
    return rt('index_form.html', title=my_title, comment_form=my_comment_form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
