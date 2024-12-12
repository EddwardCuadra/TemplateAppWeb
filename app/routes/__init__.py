from flask import Blueprint

# Crear un Blueprint por cada conjunto de rutas
usuarios_bp = Blueprint('usuarios', __name__)
productos_bp = Blueprint('productos', __name__)
items_bp = Blueprint('items', __name__)
main_bp = Blueprint('routes', __name__)

# Importar las rutas desde otros archivos para registrar los Blueprints
from .usuarios import *
from .productos import *
from .items import *
from .routes import *