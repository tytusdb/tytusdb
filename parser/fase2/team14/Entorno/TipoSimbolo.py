from enum import Enum


class TipoSimbolo(Enum):
    TABLA = 1,
    DATABASE = 2,
    CONSTRAINT_UNIQUE = 3,
    CONSTRAINT_PRIMARY = 4,
    CONSTRAINT_FOREIGN = 5,
    CONSTRAINT_CHECK = 6,
    TYPE_ENUM = 7,
    INDEX = 8
