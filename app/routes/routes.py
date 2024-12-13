# app/routes.py
from flask import Blueprint, jsonify, render_template, send_from_directory, request, redirect, url_for
import os
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/soporte')
def soporte():
    return jsonify({'message': 'Página de soporte'})

#Rutas de Statics Scss Css Js Img Vendor
@main_bp.route('/assets/css/<path:filename>')
def css(filename):
    return send_from_directory(os.path.join('static', 'css'), filename)

@main_bp.route('/assets/js/<path:filename>')
def js(filename):
    return send_from_directory(os.path.join('static', 'js'), filename)

@main_bp.route('/assets/img/<path:filename>')
def img(filename):
    return send_from_directory(os.path.join('static', 'img'), filename)

@main_bp.route('/assets/scss/<path:filename>')
def scss(filename):
    return send_from_directory(os.path.join('static', 'scss'), filename)

@main_bp.route('/assets/vendor/<path:filename>')
def vendor(filename):
    return send_from_directory(os.path.join('static', 'vendor'), filename)