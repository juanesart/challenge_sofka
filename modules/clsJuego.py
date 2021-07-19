from modules.carrera import avanzar
from modules.clsCarril import crearCarril
from modules.clsAuto import Auto, crearAutos
from .clsJugador import *
from .clsPista import Pista
import csv
import pickle

class Juego:
    def __init__(self, id):
        self.id = id

    def comenzarJuego(self):
        print('el juego numero ', self.id, ' ha comenzado')
        nJugadores = input('ingresa el numero de jugadores, minimo 3: ')
        pista = Pista(int(nJugadores))
        jugadores = []
        conductores = []
        autos = []
        carriles = []
        recorridos = []
        podio = 0
        ganadores = []
        ganador = []
        registro = []
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
                if(recorridos[i.id] < 2000):
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
        for i in ganadores:
            ganador.append(i.jugador)
        with open('records.csv', 'w') as f:
            csv_writer = csv.writer(f, delimiter=' ')
            csv_writer.writerows(ganador)
        print('Gracias por jugar')