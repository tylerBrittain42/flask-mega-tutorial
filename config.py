import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This-is-not-a-safe-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///mega.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False