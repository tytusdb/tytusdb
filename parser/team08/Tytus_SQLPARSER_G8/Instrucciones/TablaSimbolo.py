from enum import Enum

class Tipo_Dato(Enum):
    # ENTERO
    SMALLINT = 1
    INTEGER = 2
    BIGINT = 3
    DECIMAL = 4
    NUMERIC = 5
    REAL = 6
    DOUBLE_PRECISION = 7
    MONEY = 8
    # CADENA
    CHAR = 9
    VARCHAR = 10
    VARYING = 11
    CHARACTER = 12
    TEXT = 13
    # FECHA
    DATE = 14
    TIMESTAMP = 15
    TIME = 16
    INTERVAL = 17
    # BOOLEAN
    BOOLEAN = 18
    TIPOENUM = 19


class Simbolo():
    'Esta clase se utiliza para crear un símbolo de base para una declaración de variable'

    def __init__(self, id, tipo, valor, linea, columna):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

class TablaSimbolo():
    'Esta clase representa la tabla de símbolos'

    def __init__(self, anterior):
        self.anterior = anterior
        self.variables = {}
        self.funciones = {}
    
    