from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AddStyleForm(FlaskForm):
    style = StringField('Style name', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Submit')
