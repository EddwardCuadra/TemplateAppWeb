from flask import request, jsonify
from app import db
from app.models import Usuario
from . import usuarios_bp

@usuarios_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    new_usuario = Usuario(nombre=data['nombre'], correo=data['correo'], contrasena=data['contrasena'])
    db.session.add(new_usuario)
    db.session.commit()
    return jsonify({'message': 'Nuevo usuario creado'})

@usuarios_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    result = [{'id': usuario.id, 'nombre': usuario.nombre, 'correo': usuario.correo} for usuario in usuarios]
    return jsonify(result)