from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import InputRequired
from wtforms.validators import Email
from wtforms.validators import Email

class recover(FlaskForm):
    email = StringField('', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    new_password = PasswordField('', validators=[InputRequired(), Length(min=6, max=80)])
