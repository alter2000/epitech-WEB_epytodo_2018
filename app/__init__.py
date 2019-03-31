from flask import Flask
from config import Config

app = Flask(__name__)
cfg = Config()
app.config.from_object(cfg)

from app import views
