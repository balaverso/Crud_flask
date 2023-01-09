from flask import Flask
from flask_admin import Admin

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
    app.config["SECRET_KEY"] = 'secret'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    

    db.init_app(app)

    #Registro da página administrativa
    admin = Admin(app, name="Balacorp", template_mode="bootstrap3")
    import admin as administrator
    administrator.init_app(admin)

    return app