from flask import Blueprint, render_template, redirect, request, url_for
from app.models import Music, Instrument

bp = Blueprint('ui', __name__)

@bp.route('/')
def index():
    '''Browse all sheet music.'''
    music = Music.query.all()
    return render_template('music.html', music=music, title="Home")

def sheet_template(sheet):
    '''The actual template rendering for sheet music.'''
    page_title = "Viewing {}".format(sheet.name)
    # Retrieves instruments with super hacky way
    instruments = list(map(lambda i: Instrument.query.get(i.id), sheet.instruments))
    return render_template('sheet.html', sheet=sheet, title=page_title, instruments=instruments)

@bp.route('/sheet/<int:id>/<string:url>/')
def sheet_with_name(id, url):
    '''Route for sheet music when both ID and URL slug is given.'''
    sheet = Music.query.get(id)
    if sheet.url == url:
        return sheet_template(sheet)
    return redirect(url_for('sheet_with_name', id=id, url=sheet.url))

@bp.route('/sheet/<int:id>/')
def sheet_with_id(id):
    '''Route for sheet music when only ID is given. Redirects to full URL.'''
    sheet = Music.query.get(id)
    return redirect(url_for('sheet_with_name', id=id, url=sheet.url))

@bp.route('/search/')
def search():
    '''Search music by name.'''
    results = []
    if request.args.get('q'):
        results = Music.query.filter(Music.name.contains(request.args.get('q')))

    return render_template('search.html', music=results, title='Search')
