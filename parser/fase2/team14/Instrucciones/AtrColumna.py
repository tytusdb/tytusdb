from enum import Enum

class AtributosColumna(Enum):
    REFERENCES = 1,
    PRIMARY = 2,
    NULO = 3,
    NO_NULO = 4,
    DEFAULT = 5,
    CHECK = 6,
    UNICO = 7,
    CONSTRAINT = 8,
    COLUMNA_SIMPLE = 9