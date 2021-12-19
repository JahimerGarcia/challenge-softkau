#HERENCIA DE CLASE
class Configuracion(object):
    """
    Configuracion comun entre ambientes de desarrollo y produccion
    """
    SECRET_KEY = 'secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'


class DesarrolloConfiguracion(Configuracion):
    """
    Configuracion de Desarrollo
    """

    DEBUG = True


class ProduccionConfiguracion(Configuracion):
    """
    Configuraccion de Produccion
    """

    DEBUG = False


app_config = {
    'desarrollo': DesarrolloConfiguracion,
    'produccion': ProduccionConfiguracion
}
