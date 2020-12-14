from enum import Enum


class TIPO_DATOS(Enum):
    INT = 1
    DOUBLE = 2
    BOOLEAN = 3
    CHAR = 4
    STRING = 5
    DATE = 6
    ERROR = 7


class TIPO:
    def __init__(self, tipo, dim=0):
        self.tipo = tipo
        self.dim = dim
