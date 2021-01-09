# GRUPO 5
# 201213062 - Mónica Raquel Calderon Muñoz
# 201213223 - Astrid Edith Hernandez Gonzalez
# 201213255 - Leonel Eduardo Avila Calvillo
# 201220159 - Diego Ahtohil Noj Armira
# 201220165 - Oscar Rolando Bernard Peralta

# IMPORT SECTION
from enum import Enum


# LIST OF DATA TYPES
class DATA_TYPE(Enum):
    SMALLINT = 1,
    INTEGER = 2,
    BIGINT = 3,
    DECIMAL = 4,
    NUMERIC = 5,
    REAL = 6,
    DOUBLE = 7,
    MONEY = 8,
    VARCHAR = 9,
    CHAR = 10,
    TEXT = 11,
    TIME = 12,
    DATE = 13,
    TIMEINTERVAL = 14,
    BOOLEAN = 15


# SYMBOL CLASS
class Symbol:
    """ This class represent the symbol inside de symbol table """

    def __init__(self, p_tId, p_id, p_type, p_value,p_Orden,p_Declaracion):
        self.id = p_id
        self.type = p_type
        self.value = p_value
        self.tId = p_tId
        self.p_Declaracion = p_Declaracion
        self.p_Orden = p_Orden


# SYMBOL TABLE CLASS
class SymbolTable:
    """ This class represent the symbol table """

    def __init__(self, symbols={}):
        self.symbols = symbols

    def add(self, symbol):
        self.symbols[symbol.tId] = symbol

    def get(self, p_tId):
        if p_tId not in self.symbols:
            return False

        return self.symbols[p_tId]

    def update(self, symbol):
        if symbol.id not in self.symbols:
            print('ERROR :: Variable ', id, 'no definida.')
        else:
            self.symbols[symbol.id] = symbol

    def update1(self, symbol):
        if symbol.tId not in self.symbols:
            print('ERROR :: Variable no definida.')
        else:
            self.symbols[symbol.tId] = symbol

    def destroy(self, tId):
        if tId not in self.symbols:
            print('ERROR :: Variable ', id, 'no definida.')
        else:
            del self.symbols[tId]
