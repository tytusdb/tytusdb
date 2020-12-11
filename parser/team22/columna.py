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
    TIMESTAMP = 15
    DATE = 16
    TIME_WO = 17
    TIME = 18
    INTERVAL = 17
    BOOLEAN = 18

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
    def __init__(self, tipo: {}, default, references: str, constraints: [str], is_null = TipoNull.NULL, is_primary = 0, is_unique = 0):
        # tipo = {'tipo': TipoColumna, 'n': int, 'p': string, 'field': TipoFields}
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

class Constraint():
    'Esta clase representa los constraint de las columnas'
    def __init__(self, name: str, tipo: TipoConstraint, condicion):
        self.name = str
        self.tipo = tipo
        self.condicion = condicion