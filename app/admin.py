from flask import Blueprint, render_template, request
from app import db
from app.models import Instrument, Style
from app.validate import check_instrument, check_style

bp = Blueprint('admin', __name__)

@bp.route('/admin/style/', methods=['GET', 'POST'])
def add_style():
    if request.method == 'POST':
        error = False
        status = None
        try:
            name = request.form['style']
            description = request.form['description']
            print('eee')
            if check_style(name, description):
                print('aaa')
                style = Style(style=name, description=description)
                # TODO: figure out why no error is being returned when name
                # equals null
                db.session.add(style)
                db.session.commit()
                print('bbb')
                status = "Added successfully."
            else:
                # should never happen
                error = True
                status = "Something went wrong. Please try again."
        except:
            error = True
            status = "something went wrong"
        finally:
            print('status is', status)
            return render_template('admin_style.html', title="Admin", status=status, error=error)
    return render_template('admin_style.html', title="Admin")

@bp.route('/admin/instrument/', methods=['GET', 'POST'])
def add_instrument():
    if request.method == 'POST':
        error = False
        status = None
        try:
            name = request.form['name']
            info = request.form['info']
            range = request.form['range']
            image = request.form['image']
            if check_instrument(name, info, range, image):
                instrument = Instrument(name=name, info=info, range=range, image=image)
                print(instrument)
                db.session.add(instrument)
                db.session.commit()
        except InputError:
            error = True
            status = 'something went wrong'
        finally:
            return render_template('admin_instrument.html', title="Admin", status=status, error=error)
    return render_template('admin_instrument.html', title="Admin")

@bp.route('/admin/music/', methods=['GET', 'POST'])
def add_music():
    return render_template('admin_music.html', title="Admin", error=error)
