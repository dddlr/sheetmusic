from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
login = LoginManager(app)

# config
app.config['SECRET_KEY'] = b'h~ 4J\x18@F\xc4\xd2\x19\xa2\x1e\x11\xe6\\\x0cs\xf9"~\x1bV\xac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['ADMIN_PASSWORD'] = 'blepblop'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import core, models
