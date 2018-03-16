''' Example of forms implementation with Flask.  '''
from flask import Flask
from flask import render_template as rt
import forms

app = Flask(__name__)

@app.route('/')
def index():
    my_title = 'Flask Curse'
    return rt('index_form.html', title=my_title)


@app.route('/comment')
def comment():
    my_comment_form = forms.CommentForm()
    my_title = 'Flask Curse'
    return rt('comment.html', title=my_title, comment_form=my_comment_form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
