import pathlib

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SERVER_PORT = 5000


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
