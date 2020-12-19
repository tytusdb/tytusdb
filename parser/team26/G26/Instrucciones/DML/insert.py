import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Librerias/storageManager')

from jsonMode import *
from instruccion import *
from Lista import *
from TablaSimbolos import *
from datetime import *

class Insert(Instruccion):

    def __init__(self, tableid, values = []):
        self.tableid = tableid
        self.values = values

    def execute(self, data):
        valoresTabla = []
        for val in self.values:
            valor = val.execute()
            valoresTabla.append(valor.val)

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
                    return 'Error(54023): too_many_arguments'

            dentroRango = True
            valExtra = False

            try:
                prueba = valoresTabla[posColumna]
            except IndexError:
                dentroRango = False
                comprobarNull = True
                valExtra = True
                print('ERROR INDEX')

            if dentroRango:
                if columna.type == 'smallint':
                    if isinstance(valoresTabla[posColumna], int):
                        if valoresTabla[posColumna] >= -32768 and valoresTabla[posColumna] <= 32767:
                            print('correcto.')
                        else:
                            mensajeError = 'Error(???): El tamaño del dato insertado en ' + columna.name + ' es incorrecto.'
                            comprobarNull = True
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                elif columna.type == 'integer' or columna.type == 'numeric':
                    print(columna.type)
                    print(valoresTabla[posColumna])
                    print(isinstance(valoresTabla[posColumna], int))
                    if isinstance(valoresTabla[posColumna], int):
                        if valoresTabla[posColumna] >= -2147483648 and valoresTabla[posColumna] <= 2147483647:
                            print('correcto.')
                        else:
                            mensajeError = 'Error(???): El tamaño del dato insertado en ' + columna.name + ' es incorrecto.'
                            comprobarNull = True
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'

                elif columna.type == 'bigint':
                    if isinstance(valoresTabla[posColumna], int):
                        if valoresTabla[posColumna] >= -9223372036854775808 and valoresTabla[posColumna] <= 9223372036854775807:
                            print('correcto.')
                        else:
                            mensajeError = 'Error(???): El tamaño del dato insertado en ' + columna.name + ' es incorrecto.'
                            comprobarNull = True
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'

                elif columna.type == 'decimal':
                    if isinstance(valoresTabla[posColumna], int): valoresTabla[posColumna] = float(valoresTabla[posColumna])
                    if isinstance(valoresTabla[posColumna], float):
                        if valoresTabla[posColumna] >= -9223372036854775808 and valoresTabla[posColumna] <= 9223372036854775807:
                            print('correcto.')
                        else:
                            mensajeError = 'Error(???): El tamaño del dato insertado en ' + columna.name + ' es incorrecto.'
                            comprobarNull = True
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                elif columna.type == 'real':
                    if isinstance(valoresTabla[posColumna], int) or isinstance(valoresTabla[posColumna], float):
                        round(valoresTabla[posColumna], 6)
                        print('correcto')
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                elif columna.type == 'double':
                    if isinstance(valoresTabla[posColumna], int) or isinstance(valoresTabla[posColumna], float):
                        round(valoresTabla[posColumna], 15)
                        print('correcto')
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                elif columna.type == 'money':
                    if isinstance(valoresTabla[posColumna], str):
                        if isinstance(valoresTabla[posColumna][0] == '$'):
                            if isinstance(valoresTabla[posColumna][1], int):
                                print('correcto')
                            else:
                                if tamanioInferior:
                                    comprobarNull = True
                                else:
                                    return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                    else:
                        if valoresTabla[posColumna] >= -92233720368547758.08 and valoresTabla[posColumna] <= 92233720368547758.07:
                            valoresTabla[posColumna] = '$' + str(valoresTabla[posColumna])
                            print('correcto')
                        else :
                            if tamanioInferior:
                                comprobarNull = True
                            else:
                                return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                elif columna.type == 'character' or columna.type == 'varchar' or columna.type == 'char': #-------------FALTA EL CHAR
                    if isinstance(valoresTabla[posColumna], str):
                        print(columna.size)
                        print(len(valoresTabla[posColumna]))
                        if columna.size >= len(valoresTabla[posColumna]):
                            print('correct')
                        else:
                            if tamanioInferior:
                                comprobarNull = True
                            else:
                                return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                    else:
                        mensajeError = 'Error(???): El tipo de dato insertado en la columna ' + columna.name + ' es incorrecto.'
                        comprobarNull = True
                elif columna.type == 'text':
                    if isinstance(valoresTabla[posColumna], str):
                        print('correct')
                    else:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                elif columna.type == 'time':
                    try:
                        hora = valoresTabla[posColumna]
                        horaVal = datetime.strptime(hora, '%H:%M:%S')
                        valoresTabla[posColumna] = horaVal.strftime('%H:%M:%S')
                    except ValueError:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                elif columna.type == 'date':
                    try:
                        fecha = valoresTabla[posColumna]
                        fechaVal = datetime.strptime(fecha, '%d-%m-%Y')
                        valoresTabla[posColumna] = fechaVal.strftime('%d-%m-%Y %H:%M:%S')
                    except ValueError:
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                elif columna.type == 'boleano':
                    if isinstance(valoresTabla[posColumna], str):
                        if valoresTabla[posColumna].lower() == 'true' or valoresTabla[posColumna].lower() == 'yes' or valoresTabla[posColumna].lower() == 'on' or valoresTabla[posColumna].lower() == 'false' or valoresTabla[posColumna].lower() == 'no' or valoresTabla[posColumna].lower() == 'off':
                            print('correcto')
                        else:
                            if tamanioInferior:
                                comprobarNull = True
                            else:
                                return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                    elif bool(valoresTabla[posColumna]):
                        print('correct')
                    else:
                        if valoresTabla[posColumna] == 1 or valoresTabla[posColumna] == 0:
                            print('correcto')
                        else:
                            if tamanioInferior:
                                comprobarNull = True
                            else:
                                return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'
                else:
                    saltarValor = True
                    for valoresEnum in data.tablaSimbolos[data.databaseSeleccionada]['enum'][columna.type]:
                        if valoresTabla[posColumna] == valoresEnum.val:
                            print('correcto')
                            saltarValor = False
                    if saltarValor :
                        if tamanioInferior:
                            comprobarNull = True
                        else:
                            return 'Error(???): El tipo de la columna ' + columna.name + ' es incorrecto.'

            compDefault = False
            if columna.unique != None:
                tablaExtraida = extractTable(data.databaseSeleccionada, self.tableid.upper())
                for fila in tablaExtraida:
                    if fila[posColumna] == valoresTabla[posColumna]:
                        return 'Error(???): Debe insertarse un valor unico en ' + columna.name

            nullInsertado = False
            if columna.null != None and comprobarNull and tamanioInferior:
                compDefault = True
                if columna.null.val:
                    valoresTabla = self.insertarValor(valoresTabla, 'null', posColumna, valExtra)
                    nullInsertado = True

            defaultInsertado = False
            if columna.default != None and compDefault:
                if nullInsertado:
                    valoresTabla[posColumna] = columna.default.val.val
                else:
                    valoresTabla = self.insertarValor(valoresTabla, columna.default.val.val, posColumna, valExtra)
                defaultInsertado = True

            if columna.check != None:
                print(columna.check)
                if columna.check.val.executeInsert(data, listaColumnas, valoresTabla, posColumna):
                    ''
                else:
                    return 'Error(???): El valor no cumple con el check de la columna' + columna.name + '.'

            posColumna += 1

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
            print(nuevoArreglo)
            return nuevoArreglo
