from enum import Enum

class tipo_primitivo(Enum):
    SMALLINT = 0
    INTEGER = 1
    BIGINT = 2
    DECIMAL = 3
    NUMERIC = 4
    REAL = 5
    DOUBLE_PRECISION = 6
    MONEY = 7
    TIMESTAMP_TZ = 8    #WITH TIME ZONE
    TIMESTAMP = 9       #WITHOUT TIME ZONE
    DATE = 10
    TIME_TZ = 11        #WITH TIME ZONE
    TIME = 12           #WITHOUT TIME ZONE
    INTERVAL = 13
    BOOLEAN = 14
    ERROR = 15
    TEXT = 16
    CHAR = 17
    VARCHAR = 18 
    CHAR_STR = 19
    VARCHAR_STR = 20

class nodo_AST:
    def __init__(self, valor, num):
        self.valor = str(valor)
        self.num = str(num)
        self.hijos = []
