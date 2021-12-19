from .models import Categoria, Pregunta, Jugador, db
# Aqui se define la logica que usara la vista
# habran funciones que trabajaran con los modelos haran operaciones CRUD

def consultar_jugador(nombre: str) -> Jugador:
    """regresa el jugador con el nombre dado y si no existe crea un registro en la bd """
    jugador = Jugador.query.filter_by(nombre=nombre).first()
    if jugador is None:
        jugador = Jugador(nombre)
        db.session.add(jugador)
        db.session.commit()
    return jugador


def cargar_juego(nombre: str) -> list:
    """
    Carga un juego de preguntas para un jugador
    """
    jugador = consultar_jugador(nombre)
    
    return jugador

def definir_categorias():
    """
    definir las categorias que se usaran en el juego
    """
    
    crear_categoria(nombre="facil", nivel=1),
    crear_categoria(nombre="intermedio", nivel=2)
    crear_categoria(nombre="dificil", nivel=3)
    crear_categoria(nombre="avanzado", nivel=4)
    crear_categoria(nombre="extremo", nivel=5)
    
    


def crear_categoria(nombre, nivel) -> Categoria:
    """
    Crea una categoria en la base de datos
    """
    if _consultar_categoria(nombre) is None:
        categoria = Categoria(nombre, nivel)
        db.session.add(categoria)
        db.session.commit()
        return categoria

    
    

def _consultar_categoria(nombre) -> Categoria:
    """
    Consulta una categoria en la base de datos
    """
    categoria = Categoria.query.filter_by(nombre=nombre).first()
    return categoria

