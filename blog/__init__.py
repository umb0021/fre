from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

bootstrap = Bootstrap()
nav = Nav()
db = SQLAlchemy()
security = Security()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)


    from .main import main as main_bp
    app.register_blueprint(main_bp)
    bootstrap.init_app(app)
    nav.init_app(app)
    from .navbar import main_nav
    from .models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)



    return app