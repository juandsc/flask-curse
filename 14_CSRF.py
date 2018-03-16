''' Example of add login form. '''
from flask import Flask
from flask import render_template as rt
from flask import request
from flask_wtf import CsrfProtect
import forms

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    my_title = 'Flask Curse'
    login_form = forms.LoginForm()
    return rt('login.html', form=login_form, title=my_title)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
