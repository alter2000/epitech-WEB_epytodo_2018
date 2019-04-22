from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config.from_pyfile('../config.py')

auth = HTTPBasicAuth()

db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

from . import views
