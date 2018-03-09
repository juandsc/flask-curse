''' Implementation of forms in Python.'''

from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class CommentForm(Form):
    username = StringField('username',
        [
            validators.Required(message='El username es requerido!'),
            validators.length(min=4, max=25, message='Ingrese un username valido!')
        ])
    email = EmailField('e-mail',
        [
            validators.Required(message='El email es requerido!'),
            validators.Email(message='Ingrese un email valido!')
        ])
    comment = TextField('comment')
