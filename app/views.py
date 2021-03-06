from flask import Blueprint, render_template, redirect, url_for, request

from . import controller

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', "POST"])
def home():
    if request.method == "POST" and request.form.get("nombre", False):
        return redirect(url_for("views.preguntas", nombre=request.form.get("nombre")))

    return render_template("index.html")


@views.route("/<nombre>", methods=['GET', 'POST'])
def preguntas(nombre):
    lista_preguntas = controller.cargar_juego(nombre)
    jugador = controller.consultar_jugador(nombre)

    if request.method =="POST":
        if controller.validar_respuestas(request.form) and lista_preguntas:
            controller.subir_nivel(jugador)
            return redirect(url_for("views.preguntas", nombre=nombre))
        else:
            return redirect(url_for("views.preguntas", nombre=nombre))


    if lista_preguntas == False:
        return render_template("preguntas.html", jugador=jugador, preguntas="fin")

    return render_template("preguntas.html", preguntas= lista_preguntas, jugador=jugador)



