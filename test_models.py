import os
import tempfile
import pytest

from app import create_app, db
from app.models import Instrument, Style, OriginalAuthor, Music

from config import Config

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + tempfile.mkstemp()[1]
    TESTING = True
    WTF_CSRF_ENABLED = False

@pytest.fixture
def client():
    # set custom config via environment variables
    app = create_app(TestConfig)
    client = app.test_client()
    ctx = app.app_context()

    # inspired by
    # http://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/

    ctx.push()
    yield client
    ctx.pop()

def test_something(client):
    print('hello world')
