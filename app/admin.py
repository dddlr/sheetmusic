from flask import Blueprint, flash, render_template, request
from sqlalchemy import exc
from app import db
from app.forms import AddInstrumentForm, AddMusicForm, AddOriginalAuthorForm, AddStyleForm
from app.models import Instrument, Music, Style, OriginalAuthor

bp = Blueprint('admin', __name__)

@bp.route('/admin/instrument/', methods=['GET', 'POST'])
def add_instrument():
    """Renders the page for adding an instrument, as well as handling the
    addition of an instrument into the database."""
    error = False
    status = None
    form = AddInstrumentForm()

    if form.validate_on_submit():
        try:
            name = form.name.data
            info = form.info.data
            range = form.range.data
            image = form.image.data
            instrument = Instrument(name=name, info=info, range=range, image=image)
            db.session.add(instrument)
            db.session.commit()
            flash("Instrument added successfully.")
        except exc.IntegrityError as err:
            error = True
            print('/admin/instrument/:', err)
            flash("Something went wrong with adding the instrument. Please try again.")
        except Exception as err:
            error = True
            print("Unexpected error:", err)
            flash("Something went wrong with adding the instrument. Please try again.")
    return render_template('admin_instrument.html', title="Admin", error=error, form=form)

@bp.route('/admin/style/', methods=['GET', 'POST'])
def add_style():
    """Renders the page for adding a style/genre, as well as handling the
    addition of a style into the database."""
    error = False
    form = AddStyleForm()
    if form.validate_on_submit():
        try:
            style = Style(
                style=form.name.data,
                description=form.description.data,
            )
            db.session.add(style)
            db.session.commit()
            flash("Style added successfully.")
        except exc.IntegrityError as err:
            # Raised by database itself
            error = True
            print('/admin/style/:', err)
            flash("Something went wrong with adding the style. Please try again.")
        except Exception as err:
            # Any weird errors, time to debug
            error = True
            print("Unexpected error:", err)
            flash("Something went wrong with adding the style. Please try again.")
    return render_template('admin_style.html', title="Admin", error=error, form=form)

@bp.route('/admin/author/', methods=['GET', 'POST'])
def add_originalauthor():
    # Converts date in format 2010-12-25 to UNIX timestamp
    # int(time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple()))
    error = False
    status = None
    form = AddOriginalAuthorForm()

    if form.validate_on_submit():
        try:
            author = OriginalAuthor(name=form.name.data, country=form.country.data, dob=form.dob.data)
            db.session.add(author)
            db.session.commit()
            flash("Author added successfully.")
        except exc.IntegrityError as err:
            error = True
            print('/admin/author/:', err)
            flash("Something went wrong with adding the author. Please try again.")
        except Exception as err:
            error = True
            print("Unexpected error:", err)
            flash("Something went wrong with adding the author. Please try again.")
    return render_template('admin_originalauthor.html', title="Admin", error=error, form=form)

@bp.route('/admin/music/', methods=['GET', 'POST'])
def add_music():
    """Renders the page for adding music, as well as handling the addition of a
    piece of music into the database."""
    error = False
    status = None
    form = AddMusicForm()
    styles = Style.query.all()
    authors = OriginalAuthor.query.all()
    # [('', '')] is default - None
    form.style.choices = [('', '')] + [(i.style, i.style) for i in Style.query.all()]
    # TODO: see if there's a way to have ('', '') as an option
    # despite coerce=int
    form.original_author.choices = [(i.id, i.name) for i in OriginalAuthor.query.all()]
    form.instruments.choices = [(i.id, i.name) for i in Instrument.query.order_by('name')]
    if form.validate_on_submit():
        try:
            # Turn list of instrument IDs into list of instrument objects to
            # make flask happy
            instruments = [Instrument.query.get(i) for i in form.instruments.data]
            music = Music(
                name=form.name.data,
                year=form.year.data,
                url=form.url.data,
                sheet_url=form.sheet_url.data,
                style_id=form.style.data,
                original_author_id=form.original_author.data,
                instruments=instruments,
            )
            db.session.add(music)
            db.session.commit()
            flash("Music added successfully.")
        except exc.IntegrityError as err:
            error = True
            print('/admin/music/:', err)
            flash("Something went wrong with adding the music. Please try again.")
        except Exception as err:
            error = True
            print("Unexpected error:", err)
            flash("Something went wrong with adding the music. Please try again.")
    return render_template('admin_music.html', title="Admin", error=error, form=form, styles=styles)
