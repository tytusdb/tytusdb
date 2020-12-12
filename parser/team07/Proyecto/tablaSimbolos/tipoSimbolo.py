
from enum import Enum

class TipoSimbolo(Enum):
    CADENA = 1
    ENTERO = 2
    DECIMAL = 3
    BOOLEANO = 4
    DEFAULT = 5
    SUMA = 6
    RESTA = 7
    MULTIPLICACION = 8
    DIVISION = 9
    POTENCIA = 10
    MODULO = 11
    NEGATIVO_UNARIO = 12
    POSITIVO_UNARIO = 13
    IGUALACION = 14
    DISTINTO = 15
    MAYOR_QUE = 16
    MAYOR_IGUAL = 17
    MENOR_QUE = 18
    MENOR_IGUAL = 19
    AND = 20
    OR = 21
    NOT = 22
    NOMBRE_COLUMNA = 23