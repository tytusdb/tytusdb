from enum import Enum

class TipoColumna(Enum):
    SMALLINT = 1
    INTEGER = 2
    BIGINT = 3
    DECIMAL = 4
    NUMERIC = 5
    REAL = 6
    DOUBLE_PRECISION  = 7
    MONEY = 8
    CHARACTER_VARYING = 9
    VARCHAR = 10
    CHARACTER = 11
    CHAR = 12
    TEXT = 13
    TIMESTAMP_WO = 14
    TIMESTAMP_W = 15
    TIMESTAMP = 16
    DATE = 17
    TIME_WO = 18
    TIME_W = 19
    TIME = 20
    INTERVAL = 21
    BOOLEAN = 22

class TipoFields(Enum):
    YEAR = 1
    MONTH = 2
    DAY = 3
    HOUR = 4
    MINUTE = 5
    SECOND = 6

class TipoConstraint(Enum):
    UNIQUE = 1
    CHECK = 2
    PRIMARY_KEY = 3
    FOREIGN_KEY = 4

class TipoNull(Enum):
    NULL = 1
    NOT_NULL = 2

class Columna():
    'Esta clase representa las columnas de las tablas'
    def __init__(self, tipo: {}, default = '', references: str = '', constraints: [str] = [], is_null = TipoNull.NULL, is_primary = 0, is_unique = 0):
        # tipo = {'tipo': TipoColumna, 'n': int, 'p': int, 'field': {'origen': TipoFields, 'destino': TipoFields}}
        self.tipo = tipo
        self.default = default
        self.is_null = is_null
        # 0 -> No es primaria, 1 -> Es primaria
        self.is_primary = is_primary
        self.references = references
        # 0 -> No es única, 1 -> Es única
        self.is_unique = is_unique
        # constraints = ['nombre_constraint',...]
        self.constraints = constraints
    
    def printCol(self):
        print('Tipo: ', self.tipo)
        print('Default: ', self.default)
        print('Null: ', self.is_null)
        print('Primary: ', self.is_primary)
        print('References: ', self.references)
        print('Unique: ', self.is_unique)
        print('Constraints: ', self.constraints, '\n')

class Constraint():
    'Esta clase representa los constraint de las columnas'
    def __init__(self, name: str, tipo: TipoConstraint, condicion):
        self.name = str
        self.tipo = tipo
        self.condicion = condicion