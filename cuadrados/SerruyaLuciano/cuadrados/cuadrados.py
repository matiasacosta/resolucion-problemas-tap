from functools import reduce

def cuadrado(num):
    """ Cuantos cuadrados se pueden formar con una matriz de tamanio 'num' """
    return reduce((lambda acum, actual: acum + actual**2), range(1, num+1))
