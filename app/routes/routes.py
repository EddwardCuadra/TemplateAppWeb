# app/routes.py
from flask import Blueprint, jsonify, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/soporte')
def soporte():
    return jsonify({'message': 'Página de soporte'})