from modules.clsJugador import Jugador


class Carril:
    def __init__(self, limite, auto):
        self.limite = limite
        self.auto = auto.marca
        self.id = auto.id
        self.conductor = auto.conductor
        self.jugador = auto.jugador
    
def crearCarril(limite, auto):
    carril = Carril(limite, auto)
    return carril
