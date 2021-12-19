from flask import Blueprint, render_template, redirect, url_for, request

from app.models import Jugador
from . import controller

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', "POST"])
def home():
    if request.method == "POST" and request.form.get("nombre", False):
        return redirect(url_for("views.preguntas", nombre=request.form.get("nombre")))

    return render_template("index.html")


@views.route("/<nombre>")
def preguntas(nombre):
    jugador = controller.cargar_jugador(nombre)
    return render_template("preguntas.html", jugador= jugador)



