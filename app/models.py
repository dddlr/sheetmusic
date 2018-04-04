from app import db

class Instrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    info = db.Column(db.String(200))
    range = db.Column(db.String(100))
    image = db.Column(db.String(100))

    def __repr__(self):
        return '<Instrument {}>'.format(self.name)

class Style(db.Model):
    style = db.Column(db.String(32), primary_key=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Style {}>'.format(style)

class OriginalAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    country = db.Column(db.String(20))
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<OriginalAuthor {} ({})>'.format(name, id)

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    year = db.Column(db.Integer)
    url = db.Column(db.String(32))

    style_id = db.Column(db.Integer, db.ForeignKey('Style.style'))
    original_author_id = db.Column(db.Integer, db.ForeignKey('OriginalAuthor.id'))

class MusicInstrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_id = db.Column(db.Integer, db.ForeignKey('Music.id'))
    instrument_id = db.Column(db.Integer, db.ForeignKey('Instrument.id'))
