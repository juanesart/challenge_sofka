from modules.carrera import avanzar
from modules.clsCarril import crearCarril
from modules.clsAuto import Auto, crearAutos
from .clsJugador import *
from .clsPista import Pista

class Juego:
    def __init__(self, id):
        self.id = id

    def comenzarJuego(self):
        print('el juego numero ', self.id, ' ha comenzado')
        nJugadores = input('ingresa el numero de jugadores: ')
        pista = Pista(int(nJugadores))
        jugadores = []
        conductores = []
        autos = []
        carriles = []
        recorridos = []
        podio = 0
        ganadores = []
        for i in range(int(nJugadores)):
            jugadores.append(crearJugadores(i)) 
        for i in jugadores:
            conductores.append(crearConductores(i))
        for i in conductores:
            autos.append(crearAutos(i))
        for i in autos:
            carriles.append(crearCarril(5000, i))
        for i in carriles:
            recorridos.append(0)
        while(podio < 3):
            for i in carriles:
                if(recorridos[i.id] < 5000):
                    recorridos[i.id] = recorridos[i.id] + avanzar(i.id)
                elif(podio != 0):
                    if(i in ganadores):
                        pass
                    else:
                        podio = podio + 1
                        ganadores.append(i)
                        print('Felicidades el jugador {} queda en {} lugar'.format(i.id, podio))
                else:
                    podio = podio + 1
                    ganadores.append(i)
                    print('Felicidades el jugador {} queda en {} lugar'.format(i.id, podio))            
        print(recorridos)