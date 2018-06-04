from app import create_app, db
from app.models import Instrument, Style, OriginalAuthor, Music

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Instrument': Instrument,
        'Style': Style,
        'OriginalAuthor': OriginalAuthor,
        'Music': Music,
    }
