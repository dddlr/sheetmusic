import datetime
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SelectMultipleField, StringField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length,Optional, ValidationError
from app.models import Instrument, Style

class AddInstrumentForm(FlaskForm):
    """Form used to add a new instrument, long with validators used to check
    data."""
    name = StringField('Instrument name', validators=[DataRequired(), Length(max=32)])
    info = StringField('Info', validators=[Length(max=200)])
    range = StringField('Range', validators=[Length(max=100)])
    image = StringField('Image', validators=[Length(max=100)])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        name_query = Instrument.query.filter_by(name=name.data).first()
        if name_query is not None:
            raise ValidationError("This instrument already exists.")

class AddStyleForm(FlaskForm):
    """Form used to add a new style, along with validators used to check
    data."""
    style = StringField('Style name', validators=[DataRequired(), Length(max=32)])
    description = StringField('Description', validators=[Length(max=200)])
    submit = SubmitField('Submit')

    def validate_style(self, style):
        # Overload existing validate_style with own validator
        if Style.query.get(style.data) is not None:
            raise ValidationError("This style already exists.")

class AddOriginalAuthorForm(FlaskForm):
    """Form used for the original author of different pieces of music, e.g. if
    a song was arranged by another person later on."""
    name = StringField('Name', validators=[Length(max=32)])
    country = StringField('Country', validators=[Length(max=20)])
    dob = DateField('Date of birth', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Submit')

class AddMusicForm(FlaskForm):
    """Form used to add a new piece of music."""
    name = StringField('Music name', validators=[DataRequired(), Length(max=32)])
    year = IntegerField('Year', validators=[Length(max=4)])
    url = StringField('URL-friendly name', validators=[DataRequired(), Length(max=32)])
    sheet_url = StringField('URL of sheet music', validators=[Length(max=32)])
    style = SelectField('Style', coerce=str)
    original_author = SelectField('Original author', coerce=int)
    instruments = SelectMultipleField('Instruments', coerce=int)
    submit = SubmitField('Submit')
