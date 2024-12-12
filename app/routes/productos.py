from flask import request, jsonify
from app import db
from app.models import Producto
from . import productos_bp

@productos_bp.route('/productos', methods=['POST'])
def create_producto():
    data = request.get_json()
    new_producto = Producto(nombre_producto=data['nombre_producto'], descripcion=data['descripcion'], imagen=data['imagen'], enlace=data['enlace'])
    db.session.add(new_producto)
    db.session.commit()
    return jsonify({'message': 'Nuevo producto creado'})

@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    result = [{'id': producto.id, 'nombre_producto': producto.nombre_producto, 'descripcion': producto.descripcion, 'imagen': producto.imagen, 'enlace': producto.enlace} for producto in productos]
    return jsonify(result)