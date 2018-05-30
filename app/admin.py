from flask import Blueprint, render_template, request
from app.models import Style

bp = Blueprint('admin', __name__)

@bp.route('/admin/style/', methods=['GET', 'POST'])
def add_style():
    if request.method == 'POST':
        # TODO
        return "blep"
    return render_template('admin_style.html', title="Admin")

def add_instrument():
    pass

def add_music():
    pass
