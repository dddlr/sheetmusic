import os
import tempfile
import pytest

from app import create_app, db
from app.models import Instrument, Style, OriginalAuthor, Music, MusicInstrument

from config import Config

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + tempfile.mkstemp()[1]
    TESTING = True

@pytest.fixture
def client():
    # set custom config via environment variables
    app = create_app(TestConfig)
    client = app.test_client()

    print('client')

    # TODO: fix this function to use Blueprints
    yield client

def test(client):
    print(Instrument.query.all())
