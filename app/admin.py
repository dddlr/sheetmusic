from flask import Blueprint, render_template, request
from app import db
from app.models import Style
from app.validate import check_style

bp = Blueprint('admin', __name__)

@bp.route('/admin/style/', methods=['GET', 'POST'])
def add_style():
    if request.method == 'POST':
        # TODO
        name = request.form['style']
        description = request.form['description']
        if not check_style(style, description):
            return 'fail'
        style = Style(style=name, description=description)
        db.session.add(style)
        db.session.commit()
    return render_template('admin_style.html', title="Admin")

def add_instrument():
    pass

def add_music():
    pass
