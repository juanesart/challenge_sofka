import random


def avanzar(numero):
    input('presione ENTER para lanzar el dado')
    lado = random.randint(1,6)
    distacia = lado * 100
    print('el conductor ', numero, ' avanzó ', distacia, ' metros')
    return distacia