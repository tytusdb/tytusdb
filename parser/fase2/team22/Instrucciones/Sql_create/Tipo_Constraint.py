from enum import Enum
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

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

    def generar3D(self):
        code = []
        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        if self.id != None:
            code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"" + str(self.id) + " \"", "STRING"), ClassOP_ARITMETICO.SUMA))
            t0 = t1
            t1 = c3d.getTemporal()
        
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"" + self.toString().replace('_', ' ') + "(\"", "STRING"), ClassOP_ARITMETICO.SUMA))
        t0 = t1
        t1 = c3d.getTemporal()

        for cont in range(len(self.expresion)):
            code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor('"' + self.expresion[cont] + '"', "STRING"), ClassOP_ARITMETICO.SUMA))
            t0 = t1
            t1 = c3d.getTemporal()
            
            if cont + 1 != len(self.expresion):
                code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor('","', "STRING"), ClassOP_ARITMETICO.SUMA))
                t0 = t1
                t1 = c3d.getTemporal()
        
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\")\\n\"", "STRING"), ClassOP_ARITMETICO.SUMA))

        return code
    