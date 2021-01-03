from enum import Enum

class TiposOperacionesLR(Enum):
    NOT = 1
    AND = 2
    OR = 3
    MAYOR = 4
    MAYORIGUAL = 5
    MENORIGUAL = 6
    MENOR = 7
    DIFERENTE = 8
    IGUAL = 9