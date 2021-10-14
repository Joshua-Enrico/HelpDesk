from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from wtforms.validators import Length

class CreateID(FlaskForm):
    user_id = StringField('ID de usuario', validators=[InputRequired(), Length(min=3, max=3)])
    admin = StringField('Tipo De Usuario', validators=[InputRequired(), Length(min=3, max=3)])