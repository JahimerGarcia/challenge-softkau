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
    categoria = Categoria.query.filter_by(nivel_dificultad=jugador.ronda_actual).first()
    return categoria.preguntas


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


def _consultar_pregunta(enunciado) -> Pregunta:
    """
    Consulta una pregunta en la base de datos
    """
    pregunta = Pregunta.query.filter_by(enunciado=enunciado).first()
    return pregunta
   

def crear_pregunta(enunciado, opcion1, opcion2, opcion3, opcion_correcta, categoria_nombre) -> Pregunta:
    """
    Crea una pregunta en la base de datos
    """
    if _consultar_pregunta(enunciado) is None:
        pregunta = Pregunta(enunciado, opcion1, opcion2, opcion3, opcion_correcta, categoria_nombre)
        db.session.add(pregunta)
        db.session.commit()
        return pregunta





def definir_categorias():
    """
    definir las categorias que se usaran en el juego
    """
    crear_categoria(nombre="facil", nivel=1),
    crear_categoria(nombre="intermedio", nivel=2)
    crear_categoria(nombre="dificil", nivel=3)
    crear_categoria(nombre="avanzado", nivel=4)
    crear_categoria(nombre="extremo", nivel=5)
    

def definir_preguntas():
    """
    Define las preguntas que se usaran en el juego en total son 25 preguntas 5 por cada categoria
    """
    crear_pregunta(enunciado="¿Qué entendemos como lenguaje de programación?",
                   opcion1="Lo relacionado con la codificación de páginas web y sitios interactivos",
                   opcion2="Una forma de diseñar código para la máquina",
                   opcion3="Una manera de comunicarse con el hardware",
                   opcion_correcta="Una manera definida para escribir instrucciones claras para programar aplicaciones de alto nivel",
                   categoria_nombre="facil")

    crear_pregunta(enunciado="¿Qué es una variable?",
                   opcion1="Es un elemento del programa que puede cambiar su valor",
                   opcion2="Es un mecanismo para consultar información",
                   opcion3="Es un método de acceso a los datos",
                   opcion_correcta="Es una declaración dentro del programa para definir un valor dinámico",
                   categoria_nombre="facil")

    crear_pregunta(enunciado="¿Una clase es...?",
                   opcion1="Es una categoría del mismo tipo",
                   opcion2="Ninguna de las anteriores",
                   opcion3="Son varios objetos heredados",
                   opcion_correcta="Un tipo determinado para crear objetos de ese mismo tipo",
                   categoria_nombre="facil")

    crear_pregunta(enunciado="¿Cuando hablamos de un lenguaje compilado nos referimos a...?",
                   opcion1="Un lenguaje de máquina orientado al hardware",
                   opcion2="Un lenguaje de programación que transpira código nativo",
                   opcion3="Un lenguaje que requiere de un controlador específico para que pueda correr",
                   opcion_correcta="Un lenguaje que requiere pasar por un proceso de transformación a código de máquina",
                   categoria_nombre="facil")

    crear_pregunta(enunciado="¿Cuál de los siguientes es un lenguaje de programación compilado?",
                   opcion1="Python",
                   opcion2="JavaScript",
                   opcion3="HTML",
                   opcion_correcta="Java",
                   categoria_nombre="facil")
    #intermedio
    crear_pregunta(enunciado="¿Para una clase que tenga métodos get y set pero con atributos privados, ¿qué pilar de la programación se está aplicando?",
                     opcion1="Abstracciones por métodos",
                        opcion2="Evitar efectos secundarios",
                        opcion3="Programación funcional",
                        opcion_correcta="Encapsulamiento",
                        categoria_nombre="intermedio")

    crear_pregunta(enunciado="El servidor es un proveedor de información y el cliente es un consumidor de información, nos referimos a...",
                        opcion1="El cliente",
                        opcion2="El servidor",
                        opcion3="capas de aplicación",
                        opcion_correcta="cliente-servidor",
                        categoria_nombre="intermedio")

    crear_pregunta(enunciado="¿que es un algoritmo?",
                        opcion1="Un conjunto de instrucciones que se ejecutan en un orden determinado",
                        opcion2="Un conjunto de instrucciones que se ejecutan en un orden aleatorio",
                        opcion3="Una función matemática",
                        opcion_correcta="Instrucciones lógicas con un propósito específico",
                        categoria_nombre="intermedio")

    crear_pregunta(enunciado="Es un paradigma de programación orientado a mejorar la claridad, calidad y tiempo de desarrollo de un programa de computadora recurriendo únicamente a subrutinas.",
                        opcion1="Programación funcional",
                        opcion2="Programación Estructurada",
                        opcion3="Programación orientada a eventos",
                        opcion_correcta="Programación orientada a objetos",
                        categoria_nombre="intermedio")

    crear_pregunta(enunciado="Un lenguaje que se usa para hacer consultas en una base de datos relacional.",
                        opcion1="PL",
                        opcion2="Query",
                        opcion3="DDL",
                        opcion_correcta="SQL",
                        categoria_nombre="intermedio")




