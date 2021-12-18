import os
from app import create_app, db

# variable de entorno 'desarrollo' o 'produccion' y si no existe, 'desarrollo'
configuracion_modo = os.getenv('FLASK_CONFIG', 'desarrollo')
app = create_app(configuracion_modo)

if __name__ == '__main__':
    db.create_all(app=app)
    app.run()
    
