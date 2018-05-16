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
        return '<Style {}>'.format(self.style)

class OriginalAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    country = db.Column(db.String(20))
    dob = db.Column(db.Integer)

    def __repr__(self):
        return '<OriginalAuthor {} ({})>'.format(self.name, self.id)

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    year = db.Column(db.Integer)
    url = db.Column(db.String(32), nullable=False)
    sheet_url = db.Column(db.String(32))

    style_id = db.Column(db.String(32), db.ForeignKey('style.style'))
    original_author_id = db.Column(db.Integer, db.ForeignKey('original_author.id'))

    # this is not actually a database field, but a high-level feature that
    # enables access to instruments from the Music table
    instruments = db.relationship('MusicInstrument', backref='instrument', lazy='dynamic')

    def __repr__(self):
        return '<Music {} ({})>'.format(self.name, self.id)

class MusicInstrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_id = db.Column(db.Integer, db.ForeignKey('music.id'))
    instrument_id = db.Column(db.Integer, db.ForeignKey('instrument.id'))

    def __repr__(self):
        return '<MusicInstrument {} ({})>'.format(self.music_id, self.instrument_id)
