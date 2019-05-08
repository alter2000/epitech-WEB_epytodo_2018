from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('../config.py')
app.secret_key = app.config['SECRET_KEY']

login = LoginManager(app)
login.login_view = 'user_sign_in'

from . import views
