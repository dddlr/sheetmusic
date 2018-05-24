import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''Configuration. Put in a separate file, so unit tests can use different.
    settings.'''
    SECRET_KEY = b'h~ 4J\x18@F\xc4\xd2\x19\xa2\x1e\x11\xe6\\\x0cs\xf9"~\x1bV\xac'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN_PASSWORD = 'blepblop'
