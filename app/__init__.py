# app/__init__.py
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
load_dotenv('.flaskenv')

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import Usuario, Producto, Item

# Registrar los Blueprints
from app.routes import usuarios_bp, productos_bp, items_bp, main_bp
app.register_blueprint(main_bp)

app.register_blueprint(usuarios_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(items_bp)