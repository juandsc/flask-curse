''' Implementation of forms in Python.'''

from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField


class CommentForm(Form):
    username = StringField('username')
    email = EmailField('e-mail')
    comment = TextField('comment')
