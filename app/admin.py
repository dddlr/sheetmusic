from flask import Blueprint, render_template, request
from sqlalchemy import exc
from app import db
from app.models import Instrument, Style
from app.validate import check_instrument, check_style, RowExistsError

bp = Blueprint('admin', __name__)

@bp.route('/admin/style/', methods=['GET', 'POST'])
def add_style():
    """Renders the page for adding a style/genre, as well as handling the
    addition of a style into the database."""
    error = False
    status = None
    if request.method == 'POST':
        try:
            name = request.form['style']
            description = request.form['description']
            check_style(name, description)
            style = Style(style=name, description=description)
            db.session.add(style)
            db.session.commit()
        except exc.IntegrityError as err:
            error = True
            print('/admin/style/:', err)
            status = "Something went wrong. Please try again."
        except ValueError as err:
            # Covers ValueError and RowExistsError
            error = True
            status = err
        except Exception as err:
            error = True
            print("Unexpected error:", err)
            status = "Something went wrong. Please try again."
        else:
            status = "Added successfully."
    return render_template('admin_style.html', title="Admin", status=status, error=error)

@bp.route('/admin/instrument/', methods=['GET', 'POST'])
def add_instrument():
    """Renders the page for adding an instrument, as well as handling the
    addition of an instrument into the database."""
    error = False
    status = None
    if request.method == 'POST':
        try:
            print('qqqq')
            name = request.form['name']
            info = request.form['info']
            range = request.form['range']
            image = request.form['image']
            check_instrument(name, info, range, image)
            print('eeee')
            instrument = Instrument(name=name, info=info, range=range, image=image)
            print('aaaa')
            db.session.add(instrument)
            db.session.commit()
        except exc.IntegrityError as err:
            error = True
            print('/admin/instrument/:', err)
            status = "Something went wrong. Please try again."
        except ValueError as err:
            error = True
            status = err
        except Exception as err:
            error = True
            print("Unexpected error:", err)
            status = "Something went wrong. Please try again."
        else:
            status = "Added successfully."
        finally:
            print(status)
            print(error)
    return render_template('admin_instrument.html', title="Admin", status=status, error=error)

@bp.route('/admin/music/', methods=['GET', 'POST'])
def add_music():
    return render_template('admin_music.html', title="Admin", error=error)
