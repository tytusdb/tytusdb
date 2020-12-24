from random import random
from random import seed
from sklearn.preprocessing import StandardScaler
import math
import hashlib
import numpy as np

scaler = StandardScaler()


def getNativeFuncs():
    functions = {
        # Mathematical Functions
        'abs': lambda z: math.fabs(z),
        'cbrt': '',
        'ceil': lambda z: math.ceil(z),
        'ceiling': lambda z: math.ceil(z),
        'degrees': lambda z: math.degrees(z),
        'div': '',
        'exp': lambda z: math.frexp(z),
        'factorial': lambda z: math.factorial(z),
        'floor': lambda z: math.floor(z),
        'gcd': lambda x, y: math.gcd(x, y),
        'lcm': lambda x, y: comp_lcm(x, y),
        'ln': lambda z: math.log(z),
        'log': lambda x, y: math.log(x, y),
        'log10': lambda z: math.log10(z),
        'min_scale': '',

        'mod': lambda x, y: math.fmod(x, y),
        'pi': math.pi,
        'power': lambda x, y: math.pow(x, y),
        'radians': lambda z: math.radians(z),
        'round': lambda x, y: round(x, y),

        # 'SCALE': lambda x, y: scaler.fit_transform(x, None, y),
        # 'SIGN': lambda z: np.sign(z),
        'sqrt': lambda z: math.sqrt(z),
        'trim_scale': '',
        'truc': lambda z: math.trunc(z),
        'width_bucket': '',
        'random': random(),
        'setseed': lambda z: seed(z),
        # Trigonometric Functions
        'acos': lambda z: math.cosh(z),
        'acosd': lambda z: getAcosd(z),
        'asin': lambda z: math.asin(z),
        'asind': lambda z: getAsind(z),
        'atan': lambda z: math.atan(z),
        'atand': lambda z: getAtand(z),
        'atan2': lambda z: math.atan2(z),
        'atan2d': lambda z: getAtand2(z),
        'cos': lambda z: math.cos(z),
        'cosd': lambda z: getCosd(z),
        'cot': lambda z: getCot(z),
        'cotd': lambda z: getCotd(z),
        'sin': lambda z: math.sin(z),
        'sind': lambda z: getSind(z),
        'tan': lambda z: math.tan(z),
        'tand': lambda z: getTand(z), 
        'sinh': lambda z: math.sinh(z),
        'cosh': lambda z: math.cosh(z),
        'tanh': lambda z: math.tanh(z),
        'asinh': lambda z: getArcsinh(z),
        'acosh': lambda z: getArccosh(z),
        'atanh': lambda z: getAtanh(z),
        # Binary String Functions
        'lengtn': lambda z: len(z),
        'substring': lambda x, y: getSubstring(x, y),
        'trip': lambda z: z.strip(),
        'get_byte': lambda z: bytes(z, 'utf-8'),
        'md5': lambda z: hashlib.md5(z),
        'set_byte': '',
        'sha256': lambda z: hashlib.sha256(z),
        'substr': lambda x, y: getSubstring(x, y),
        'convert': lambda x, y: getConvert(x, y),
        'encode': lambda x, y, z: getEncode(x, y, z),
        'deconde': lambda x, y, z: getDecode(x, y, z),

        'fsum': lambda z: math.fsum(z),
        'fmond': lambda x, y: math.fmod(x, y),
        'copysing': lambda x, y: math.copysign(x, y)
    }
    return functions


def comp_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


def getSubstring(cadena, subcadena):
    if subcadena in cadena:
        return True
    else:
        return False


def getTrim(cadena):
    return cadena.strip()


def getConvert(tipo, cadena):
    if tipo == "int":
        return int(cadena)
    elif tipo == "varchar":
        return str(cadena)
    elif tipo == "float":
        return float(cadena)
    else:
        return bool(cadena)


def getEncode(cadena, tipo, formato):

    return cadena.encode(tipo, formato)


def getDecode(cadena, tipo, formato):
    return cadena.decode(tipo, formato)

#Funcion para convertir el coseno inverso de radianes a grados ACOSD()
def getAcosd(valor):
    enRadianes = math.acos(valor)
    enGrados = enRadianes * (180/math.pi)
    return enGrados

def getAsind(valor):
    enRadianes = math.asin(valor)
    enGrados = enRadianes * (180/math.pi)
    return enGrados

def getAtand(valor):
    enRadianes = math.atan(valor)
    enGrados = enRadianes * (180/math.pi)
    return enGrados

def getAtand2(valor):
    enRadianes = math.atan2(valor)
    enGrados = enRadianes * (180/math.pi)
    return enGrados

def getCosd(valor):
    enRadianes = math.cos(valor)
    enGrados = enRadianes * (180/math.pi)
    return enGrados

def getSind(valor):
    enRadianes = math.sin(valor)
    enGrados = enRadianes * (180/math.pi)
    return enGrados

def getCot(valor):
    tangente = math.tan(valor)
    cot = 1/tangente
    return cot

def getCotd(valor):
    enRadianes = 1/(math.tan(valor))
    enGrados = enRadianes * (180/math.pi)
    return enGrados

def getTand(valor):
    enRadianes = math.tan(valor)
    enGrados = enRadianes * (180/math.pi)
    return enGrados

def getArcsinh(valor):
    ln = math.log(valor + math.sqrt((valor ** 2) + 1))
    return ln

def getArccosh(valor):
    ln = math.log(valor + math.sqrt((valor ** 2) - 1))
    return ln

def getAtanh(valor):
    if valor < 1:
        resultado = (1/2)*(math.log((1-valor)/(1+valor)))
    else:
        resultado = 0
    
    return resultado



