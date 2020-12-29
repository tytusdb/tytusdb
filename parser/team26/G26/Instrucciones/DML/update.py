import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Librerias/storageManager')
sys.path.append('../G26/Utils')

from instruccion import *
from Error import *
from jsonMode import *

from TablaSimbolos import *

class Update(Instruccion):

    def __init__(self, tableid, asignaciones, condiciones):
        self.tableid = tableid
        self.asignaciones = asignaciones
        self.condiciones = condiciones

    def execute(self, data):

        # Send to update function
        register = {}

        tables = showTables(str(data.databaseSeleccionada))
        if not self.tableid.table.upper() in tables :
            error = Error('Semántico', 'Error(???): La tabla no existe.', 0, 0)
            return error

        for asignacion in self.asignaciones:
            #valor del argumento
            try:
                arg = asignacion.argument.execute()
            except:
                arg = asignacion.argument.execute(data, None)

            if isinstance(arg, Error):
                return arg
            #validar si existe columna
            found = False #para saber si encontré la columna
            colPosition = 0 #var para guardar la posición de la columna
            for columna in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.tableid.table.upper()]['columns'] :
                if asignacion.columnid.column.upper() == columna.name :
                    found = True
                    #validar tipo de dato argumento vs tipo de columna
                    validatio = self.TypeValidation(columna, arg, data)
                    if isinstance(validatio, Error) :
                        return validatio

                    break
                colPosition += 1

            if not found :
                error = Error('Semántico', 'Error(???): El campo '+asignacion.columnid.column.upper()+' no pertence a la tabla ' + self.tableid.table.upper(), 0, 0)
                return error

            register[colPosition] = arg.val

        #mandar a condiciones
        # Send to execute condition
        filas = extractTable(data.databaseSeleccionada, self.tableid.table.upper())
        #print(filas)
        if filas == None :
            error = Error('Semántico', 'Error(???): no existe la tabla ' + self.tableid.table.upper(), 0, 0)
            return error
        elif filas == [] :
            error = Error('Semántico', 'Error(???): La tabla ' + self.tableid.table.upper()+' está vacía.', 0, 0)
            return error

        pks = []
        contp = 0
        for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.tableid.table.upper()]['columns'] :
            if col.pk != None :
                if col.pk.val :
                    pks.append(contp)
            contp += 1



        if self.condiciones == None :
            'Se cambian todas los campos que vienen en el set'
            print(register)
            index = 0
            for fila in filas :
                rowlist = []
                if not pks == [] :
                    for pk in pks :
                        rowlist.append(fila[pk])
                else :
                    rowlist.append(index)
                    index += 1

                print(rowlist)

            index = 0
            for fila in filas :
                rowlist = []
                if not pks == [] :
                    for pk in pks :
                        rowlist.append(fila[pk])
                else :
                    rowlist.append(index)
                    index += 1

                reto = update(data.databaseSeleccionada, self.tableid.table.upper(), register, rowlist)

                if reto == 0:
                    print('Operación exitosa')
                elif reto == 1:
                    error = Error('Storage', 'Error(1): Error en la operación', 0, 0)
                    return error
                elif reto == 2:
                    error = Error('Storage', 'Error(2): Database no existente', 0, 0)
                    return error
                elif reto == 3:
                    error = Error('Storage', 'Error(3): Table no existente', 0, 0)
                    return error
                else :
                    error = Error('Storage', 'Error(4): Llave primaria inexistente', 0, 0)
                    return error


        else :
            #diccionario para mandar a condiciones:
            #dicciPrueba = {'NombreTabla1': {'fila': [1, 3, "f"], 'alias': 'nombre'}, 'NombreTabla2': {'fila': [], 'alias': None}}

            print(register)
            index = 0
            for fila in filas :
                condObj = {self.tableid.table.upper() : {'fila' : fila, 'alias':''}}

                toadd = self.condiciones.execute(data, condObj)
                if isinstance(toadd, Error):
                    return toadd


                rowlist = []
                if toadd :
                    if not pks == [] :
                        for pk in pks :
                            rowlist.append(fila[pk])
                    else :
                        rowlist.append(index)

                    print(rowlist)

                index += 1


            index = 0
            for fila in filas :
                condObj = {self.tableid.table.upper() : {'fila' : fila, 'alias':''}}

                toadd = self.condiciones.execute(data, condObj)
                if isinstance(toadd, Error):
                    return toadd


                rowlist = []
                if toadd :
                    if not pks == [] :
                        for pk in pks :
                            rowlist.append(fila[pk])
                    else :
                        rowlist.append(index)

                    reto = update(data.databaseSeleccionada, self.tableid.table.upper(), register, rowlist)

                    if reto == 0:
                        print('Operación exitosa')
                    elif reto == 1:
                        error = Error('Storage', 'Error(1): Error en la operación', 0, 0)
                        return error
                    elif reto == 2:
                        error = Error('Storage', 'Error(2): Database no existente', 0, 0)
                        return error
                    elif reto == 3:
                        error = Error('Storage', 'Error(3): Table no existente', 0, 0)
                        return error
                    else :
                        error = Error('Storage', 'Error(4): Llave primaria inexistente', 0, 0)
                        return error

                index += 1

        #return self.tableid

    def TypeValidation(self, columna, arg, data):
        #default error
        error = Error('Semántico', 'Error de Tipos(???): El tamaño del dato insertado en ' + columna.name + ' es incorrecto.', 0, 0)
        #validations
        if columna.type == 'smallint':
            if isinstance(arg.val, int):
                if arg.val >= -32768 and arg.val <= 32767:
                    return 'correcto'
                else:
                    return error
            else:
                return error
        elif columna.type == 'integer' or columna.type == 'numeric' or columna.type == 'int':
            if isinstance(arg.val, int):
                if arg.val >= -2147483648 and arg.val <= 2147483647:
                    return 'correcto'
                else:
                    return error
            else:
                return error
        elif columna.type == 'bigint':
            if isinstance(arg.val, int):
                if arg.val >= -9223372036854775808 and arg.val <= 9223372036854775807:
                    return 'correcto'
                else:
                    return error
            else:
                return error
        elif columna.type == 'decimal':
            if isinstance(arg.val, int): arg.val = float(arg.val)
            if isinstance(arg.val, float):
                if arg.val >= -9223372036854775808 and arg.val <= 9223372036854775807:
                    return 'correcto'
                else:
                    return error
            else:
                return error
        elif columna.type == 'real':
            if isinstance(arg.val, int) or isinstance(arg.val, float):
                round(arg.val, 6)
                return 'correcto'
            else:
                return error
        elif columna.type == 'double':
            if isinstance(arg.val, int) or isinstance(arg.val, float):
                round(arg.val, 15)
                return 'correcto'
            else:
                return error
        elif columna.type == 'money':
            if isinstance(arg.val, str):
                if isinstance(arg.val[0] == '$'):
                    if isinstance(arg.val[1], int):
                        arg.val = arg.val.replace("$", "")
                        arg.val = int(arg.val)
                        return 'correcto'
                    else:
                        return error
            else:
                if arg.val >= -92233720368547758.08 and arg.val <= 92233720368547758.07:
                    arg.val = int(arg.val)
                    return arg
                else :
                    return error
        elif columna.type == 'character' or columna.type == 'varchar' or columna.type == 'char': #-------------FALTA EL CHAR
            if isinstance(arg.val, str):
                if columna.size >= len(arg.val):
                    return 'correcto'
                else:
                    return error
            else:
                return error
        elif columna.type == 'text':
            if isinstance(arg.val, str):
                return 'correcto'
            else:
                return error
        elif columna.type == 'time':
            try:
                hora = arg.val
                horaVal = datetime.strptime(hora, '%H:%M:%S')
                arg.val = horaVal.strftime('%H:%M:%S')
                return arg
            except ValueError:
                return error
        elif columna.type == 'date':
            try:
                fecha = arg.val
                fechaVal = datetime.strptime(fecha, '%d-%m-%Y')
                arg.val = fechaVal.strftime('%d-%m-%Y %H:%M:%S')
                return arg
            except ValueError:
                return error

        elif columna.type == 'boolean':
            if isinstance(arg.val, str):
                if arg.val.lower() == 'yes' or arg.val.lower() == 'on' or arg.val.lower() == 'no' or arg.val.lower() == 'off':
                    return arg
                else:
                    return error
            elif isinstance(arg.val, bool) :
                return arg
            else:
                if arg.val == 1 or arg.val == 0:
                    return arg
                else:
                    return error

        else:
            #print(data.tablaSimbolos[data.databaseSeleccionada]['enum'])
            #for valoresEnum in data.tablaSimbolos[data.databaseSeleccionada]['enum'][columna.type]:
            if not data.tablaSimbolos[data.databaseSeleccionada]['enum'] == {} :
                for valoresEnum in data.tablaSimbolos[data.databaseSeleccionada]['enum'][columna.type]:
                    if arg.val == valoresEnum.val:
                        return arg

            return error



    def __repr__(self):
        return str(self.__dict__)


class AsignacionUpdate(Instruccion):

    def __init__(self, columnid, argument):
        self.columnid = columnid
        self.argument = argument

    def execute(self, datos):

        return self.tableid

    def __repr__(self):
        return str(self.__dict__)
