# app/__init__.py
import os
from dotenv import load_dotenv
load_dotenv('.flaskenv')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import Usuario, Producto, Item
from app import routes