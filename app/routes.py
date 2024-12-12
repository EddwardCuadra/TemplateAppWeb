# app/routes.py
from app import app
from flask import render_template, jsonify

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return jsonify(message="¡Hola, soy Hello!")