import math


def sum(column):
    """
    Funcion encargada de sumar todas las cantidades de una columna
    """

    return math.fsum(column)


def count(column):
    """
    Funcion encargada de contar cuantas filas tiene una columna
    """
    return len(column)


def avg(column):
    """
    Funcion encargada de promediar todas las cantidades de una columna
    """
    return sum(column) / count(column)


def max(column):
    """
    Funcion encargada de devolver el valor maximo de una columna
    """
    return max(column)


def min(column):
    """
    Funcion encargada de devolver el valor minimo de una columna
    """
    return min(column)
