from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../config.py')


db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

users = []

from . import views
