from flask import render_template
from flask_login import current_user, login_user
from app.models import Instrument, Music, MusicInstrument, OriginalAuthor, Style

def 
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page."""
    if current_user.is_authenticated:
        return render_template('admin.html')
    if request.method == 'POST':
        if request.form['password'] != app.config['ADMIN_PASSWORD']:
            flash('Wrong username or password.')
            return redirect(url_for('login'))
        # TODO: update this because no username
        login_user(user)
        redirect(url_for('admin'))
    return render_template('admin.html')

def admin():
    """Admin page."""
    return render_template('admin.html')

@app.route('/admin/composer/', methods=['GET', 'POST'])
def composer():
    """Web page for add, change, delete composers."""
    if request.method == 'POST':
        pass
    return render_template('admin_subpage.html', title="composers", table=Composer)

@app.route('/admin/instrument/', methods=['GET', 'POST'])
def instrument():
    """Web page for add, change, delete instruments."""
    if request.method == 'POST':
        pass
    return render_template('admin_subpage.html', title="instruments", table=Instrument)

@app.route('/admin/music/')
def music():
    """Web page for add, change, delete music. Affects Music AND MusicInstrument tables."""
    if request.method == 'POST':
        pass
    return render_template('admin_music.html', music=Music, music_instrument=MusicInstrument)

@app.route('/admin/style/')
def style():
    """Web page to add, change, delete music styles (genres)."""
    if request.method == 'POST':
        pass
    return render_template('admin_subpage.html', title="style", table=Instrument)
