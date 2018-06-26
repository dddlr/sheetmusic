from app.models import Instrument, Style
from sqlalchemy import exc

class RowExistsError(ValueError):
    """Exception raised when a row in the database already exists."""

    def __init__(self, message):
        self.message = message

def check_instrument(name, info=None, range=None, image=None):
    """Checks if style is valid according to the database models."""
    too_long = []
    if Instrument.query.filter_by(name=name).scalar() is not None:
        raise RowExistsError("Instrument already exists.")
    if len(name) > 32:
        too_long.append('name')
    if len(info) > 200:
        too_long.append('info')
    if len(range) > 100:
        too_long.append('range')
    if len(image) > 100:
        too_long.append('image URL')
    if len(too_long) > 0:
        raise ValueError("The following instrument information is too long: " +
            ', '.join(too_long))

    elif not name:
        raise ValueError("Name of instrument cannot be empty.")
    return True

def check_music():
    return True
