from enum import Enum

class Tipos(Enum):
    Numero = 1
    Cadena = 2
    Booleano = 3
    Decimal = 4 
    Id = 5
    ISQL = 6
    Void = 7


class Expresion():
    def __init__(self):
        self.trueLabel = self.falseLabel = ''
