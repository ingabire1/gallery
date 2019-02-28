# import os

# class Config:

#     MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key=b8e19cc3ea78b217ae0eddb1a13646d1'
#     MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:12345@localhost/yvette'


# class ProdConfig(Config):
#     pass


# class DevConfig(Config):
#     DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig
# }
# class Config:
# # ....
#     UPLOADED_PHOTOS_DEST ='app/static/photos'
# #  email configurations
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:12345@localhost/yvette'


# class DevConfig(Config):

#     SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://wecode:12345@localhost/yvette'
#     DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig,
# 'test':TestConfig
# }
import os

class Config:

    
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:12345@localhost/yvette'
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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:12345@localhost/yvette'
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
