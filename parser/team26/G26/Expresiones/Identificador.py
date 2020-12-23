import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *
from Primitivo import *
from Error import *

class Identificador(Instruccion):

    def __init__(self, table, column):
        self.table = table
        self.column = column

    def execute(self, data, valoresTabla):
        listaColumnas = None
        if self.table != None:
            try:
                filaTabla = valoresTabla[self.table.upper()]['fila']
                listaColumnas = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.table.upper()]['columns']
            except:
                banderaAlias = True
                keysTablas = valoresTabla.keys()
                for tablas in keysTablas:
                    if self.table.upper() == valoresTabla[tablas]['alias']:
                        filaTabla = valoresTabla[tablas]['fila']
                        listaColumnas = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tablas]['columns']
                        banderaAlias = False
                        break
                if banderaAlias:
                    return Error('Semántico', 'Error(42P01): undefined_table', 0, 0)
        else:
            buscarAmbiguedad = False
            banderaIndefinida = True
            for tablas in valoresTabla.keys():
                columnasTabla = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tablas]['columns']
                for columna in columnasTabla:
                    if columna.name == self.column.upper():
                        if buscarAmbiguedad:
                            return Error('Semántico', 'Error(42702): ambiguous_column ', 0, 0)
                        filaTabla = valoresTabla[tablas]['fila']
                        listaColumnas = columnasTabla
                        buscarAmbiguedad = True
                        banderaIndefinida = False
                        break;
            if banderaIndefinida:
                Error('Semántico', 'Error(42P01): undefined_table', 0, 0)

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
                nuevoPrimitivo = Primitive(typeN, filaTabla[contador])
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
