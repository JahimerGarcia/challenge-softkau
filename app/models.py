from app import db


class Categoria(db.Model):
    """Categoria de preguntas"""
    nombre = db.Column(db.String(100), primary_key=True)
    nivel = db.Column(db.Integer, nullable=False)
    preguntas = db.relationship('Pregunta', backref='categoria', lazy=True)

    def __repr__(self):
        return '<Categoria %r>' % self.nombre


class Pregunta(db.Model):
    """Tabla preguntas en la base de datos y aqui se especifica los campos que tiene"""

    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(500), nullable=False)
    opcion1 = db.Column(db.String(200), nullable=False)
    opcion2 = db.Column(db.String(200), nullable=False)
    opcion3 = db.Column(db.String(200), nullable=False)
    opcion_correcta = db.Column(db.String(200), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey(
        'categoria.nombre'), nullable=False)



