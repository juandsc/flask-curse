''' Implementation of forms in Python.'''

from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms import PasswordField
from wtforms import validators

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

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
    honey_pot = HiddenField('', [length_honeypot])


class LoginForm(Form):
    username = StringField('Username',
        [
            validators.Required(message='El username es requerido!'),
            validators.length(min=4, max=25, message='Ingrese un username valido!')
        ])
    password = PasswordField('Password',
        [
            validators.Required(message='El password es requerido')
        ])
