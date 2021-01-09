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

    
    def __repr__(self):
            return str(self.name)
            
class DATA_TYPE(Enum):
    NUMBER = 1
    STRING = 2
    CHAR = 3
    BOOLEANO = 4

    def __repr__(self):
            return str(self.name)

class SymbolsTime(Enum):
    EXTRACT = 1
    NOW = 2
    DATE_PART = 3
    CURRENT_DATE = 4
    CURRENT_TIME = 5
    TIMESTAMP = 6
    
    def __repr__(self):
            return str(self.name)

class SymbolsRelop(Enum):
    EQUALS = 1
    NOT_EQUAL = 2
    GREATE_EQUAL = 3
    GREATE_THAN = 4
    LESS_THAN = 5
    LESS_EQUAL = 6
    NOT_EQUAL_LR = 7
    
    def __repr__(self):
            return str(self.name)

class SymbolsUnaryOrOthers(Enum):
    UMINUS = 1
    UPLUS = 2
    BITWISE_NOT = 3
    SQUARE_ROOT = 4
    CUBE_ROOT = 5

    def __repr__(self):
            return str(self.name)

class ColumnsTypes(Enum):
    BIGINT = 1
    BOOLEAN = 2
    CHAR = 3
    CHARACTER = 4
    CHARACTER_VARYING = 5
    DATE = 6
    DECIMAL = 7
    DOUBLE_PRECISION = 8
    INTEGER = 9
    INTERVAL = 10
    MONEY = 11
    NUMERIC = 12
    REAL = 13
    SMALLINT = 14
    TEXT = 15
    TIMESTAMP = 16
    TIME = 17    
    VARCHAR = 18

    def __repr__(self):
        return str(self.name)


