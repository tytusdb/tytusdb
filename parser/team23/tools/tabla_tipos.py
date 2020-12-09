from enum import Enum

class tipo_primitivo(Enum):
    ENTERO = 1
    DECIMAL = 2
    STRING = 3
    BOOLEAN = 4
    ARREGLO = 5
    ERROR = 6

class nodo_AST:
    def __init__(self, valor, num):
        self.valor = str(valor)
        self.num = str(num)
        self.hijos = []

tipos_tabla = [
    [tipo_primitivo.ENTERO, tipo_primitivo.DECIMAL, tipo_primitivo.STRING, tipo_primitivo.ENTERO, tipo_primitivo.ERROR, tipo_primitivo.ERROR],
    [tipo_primitivo.DECIMAL, tipo_primitivo.DECIMAL, tipo_primitivo.STRING, tipo_primitivo.DECIMAL, tipo_primitivo.ERROR, tipo_primitivo.ERROR],
    [tipo_primitivo.STRING, tipo_primitivo.STRING, tipo_primitivo.STRING, tipo_primitivo.STRING, tipo_primitivo.ERROR, tipo_primitivo.ERROR],
    [tipo_primitivo.ENTERO, tipo_primitivo.DECIMAL, tipo_primitivo.STRING, tipo_primitivo.BOOLEAN, tipo_primitivo.ERROR, tipo_primitivo.ERROR],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ARREGLO, tipo_primitivo.ERROR],
    [tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR, tipo_primitivo.ERROR]
]

# ENTERO    DECIMAL     STRING      ENTERO      ERROR       ERROR
# DECIMAL   DECIMAL     STRING      DECIMAL     ERROR       ERROR
# STRING    STRING      STRING      STRING      ERROR       ERROR
# ENTERO    DECIMAL     STRING      BOOLEAN     ERROR       ERROR
# ERROR     ERROR       ERROR       ERROR       ARREGLO     ERROR
# ERROR     ERROR       ERROR       ERROR       ERROR       ERROR