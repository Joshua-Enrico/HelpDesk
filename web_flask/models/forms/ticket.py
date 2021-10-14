from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms.validators import InputRequired
from wtforms.validators import Length

class TicketForm(FlaskForm):
    subject = StringField('Asunto', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Descripcion', validators=[InputRequired(), Length(max=1000)])
    problemType = SelectField(
        'Tipo de Problema',
        choices=[
            ('Hardware', 'Hardware'),
            ('Software', 'Software'),
        ], validators=[InputRequired()]
    )
    company_area = SelectField(
        'Seleccione su Area',
        choices=[
            ('Recursos Humanos', 'Recursos Humanos'),
            ('Marketing', 'Marketing'),
            ('Gerencia', 'Gerencia'),
        ], validators=[InputRequired()]
    )