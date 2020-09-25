# This is from outside the base tutorial
# https://hackingandslacking.com/configuring-your-flask-application-4e5341d7affb


"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = environ.get('SECRET')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True