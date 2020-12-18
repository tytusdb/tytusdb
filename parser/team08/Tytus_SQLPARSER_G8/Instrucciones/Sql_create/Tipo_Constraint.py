
from enum import Enum

class Tipo_Dato_Constraint(Enum):
    # ENTERO
    PRIMARY_KEY = 1
    REFERENCES = 2
    DEFAULT = 3
    NOT_NULL = 4
    NULL = 5
    UNIQUE = 6
    CONSTRAINT = 7
    CHECK = 8

class Tipo_Constraint():
    'Esta clase será de utilidad para la comprobación de tipos.'
    def __init__(self,id, tipo, expresion):
        self.id =id
        self.tipo = tipo
        self.expresion =expresion
        
    def toString(self):
        if self.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
            return "primary_key"
        elif self.tipo == Tipo_Dato_Constraint.REFERENCES:
            return "references"
        elif self.tipo == Tipo_Dato_Constraint.DEFAULT:
            return "default"
        elif self.tipo == Tipo_Dato_Constraint.NOT_NULL:
            return "not_null"
        elif self.tipo == Tipo_Dato_Constraint.NULL:
            return "null"
        elif self.tipo == Tipo_Dato_Constraint.UNIQUE:
            return "unique"
        elif self.tipo == Tipo_Dato_Constraint.CONSTRAINT:
            return "constraint"
        elif self.tipo == Tipo_Dato_Constraint.CHECK:
            return "check"