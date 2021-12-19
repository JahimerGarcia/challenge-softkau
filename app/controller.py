from .models import Categoria, Pregunta, Jugador, db
# Aqui se define la logica que usara la vista
# habran funciones que trabajaran con los modelos haran operaciones CRUD

def _consultar_jugador(nombre: str) -> Jugador:
    """regresa el jugador con el nombre dado que es un objeto que representa un registro en la bd """
    jugador = Jugador.query.filter_by(nombre=nombre).first()
    return jugador

def cargar_jugador(nombre: str) -> Jugador:
    """
    Carga un juego de preguntas para un jugador
    """
    jugador = _consultar_jugador(nombre)
    if jugador is None:
        jugador = Jugador()
        jugador.nombre = nombre
        db.session.add(jugador)
        db.session.commit()
    return jugador

#def cargar_preguntas

