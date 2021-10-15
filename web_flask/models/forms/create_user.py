from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms import PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired
from wtforms.validators import Length
from wtforms.validators import Email

class CreateUser(FlaskForm):
    Username = StringField('Nombre de Usuario Para Ingreso', validators=[InputRequired(), Length(min=4, max=30)])
    Email = StringField('Email', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    Nombre = StringField('Nombre de Usuario', validators=[InputRequired(), Length(min=4, max=30)])
    Apellido = StringField('Apellido de Usuario', validators=[InputRequired(), Length(min=4, max=30)])
    Password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=5, max=80)])
    Confirmed_Password = PasswordField('Confirmar Contraseña', validators=[InputRequired(), Length(min=5, max=80)])
    Area = SelectField(
        'Area del Nuevo Usuario',
        choices=[
            ('Seleccionar', 'Seleccionar'),
            ('Recursos Humanos', 'Recursos Humanos'),
            ('Marketing', 'Marketing'),
            ('Gerencia', 'Gerencia'),
            ('Logistica', 'Logistica'),
            ('Sistemas', 'Sistemas'),
            ('Otros', 'Otros'),
        ], validators=[InputRequired()]
    )
    Rol = SelectField(
        'Seleccion El Rol Del Usuario',
        choices=[
            ('Seleccionar', 'Seleccionar'),
            ('Usuario', 'Usuario'),
            ('Administrador', 'Administrador'),
            ('HelpDesk', 'HelpDesk'),
        ], validators=[InputRequired()]
    )
    Desde = DateField('Fecha de Inicio', format='%Y-%m-%d')
    Hasta = DateField('Fecha Fin', format='%Y-%m-%d')