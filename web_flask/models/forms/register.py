from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import InputRequired
from wtforms.validators import Email
from wtforms.validators import Length

class RegisterForm(FlaskForm):
    email = StringField('Correo', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    username = StringField('Nombre de Usuario', validators=[InputRequired(), Length(min=4, max=15)])
    nombre = StringField('Nombre', validators=[InputRequired(), Length( max=15)])
    apellido = StringField('Apellido', validators=[InputRequired(), Length( max=15)])
    user_id = StringField('Id personal', validators=[InputRequired(), Length(min=3, max=3)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=6, max=80)])
