from G26.Expresiones.Primitivo import Primitive
import sys
sys.path.append('../team01/G26/Instrucciones')
sys.path.append('../team01/G26/Utils')
sys.path.append('../team01/G26/Expresiones')
sys.path.append('../team01/G26/Librerias/storageManager')
sys.path.append('../team01/G26/Librerias/prettytable')

from jsonMode import *
from instruccion import *
from Error import *
from Primitivo import *
from datetime import *
from TablaSimbolos import *
from prettytable import *
from operator import itemgetter
from Identificador import *

import math
import random
import hashlib

class Select(Instruccion):

    global columnasAceptadas

    def __init__(self, parametros, fromopcional):
        self.parametros = parametros
        self.fromopcional = fromopcional

    def execute(self, data):
        fromData = self.fromopcional
        if fromData == None:
            diccionarioColumnasAceptadas = {}
            nuevaColumna = []
            i = 0
            contadorNombre = 0
            nombreTabla = ''
            select = self.parametros
            columnasImprimir = select.listadeseleccion
            for columnasSeleccionadas in columnasImprimir:
                nombreColumna = columnasSeleccionadas.listaseleccionados

                while True:
                    try:
                        if contadorNombre == 0: nombreTabla = nombreColumna.tipofuncionmatematica
                        else: nombreTabla = nombreColumna.tipofuncionmatematica + str(contadorNombre)
                    except:
                        try:
                            if nombreColumna.operador == 'md5':
                                return Error('Sintactico', 'El md5 solamente puede venir en el insert y update', 0, 0)
                            if contadorNombre == 0: nombreTabla = nombreColumna.operador
                            else: nombreTabla = nombreColumna.operador + str(contadorNombre)
                        except:
                            try:
                                if contadorNombre == 0: nombreTabla = nombreColumna.tipofuncionTrigonometrica
                                else: nombreTabla = nombreColumna.tipofuncionTrigonometrica + str(contadorNombre)
                            except:
                                try:
                                    if contadorNombre == 0: nombreTabla = nombreColumna.tipofuncionfehca
                                    else: nombreTabla = nombreColumna.tipofuncionfehca + str(contadorNombre)
                                except:
                                    if contadorNombre == 0: nombreTabla = nombreColumna.val
                                    else: nombreTabla = nombreColumna.val + str(contadorNombre)

                    try:
                        s = diccionarioColumnasAceptadas[nombreTabla]
                        contadorNombre = contadorNombre + 1
                    except:
                        break

                try:
                    comprobar = nombreColumna.execute(data, None)
                except:
                    comprobar = nombreColumna.execute()

                if isinstance(comprobar, Error):
                    return comprobar

                diccionarioColumnasAceptadas[nombreTabla] = {'columnas': [], 'tipo': ''}

                diccionarioColumnasAceptadas[nombreTabla]['columnas'].append([comprobar.val])
                diccionarioColumnasAceptadas[nombreTabla]['tipo'] = comprobar.type

            return diccionarioColumnasAceptadas


        tablas = fromData.execute(data).execute(data)
        where = tablas.whereopcional
        directorioTablas = {}
        tablasFromTemporales = []
        columnasFromTemporales = {}

        for tablasSeleccionadas in tablas.parametros:
            if isinstance(tablasSeleccionadas.parametros.operador, Select):
                tablas = tablasSeleccionadas.parametros.operador.execute(data)
                if isinstance(tablas, Error):
                    return tablas
                if tablasSeleccionadas.asop == None:
                    return Error('Sintactico', 'Se esperaba As o un Alias.', 0, 0)
                else:
                    tablasFromTemporales.append(tablas)
                    contador = 0
                    nombre = ''
                    while True:
                        try:
                            if contador == 0:
                                nombre = tablasSeleccionadas.asop.upper()
                            else:
                                nombre = tablasSeleccionadas.asop.upper() + str(contador)
                            prueba = data.tablaSimbolos[data.databaseSeleccionada]['tablas'][nombre]
                            contador = contador + 1
                        except:
                            data.tablaSimbolos[data.databaseSeleccionada]['tablas'][nombre] = {'columns': []}
                            break

                    directorioNombres = []
                    for keysTemporales in tablas.keys():
                        eliminarPunto = False
                        nombreNuevo = ''
                        for letras in keysTemporales:
                            if eliminarPunto:
                                nombreNuevo = nombreNuevo + letras

                            if letras == '.':
                                eliminarPunto = True

                        directorioNombres.append({'viejo': keysTemporales, 'nuevo': nombreNuevo})

                        data.tablaSimbolos[data.databaseSeleccionada]['tablas'][nombre]['columns'].append(TableData(nombreNuevo, tablas[keysTemporales]['tipo'], None, None, None, None, None, None, None))

                    for nombres in directorioNombres:
                        tablas[nombres['nuevo']] = tablas.pop(nombres['viejo'])

                    juntarValores = []
                    inicio = 0
                    for keys in tablas.keys():
                        contador = 0
                        for val in tablas[keys]['columnas']:
                            if inicio == 0:
                                juntarValores.append(val)
                            else:
                                juntarValores[contador].append(val[0])
                            contador = contador + 1
                        inicio = inicio + 1

                    columnasFromTemporales[nombre] = juntarValores

                    directorioTablas[nombre] = {'fila' : None, 'alias': tablasSeleccionadas.asop.upper(), 'temporal': True}
            elif tablasSeleccionadas.asop == None:
                directorioTablas[tablasSeleccionadas.parametros.operador.upper()] = {'fila' : None, 'alias': '', 'temporal': False}
            else:
                directorioTablas[tablasSeleccionadas.parametros.operador.upper()] = {'fila' : None, 'alias': tablasSeleccionadas.asop.upper(), 'temporal': False}

        try:
            for keys in directorioTablas.keys():
                data.tablaSimbolos[data.databaseSeleccionada]['tablas'][keys]
        except:
            for borrarTemporales in columnasFromTemporales.keys():
                del(data.tablaSimbolos[data.databaseSeleccionada]['tablas'][borrarTemporales])
            return Error('Semántico', 'Error(42P01): undefined_table.', 0, 0)

        valores = []
        temporales = []
        columnasAceptadas = {}
        for keys in directorioTablas.keys():
            valores.append(keys)
            columnasAceptadas[keys] = []
            temporales.append(directorioTablas[keys]['temporal'])

        if where == None:
            val = self.funcionPosibilidades(data, valores, [], [], directorioTablas, True, columnasAceptadas, temporales, columnasFromTemporales)
        else:
            val = self.funcionPosibilidades(data, valores, [], [], directorioTablas, False, columnasAceptadas, temporales, columnasFromTemporales)

        if isinstance(val, Error):
            for borrarTemporales in columnasFromTemporales.keys():
                del(data.tablaSimbolos[data.databaseSeleccionada]['tablas'][borrarTemporales])
            return val

        select = self.parametros

        columnasImprimir = select.listadeseleccion

        diccionarioColumnasAceptadas = {}
        columnasAgregacion = []
        for columnasSeleccionadas in columnasImprimir:
            nombreColumna = columnasSeleccionadas.listaseleccionados
            if isinstance(nombreColumna, FuncionMatematicaSimple):
                columnasAgregacion.append(nombreColumna)
                continue
            try:
                retorno = nombreColumna.obtenerSeleccionado(data, directorioTablas, columnasAceptadas, diccionarioColumnasAceptadas)
                if isinstance(retorno, Error):
                    for borrarTemporales in columnasFromTemporales.keys():
                        del(data.tablaSimbolos[data.databaseSeleccionada]['tablas'][borrarTemporales])
                    return retorno
            except:
                cant = 0
                for keys in columnasAceptadas:
                    cant = len(columnasAceptadas[keys])
                    break

                nuevaColumna = []
                i = 0
                contadorNombre = 0
                nombreTabla = ''
                while True:
                    try:
                        if contadorNombre == 0: nombreTabla = nombreColumna.tipofuncionmatematica
                        else: nombreTabla = nombreColumna.tipofuncionmatematica + str(contadorNombre)
                    except:
                        try:
                            if nombreColumna.operador == 'md5':
                                return Error('Sintactico', 'El md5 solamente puede venir en el insert y update', 0, 0)
                            if contadorNombre == 0: nombreTabla = nombreColumna.operador
                            else: nombreTabla = nombreColumna.operador + str(contadorNombre)
                        except:
                            try:
                                if contadorNombre == 0: nombreTabla = nombreColumna.tipofuncionTrigonometrica
                                else: nombreTabla = nombreColumna.tipofuncionTrigonometrica + str(contadorNombre)
                            except:
                                try:
                                    if contadorNombre == 0: nombreTabla = nombreColumna.tipofuncionfehca
                                    else: nombreTabla = nombreColumna.tipofuncionfehca + str(contadorNombre)
                                except:
                                    if contadorNombre == 0: nombreTabla = nombreColumna.val
                                    else: nombreTabla = nombreColumna.val + str(contadorNombre)

                    try:
                        a = diccionarioColumnasAceptadas[nombreTabla]
                        contadorNombre = contadorNombre + 1
                    except:
                        diccionarioColumnasAceptadas[nombreTabla] = {'columnas': [], 'tipo': ''}
                        break;

                while True:
                    if i == cant:
                        break;
                    for keys in columnasAceptadas:
                        directorioTablas[keys]['fila'] = columnasAceptadas[keys][i]
                    try:
                        comprobar = nombreColumna.execute(data, directorioTablas)
                    except:
                        comprobar = nombreColumna.execute()

                    if isinstance(comprobar, Error):
                        return comprobar

                    diccionarioColumnasAceptadas[nombreTabla]['columnas'].append([comprobar.val])
                    diccionarioColumnasAceptadas[nombreTabla]['tipo'] = comprobar.type
                    i = i + 1


        if select.distinct:
            juntarValores = []
            inicio = 0

            for keys in diccionarioColumnasAceptadas.keys():
                contador = 0
                for val in diccionarioColumnasAceptadas[keys]['columnas']:
                    if inicio == 0:
                        juntarValores.append(val)
                    else:
                        juntarValores[contador].append(val[0])
                    contador = contador + 1
                inicio = inicio + 1

            contador = 0
            nuevoArregloDistinct = []

            routes = juntarValores
            dups = set()

            duplicadas = 0
            for route in routes:
                if tuple(route) in dups:
                    duplicadas = duplicadas + 1
                else:
                    nuevoArregloDistinct.append(route)
                    dups.add(tuple(route))
            contador = contador + 1

            if duplicadas == 0:
                nuevoArregloDistinct = juntarValores

            contador = 0
            for tablas in diccionarioColumnasAceptadas.keys():
                datosTablas = diccionarioColumnasAceptadas[tablas]
                columnaSelect = []
                for filaActual in nuevoArregloDistinct:
                    columnaSelect.append([filaActual[contador]])
                diccionarioColumnasAceptadas[tablas]['columnas'] = columnaSelect
                contador = contador + 1

        whereOpcional = True
        groupByOpcional = False
        groupByData = None
        if self.fromopcional.whereopcional == None and self.fromopcional.groupbyopcional == None:
            ''
        else:
            if self.fromopcional.groupbyopcional == None:
                groupByData = self.fromopcional.whereopcional.groupbyopcional
                groupByOpcional = True
            else:
                groupByData = self.fromopcional.groupbyopcional
                whereOpcional = False
                groupByOpcional = True

        if groupByData == None:
            bFlag = False
            cantColumnas = 0
            for columnasSeleccionadas in columnasImprimir:
                nombreColumna = columnasSeleccionadas.listaseleccionados
                cantColumnas = cantColumnas + 1
                if isinstance(nombreColumna, FuncionMatematicaSimple):
                    if nombreColumna.operador == 'max' or nombreColumna.operador == 'min' or nombreColumna.operador == 'count':
                        bFlag = True
                    else:
                        return Error('Semantico', 'Solo MAX, MIN y COUNT se pueden realizar sin GROUP BY.', 0, 0)

            if bFlag:
                for columnasSeleccionadas in columnasImprimir:
                    nombreColumna = columnasSeleccionadas.listaseleccionados
                    try:
                        a = Identificador('*', None)
                        retorno = a.obtenerSeleccionado(data, directorioTablas, columnasAceptadas, diccionarioColumnasAceptadas)

                        if isinstance(retorno, Error):
                            for borrarTemporales in columnasFromTemporales.keys():
                                del(data.tablaSimbolos[data.databaseSeleccionada]['tablas'][borrarTemporales])
                            return retorno
                    except:
                        cant = 0
                        for keys in columnasAceptadas:
                            cant = len(columnasAceptadas[keys])
                            break

                        nuevaColumna = []
                        i = 0
                        contadorNombre = 0
                        nombreTabla = ''
                        while True:
                            try:
                                if contadorNombre == 0: nombreTabla = nombreColumna.tipofuncionmatematica
                                else: nombreTabla = nombreColumna.tipofuncionmatematica + str(contadorNombre)
                            except:
                                try:
                                    if nombreColumna.operador == 'md5':
                                        return Error('Sintactico', 'El md5 solamente puede venir en el insert y update', 0, 0)
                                    if contadorNombre == 0: nombreTabla = nombreColumna.operador
                                    else: nombreTabla = nombreColumna.operador + str(contadorNombre)
                                except:
                                    try:
                                        if contadorNombre == 0: nombreTabla = nombreColumna.tipofuncionTrigonometrica
                                        else: nombreTabla = nombreColumna.tipofuncionTrigonometrica + str(contadorNombre)
                                    except:
                                        try:
                                            if contadorNombre == 0: nombreTabla = nombreColumna.tipofuncionfehca
                                            else: nombreTabla = nombreColumna.tipofuncionfehca + str(contadorNombre)
                                        except:
                                            if contadorNombre == 0: nombreTabla = nombreColumna.val
                                            else: nombreTabla = nombreColumna.val + str(contadorNombre)

                            try:
                                a = diccionarioColumnasAceptadas[nombreTabla]
                                contadorNombre = contadorNombre + 1
                            except:
                                diccionarioColumnasAceptadas[nombreTabla] = {'columnas': [], 'tipo': ''}
                                break;

                        while True:
                            if i == cant:
                                break;
                            for keys in columnasAceptadas:
                                directorioTablas[keys]['fila'] = columnasAceptadas[keys][i]
                                print(directorioTablas)
                            try:
                                comprobar = nombreColumna.execute(data, directorioTablas)
                            except:
                                comprobar = nombreColumna.execute()

                            if isinstance(comprobar, Error):
                                return comprobar

                            diccionarioColumnasAceptadas[nombreTabla]['columnas'].append([comprobar.val])
                            diccionarioColumnasAceptadas[nombreTabla]['tipo'] = comprobar.type
                            i = i + 1
                    break

                agregarColumnas = False
                columnasGNuevas = []
                for agregacion in columnasAgregacion:
                    val = agregacion.execute(data, {}, diccionarioColumnasAceptadas, columnasAceptadas)

                    if isinstance(val, Error):
                        for borrarTemporales in columnasFromTemporales.keys():
                            del(data.tablaSimbolos[data.databaseSeleccionada]['tablas'][borrarTemporales])
                        return val

                    columnasGNuevas.append(val)
                    agregarColumnas = True

                if len(columnasGNuevas) == cantColumnas:
                    diccionarioColumnasAceptadas = {}
                    for c in columnasGNuevas:
                        for v in c['val']:
                            valor = c['val'][v]
                        diccionarioColumnasAceptadas[c['name'].upper()] = {'columnas': [valor], 'tipo': c['type']}
                    return diccionarioColumnasAceptadas
                else:
                    return Error('Semantico', 'Se debe de utilizar el MAX, MIN o COUNT solos o con Group By.', 0, 0)
        else:
            if len(diccionarioColumnasAceptadas.keys()) == len(groupByData.lista):
                for keys in groupByData.lista:
                    if keys.column.upper() in diccionarioColumnasAceptadas:
                        ''
                    else:
                        return Error('Semantico', 'No se reconoce la columna ' + keys.column + '.', 0, 0)
            else:
                return Error('Semantico', 'Faltan columnas para agrupar en el group by.', 0, 0)

            columnasMostrar = diccionarioColumnasAceptadas
            juntarValoresN = []
            inicio = 0
            for keys in columnasMostrar.keys():
                contador = 0
                for val in columnasMostrar[keys]['columnas']:
                    if inicio == 0:
                        s = val.copy()
                        juntarValoresN.append(s)
                    else:
                        juntarValoresN[contador].append(val[0])
                    contador = contador + 1
                inicio = inicio + 1

            diccionarioAgrupacion = {}

            pos = 0
            for fila in juntarValoresN:
                nombre = ''
                for valorIndividual in fila:
                    nombre = nombre + str(valorIndividual)

                if nombre in diccionarioAgrupacion:
                    diccionarioAgrupacion[nombre].append(pos)
                else:
                    diccionarioAgrupacion[nombre] = []
                    diccionarioAgrupacion[nombre].append(pos)
                pos = pos + 1


            cambiarValores = False
            for keys in diccionarioColumnasAceptadas.keys():
                if len(diccionarioAgrupacion.keys()) < len(diccionarioColumnasAceptadas[keys]['columnas']):
                    cambiarValores = True
                break

            agregarColumnas = False
            columnasGNuevas = []

            for agregacion in columnasAgregacion:
                val = agregacion.execute(data, diccionarioAgrupacion, diccionarioColumnasAceptadas, columnasAceptadas)

                if isinstance(val, Error):
                    for borrarTemporales in columnasFromTemporales.keys():
                        del(data.tablaSimbolos[data.databaseSeleccionada]['tablas'][borrarTemporales])
                    return val

                columnasGNuevas.append(val)
                agregarColumnas = True

            if agregarColumnas or cambiarValores:
                juntarValores = []
                inicio = 0

                for keys in diccionarioColumnasAceptadas.keys():
                    contador = 0
                    for val in diccionarioColumnasAceptadas[keys]['columnas']:
                        if inicio == 0:
                            s = val.copy()
                            juntarValores.append(s)
                        else:
                            juntarValores[contador].append(val[0])
                        contador = contador + 1
                    inicio = inicio + 1

                contador = 0
                nuevoArregloDistinct = []

                routes = juntarValores
                dups = set()

                duplicadas = 0
                for route in routes:
                    if tuple(route) in dups:
                        duplicadas = duplicadas + 1
                    else:
                        nuevoArregloDistinct.append(route)
                        dups.add(tuple(route))
                    contador = contador + 1

                if duplicadas == 0:
                    nuevoArregloDistinct = juntarValores

                contador = 0
                for tablas in diccionarioColumnasAceptadas.keys():
                    datosTablas = diccionarioColumnasAceptadas[tablas]
                    columnaSelect = []
                    for filaActual in nuevoArregloDistinct:
                        columnaSelect.append([filaActual[contador]])
                    diccionarioColumnasAceptadas[tablas]['columnas'] = columnaSelect
                    contador = contador + 1

                for nuevas in columnasGNuevas:
                    cont = 0
                    for col in nuevas['val'].keys():
                        if cont == 0:
                            diccionarioColumnasAceptadas[nuevas['name']] = {'columnas': [], 'tipo': nuevas['type']}
                        diccionarioColumnasAceptadas[nuevas['name']]['columnas'].append(nuevas['val'][col])
                        cont = cont + 1

        if self.fromopcional.orderby != None:
            for ordenColumnas in self.fromopcional.orderby:
                nombre = ''
                if ordenColumnas.table != None:
                    nombre = ordenColumnas.table.upper() + '.'
                nombre = nombre + ordenColumnas.column.upper()
                try:
                    columna = diccionarioColumnasAceptadas[nombre]
                except:
                    for borrarTemporales in columnasFromTemporales.keys():
                        del(data.tablaSimbolos[data.databaseSeleccionada]['tablas'][borrarTemporales])
                    return Error('Semántico', 'Error(42P01): undefined_table. Descripcion: La columna ' + nombre + " no existe.", 0, 0)
                cont = 0
                vals = []
                tamanio = len(columna['columnas'])
                for val in columna['columnas']:
                    vals.append(cont)
                    cont = cont + 1
                self.quick_sort(columna['columnas'], vals,  0, tamanio - 1)
                diccionarioValoresNuevos = {}
                cont = 0
                for filas in diccionarioColumnasAceptadas.keys():
                    if filas == nombre:
                        continue
                    diccionarioValoresNuevos[filas] = {'columnas' : []}
                    for x in range(len(vals)):
                        diccionarioValoresNuevos[filas]['columnas'].append(diccionarioColumnasAceptadas[filas]['columnas'][vals[x]])
                    cont = cont + 1

                for llaves in diccionarioValoresNuevos.keys():
                    diccionarioColumnasAceptadas[llaves]['columnas'] = diccionarioValoresNuevos[llaves]['columnas']

        for borrarTemporales in columnasFromTemporales.keys():
            del(data.tablaSimbolos[data.databaseSeleccionada]['tablas'][borrarTemporales])

        return diccionarioColumnasAceptadas

    def __repr__(self):
        return str(self.__dict__)

    def partition(self, array, array2, start, end):
        pivot = array[start]
        low = start + 1
        high = end

        while True:

            while low <= high and array[high] >= pivot:
                high = high - 1


            while low <= high and array[low] <= pivot:
                low = low + 1

            if low <= high:
                array[low], array[high] = array[high], array[low]
                array2[low], array2[high] = array2[high], array2[low]
            else:
                break

        array[start], array[high] = array[high], array[start]
        array2[start], array2[high] = array2[high], array2[start]

        return high


    def quick_sort(self, array, array2, start, end):
        if start >= end:
            return

        p = self.partition(array, array2, start, end)
        self.quick_sort(array, array2, start, p-1)
        self.quick_sort(array, array2, p+1, end)


    def funcionPosibilidades(self, data, nombres, columna, nombreAux, ordenTablas, noWhere, columnasAceptadas, temporales, columnasFromTemporales):
        if len(nombres) == 0:
            if noWhere:
                val = 0
                for fila in columna:
                    columnasAceptadas[nombreAux[val]].append(fila)
                    val = val + 1
            else:
                val = 0
                for fila in columna:
                    ordenTablas[nombreAux[val]]['fila'] = fila
                    val = val + 1

                result = self.fromopcional.whereopcional.operador.execute(data, ordenTablas)
                if isinstance(result, Error):
                    return result

                if result:
                    val = 0
                    for fila in columna:
                        columnasAceptadas[nombreAux[val]].append(fila)
                        val = val + 1
            return 'fin'
        nombre = nombres[0]
        nombres.remove(nombre)
        temporal = temporales[0]
        temporales.pop(0)
        if temporal:
            filas = columnasFromTemporales[nombre]
        else:
            filas = extractTable(data.databaseSeleccionada, nombre)

        for fila in filas:
            s = fila
            columna.append(fila)
            nombreAux.append(nombre)
            comp = self.funcionPosibilidades(data, nombres, columna, nombreAux, ordenTablas, noWhere, columnasAceptadas, temporales, columnasFromTemporales)
            if isinstance(comp, Error):
                return comp
            columna.remove(s)
            nombreAux.remove(nombre)
        nombres.append(nombre)
        temporales.append(temporal)
        return 'hola'

    def ImprimirTabla(self, columnasMostrar):
        juntarValores = []
        inicio = 0
        for keys in columnasMostrar.keys():
            contador = 0
            for val in columnasMostrar[keys]['columnas']:
                if inicio == 0:
                    juntarValores.append(val)
                else:
                    juntarValores[contador].append(val[0])
                contador = contador + 1
            inicio = inicio + 1

        x = PrettyTable()

        keys = columnasMostrar.keys()
        x.field_names = keys
        x.add_rows(
            juntarValores
        )
        return x

class Casos(Instruccion):

    def __init__(self, caso,elsecase):
        self.caso = caso
        self.elsecase = elsecase

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class FromOpcional(Instruccion):

    def __init__(self, parametros, whereogroup, groupbyopcional, orderby):
        self.parametros = parametros
        self.whereopcional = whereogroup
        self.groupbyopcional = groupbyopcional
        self.orderby = orderby

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class ParametrosFromR(Instruccion):

    def __init__(self, parametros, asop):
        self.parametros = parametros
        self.asop = asop

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class ListaDeSeleccionadosConOperador(Instruccion):
    #puede venir grastest con arg1
    #least con arg 1
    #case con arg1 y 2
    def __init__(self, operador,arg1,arg2):
        self.operador = operador
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self,data, valoresTabla):
        if self.operador.upper() == 'CASE' :
            left = ''
            for arg in self.arg1 :
                condit = arg.caso.whenCase.execute(data, valoresTabla)

                if isinstance(condit, Error):
                    return condit

                if condit :
                    return Primitive(str(arg.caso.thenCase.type), arg.caso.thenCase.val)

                if arg.elsecase != None :
                    left = arg.elsecase.elseopcional
            if left == None :
                error = Error('Semántico', 'Error(????): Else case no específicado.', 0, 0)
                return error

            return left
        else :
            ''
            items = []
            tipo = None
            tipofecha = False
            for arg in self.arg1 :
                try:
                    resp = arg.execute(data, valoresTabla)
                except:
                    resp = arg.execute()

                if isinstance(resp, Error):
                    return resp

                if tipo == None :
                    tipo = resp.type
                elif tipo != resp.type :
                    error = Error('Semántico', 'Error(????): Error de tipos.', 0, 0)
                    return error

                if resp.type == 'string' :
                    try :
                        dextraccion = resp
                        fechacopleta = datetime.strptime(dextraccion.val,'%Y-%m-%d %H:%M:%S')
                        tipofecha = True
                    except :
                        try:
                            dextraccion = resp
                            fechacopleta = datetime.strptime(dextraccion.val,'%H:%M:%S')
                            tipofecha = True
                        except :
                            try :
                                dextraccion = resp
                                fechacopleta = datetime.strptime(dextraccion.val,'%Y-%m-%d')
                                tipofecha = True
                            except :
                                if tipofecha :
                                    error = Error('Semántico', 'Error(????): Error de tipos.', 0, 0)
                                    return error



                items.append(resp.val)

            if  self.operador.upper() == 'GREATEST' :

                try:
                    return Primitive('integer', int(max(items)))
                except:
                    return Primitive('string', max(items))

            else :
                'LEAST'
                return Primitive('string', min(items))

    def __repr__(self):
        return str(self.__dict__)

class ListaDeSeleccionados(Instruccion):
    #puede venir asterisco(*) entonces tipo == True
    #puede venir un select completo -> Tipo == False
    def __init__(self, argumento,tipo):
        self.argumento = argumento
        self.tipo = tipo

    def execute(self, data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class ElseOpcional(Instruccion):

    def __init__(self, elseopcional):
        self.elseopcional = elseopcional

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class QuerysSelect(Instruccion):

    def __init__(self, operador,select1,allopcional,select2):
        self.operador = operador
        self.select1 = select1
        self.allopcional = allopcional
        self.select2 = select2

    def execute(self,data):
        query1 = self.select1.execute(data)
        if isinstance(query1, Error):
            return query1

        query2 = self.select2.execute(data)
        if isinstance(query2, Error):
            return query2

        if len(query1.keys()) != len(query2.keys()):
            return Error('Semantico', 'La cantidad de columnas en el ' + self.operador + ' tiene que ser la misma.', 0, 0)

        if self.operador == 'union':
            keys2 = []
            for key in query2.keys():
                keys2.append(key)

            cont = 0
            for key in query1.keys():
                query1[key]['columnas'] = query1[key]['columnas'] + query2[keys2[cont]]['columnas']
                cont = cont + 1

            return query1

        elif self.operador == 'intersect':

            return query1

        return self

    def __repr__(self):
        return str(self.__dict__)

    def ImprimirTabla(self, columnasMostrar):
        juntarValores = []
        inicio = 0
        for keys in columnasMostrar.keys():
            contador = 0
            for val in columnasMostrar[keys]['columnas']:
                if inicio == 0:
                    juntarValores.append(val)
                else:
                    juntarValores[contador].append(val[0])
                contador = contador + 1
            inicio = inicio + 1

        x = PrettyTable()

        keys = columnasMostrar.keys()
        x.field_names = keys
        x.add_rows(
            juntarValores
        )
        return x

class ParametrosFrom(Instruccion):
    #true select
    #false id
    def __init__(self, parametro,tipoparametro):
        self.operador = parametro
        self.tipoparametro = tipoparametro

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class WhereOpcional(Instruccion):

    def __init__(self, condiciones,groupbyopcional):
        self.operador = condiciones
        self.groupbyopcional = groupbyopcional

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class GroupByOpcional(Instruccion):

    def __init__(self, lista,havingopcional):
        self.lista = lista
        self.havingopcional = havingopcional

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class HavingOpcional(Instruccion):

    def __init__(self, Condiciones):
        self.Condiciones = Condiciones

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class Allopcional(Instruccion):

    def __init__(self, allopcional):
        self.allopcional = allopcional

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class Case(Instruccion):

    def __init__(self, whenCase,thenCase):
        self.whenCase = whenCase
        self.thenCase = thenCase


    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class ListaDeSeleccionadosR(Instruccion):

    def __init__(self, listaseleccionados,asopcional):
        self.listaseleccionados = listaseleccionados
        self.asopcional = asopcional


    def execute(self, data):
        return self.listaseleccionados.execute(data)
        #return self

    def __repr__(self):
        return str(self.__dict__)

class ParametrosSelect(Instruccion):
    #true si hay distinct
    #false no hay distinct
    def __init__(self, distinct, listadeseleccion):
        self.distinct = distinct
        self.listadeseleccion = listadeseleccion

    def execute(self, data):
        if self.listadeseleccion != None:
            for selection in self.listadeseleccion:
                return selection.execute(data)
        return self

    def __repr__(self):
        return str(self.__dict__)

class As(Instruccion):

    def __init__(self, argumento):
        self.argumento = argumento

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class TipoRound(Instruccion):

    def __init__(self, arg1):
        self.arg1 = arg1

    def execute(self,data):
        return self

    def __repr__(self):
        return str(self.__dict__)

class FuncionBinaria(Instruccion):
    #convert tiene un tipo no un argumento
    def __init__(self, operador, arg1,arg2,arg3):
        self.operador = operador
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def execute(self, data, valoresTabla):
        tipo = str(self.operador)
        if tipo == 'length':
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'string' or argumento.type == 'ID' :
                return Primitive('integer',len(str(argumento.val)))
            else:
                error = Error('Semántico', 'Error de tipos en LENGTH, solo se aceptan valores de cadenas, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'substring' or tipo == 'substr':
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            try:
                argumento1 = self.arg2.execute()
            except:
                argumento1 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento1, Error):
                return argumento1

            try:
                argumento2 = self.arg3.execute()
            except:
                argumento2 = self.arg3.execute(data, valoresTabla)

            if isinstance(argumento2, Error):
                return argumento2

            if argumento.type == 'string' or argumento.type == 'ID' :
                return Primitive('integer',str(argumento.val)[argumento1.val:argumento2.val])
            else:
                error = Error('Semántico', 'Error de tipos en LENGTH, solo se aceptan valores de cadenas, se obtuvo: '+str(argumento.val),0,0)
                return error
        elif tipo == 'md5':
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'string' or argumento.type == 'ID' :
                textoaconvertir = str(argumento.val)
                md5_object = hashlib.md5(textoaconvertir.encode())
                md5_hash = md5_object.hexdigest()
                return Primitive('string',md5_hash)
            else:
                error = Error('Semántico', 'Error de tipos en MD5, solo se aceptan valores de cadenas, se obtuvo: '+str(argumento.val),0,0)
                return error
        elif tipo == 'sha256':
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'string' or argumento.type == 'ID' :
                textoaconvertir = str(argumento.val)
                sha256_object = hashlib.sha256(textoaconvertir.encode())
                sha256_hash = sha256_object.hexdigest()
                return Primitive('string',sha256_hash)
            else:
                error = Error('Semántico', 'Error de tipos en MD5, solo se aceptan valores de cadenas, se obtuvo: '+str(argumento.val),0,0)
                return error
        return self

    def __repr__(self):
        return str(self.__dict__)

class FucionTrigonometrica(Instruccion):

    def __init__(self, tipofuncionTrigonometrica, arg1,arg2):
        self.tipofuncionTrigonometrica = tipofuncionTrigonometrica
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self, data, valoresTabla):
        tipo = str(self.tipofuncionTrigonometrica)
        if tipo == 'acos' :
            'devuelve el coseno inverso'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try :
                    return Primitive('float',math.acos(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ACOS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ACOS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'acosd' :
            'devuelve el coseno inverso en grados '
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.degrees(math.acos(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ACOSD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ACOSD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'asin' :
            'devuelve el seno inverso'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.asin(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ASIN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ASIN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'asind' :
            'devuelve el seno inverso en grados'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.degrees(math.asin(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ASIND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ASIND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atan' :
            'devuelve el tangente inverso'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.atan(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ATAN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ATAN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atand' :
            'devuelve el tangente inverso en grados'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.degrees(math.atan(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ACOS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ATAND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atan2' :
            'devuelve el tangente inverso de una div'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento2, Error):
                return argumento2

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento2.type == 'float' :
                    try:
                        return Primitive('float',math.atan2(argumento.val,argumento2.val))
                    except :
                        error = Error('Semántico', 'Error de DOMINIO en ATAN2, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                        return error
                else :
                    error = Error('Semántico', 'Error de tipos en ATAN2, solo se aceptan valores numéricos, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ATAN2, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atan2d' :
            'devuelve el tangente inverso de una div en grados'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento2, Error):
                return argumento2

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento2.type == 'float' :
                    try:
                        return Primitive('float',math.degrees(math.atan2(argumento.val,argumento2.val)))
                    except :
                        error = Error('Semántico', 'Error de DOMINIO en ATAN2D, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                        return error
                else :
                    error = Error('Semántico', 'Error de tipos en ATAN2D, solo se aceptan valores numéricos, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ATAN2D, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cos' :
            'devuelve el coseno'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.cos(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en COS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cosd' :
            'devuelve el coseno en grados'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.degrees(math.cos(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COSD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en COSD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cot' :
            'devuelve el cotangente'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.cos(argumento.val)/math.sin(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COT, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en COT, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cotd' :
            'devuelve el cotangente en grados'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.degrees(math.cos(argumento.val)/math.sin(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COTD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en COTD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'sin' :
            'devuelve el sin'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.sin(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en SIN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en SIN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'sind' :
            'devuelve el coseno en grados'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.degrees(math.sin(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en SIND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en SIND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'tan' :
            'devuelve el tan'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.tan(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en TAN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en TAN, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'tand' :
            'devuelve el tan en grados'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.degrees(math.tan(argumento.val)))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en TAND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en TAND, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'sinh' :
            'devuelve el sinh'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.sinh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en SINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en SINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cosh' :
            'devuelve el cosh'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.cosh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en COSH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en COSH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'tanh' :
            'devuelve el tanh'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.tanh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en TANH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en SINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'asinh' :
            'devuelve el asinh'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.asinh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ASINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ASINH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'acosh' :
            'devuelve el asinh'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.asinh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ACOSH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ACOSH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'atanh' :
            'devuelve el atanh'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                try:
                    return Primitive('float',math.atanh(argumento.val))
                except :
                    error = Error('Semántico', 'Error de DOMINIO en ATANH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en ATANH, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error

        #return self


    def __repr__(self):
        return str(self.__dict__)

class OperadoresSelect(Instruccion):
        # | square
        # ||  cube
        # & and
        # | or dos args
        # # <- xor
        # ~ not
        # << sl(bitwise shift left)
        # >> sr(bitwise shift right)
    def __init__(self, tipoOperador, arg1,arg2):
        self.tipoOperador = tipoOperador
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self,data):
        try:
            argumento = self.arg1.execute()
        except:
            argumento = self.arg1.execute(data, valoresTabla)

        if isinstance(argumento, Error):
            return argumento

        if self.tipoOperador == 'square':
            if argumento.type == 'integer' or argumento.type == 'float' :
                return Primitive('float', math.pow(float(argumento.val),2))
            else:
                error = Error('Semántico', 'Error de tipos en |, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif self.tipoOperador == 'cube':
            if argumentotype == 'integer' or argumento.type == 'float' :
                return Primitive('float', math.pow(float(argumento.val),3))
            else:
                error = Error('Semántico', 'Error de tipos en ||, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif self.tipoOperador == 'and':
            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if (argumento.type == 'integer' or argumento.type == 'float') and (argumento2.type == 'integer' or argumento2.type == 'float') :
                return Primitive('float', float(argumento.val & argumento2.val))
            else:
                error = Error('Semántico', 'Error de tipos en ||, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif self.tipoOperador == 'or':
            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if (argumento.type == 'integer' or argumento.type == 'float') and (argumento2.type == 'integer' or argumento2.type == 'float') :
                return Primitive('float', float(argumento.val | argumento2.val))
            else:
                error = Error('Semántico', 'Error de tipos en ||, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif self.tipoOperador == 'xor':
            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if (argumento.type == 'integer' or argumento.type == 'float') and (argumento2.type == 'integer' or argumento2.type == 'float') :
                return Primitive('float', float(argumento.val ^ argumento2.val))
            else:
                error = Error('Semántico', 'Error de tipos en #, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif self.tipoOperador == 'not':
            if (argumento.type == 'integer' or argumento.type == 'float'):
                return Primitive('float', float(~argumento.val))
            else:
                error = Error('Semántico', 'Error de tipos en ~, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif self.tipoOperador == 'sl':
            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if (argumento.type == 'integer' or argumento.type == 'float') and (argumento2.type == 'integer' or argumento2.type == 'float') :
                return Primitive('float', float(argumento.val << argumento2.val))
            else:
                error = Error('Semántico', 'Error de tipos en <<, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif self.tipoOperador == 'sr':
            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if (argumento.type == 'integer' or argumento.type == 'float') and (argumento2.type == 'integer' or argumento2.type == 'float') :
                return Primitive('float', float(argumento.val >> argumento2.val))
            else:
                error = Error('Semántico', 'Error de tipos en >>, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error

        return self


    def __repr__(self):
        return str(self.__dict__)

class FuncionMatematica(Instruccion):

    def __init__(self, tipofuncionmatematica, arg1, arg2, arg3, arg4):
        self.tipofuncionmatematica = tipofuncionmatematica
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4

    def execute(self, data, valoresTabla):
        tipo = str(self.tipofuncionmatematica)
        if tipo == 'abs' :
            'valor absoluto - FALTA IDS'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                return Primitive('float', math.fabs(float(argumento.val)))
            else :
                error = Error('Semántico', 'Error de tipos en ABS, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error
        elif tipo == 'cbrt' :
            'raíz cúbica - solo numeros positivos'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = argumento.val**(1/3)
                    if isinstance(reto, int) :
                        return Primitive('integer', reto)

                    return Primitive('float', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en CBRT, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en CBRT, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'ceil' :
            'redondear - solo numeros positivos'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.ceil(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'ceiling' :
            'redondear - solo numeros positivos'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.ceil(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en CEIL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'degrees' :
            'radianes a grados - '
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                reto = math.degrees(argumento.val)
                return Primitive('float', reto)
            else :
                error = Error('Semántico', 'Error de tipos en DEGREES, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'div' :
            'cociente - '
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento2, Error):
                return argumento2

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento2.type == 'float' :
                    reto = math.trunc(argumento.val / argumento2.val)
                    return Primitive('integer', reto)
                else:
                    error = Error('Semántico', 'Error de tipos en DIV, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en DIV, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'exp' :
            'e^ argumento - '
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                reto = math.exp(argumento.val)
                return Primitive('float', reto)
            else :
                error = Error('Semántico', 'Error de tipos en EXP, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'factorial' :
            'x! - solo numeros positivos'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' :
                if argumento.val > 0 :
                    reto = math.factorial(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en FACTORIAL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en FACTORIAL, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'floor' :
            'redondear al menor -'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                reto = math.trunc(argumento.val)
                return Primitive('integer', reto)
            else :
                error = Error('Semántico', 'Error de tipos en FLOOR, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'gcd' :
            'MCD - '
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            try:
                argument2 = self.arg2.execute()
            except:
                argument2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argument2, Error):
                return argumento2

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento2.type == 'float' :
                    if argumento.val > 0 and argumento2.val > 0 :
                        reto = math.gcd(argumento.val, argumento2.val)
                        return Primitive('integer', reto)
                    else :
                        error = Error('Semántico', 'Error de tipos en GCD, solo se aceptan valores numéricos positivos', 0, 0)
                        return error
                else:
                    error = Error('Semántico', 'Error de tipos en GCD, solo se aceptan valores numéricos, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en GCD, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'ln' :
            'Ln -'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.log(argumento.val)
                    return Primitive('float', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en Ln, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en Ln, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'log' :
            'Log10 -'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0 :
                    reto = math.log10(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en LOG, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en LOG, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'mod' :
            'modulo - '
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento2, Error):
                return argumento2

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento.type == 'float' :
                    reto = math.remainder(argumento.val, argumento2.val)
                    return Primitive('integer', reto)
                else:
                    error = Error('Semántico', 'Error de tipos en MOD, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en MOD, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'pi' :
            'PI'
            return Primitive('float', math.pi)


        elif tipo == 'power' :
            'power - solo positivos'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento2, Error):
                return argumento2

            if argumento.type == 'integer' or 'float' :
                if argumento2.type == 'integer' or 'float' :
                    if argumento.val > 0 and argumento2.val > 0 :
                        reto = math.pow(argumento.val, argumento2.val)
                        if isinstance(reto, int) : return Primitive('integer', reto)
                        else : return Primitive('float', reto)
                    else :
                        error = Error('Semántico', 'Error de tipos en POWER, solo se aceptan valores numéricos positivo', 0, 0)
                        return error
                else:
                    error = Error('Semántico', 'Error de tipos en POWER, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento2.val, 0, 0)
                    return error
            else :
                error = Error('Semántico', 'Error de tipos en POWER, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'radians' :
            'grados a radianes - '
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0:
                    reto = math.radians(argumento.val)
                    return Primitive('float', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en RADIANS, solo se aceptan valores numéricos positivo', 0, 0)
                    return error

            else :
                error = Error('Semántico', 'Error de tipos en RADIANS, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'round' :
            'round - redondear n decimales'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if self.arg2 == None :
                    'numero de redondeo no específicado'
                    reto = round(argumento.val)
                    return Primitive('integer', reto)
                else:
                    'numero de redondeo específicado'

                    try:
                        argumento2 = self.arg2.execute()
                    except:
                        argumento2 = self.arg2.execute(data, valoresTabla)

                    if isinstance(argumento2, Error):
                        return argumento2

                    if argumento2.type == 'integer' or rgumento2.type == 'float' :
                        if argumento2.val > 0 :
                            reto = round(argumento.val, argumento2.val)
                            if isinstance(reto, int): return Primitive('integer', reto)
                            else: return Primitive('float', reto)
                        else :
                            error = Error('Semántico', 'Error de tipos en ROUND, solo se aceptan valores numéricos positivo', 0, 0)
                            return error
                    else:
                        error = Error('Semántico', 'Error de tipos en ROUND, solo se aceptan valores numéricos positivo, se obtuvo: '+argumento2.val, 0, 0)
                        return error
            else :
                error = Error('Semántico', 'Error de tipos en ROUND, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'sign' :
            'devuelve signo - 1 o -1'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0:
                    return Primitive('integer', 1)
                else :
                    return Primitive('integer', -1)

            else :
                error = Error('Semántico', 'Error de tipos en SIGN, solo se aceptan valores numéricos positivo, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'sqrt' :
            'grados a radianes - '
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0:
                    reto = math.sqrt(argumento.val)
                    return Primitive('float', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en SQRT, solo se aceptan valores numéricos positivo', 0, 0)
                    return error

            else :
                error = Error('Semántico', 'Error de tipos en SQRT, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error


        elif tipo == 'width_bucket' :
            'histograma - argumento1 puede ser una columna'
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            try:
                argumento2 = self.arg2.execute()
            except:
                argumento2 = self.arg2.execute(data, valoresTabla)

            if isinstance(argumento2, Error):
                return argumento2

            try:
                argumento3 = self.arg3.execute()
            except:
                argumento3 = self.arg3.execute(data, valoresTabla)

            if isinstance(argumento3, Error):
                return argumento3

            try:
                argumento4 = self.arg4.execute()
            except:
                argumento4 = self.arg4.execute(data, valoresTabla)

            if isinstance(argumento4, Error):
                return argumento4

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento2.type == 'integer' or argumento2.type == 'float' :
                    if argumento3.type == 'integer' or argumento3.type == 'float' :
                        if argumento4.type == 'integer' or argumento4.type == 'float' :
                            return Primitive('integer', self.widthbucket(int(argumento.val), int(argumento2.val), int(argumento3.val), int(argumento4.val)))
                            #return Primitive('integer', self.widthbucket(9, 1, 12, 4))
                        else:
                            error = Error('Semántico', 'Error de tipos en width_bucket, solo se aceptan valores numéricos', 0, 0)
                            return error
                    else:
                        error = Error('Semántico', 'Error de tipos en width_bucket, solo se aceptan valores numéricos', 0, 0)
                        return error
                else:
                    error = Error('Semántico', 'Error de tipos en width_bucket, solo se aceptan valores numéricos', 0, 0)
                    return error
            else:
                error = Error('Semántico', 'Error de tipos en width_bucket, solo se aceptan valores numéricos', 0, 0)
                return error


        elif tipo == 'trunc' :
            'grados a radianes - '
            try:
                argumento = self.arg1.execute()
            except:
                argumento = self.arg1.execute(data, valoresTabla)

            if isinstance(argumento, Error):
                return argumento

            if argumento.type == 'integer' or argumento.type == 'float' :
                if argumento.val > 0:
                    reto = math.trunc(argumento.val)
                    return Primitive('integer', reto)
                else :
                    error = Error('Semántico', 'Error de tipos en trunc, solo se aceptan valores numéricos positivo', 0, 0)
                    return error

            else :
                error = Error('Semántico', 'Error de tipos en trunc, solo se aceptan valores numéricos, se obtuvo: '+str(argumento.val), 0, 0)
                return error

        elif tipo == 'random' :
            'random entre 0 and 1'
            return Primitive('integer', random.randint(0,1))


        elif tipo == 'setseed' :
            ''
        elif tipo == 'scale' :
            ''

        return self

    def widthbucket(self, nnum, nmin, nmax, nbuckets):
        if nnum < nmin :
            return 0
        elif nnum > nmax :
            return nbuckets+1
        else:
            bucket_width = (nmax - nmin + 1) / nbuckets
            i = nmin-1
            bucket = 1
            while i < nmax:
                if i+bucket_width > nmax:
                    #if nnum >= i or nnum <= nmax:
                        #return bucket
                    break
                else:
                    if nnum > i and  nnum <= i+bucket_width:
                        #return bucket
                        break
                i = i+bucket_width
                bucket = bucket + 1
            return bucket

    def __repr__(self):
        return str(self.__dict__)

class FuncionFecha(Instruccion):
    #2arg:
    #extract(parte y tamestap) y datepart ( argument y argument)
    def __init__(self, tipofuncionfehca, arg1,arg2):
        self.tipofuncionfehca = tipofuncionfehca
        self.arg1 = arg1
        self.arg2 = arg2

    def execute(self, data, valoresTabla):
        tipo = self.tipofuncionfehca
        if tipo == 'extract':
            extraccion = self.arg1
            dextraccion = self.arg2.execute()
            fechacopleta = ''
            hora = ''
            años = ''
            try:
                fechacopleta = datetime.strptime(dextraccion.val,'%Y-%m-%d %H:%M:%S')
            except:
                try:
                    hora = datetime.strptime(dextraccion.val,'%H:%M:%S')
                except:
                    try :
                         años = datetime.strptime(dextraccion.val,'%Y-%m-%d')
                    except :
                        error = Error('Semántico', 'Error de tipos en DATE, solo se aceptan valores de fechas, se obtuvo: '+str(dextraccion.val), 0, 0)
                        return error

            if fechacopleta != '' :
                if extraccion == 'YEAR':
                    return Primitive('integer',fechacopleta.year)
                elif extraccion == 'MONTH':
                    return Primitive('integer',fechacopleta.month)
                elif extraccion == 'DAY':
                    return Primitive('integer',fechacopleta.day)
                elif extraccion == 'HOUR':
                    return Primitive('integer',fechacopleta.hour)
                elif extraccion == 'MINUTE':
                    return Primitive('integer',fechacopleta.minute)
                elif extraccion == 'SECOND':
                    return Primitive('integer',fechacopleta.second)
            elif hora != '' :
                if extraccion == 'HOUR':
                    return Primitive('integer',fechacopleta.hour)
                elif extraccion == 'MINUTE':
                    return Primitive('integer',fechacopleta.minute)
                elif extraccion == 'SECOND':
                    return Primitive('integer',fechacopleta.second)
                else :
                    error = Error('Semántico', 'Error de tipos en DATE, se quiere extraer una parte de la fecha no ingresada', 0, 0)
                    return error
            elif hora != '' :
                if extraccion == 'YEAR':
                    return Primitive('integer',fechacopleta.year)
                elif extraccion == 'MONTH':
                    return Primitive('integer',fechacopleta.month)
                elif extraccion == 'DAY':
                    return Primitive('integer',fechacopleta.day)
                else :
                    error = Error('Semántico', 'Error de tipos en DATE, se quiere extraer una parte de la fecha no fue ingresada', 0, 0)
                    return error
        elif tipo == 'now' :
            return Primitive('string', str(datetime.now())[:19])
        elif tipo == 'current_date' :
            return Primitive('string', str(datetime.now().date()))
        elif tipo == 'current_time' :
            return Primitive('string', str(datetime.now().time())[:8])
        elif tipo == 'timestamp' :
            dextraccion = self.arg2.execute()
            fechaval = datetime.strptime(dextraccion.val,'%Y-%m-%d %H:%M:%S')
            return Primitive('string',str(fechaval))
        elif tipo == 'date_part' :
            extraccion = self.arg1.execute()
            dextraccion = self.arg2.execute()
            dic ={}
            valor = ''
            descrip = ''
            for dex in dextraccion.val:
                if dex.isnumeric():
                    valor += dex
                elif (dex == ' ' and descrip != ''):
                    dic[descrip] = valor
                    valor = ''
                    descrip = ''
                elif dex.isalpha() :
                    descrip +=dex
            dic[descrip] = valor
            for key in dic:
                if str(key).find(extraccion.val) != -1 :
                     return Primitive('integer',dic[key])
            error = Error('Semántico', 'Error de valores en DATEPART, se solicita un valo no encontrado en la cadena  ', 0, 0)
            return error

        return self


    def __repr__(self):
        return str(self.__dict__)

class FuncionMatematicaSimple(Instruccion):
    #puede venir:
    #Count,max,sum,avg,min
    def __init__(self, operador, argumento):
        self.argumento = argumento
        self.operador = operador

    def execute(self, data, diccionarioAgrupacion, diccionarioColumnasAceptadas, columnasAceptadas):
        diccionarioRetorno = {'val': {}, 'type': None, 'name': ''}
        contador = 0
        noEncontrado = True
        columnaImprimir = None
        tablaAceptada = None
        for keys in columnasAceptadas:
            contador = 0
            for columnas in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][keys]['columns']:
                if columnas.name.upper() == self.argumento.column.upper():
                    noEncontrado = False
                    tablaAceptada = keys
                    columnaImprimir = columnas
                    diccionarioRetorno['type'] = columnas.type
                    break
                else:
                    contador = contador + 1
            if not noEncontrado :
                break
        if noEncontrado:
            if self.operador == 'count':
                if self.argumento.column == '*':
                    contador = 0
                else:
                    return Error('Semantico', 'La columna ' + self.argumento.column.upper() + ' no existe.', 0, 0)
            else:
                return Error('Semantico', 'La columna ' + self.argumento.column.upper() + ' no existe.', 0, 0)
        diccionarioRetorno['name'] = self.operador
        if self.operador == 'avg':
            if columnaImprimir.type == 'integer' or columnaImprimir.type == 'float':
                val = 0
                cont = 0

                for key in diccionarioAgrupacion:
                    val = 0
                    cont = 0
                    for pos in diccionarioAgrupacion[key]:
                        val = val + columnasAceptadas[tablaAceptada][pos][contador]
                        cont = cont + 1
                    res = val/cont
                    diccionarioRetorno['val'][key] = [res]

                return diccionarioRetorno
            else:
                return Error('Semantico', 'El tipo para AVG debe ser numerico o float.', 0, 0)

        elif self.operador == 'sum':
            if columnaImprimir.type == 'integer' or columnaImprimir.type == 'float':
                val = 0
                for key in diccionarioAgrupacion:
                    val = 0
                    for pos in diccionarioAgrupacion[key]:
                        val = val + columnasAceptadas[tablaAceptada][pos][contador]
                    diccionarioRetorno['val'][key] = [val]

                return diccionarioRetorno
            else:
                return Error('Semantico', 'El tipo para SUM debe ser numerico o float.', 0, 0)
        elif self.operador == 'count':
            if diccionarioAgrupacion == {}:
                val = 0
                arr = []
                for key in columnasAceptadas:
                    for v in columnasAceptadas[key]:
                        arr.append(v)
                    val = len(arr)
                    diccionarioRetorno['val'][key] = [val]
                    break
            else:
                val = 0
                for key in diccionarioAgrupacion:
                    val = len(diccionarioAgrupacion[key])
                    diccionarioRetorno['val'][key] = [val]

            return diccionarioRetorno

        elif self.operador == 'max':
            if diccionarioAgrupacion == {}:
                val = 0
                valComp = []
                for key in columnasAceptadas:
                    val = 0
                    valComp = []
                    for pos in columnasAceptadas[key]:
                        valComp.append(pos[contador])
                r = max(valComp)
                diccionarioRetorno['val'][key] = [r]
            else:
                val = 0
                valComp = []
                for key in diccionarioAgrupacion:
                    val = 0
                    valComp = []
                    for pos in diccionarioAgrupacion[key]:
                        valComp.append(columnasAceptadas[tablaAceptada][pos][contador])
                    r = max(valComp)
                    diccionarioRetorno['val'][key] = [r]

            return diccionarioRetorno

        elif self.operador == 'min':
            if diccionarioAgrupacion == {}:
                val = 0
                valComp = []
                for key in columnasAceptadas:
                    val = 0
                    valComp = []
                    for pos in columnasAceptadas[key]:
                        valComp.append(pos[contador])
                r = min(valComp)
                diccionarioRetorno['val'][key] = [r]
            else:
                val = 0
                valComp = []
                for key in diccionarioAgrupacion:
                    val = 0
                    valComp = []
                    for pos in diccionarioAgrupacion[key]:
                        valComp.append(columnasAceptadas[tablaAceptada][pos][contador])
                    r = min(valComp)
                    diccionarioRetorno['val'][key] = [r]

            return diccionarioRetorno
        return self

    def __repr__(self):
        return str(self.__dict__)
