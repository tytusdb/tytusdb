import math
import numpy as np
import random

list_errors_mt = list()


def absolute(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(abs(column[i]))
        else:
            result.append(column[i])
        i += 1

    return result


def cbrt(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            valor = column[i] ** (1.0 / 3.0)
            result.append(valor)
        else:
            result.append(column[i])
        i += 1

    return result


def ceil(column):

    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.ceil(column[i]))
        else:
            result.append(column[i])
        i += 1

    return result


def ceiling(column):
    return ceil(column)


def degrees(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.degrees(column[i]))
        else:
            result.append(column[i])
        i += 1

    return result


def div(column1, column2):
    return div_columns(column1, column2)


def exp(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.exp(column[i]))
        else:
            result.append(column[i])
        i += 1

    return result


def factorial(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            if column[i] >= 0:
                result.append(math.factorial(column[i]))
            else:
                result.append(1)
        else:
            result.append(column[i])
        i += 1

    return result


def floor(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.floor(column[i]))
        else:
            result.append(column[i])
        i += 1

    return result


def gcd(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[i], int) or isinstance(column2[i], float)
            ):
                result.append(math.gcd(column1[i], column2[i]))
            else:
                result.append(column1[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[0], int) or isinstance(column2[0], float)
            ):
                result.append(math.gcd(column1[i], column2[0]))
            else:
                result.append(column1[i])
            i += 1

    return result


def lcm(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[i], int) or isinstance(column2[i], float)
            ):
                result.insert(
                    i + 1,
                    abs(column1[i] * column2[i]) // math.gcd(column1[i], column2[i]),
                )
            else:
                result.append(column1[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[0], int) or isinstance(column2[0], float)
            ):
                result.insert(
                    i + 1,
                    abs(column1[i] * column2[0]) // math.gcd(column1[i], column2[0]),
                )
            else:
                result.append(column1[i])

            i += 1
    return result


def ln(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            if 0 >= column[i]:
                list_errors_mt.append(
                    "Error: 2201E: no se puede calcular el algoritmo de un numero menor o igual a cero "
                )
                result.append("Error de dominio")
            else:
                result.append(math.log(column[i]))
        else:
            result.append(column[i])
        i += 1

    return result


def log10(column):
    return log(column, 10)


def log(column, base=10):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.log(column[i], base))
        else:
            result.append(column[i])
        i += 1

    return result


def mod(column1, column2):
    return mod_columns(column1, column2)


def pi():
    return [math.pi]


def pow(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            result.append(math.pow(column1[i], column2[i]))
            i += 1

    return result


def radians(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.radians(column[i]))
        else:
            result.append(column[i])
        i += 1

    return result


def random_():
    value = random.random()
    return [value]


def sign(column):
    return np.sign(column)


def round_(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(round(column[i]))
        else:
            result.append(column[i])
        i += 1
    return result


def sqrt(column):
    i = 0
    column = convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            if column[i] >= 0:
                result.append(math.sqrt(column[i]))
            else:
                result.append("Error en el dominio")
                list_errors_mt.append(
                    "Error: 2201F: no se puede calcular la raiz cuadrada de un numero negativo"
                )
        else:
            result.append(column[i])
        i += 1
    return result


def with_bucket(expresion, rango_izq, rango_der, number_buckets):
    if rango_izq != rango_der:
        if rango_izq > expresion:
            return 0
        if rango_izq == expresion:
            return 1
        if rango_der == expresion:
            return number_buckets + 1
        incremento = (rango_der - rango_izq) / number_buckets
        valor = int((expresion - rango_izq) / incremento) + 1
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
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(truncate(column[i], decimals))
        else:
            result.append(column[i])
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
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[i], int) or isinstance(column2[i], float)
            ):
                result.append(column1[i] + column2[i])
            else:
                result.append(column1[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[0], int) or isinstance(column2[0], float)
            ):
                result.append(column1[i] + column2[0])
            else:
                result.append(column1[i])
            i += 1

    return result


def rest_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[i], int) or isinstance(column2[i], float)
            ):
                result.append(column1[i] - column2[i])
            else:
                result.append(column1[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[0], int) or isinstance(column2[0], float)
            ):
                result.append(column1[i] - column2[0])
            else:
                result.append(column1[i])
            i += 1

    return result


def mult_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[i], int) or isinstance(column2[i], float)
            ):
                result.append(column1[i] * column2[i])
            else:
                result.append(column1[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[0], int) or isinstance(column2[0], float)
            ):
                result.append(column1[i] * column2[0])
            else:
                result.append(column1[i])
            i += 1

    return result


def div_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[i], int) or isinstance(column2[i], float)
            ):
                if column2[i] != 0:
                    result.append(column1[i] / column2[i])
                else:
                    list_errors_mt.append("Error: 22012: division por cero")
                    result.append("Error no se puede dividir por cero")
            else:
                result.append(column1[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[0], int) or isinstance(column2[0], float)
            ):
                if column2[0] != 0:
                    result.append(column1[i] / column2[0])
                else:
                    list_errors_mt.append("Error: 22012: division por cero")
                    result.append("Error no se puede dividir por cero")
            else:
                result.append(column1[i])
            i += 1
    return result


def mod_columns(column1, column2):
    i = 0
    column1 = convert_num_col(column1)
    column2 = convert_num_col(column2)
    result = list()
    if len(column1) == len(column2):
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[i], int) or isinstance(column2[i], float)
            ):
                if column2[i] != 0:
                    result.append(column1[i] % column2[i])
                else:
                    list_errors_mt.append("Error: 22012: modulo por cero")
                    result.append("Error no se puede modular por cero")
            else:
                result.append(column1[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[0], int) or isinstance(column2[0], float)
            ):
                if column2[0] != 0:
                    result.append(column1[i] % column2[0])
                else:
                    list_errors_mt.append("Error: 22012: modulo por cero")
                    result.append("Error no se puede modular por cero")
            else:
                result.append(column1[i])
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
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[i], int) or isinstance(column2[i], float)
            ):
                result.append(column1[i] ** column2[i])
            else:
                result.append(column1[i])
            i += 1
    elif len(column2) == 1:
        while i < len(column1):
            if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
                isinstance(column2[0], int) or isinstance(column2[0], float)
            ):
                result.append(column1[i] ** column2[0])
            else:
                result.append(column1[i])
            i += 1

    return result
