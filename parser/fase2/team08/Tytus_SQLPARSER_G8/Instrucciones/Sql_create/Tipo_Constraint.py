
from Instrucciones.Expresiones.Relacional import Relacional
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
    
    def traducir(self, arbol, tabla):
        #print(self.id)
        #print(self.tipo)
        #print(self.expresion)
        #print(self.referencia)
        cadena = " "
        if self.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
            cadena += "primary key"
        elif self.tipo == Tipo_Dato_Constraint.FOREIGN_KEY:
            cadena += "foreign key"
        elif self.tipo == Tipo_Dato_Constraint.REFERENCES:
            cadena += "references"
        elif self.tipo == Tipo_Dato_Constraint.DEFAULT:
            cadena += "default"
        elif self.tipo == Tipo_Dato_Constraint.NOT_NULL:
            cadena += "not null"
        elif self.tipo == Tipo_Dato_Constraint.NULL:
            cadena += "null"
        elif self.tipo == Tipo_Dato_Constraint.UNIQUE:
            cadena += "unique"
        elif self.tipo == Tipo_Dato_Constraint.CONSTRAINT:
            cadena += "constraint"
        elif self.tipo == Tipo_Dato_Constraint.CHECK:
            cadena += "check"

        if(self.expresion != None):
            cadena += "(" 
            '''if(self.expresion):
                cadena += self.expresion.traducir(arbol,tabla) 
            else:
            '''
            if isinstance(self.expresion, Relacional):
                cadena += self.expresion.concatenar(tabla, arbol)
            else:
                for x in range(0,len(self.expresion)):
                    if(x>0):
                        cadena+=", "
                    cadena += self.expresion[x]
            cadena += ")"
        
        return cadena        