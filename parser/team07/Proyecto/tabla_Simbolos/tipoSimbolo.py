
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
    BETWEEN = 24
    NOT_BETWEEN = 25
    INN = 26
    NOT_INN = 27
    LIKE = 28
    NOT_LIKE = 29
    ILIKE = 30
    NOT_ILIKE = 31
    SIMILAR = 32
    IS_NULL = 33
    IS_NOT_NULL = 34
    COLUMNA_DATO = 35
    NULO = 36
