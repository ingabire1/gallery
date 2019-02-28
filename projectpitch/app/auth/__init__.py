from flask import Blueprint
from flask_login import LoginManager
from . import views,forms
from flask_uploads import UploadSet,configure_uploads,IMAGES

auth = Blueprint('auth',__name__)

from . import views

def create_app(config_name):
    #...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'

def create_app(config_name):
    #....
    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

def create_app(config_name):
    app = Flask(__name__)
    #........

    # configure UploadSet
    configure_uploads(app,photos)
