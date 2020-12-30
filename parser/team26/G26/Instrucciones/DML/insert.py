import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Librerias/storageManager')

from jsonMode import *
from instruccion import *
from Lista import *
from TablaSimbolos import *
from datetime import *
from Error import *

class Insert(Instruccion):

    def __init__(self, tableid, values = []):
        self.tableid = tableid
        self.values = values

    def execute(self, data):
        valoresTabla = []
        for val in self.values:
            try:
                valor = val.execute()
            except:
                valor = val.execute(data, None)
            valoresTabla.append(valor.val)

        if not self.tableid.upper() in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
            error = Error('Semántico', 'Error(23503): La tabla ' + self.tableid.upper() + ' no existe.', 0, 0)
            return error

        listaColumnas = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][self.tableid.upper()]['columns']

        tamanioInferior = False

        datosColumna = extractTable(data.databaseSeleccionada, self.tableid.upper())

        posColumna = 0
        mensajeError = None
        comprobarNull = False

        for columna in listaColumnas:

            tamanioInferior = False

            if len(valoresTabla) != len(listaColumnas):
                if len(valoresTabla) < len(listaColumnas):
                    tamanioInferior = True
                elif len(valoresTabla) > len(listaColumnas):
                    error = Error('Semántico', 'Error(54023): too_many_arguments.', 0, 0)
                    return error

            dentroRango = True
            valExtra = False

            try:
                prueba = valoresTabla[posColumna]
            except IndexError:
                dentroRango = False
                comprobarNull = True
                valExtra = True
                #print('ERROR INDEX')

            if dentroRango:
                tipo = ""
                try:
                    tipo = (columna.type)
                except:
                    tipo = columna['type']
                if tipo == 'smallint':
                    if isinstance(valoresTabla[posColumna], int):
                        if valoresTabla[posColumna] >= -32768 and valoresTabla[posColumna] <= 32767:
                            ''
                        else:
                            mensajeError = 'Error(???): El tamaño del dato insertado en ' + columna.name + ' es incorrecto.'
                            comprobarNull = True
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                elif tipo == 'integer' or tipo == 'numeric':
                    if isinstance(valoresTabla[posColumna], int):
                        if valoresTabla[posColumna] >= -2147483648 and valoresTabla[posColumna] <= 2147483647:
                            ''
                        else:
                            mensajeError = 'Error(???): El tamaño del dato insertado en ' + columna.name + ' es incorrecto.'
                            comprobarNull = True
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                            return error

                elif tipo == 'bigint':
                    if isinstance(valoresTabla[posColumna], int):
                        if valoresTabla[posColumna] >= -9223372036854775808 and valoresTabla[posColumna] <= 9223372036854775807:
                            ''
                        else:
                            mensajeError = 'Error(???): El tamaño del dato insertado en ' + columna.name + ' es incorrecto.'
                            comprobarNull = True
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                            return error

                elif tipo == 'decimal':
                    if isinstance(valoresTabla[posColumna], int): valoresTabla[posColumna] = float(valoresTabla[posColumna])
                    if isinstance(valoresTabla[posColumna], float):
                        if valoresTabla[posColumna] >= -9223372036854775808 and valoresTabla[posColumna] <= 9223372036854775807:
                            ''
                        else:
                            mensajeError = 'Error(???): El tamaño del dato insertado en ' + columna.name + ' es incorrecto.'
                            comprobarNull = True
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                            return error
                elif tipo == 'real':
                    if isinstance(valoresTabla[posColumna], int) or isinstance(valoresTabla[posColumna], float):
                        round(valoresTabla[posColumna], 6)
                        ''
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                            return error
                elif tipo == 'double':
                    if isinstance(valoresTabla[posColumna], int) or isinstance(valoresTabla[posColumna], float):
                        round(valoresTabla[posColumna], 15)
                        ''
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                            return error
                elif tipo == 'money':
                    if isinstance(valoresTabla[posColumna], str):
                        if (valoresTabla[posColumna][0] == '$'):
                            if isinstance(valoresTabla[posColumna][1], int):
                                ''
                            else:
                                if tamanioInferior:
                                    comprobarNull = True
                                else:
                                    error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                                    return error
                    else:
                        if valoresTabla[posColumna] >= -92233720368547758.08 and valoresTabla[posColumna] <= 92233720368547758.07:
                            valoresTabla[posColumna] = '$' + str(valoresTabla[posColumna])
                            ''
                        else :
                            if tamanioInferior:
                                comprobarNull = True
                            else:
                                error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                                return error
                elif tipo == 'character' or tipo == 'varchar' or tipo == 'char': #-------------FALTA EL CHAR
                    if isinstance(valoresTabla[posColumna], str):
                        valor = 0
                        if columna.type == 'character' :
                            valor = columna.size.varying
                        else :
                            valor = columna.size
                        if valor >= len(valoresTabla[posColumna]):
                            ''
                        else:
                            if tamanioInferior:
                                comprobarNull = True
                            else:
                                error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                                return error
                    else:
                        mensajeError = 'Error(???): El tipo de dato insertado en la columna ' + columna.name + ' es incorrecto.'
                        comprobarNull = True
                elif tipo == 'text':
                    if isinstance(valoresTabla[posColumna], str):
                        ''
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                            return error
                elif tipo == 'time':
                    try:
                        hora = valoresTabla[posColumna]
                        horaVal = datetime.strptime(hora, '%H:%M:%S')
                        valoresTabla[posColumna] = horaVal.strftime('%H:%M:%S')
                    except:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                            return error
                elif tipo == 'date':
                    try:
                        fecha = valoresTabla[posColumna]
                        fechaN = fecha.replace('/', '-')
                        fechaVal = datetime.strptime(fechaN, '%Y-%m-%d')
                        valoresTabla[posColumna] = fechaVal.strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        try:
                            fecha = valoresTabla[posColumna]
                            fechaN = fecha.replace('/', '-')
                            fechaVal = datetime.strptime(fechaN, '%Y-%m-%d %H:%M:%S')
                            valoresTabla[posColumna] = fechaVal.strftime('%Y-%m-%d %H:%M:%S')
                        except:
                            if tamanioInferior:
                                comprobarNull = True
                            else:
                                error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                                return error
                elif tipo == 'boolean':
                    if isinstance(valoresTabla[posColumna], str):
                        if valoresTabla[posColumna].lower() == 'true' or valoresTabla[posColumna].lower() == 'yes' or valoresTabla[posColumna].lower() == 'on' or valoresTabla[posColumna].lower() == 'false' or valoresTabla[posColumna].lower() == 'no' or valoresTabla[posColumna].lower() == 'off':
                            ''
                        else:
                            if tamanioInferior:
                                comprobarNull = True
                            else:
                                error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                                return error
                    elif bool(valoresTabla[posColumna]):
                        ''
                    else:
                        if valoresTabla[posColumna] == 1 or valoresTabla[posColumna] == 0:
                            ''
                        else:
                            if tamanioInferior:
                                comprobarNull = True
                            else:
                                error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                                return error
                else:
                    saltarValor = True
                    for valoresEnum in data.tablaSimbolos[data.databaseSeleccionada]['enum'][columna.type]:
                        if valoresTabla[posColumna] == valoresEnum.val:
                            ''
                            saltarValor = False
                    if saltarValor :
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            error = Error('Semántico', 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.', 0, 0)
                            return error

            compDefault = False
            columnn = ""
            try:
                columnn = columna.unique
            except:
                columnn = columna['unique']
            if columnn != None:
                tablaExtraida = extractTable(data.databaseSeleccionada, self.tableid.upper())
                for fila in tablaExtraida:
                    if fila[posColumna] == valoresTabla[posColumna]:
                        error = Error('Semántico', 'Error(???): Debe insertarse un valor unico en ' + columna.name, 0, 0)
                        return error

            nullInsertado = False
            nulll = ""
            try:
                nulll = columna.null
            except:
                nulll = columna['null']
            if nulll != None and comprobarNull and tamanioInferior:
                compDefault = True
                if nulll:
                    valoresTabla = self.insertarValor(valoresTabla, 'null', posColumna, valExtra)
                    nullInsertado = True

            defaultInsertado = False
            comprobarNull = False
            tamanioInferior = False
            defff = ""
            try:
                defff = columna.default
            except:
                defff = columna['default']
            if defff != None and compDefault:
                if nullInsertado:
                    valoresTabla[posColumna] = columna.default.val.val
                else:
                    valoresTabla = self.insertarValor(valoresTabla, columna.default.val.val, posColumna, valExtra)
                defaultInsertado = True
            checkk = ""
            try:
                checkk = columna.check
            except:
                checkk = columna['check']
            if checkk != None:
                diccionarioTabla = {}
                diccionarioTabla[self.tableid.upper()] = {'fila': valoresTabla, 'alias': None}
                for chk in checkk :
                    if chk == None:
                        continue
                    try:
                        pruebabool = chk.val.executeInsert(data, diccionarioTabla)
                    except :
                        pruebabool = chk.val.execute(data, diccionarioTabla)

                    if pruebabool :
                        ''
                    else:
                        error = Error('Semántico', 'Error(???): El valor no cumple con el check de la columna' + columna.name + '.', 0, 0)
                        return error

             #validando foreign keys
            forr = ""
            try:
                forr = columna.fk
            except:
                forr = columna['fk']
            try:
                for fk in forr :
                    'validar las foreign keys alv :,VVV'
                    if fk == None :
                        continue
                    #obteniendo el index de la PK
                    colindex = 0
                    for col in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][fk.val.table]['columns'] :
                        if col.name == fk.val.column:
                            break
                        colindex += 1

                    #comparando si existe
                    filas = extractTable(data.databaseSeleccionada, fk.val.table) #obtengo filas de la tabla al que hago referencia
                    found = False #bndera para saber si se hizo match entre la referencia y el dato nuevo
                    for fila in filas :
                        if fila[colindex] == valoresTabla[posColumna]:  #revisando si se hizo match
                            found = True

                    if not found : #si no hay match, hay error
                        error = Error('Semántico', 'Error(???): La FK '+str(valoresTabla[posColumna])+' no concuerda con la PK de la tabla referenciada.', 0, 0)
                        return error
            except:
                print("")
            posColumna += 1

        if len(valoresTabla) != len(listaColumnas):
            if len(valoresTabla) < len(listaColumnas):
                error = Error('Semántico', 'Error(54023): not_enough_arguments.', 0, 0)
                return error
            elif len(valoresTabla) > len(listaColumnas):
                error = Error('Semántico', 'Error(54023): too_many_arguments.', 0, 0)
                return error

        valRetorno = insert(data.databaseSeleccionada, self.tableid.upper(), valoresTabla)

        if valRetorno == 0:
            return 'Se ha insertado correctamente.'
        elif valRetorno == 1:
            return 'Error(???): unknown_error'
        elif valRetorno == 2:
            return 'Error(???): No existe la base de datos ' + data.databaseSeleccionada
        elif valRetorno == 3:
            return 'Error(???): No existe la tabla ' + self.tableid.upper()
        elif valRetorno == 4:
            return 'Error(???): Llave primaria duplicada.'
        elif valRetorno == 5:
            return 'Error(54023): too_many_arguments'

        return self

    def __repr__(self):
        return str(self.__dict__)

    def insertarValor(self, data, valorInsertar, posicion, extra):
        if extra:
            data.append(valorInsertar)
            return data
        else:
            contador = 0
            contadorPos = 0
            nuevoArreglo = []
            for columnas in data:
                if contador == posicion:
                    nuevoArreglo.append(valorInsertar)
                    nuevoArreglo.append(data[contadorPos])
                    contadorPos -= 1
                else:
                    nuevoArreglo.append(data[contadorPos])
                contador += 1
                contadorPos += 1
            return nuevoArreglo
