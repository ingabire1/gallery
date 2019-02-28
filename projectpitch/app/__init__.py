
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_mail import Mail
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()


def create_app(config_name):

    app = Flask(__name__)
    db.init_app(app)
    mail.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    configure_request(app)
    # Will add the views and forms
   

    return app

    

    