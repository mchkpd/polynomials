from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from . import models

    db.init_app(app)

    with app.app_context():
        from .exceptions import exceptions_blueprint
        app.register_blueprint(exceptions_blueprint)
        from .routes import api_blueprint
        app.register_blueprint(api_blueprint, url_prefix="/api")
        db.create_all()

    return app
