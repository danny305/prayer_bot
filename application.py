from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_admin import Admin
from flask_login import LoginManager


application = Flask(__name__)
application.config.from_pyfile('prayerconfig.cfg')


db = SQLAlchemy(application)
bs = Bootstrap(application)
mail = Mail(application)
admin = Admin(application)
login_manager = LoginManager(application)





