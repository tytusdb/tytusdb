import math
import random

# Funciones trigonometricas con validaciones de dominio


def cosenoinv(value):
    if value >= -1 and value <= 1:
        return math.acos(value)
    else:
        return None


def cosenoinvd(value):
    if value >= -1 and value <= 1:
        return math.degrees(math.acos(value))
    else:
        return None


def senoinv(value):
    if value >= -1 and value <= 1:
        return math.asin(value)
    else:
        return None


def senoinvd(value):
    if value >= -1 and value <= 1:
        return math.degrees(math.asin(value))
    else:
        return None


def tangenteinv(value):
    return math.atan(value)


def tangenteinvd(value):
    return math.degrees(math.atan(value))


def tangenteinv2(value1, value2):
    return math.atan2(value1, value2)


def tangenteinv2d(value1, value2):
    return math.degrees(math.atan2(value1, value2))


def coseno(value):
    return math.cos(value)


def cosenod(value):
    return math.degrees(math.cos(value))


def cotangente(value):
    tangente = math.tan(value)
    if tangente == 0:
        return None
    else:
        return (1/tangente)


def cotangented(value):
    tangente = math.tan(value)
    if tangente == 0:
        return None
    else:
        return math.degrees(1/tangente)


def seno(value):
    return math.sin(value)


def senod(value):
    return math.degrees(math.sin(value))


def tangente(value):
    return math.tan(value)


def tangented(value):
    return math.degrees(math.tan(value))


def senohiper(value):
    return math.sinh(value)


def cosenohiper(value):
    return math.cosh(value)


def tangentehiper(value):
    return math.tanh(value)


def senoinversohiper(value):
    return math.asinh(value)


def cosenoinversohiper(value):
    if value >= 1:
        return math.acosh(value)
    else:
        return None


def tangenteinversahiper(value):
    if value > -1 and value < 1:
        return math.atanh(value)
    else:
        return None
