
from enum import Enum

class Tipo_Dato_Constraint(Enum):
    # ENTERO
    PRIMARY_KEY = 1
    FOREIGN_KEY = 2
    REFERENCES = 3
    DEFAULT = 4
    NOT_NULL = 5
    NULL = 6
    UNIQUE = 7
    CONSTRAINT = 8
    CHECK = 9

class Tipo_Constraint():
    'Esta clase será de utilidad para la comprobación de tipos.'
    def __init__(self,id, tipo, expresion):
        self.id =id
        self.tipo = tipo
        self.expresion = expresion
        self.referencia = ''
        
    def toString(self):
        if self.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
            return "primary_key"
        elif self.tipo == Tipo_Dato_Constraint.FOREIGN_KEY:
            return "foreign_key"
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