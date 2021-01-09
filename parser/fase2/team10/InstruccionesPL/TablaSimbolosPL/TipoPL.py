from enum import Enum
from InstruccionesPL.TablaSimbolosPL.InstruccionPL import InstruccionPL

class Tipo_DatoPL(Enum):
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
class TipoPL(InstruccionPL):
    'Esta clase será de utilidad para la comprobación de tipos de PL.'
    def __init__(self, tipo, dimension=None):
        self.tipo = tipo
        self.dimension = dimension
        self.nombre = ''

    def getTipo(self):
        return self.tipo

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        print('ejecutando...')

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        if self.tipo==Tipo_DatoPL.SMALLINT or self.tipo==Tipo_DatoPL.INTEGER or self.tipo==Tipo_DatoPL.BIGINT or self.tipo==Tipo_DatoPL.DECIMAL or self.tipo==Tipo_DatoPL.NUMERIC or self.tipo==Tipo_DatoPL.REAL or self.tipo==Tipo_DatoPL.DOUBLE_PRECISION or self.tipo==Tipo_DatoPL.MONEY:
            res = '{0}'.format( '0')
            
        elif self.tipo==Tipo_DatoPL.CHAR or self.tipo==Tipo_DatoPL.VARCHAR or self.tipo==Tipo_DatoPL.VARYING or self.tipo==Tipo_DatoPL.CHARACTER or self.tipo==Tipo_DatoPL.TEXT:
            res = '{0} '.format( '""')
        elif self.tipo==Tipo_DatoPL.BOOLEAN:
            res = '{0} '.format( 'False')

        elif self.tipo==Tipo_DatoPL.TIPOENUM:
            res = '{0} '.format( '0')
        else:
            res =  '{0}'.format(' ')
        return res