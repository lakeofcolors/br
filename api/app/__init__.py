from flask import Flask
from app.core.extensions import migrate, ma, admin
from app.core.config import Config
from app.core.utils import register_blueprints, register_admin_pages


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.debug = True
    ma.init_app(app)
    admin.init_app(app)
    register_admin_pages()
    register_blueprints(app, Config.BLUEPRINTS)

    return app
