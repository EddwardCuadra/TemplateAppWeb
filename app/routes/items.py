from flask import request, jsonify
from app import db
from app.models import Item, Producto
from . import items_bp

@items_bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(nombre_item=data['nombre_item'], descripcion=data['descripcion'], imagen=data['imagen'], precio=data['precio'], producto_id=data['producto_id'], enlace=data['enlace'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Nuevo item creado'})

@items_bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    result = [{'id': item.id, 'nombre_item': item.nombre_item, 'descripcion': item.descripcion, 'imagen': item.imagen, 'precio': item.precio, 'producto_id': item.producto_id, 'enlace': item.enlace} for item in items]
    return jsonify(result)