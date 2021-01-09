
from enum import Enum

class Tipo_Dato(Enum):
    # ENTERO
    SMALLINT = 1
    INTEGER = 2
    BIGINT = 3
    DECIMAL = 4
    NUMERIC = 5
    REAL = 6
    DOUBLE_PRECISION = 7
    MONEY = 8
    # CADENA
    CHAR = 9
    VARCHAR = 10
    VARYING = 11
    CHARACTER = 12
    TEXT = 13
    # FECHA
    DATE = 14
    TIMESTAMP = 15
    TIME = 16
    INTERVAL = 17
    # BOOLEAN
    BOOLEAN = 18
    TIPOENUM = 19
    # ID 
    ID = 20
    QUERY =21

class Tipo():
    'Esta clase será de utilidad para la comprobación de tipos.'
    def __init__(self, tipo, dimension=None):
        self.tipo = tipo
        self.dimension = dimension
        self.nombre = ''
        
    def ejecutar(self, tabla, arbol):
        return self
        
    def toString(self):
        if self.tipo == Tipo_Dato.SMALLINT:
            return "smallint"
        elif self.tipo == Tipo_Dato.INTEGER:
            return "integer"
        elif self.tipo == Tipo_Dato.BIGINT:
            return "bigint"
        elif self.tipo == Tipo_Dato.DECIMAL:
            return f"decimal ({self.dimension[0]},{self.dimension[1]})"
        elif self.tipo == Tipo_Dato.NUMERIC:
            return "numeric"
        elif self.tipo == Tipo_Dato.REAL:
            return "real"
        elif self.tipo == Tipo_Dato.DOUBLE_PRECISION:
            return "double precision"
        elif self.tipo == Tipo_Dato.MONEY:
            return "money"
        elif self.tipo == Tipo_Dato.CHAR:
            return f"char ({self.dimension})"
        elif self.tipo == Tipo_Dato.VARCHAR:
            return f"varchar ({self.dimension})"
        elif self.tipo == Tipo_Dato.VARYING:
            return f"character varying ({self.dimension})"
        elif self.tipo == Tipo_Dato.CHARACTER:
            return f"character ({self.dimension})"
        elif self.tipo == Tipo_Dato.TEXT:
            return "text"
        elif self.tipo == Tipo_Dato.DATE:
            return "date"
        elif self.tipo == Tipo_Dato.TIMESTAMP:
            return "timestamp"
        elif self.tipo == Tipo_Dato.TIME:
            return "time"
        elif self.tipo == Tipo_Dato.INTERVAL:
            return "interval"
        elif self.tipo == Tipo_Dato.BOOLEAN:
            return "boolean"
        elif self.tipo == Tipo_Dato.TIPOENUM:
            return "enum"
        elif self.tipo == Tipo_Dato.ID:
            return "id"
        elif self.tipo == Tipo_Dato.QUERY:
            return "query"
        
    def getCodigo(self, tabla, arbol):       
        value_list = []
        
        value_list.append(self.tipo)
        value_list.append(self.dimension)
        return arbol.getExpressionCode(value_list, 'tipo')