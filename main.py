from modules.clsJuego import Juego
import csv

print('Bienbenido a Cars Rasing')

seleccion = input('escribe (1) para comenzar  el juego o (2) para ver la tabla de clasificación, luego presiona enter para continuar: ')

def verHistorial():
    print('este es el historial')

if int(seleccion) != 1 and int(seleccion) != 2:
    raise Exception('ingresa una opción valida')

if int(seleccion) == 1:
    juego = Juego(1)
    juego.comenzarJuego()
elif int(seleccion) == 2:
    with open('records.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            print(line)
