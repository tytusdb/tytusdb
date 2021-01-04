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
                return Error('Semántico', 'Error(42P01): undefined_table', 0, 0)

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
            if self.table == None: return Error('Semántico', 'La columna ' + self.column.upper() + ' no existe.', 0, 0)
            else: return Error('Semántico', 'La columna ' + self.column.upper() + ' de la tabla ' + self.table.upper() + ' no existe.', 0, 0)


    def obtenerSeleccionado(self, data, valoresTabla, tablasSeleccionadas, columnasSelect):
        listaColumnas = None
        datosTablas = None
        nombreTablaSeleccionada = ''

        if self.table == '*':
            for tablas in valoresTabla.keys():
                columnasTablaActual = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tablas]['columns']
                contador = 0
                datosTablas = tablasSeleccionadas[tablas]
                for columnaActual in columnasTablaActual:
                    columnaSelect = []
                    for filaActual in datosTablas:
                        columnaSelect.append([filaActual[contador]])
                    if valoresTabla[tablas]['alias'] != '':
                        texto = valoresTabla[tablas]['alias'] + '.' + columnaActual.name
                    else:
                        texto = tablas + '.' + columnaActual.name
                    columnasSelect[texto] = {'columnas': columnaSelect, 'tipo': columnaActual.type}
                    contador = contador + 1
            return columnasSelect


        if self.table != None:
            try:
                filaTabla = valoresTabla[self.table.upper()]
                if not filaTabla['alias'] == '':
                    if filaTabla['alias'] == self.table.upper():
                        ''
                    else:
                        return Error('Semántico', 'Error(42P01): undefined_table Descripcion: Posiblemente el alias <' + filaTabla['alias'] + '> este haciendo referencia a la tabla ' + self.table.upper(), 0, 0)
                listaColumnas = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.table.upper()]['columns']
                datosTablas = tablasSeleccionadas[self.table.upper()]
                nombreTablaSeleccionada = self.table.upper()
            except:
                banderaAlias = True
                keysTablas = valoresTabla.keys()
                for tablas in keysTablas:
                    if self.table.upper() == valoresTabla[tablas]['alias']:
                        filaTabla = valoresTabla[tablas]['fila']
                        listaColumnas = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tablas]['columns']
                        datosTablas = tablasSeleccionadas[tablas]
                        banderaAlias = False
                        nombreTablaSeleccionada = tablas
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
                        datosTablas = tablasSeleccionadas[tablas]
                        listaColumnas = columnasTabla
                        buscarAmbiguedad = True
                        banderaIndefinida = False
                        break;
            if banderaIndefinida:
                return Error('Semántico', 'Error(42P01): undefined_table', 0, 0)

        contador = 0
        columnaSelect = []
        encontrado = False

        if self.column == '*':
            for columna in listaColumnas:
                columnaSelect = []
                for columnaDevolver in datosTablas:
                    columnaSelect.append([columnaDevolver[contador]])

                texto = nombreTablaSeleccionada + '.' + columna.name
                contador = 0
                for keysDisponibles in columnasSelect.keys():
                    if texto == keysDisponibles:
                        contador = contador + 1
                        texto = nombreTablaSeleccionada + '.' + columna.name + str(contador)

                if contador == 0:
                    texto = nombreTablaSeleccionada + '.' + columna.name

                columnasSelect[texto] = { 'columnas': columnaSelect, 'tipo': columna.type }
                contador += 1
            return columnasSelect
        else:
            tipo = ''
            for columna in listaColumnas:
                if self.column.upper() == columna.name:
                    for columnaDevolver in datosTablas:
                        columnaSelect.append([columnaDevolver[contador]])
                        encontrado = True
                        tipo = columna.type
                    break
                contador += 1
            if encontrado:

                if self.table == None:
                    texto = self.column.upper()
                else:
                    texto = self.table.upper() + '.' + self.column.upper()

                contador = 0
                for keysDisponibles in columnasSelect.keys():
                    if texto == keysDisponibles:
                        contador = contador + 1
                        if self.table == None:
                            texto = self.column.upper() + str(contador)
                        else:
                            texto = self.table.upper() + '.' + self.column.upper() + str(contador)

                if contador == 0:
                    if self.table == None:
                        texto = self.column.upper()
                    else:
                        texto = self.table.upper() + '.' + self.column.upper()

                columnasSelect[texto] = {'columnas': columnaSelect, 'tipo': tipo}
                return columnasSelect
            else:
                if self.table == None: return Error('Semántico', 'La columna ' + self.column.upper() + ' no existe.', 0, 0)
                else: return Error('Semántico', 'La columna ' + self.column.upper() + ' de la tabla ' + self.table.upper() + ' no existe.', 0, 0)

    def __repr__(self):
        return str(self.__dict__)

class Identificadordb(Instruccion):
    def __init__(self, id):
        self.id = id

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)
