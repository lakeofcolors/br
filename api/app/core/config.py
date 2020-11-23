import os
from flask import Config as FlaskConfig
from flask_sqlalchemy import string_types


class Config(object):
    """
    Base Config
    """
    DEBUG = True
    TESTING = True
    PROFILE = False

    SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{database}".format \
        (user='postgres',
         password='postgres',
         host='postgres',
         port='5432',
         database='postgres')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    BLUEPRINTS = [
        'app.views.auth',
        'app.views.route',
    ]
    SECRET_KEY = "any-secret"

