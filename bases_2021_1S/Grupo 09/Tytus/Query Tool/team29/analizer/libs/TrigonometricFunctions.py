import math
import team29.analizer.libs.MathFunctions as mt


list_errors_tg = list()


def acos(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            valor = ""
            if column[i] >= -1 and 1 >= column[i]:
                valor = str(math.acos(column[i]))
            else:
                valor = "Error de dominio"
                list_errors_tg.append("Error: 22003: la entrada esta fuera del dominio")
            result.append(valor)
        else:
            result.append(column[i])
        i += 1

    return result


def acosd(column):
    return mt.degrees(acos(column))


def asin(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            valor = ""
            if column[i] >= -1 and 1 >= column[i]:
                valor = str(math.asin(column[i]))
            else:
                valor = "Error de dominio"
                list_errors_tg.append("Error: 22003: la entrada esta fuera del dominio")
            result.append(valor)
        else:
            result.append(column[i])
        i += 1

    return result


def asind(column):
    return mt.degrees(asin(column))


def atan(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.atan(column[i]))
        else:
            result.append(column[i])
        i += 1
    return result


def atand(column):

    return mt.degrees(atan(column))


def atan2(column1, column2):
    i = 0
    column1 = mt.convert_num_col(column1)
    column2 = mt.convert_num_col(column2)
    result = list()
    while i < len(column1):
        if (isinstance(column1[i], int) or isinstance(column1[i], float)) and (
            isinstance(column2[i], int) or isinstance(column2[i], float)
        ):
            result.append(math.atan2(column1[i], column2[i]))
        else:
            result.append(column1[i])
        i += 1
    return result


def atan2d(column1, column2):

    return mt.degrees(atan2(column1, column2))


def cos(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.cos(column[i]))
        else:
            result.append(column[i])
        i += 1
    return result


def cosd(column):

    return mt.degrees(cos(column))


def cot(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            if column[i] % math.pi != 0:
                result.append((math.cos(column[i]) / math.sin(column[i])))
            else:
                result.append("Error de dominio")
                list_errors_tg.append("Error: 22003: la entrada esta fuera del dominio")
        else:
            result.append(column[i])
        i += 1
    return result


def cotd(column):

    return mt.degrees(cot(column))


def sin(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.sin(column[i]))
        else:
            result.append(column[i])
        i += 1
    return result


def sind(column):

    return mt.degrees(sin(column))


def tan(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            if (column[i] - (math.pi / 2)) % (math.pi) != 0:
                result.append(math.tan(column[i]))
            else:
                result.append("Error de dominio")
                list_errors_tg.append("Error: 22003: la entrada esta fuera del dominio")
        else:
            result.append(column[i])
        i += 1
    return result


def tand(column):

    return mt.degrees(tan(column))


def sinh(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.sinh(column[i]))
        else:
            result.append(column[i])
        i += 1
    return result


def cosh(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.cosh(column[i]))
        else:
            result.append(column[i])
        i += 1
    return result


def tanh(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.tanh(column[i]))
        else:
            result.append(column[i])
        i += 1
    return result


def asinh(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            result.append(math.asinh(column[i]))
        else:
            result.append(column[i])
        i += 1
    return result


def acosh(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            if column[i] >= 1:
                result.append(math.acosh(column[i]))
            else:
                result.append("Error de dominio")
                list_errors_tg.append("Error: 22003: la entrada esta fuera del dominio")
        else:
            result.append(column[i])
        i += 1
    return result


def atanh(column):
    i = 0
    column = mt.convert_num_col(column)
    result = list()
    while i < len(column):
        if isinstance(column[i], int) or isinstance(column[i], float):
            if column[i] < 1 and column[i] > -1:
                result.append(math.atanh(column[i]))
            else:
                result.append("Error de dominio")
                list_errors_tg.append("Error: 22003: la entrada esta fuera del dominio")
        else:
            result.append(column[i])
        i += 1
    return result
