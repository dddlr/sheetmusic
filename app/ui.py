from app import app
from flask import render_template, redirect, request, url_for
from app.models import Music

@app.route('/')
def index():
    '''Browse all sheet music.'''
    music = Music.query.all()
    return render_template('test.html', music=music)

def sheet_template(sheet):
    '''The actual template rendering for sheet music.'''
    return render_template('test.html', music=[sheet])

@app.route('/sheet/<int:id>/<string:url>/')
def sheet_with_name(id, url):
    '''Route for sheet music when both ID and URL slug is given.'''
    sheet = Music.query.get(id)
    if sheet.url == url:
        return sheet_template(sheet)
    return redirect(url_for('sheet_with_name', id=id, url=sheet.url))

@app.route('/sheet/<int:id>/')
def sheet_with_id(id):
    '''
    Route for sheet music when only ID is given. Redirects to full
    URL.'''
    sheet = Music.query.get(id)
    return redirect(url_for('sheet_with_name', id=id, url=sheet.url))

@app.route('/search/')
def search():
    '''Search music by name.'''
    results = []
    if request.args.get('q'):
        results = Music.query.filter(Music.name.contains(request.args.get('q')))

    return render_template('search.html', music=results)
