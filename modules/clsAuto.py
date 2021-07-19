import random

class Auto:
    def __init__(self, conductor):
        self.jugador = conductor.nickname
        self.conductor = conductor.nombre
        self.id = conductor.id
        self.marca = list_marca[random.randint(0,7)]

list_marca = [
    'BMW',
    'Mercedes-Benz',
    'Audi',
    'Lexus',
    'Renault',
    'Ford',
    'Opel',
    'Seat'
]

def crearAutos(conductor):
    auto = Auto(conductor)
    return auto