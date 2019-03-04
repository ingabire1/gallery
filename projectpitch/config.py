import os

class Config:

    
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = '12345'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:54321@localhost/yvett'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'my project '
    SENDER_EMAIL = 'ingabire.sylvie@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:54321@localhost/yvett'
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
