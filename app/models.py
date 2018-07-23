from app import db

class Instrument(db.Model):
    '''Stores different instruments and info about them.'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, nullable=False, unique=True)
    info = db.Column(db.String(200))
    range = db.Column(db.String(100))
    image = db.Column(db.String(100))

    def __repr__(self):
        return '<Instrument {}>'.format(self.name)

class Style(db.Model):
    '''Stores styles of music and their descriptions.'''
    style = db.Column(db.String(32), primary_key=True, nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Style {}>'.format(self.style)

class OriginalAuthor(db.Model):
    '''Stores the original composer of different pieces of music, e.g. if a
    song was arranged by another person.'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    country = db.Column(db.String(20))
    dob = db.Column(db.String(10))

    def __repr__(self):
        return '<OriginalAuthor {} ({})>'.format(self.name, self.id)

musicinstrument = db.Table('musicinstrument',
    db.Column('music_id', db.Integer, db.ForeignKey('music.id'), primary_key=True),
    db.Column('instrument_id', db.Integer, db.ForeignKey('instrument.id'), primary_key=True)
)

class Music(db.Model):
    '''Stores a piece of music.'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    year = db.Column(db.Integer)
    url = db.Column(db.String(32), nullable=False)
    sheet_url = db.Column(db.String(32))

    style_id = db.Column(db.String(32), db.ForeignKey('style.style'))
    # Lets us see style as a style object, and not just the ID of the style
    style = db.relationship('Style')
    original_author_id = db.Column(db.Integer, db.ForeignKey('original_author.id'))
    original_author = db.relationship('OriginalAuthor')

    # this is not actually a database field, but a high-level feature that
    # enables access to instruments from the Music table
    instruments = db.relationship('Instrument', secondary=musicinstrument,
        lazy='subquery', backref=db.backref('music', lazy=True))

    def __repr__(self):
        return '<Music {} ({})>'.format(self.name, self.id)
