import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This-is-not-a-safe-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///mega.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # configuring flask to send email right after error
    # using the gmail defaults
    MAIL_SERVER = 'smtp.googlemail.com' or os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587 or int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = 1 or os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    POSTS_PER_PAGE = 3
