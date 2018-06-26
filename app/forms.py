from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Instrument, Style

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

class AddInstrumentForm(FlaskForm):
    """Form used to add a new instrument, long with validators used to check
    data."""
    pass
