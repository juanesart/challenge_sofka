from modules.clsConductor import crearConductores


class Jugador:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

def crearJugadores(i):
    nombre = input('ingresa el nombre del jugador {}: '.format(i))
    jugador = Jugador(nombre, i)
    return jugador