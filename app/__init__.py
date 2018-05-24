from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

from config import Config

db = SQLAlchemy()
# For migrating changes of database models to actual database
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    print('sql database is at', app.config.get('SQLALCHEMY_DATABASE_URI'))

    db.init_app(app)
    migrate.init_app(app, db)
    login = LoginManager(app)

    from app.ui import bp as ui_bp
    app.register_blueprint(ui_bp)

    return app

from app import models
