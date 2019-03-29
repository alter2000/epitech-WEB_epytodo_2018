from flask import Flask
from config import Config


app = Flask(__name__)
cfg = Config()

from app import views
