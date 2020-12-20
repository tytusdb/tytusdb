from enum import Enum


class TIPO(Enum):
    ENTERO = 0
    DECIMAL = 1
    CADENA = 2
    BOOLEAN = 3
    SMALLINT = 4
    BIGINT = 5
    NUMERIC = 6
    REAL = 7
    MONEY = 8
    TEXT = 9
    LISTA = 10
    TIME = 11
    DATE = 12
    TIMESTAMP = 13
    INTERVAL = 14
    DOUBLE_PRECISION = 15
    CHARACTER_VARYING = 16
    CHARACTER = 17
    VARCHAR = 18
    CHAR = 19
    MATRIZ = 20

    ERROR = 98