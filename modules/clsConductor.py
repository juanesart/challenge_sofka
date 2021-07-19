from modules.clsAuto import crearAutos
import random

class Conductor:
    def __init__(self, jugador):
        self.nickname = jugador.nombre
        self.id = jugador.id
        self.nombre = listNombres[random.randint(0,4)]

listNombres = [
    'Michael Schumacher',
    'Fernando Alonso',
    'Lewis Hamilton',
    'Juan Pablo Montoya',
    'Ayrton Senna'
]

def crearConductores(jugador):
    conductor = Conductor(jugador)
    return conductor