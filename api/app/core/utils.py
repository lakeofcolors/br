from importlib import import_module
from flask_sqlalchemy import string_types
from app.core.config import Config
from werkzeug.utils import import_string
from .extensions import admin
from app.core.database.models import User, Point, Route
from flask_admin.contrib.sqla import ModelView
from app.core.database.db import db_session

def register_blueprints(app, blueprints):
    for blueprint in blueprints:
        data = import_module(blueprint)
        app.register_blueprint(data.bp)


def register_admin_pages():
    admin.add_view(ModelView(User, db_session))
    admin.add_view(ModelView(Point, db_session))
    admin.add_view(ModelView(Route, db_session))
