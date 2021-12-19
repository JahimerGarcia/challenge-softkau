from config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()
#  toca importar los modelos despues de usar el orm porque me da error
# aun no encuentro como hacerlo optimo creo que flask es asi
from . import models, controller
from .views import views


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    
    db.init_app(app)

    app.register_blueprint(views)
    
    @app.before_first_request
    def crear_categorias_preguntas():
        db.create_all()
        controller.definir_categorias()
    
    #debo hacer un blueprint de flask para cargar las vistas

    return app
