from enum import Enum

class SymbolsAritmeticos(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVISON = 4
    EXPONENT = 5
    MODULAR = 6
    BITWISE_SHIFT_RIGHT = 7
    BITWISE_SHIFT_LEFT = 8
    BITWISE_AND = 9
    BITWISE_OR = 10
    BITWISE_XOR = 11

class DATA_TYPE(Enum):
    NUMBER = 1
    STRING = 2
    CHAR = 3
    BOOLEANO = 4

class SymbolsTime(Enum):
    EXTRACT = 1
    NOW = 2
    DATE_PART = 3
    CURRENT_DATE = 4
    CURRENT_TIME = 5
    TIMESTAMP = 6


class SymbolsRelop(Enum):
    EQUALS = 1
    NOT_EQUAL = 2
    GREATE_EQUAL = 3
    GREATE_THAN = 4
    LESS_THAN = 5
    LESS_EQUAL = 6
    NOT_EQUAL_LR = 7

class SymbolsUnaryOrOthers(Enum):
    UMINUS = 1
    UPLUS = 2
    BITWISE_NOT = 3
    SQUARE_ROOT = 4
    CUBE_ROOT = 5
