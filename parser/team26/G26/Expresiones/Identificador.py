import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *
from Primitivo import *

class Identificador(Instruccion):

    def __init__(self, table, column):
        self.table = table
        self.column = column

    def execute(self, data, listaColumnas, valoresTabla):
        if self.table != None:
            ''
        contador = 0
        nuevoPrimitivo = None
        typeN = ''

        for columna in listaColumnas:
            if self.column.upper() == columna.name:
                if columna.type == 'integer' or columna.type == 'smallint' or columna.type == 'bigint' or columna.type == 'numeric' or columna.type == 'money':
                    typeN = 'integer'
                elif columna.type == 'decimal' or columna.type == 'real' or columna.type == 'double':
                    typeN = 'float'
                elif columna.type == 'text' or columna.type == 'varchar' or columna.type == 'char' or columna.type == 'character':
                    typeN = 'string'
                else: typeN = columna.type
                nuevoPrimitivo = Primitive(typeN, valoresTabla[contador])
                break
            contador += 1
        if isinstance(nuevoPrimitivo, Primitive):
            return nuevoPrimitivo
        else:
            return Error('Semántico', 'La columna ' + self.column.upper() + ' no existe.', 0, 0)

    def __repr__(self):
        return str(self.__dict__)

class Identificadordb(Instruccion):
    def __init__(self, id):
        self.id = id

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)
