import math
import numpy as np
import random


def absolute(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, abs(column[i]))
        i += 1

    return result


def cbrt(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        valor = column[i] ** (1 / 3.0)
        result.insert(i + 1, round(valor))
        i += 1

    return result


def ceil(column):

    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, math.ceil(column[i]))
        i += 1

    return result


def ceiling(column):
    return ceil(column)


def degrees(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, math.degrees(column[i]))
        i += 1

    return result


def div(column1, column2):
    return div_columns(column1, column2)


def exp(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, math.exp(column[i]))
        i += 1

    return result


def factorial(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, math.factorial(column[i]))
        i += 1

    return result


def floor(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, math.floor(column[i]))
        i += 1

    return result


def gcd(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.insert(i + 1, math.gcd(column1[i], column2[i]))
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            result.insert(i + 1, math.gcd(column1[i], column2[0]))
            i += 1

    return result


def lcm(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.insert(
                i + 1, abs(column1[i] * column2[i]) // math.gcd(column1[i], column2[i])
            )
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            result.insert(
                i + 1, abs(column1[i] * column2[0]) // math.gcd(column1[i], column2[0])
            )
            i += 1
    return result


def ln(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, math.log(column[i]))
        i += 1

    return result


def log(column):

    return log10(column)


def log10(column):
    return log(column, 10)


def log(column, base):
    i = 0
    column1 = convert_num_col(column)
    result = list()
    while i < len(column1):
        result.insert(i + 1, math.log(column[i], base))
        i += 1

    return result


def mod(column1, column2):
    return mod_columns(column1, column2)


def pi():
    return [math.pi]


def pow(column1, column2):
    i = 0
    column = convert_num_col(column)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.insert(i + 1, math.pow(column1[i], column2[i]))
            i += 1

    return result


def radians(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, math.radians(column[i]))
        i += 1

    return result


def random_():
    value = random.random()
    return [value]


def sign(column):
    return np.sign(column)


def round(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, round(column[i]))
        i += 1

    return result


def sqrt(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, math.sqrt(column[i]))
        i += 1

    return result


def with_bucket(expresion, rango_izq, rango_der, number_buckets):
    if rango_izq != rango_der:
        if rango_izq == expresion:
            return 0
        if rango_der == expresion:
            return number_buckets + 1
        incremento = (rango_der - rango_izq) / number_buckets
        valor = ((expresion - rango_izq) / incremento) + 1
        if valor > number_buckets:
            return number_buckets + 1
        elif valor < 0:
            return 0
        else:
            return int(valor)


def truncate_col(column, decimals=0):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i + 1, truncate(column[i], decimals))
        i += 1

    return result


def truncate(number, decimals=0):
    if decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def sum_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.insert(i + 1, column1[i] + column2[i])
            i += 1

    return result


def rest_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.insert(i + 1, column1[i] - column2[i])
            i += 1

    return result


def mult_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.insert(i + 1, column1[i] * column2[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            result.insert(i + 1, column1[i] * column2[0])
            i += 1

    return result


def div_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.insert(i + 1, column1[i] / column2[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            result.insert(i + 1, column1[i] / column2[0])
            i += 1
    return result


def mod_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.insert(i + 1, column1[i] % column2[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            result.insert(i + 1, column1[i] % column2[0])
            i += 1

    return result


def convert_num_col(num):
    if isinstance(num, int) or isinstance(num, float):
        return [num]
    else:
        return num


def exp_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.insert(i + 1, column1[i] ** column2[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            result.insert(i + 1, column1[i] ** column2[0])
            i += 1

    return result
