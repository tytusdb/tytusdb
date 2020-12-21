import ts as TS
import jsonMode as Master
import interprete as Inter
from six import string_types
from errores import *
from expresiones import *
from prettytable import PrettyTable
from random import *
from expresiones import *

from prettytable import PrettyTable


LisErr = TablaError([])
ts_global = TS.TablaDeSimbolos()
Lista = []
ListaTablasG = []
baseN = []
baseActual = ""
Ejecucion = ">"

listaGeneral = {}




Lista.append(Ejecucion)


class Instruccion():
    'Abstracta'

    def Ejecutar(self):
        pass


# Este retorna el orden dependiendo de que columna le mandemos
def gets(Lista, data2, pos):
    for data in Lista:
        if (data2 == Lista.get(data)[pos]):
            return data
    return 0


def imprir(string):
    global Ejecucion
    Ejecucion += string + "\n"
    Lista.clear();
    Lista.append(Ejecucion)

def mostrarConsulta(resultado):
    tabla = PrettyTable()
    for key, val in resultado.items():
        tabla.add_column(key, val)

    imprir(str(tabla))


#Ingresan campos y tablas
def GenerarTablaQuery(Lista_Campos, Nombres_Tablas):
    global ts_global, baseActual
    global LisErr
    r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos

    if r is not None:

        for ee in Nombres_Tablas:

            if (isinstance(ee, AccesoTablaSinLista)):  # viene sin alias

                # Recorremos el diccionario general para ver si existe la tabla que queremos
                # recorremos lista General de Tablas
                for elemento2 in ts_global.Tablas:

                    x: CreateTable = ts_global.obtenerTabla(elemento2)

                    if (str(x.id) == str(ee.NombreT)):
                        # si es la tabla validamos que tipo de campo viene

                        for ii in Lista_Campos:

                            if (isinstance(ii,
                                           Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                # *  , nombrecampo,  nombrecampo alias
                                # listaGeneral
                                for ele in x.cuerpo:  # recorremos lista de columnas
                                    y: CampoTabla = ele
                                    if (str(y.id) == str(ii.Columna)):

                                        print("LA columan " + str(
                                            ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                        # Bamos a sacar todos los datos coincidentes
                                        # recorremos datos

                                        # Vallidamos que la no venga sin datos
                                        print(ii.NombreT)
                                        if (ii.NombreT != ""):
                                            # hacemos una doble condicion para agarrar la columna que es

                                            if (str(x.id) == ii.NombreT):
                                                print("Estoy entrando <<<<<<<<<<<<<<<<<<<<< ")
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))
                                                listaGeneral[ii.Columna] = lista
                                            else:
                                                print("")

                                        else:

                                            i = ts_global.Datos
                                            lista = []
                                            for gg in ts_global.Datos:
                                                t: DatoInsert = ts_global.obtenerDato(gg)

                                                if (str(t.columna) == str(ii.Columna)):
                                                    print(str(t.valor))

                                                    lista.append(str(t.valor))
                                            listaGeneral[ii.Columna] = lista


                                    elif (str(ii.Columna) == "*"):
                                        print("Vienen todo los datos de la tabla")

                                        # Vallidamos que la no venga sin datos
                                        if (ii.NombreT != ""):
                                            # hacemos una doble condicion para agarrar la columna que es
                                            if (str(x.id) == ii.NombreT):

                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[pp.id] = Lista2

                                        # viene sin referencia a tabla
                                        else:
                                            # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                            for columnas in x.cuerpo:
                                                pp: CampoTabla = columnas
                                                Lista2 = []
                                                i = ts_global.Datos
                                                for gg in i:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (pp.id == t.columna):
                                                        print(str(t.valor))
                                                        Lista2.append(str(t.valor))
                                                listaGeneral[pp.id] = Lista2


                                    else:
                                        print("")

                            elif (isinstance(ii,
                                             Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                # listaGeneral
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele

                                    if (y.id == ii.Columna):
                                        print("LA columan " + str(
                                            ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")

                                        # verificamos el alias

                                        ListaAlias = ii.Lista_Alias
                                        # Tenemos el alias
                                        nuevoNave = ListaAlias.Alias
                                        print("ahora la columna se llama" + str(nuevoNave))

                                        # Bamos a sacar todos los datos coincidentes
                                        # Vallidamos que la no venga sin datos
                                        if (ii.NombreT != ""):
                                            # hacemos una doble condicion para agarrar la columna que es
                                            if (str(x.id) == ii.NombreT):
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = lista
                                            else:
                                                print("")
                                        else:
                                            i = ts_global.Datos
                                            lista = []
                                            for gg in ts_global.Datos:
                                                t: DatoInsert = ts_global.obtenerDato(gg)

                                                if (str(t.columna) == str(ii.Columna)):
                                                    print(str(t.valor))
                                                    lista.append(str(t.valor))
                                            listaGeneral[str(nuevoNave)] = lista


                                    elif (y.id == '*'):
                                        # Recorrer todos los datos de la columna
                                        print("Vienen todo los datos  los datos de esa columna")

                                        ListaAlias = ii.Lista_Alias
                                        # Tenemos el alias
                                        nuevoNave = ListaAlias.Alias

                                        # Vallidamos que la no venga sin datos
                                        if (ii.NombreT != ""):
                                            # hacemos una doble condicion para agarrar la columna que es
                                            if (str(x.id) == ii.NombreT):

                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = Lista2

                                        # viene sin referencia a tabla
                                        else:
                                            # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                            for columnas in x.cuerpo:
                                                pp: CampoTabla = columnas
                                                Lista2 = []
                                                i = ts_global.Datos
                                                for gg in i:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (pp.id == t.columna):
                                                        print(str(t.valor))
                                                        Lista2.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = Lista2
                                    else:
                                        print("")
                            elif (isinstance(ii, AccesoSubConsultas)):
                                listaQ = {}
                                if (ii.Lista_Alias != False):
                                    print("Bamos a ver el cuerpo de cada subconsulta")
                                    li2 = ii.Lista_Alias[0]
                                    # Cuerpo de Tipo Subconsulta
                                    sub = ii.Query
                                    if (isinstance(sub, SubSelect)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect2)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect3)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect4)):
                                        sub.Ejecutar()
                                    else:
                                        print("viene otro tipo de subconsulta")
                                else:
                                    print("Bamos a ver el cuerpo de cada subconsulta")
                                    # Cuerpo de Tipo Subconsulta
                                    sub = ii.Query
                                    if (isinstance(sub, SubSelect)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect2)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect3)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect4)):
                                        sub.Ejecutar()
                                    else:
                                        print("viene otro tipo de subconsulta")
                            else:
                                print("Otros posibles tipos ")
                    else:
                        print("")


            # ============================================================================   Acceso a las tablas con alias
            elif (isinstance(ee, AccesoTabla)):  # viene con un alias

                # verificamos el alias
                AliasTabla = ee.Lista_Alias
                # Tenemos el alias
                AliasT = AliasTabla.Alias

                # Recorremos el diccionario general para ver si existe la tabla que queremos
                # recorremos lista General de Tablas
                for elemento2 in ts_global.Tablas:
                    x: CreateTable = ts_global.obtenerTabla(elemento2)

                    if (str(x.id) == str(ee.NombreT)):
                        # si es la tabla validamos que tipo de campo viene
                        for ii in Lista_Campos:

                            if (isinstance(ii,
                                           Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                # *  , nombrecampo,  nombrecampo alias
                                # listaGeneral
                                for ele in x.cuerpo:  # recorremos lista de columnas
                                    y: CampoTabla = ele
                                    if (str(y.id) == str(ii.Columna)):
                                        print("LA columan " + str(
                                            ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                        # Bamos a sacar todos los datos coincidentes
                                        # recorremos datos
                                        # Vallidamos que la no venga sin datos
                                        if (ii.NombreT != ""):
                                            if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))

                                                listaGeneral[ii.Columna] = lista

                                            else:
                                                print("")

                                        else:
                                            i = ts_global.Datos
                                            lista = []
                                            for gg in ts_global.Datos:
                                                t: DatoInsert = ts_global.obtenerDato(gg)
                                                if (str(t.columna) == str(ii.Columna)):
                                                    print(str(t.valor))
                                                    lista.append(str(t.valor))
                                            listaGeneral[ii.Columna] = lista

                                    elif (str(ii.Columna) == "*"):
                                        print("Vienen todo los datos de la tabla")
                                        # Vallidamos que la no venga sin datos
                                        if (ii.NombreT != ""):

                                            # hacemos una doble condicion para agarrar la columna que es
                                            if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[pp.id] = Lista2
                                        # viene sin referencia a tabla
                                        else:
                                            # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                            for columnas in x.cuerpo:
                                                pp: CampoTabla = columnas
                                                Lista2 = []
                                                i = ts_global.Datos
                                                for gg in i:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (pp.id == t.columna):
                                                        print(str(t.valor))
                                                        Lista2.append(str(t.valor))
                                                listaGeneral[pp.id] = Lista2
                                    else:
                                        print("")

                            elif (isinstance(ii,
                                             Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                # listaGeneral
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    if (y.id == ii.Columna):
                                        print("LA columan " + str(
                                            ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                        # verificamos el alias

                                        ListaAlias = ii.Lista_Alias
                                        # Tenemos el alias
                                        nuevoNave = ListaAlias.Alias
                                        print("ahora la columna se llama" + str(nuevoNave))

                                        # Bamos a sacar todos los datos coincidentes
                                        # Vallidamos que la no venga sin datos
                                        if (ii.NombreT != ""):
                                            # hacemos una doble condicion para agarrar la columna que es
                                            if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = lista
                                            else:
                                                print("")
                                        else:
                                            i = ts_global.Datos
                                            lista = []
                                            for gg in ts_global.Datos:
                                                t: DatoInsert = ts_global.obtenerDato(gg)
                                                if (str(t.columna) == str(ii.Columna)):
                                                    print(str(t.valor))
                                                    lista.append(str(t.valor))
                                            listaGeneral[str(nuevoNave)] = lista

                                    elif (y.id == '*'):
                                        # Recorrer todos los datos de la columna
                                        print("Vienen todo los datos  los datos de esa columna")
                                        ListaAlias = ii.Lista_Alias
                                        # Tenemos el alias
                                        nuevoNave = ListaAlias.Alias

                                        # Vallidamos que la no venga sin datos
                                        if (ii.NombreT != ""):
                                            # hacemos una doble condicion para agarrar la columna que es
                                            if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = Lista2
                                        # viene sin referencia a tabla
                                        else:
                                            # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                            for columnas in x.cuerpo:
                                                pp: CampoTabla = columnas
                                                Lista2 = []
                                                i = ts_global.Datos
                                                for gg in i:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (pp.id == t.columna):
                                                        print(str(t.valor))
                                                        Lista2.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = Lista2
                                    else:
                                        print("")
                            elif (isinstance(ii, AccesoSubConsultas)):
                                listaQ = {}
                                if (ii.Lista_Alias != False):
                                    # tomamos la lista de los alias
                                    li2 = ii.Lista_Alias[0]

                                    print("Bamos a ver el cuerpo de cada subconsulta")
                                    # Cuerpo de Tipo Subconsulta
                                    sub = ii.Query
                                    if (isinstance(sub, SubSelect)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect2)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect3)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect4)):
                                        sub.Ejecutar()
                                    else:
                                        print("viene otro tipo de subconsulta")

                                else:
                                    print("Bamos a ver el cuerpo de cada subconsulta")
                                    # Cuerpo de Tipo Subconsulta
                                    sub = ii.Query
                                    if (isinstance(sub, SubSelect)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect2)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect3)):
                                        sub.Ejecutar()
                                    elif (isinstance(sub, SubSelect4)):
                                        sub.Ejecutar()
                                    else:
                                        print("viene otro tipo de subconsulta")
                            else:
                                print("Otros posibles tipos ")
                    else:
                        print("")

            elif (isinstance(ee, AccesoSubConsultas)):

                if (ee.Lista_Alias != False):
                    # tomamos la lista de los alias
                    li2 = ee.Lista_Alias[0]

                    print("Bamos a ver el cuerpo de cada subconsulta")
                    # Cuerpo de Tipo Subconsulta
                    sub = ee.Query
                    if (isinstance(sub, SubSelect)):
                        sub.Ejecutar()
                    elif (isinstance(sub, SubSelect2)):
                        sub.Ejecutar()
                    elif (isinstance(sub, SubSelect3)):
                        sub.Ejecutar()
                    elif (isinstance(sub, SubSelect4)):
                        sub.Ejecutar()
                    else:
                        print("viene otro tipo de subconsulta")

                else:
                    print("Bamos a ver el cuerpo de cada subconsulta")
                    # Cuerpo de Tipo Subconsulta
                    sub = ee.Query
                    if (isinstance(sub, SubSelect)):
                        sub.Ejecutar()
                    elif (isinstance(sub, SubSelect2)):
                        sub.Ejecutar()
                    elif (isinstance(sub, SubSelect3)):
                        sub.Ejecutar()
                    elif (isinstance(sub, SubSelect4)):
                        sub.Ejecutar()
                    else:
                        print("viene otro tipo de subconsulta")
            else:
                imprir("Viene otro tipo de accion ")
    else:
        imprir("SELECT : No existe la base de datos acual")
    print(listaGeneral)
    mostrarConsulta(listaGeneral)

    return listaGeneral


#filtra un diccionario
def FiltrarCuerpo(listaGeneral,Cuerpo):
    # ====================================================================   Proceso del cuerpo para editar valores en la tabla
    # procesando el cuerpo General de las tablas al insertar correctamente


    for tiposCuerpo in Cuerpo:
        if (isinstance(tiposCuerpo, Cuerpo_TipoWhere)):
            print("Vamos a ver condiciones y luego a mostrar datos de las condiciones")
            resultado = Inter.procesar_expresion_select(tiposCuerpo.Cuerpo, ts_global)
            if resultado is None:
                imprir("SELECT: No existen registros.")
            else:
                for r in resultado:
                    print(">>" + str(r.valor))

        elif (isinstance(tiposCuerpo, GroupBy)):
            print("Vamos a ver los tipos de grupos a realizar ")
            # si no trae having va a tomar directamente el objeto relacionado
            if (tiposCuerpo.Condiciones == False):
                # ====================================================================== ASC
                # ============== Aqui Amarramos las Tuplas para tomar todos los valores
                # Diccionarios auxiliares
                ListaN = {}
                # listas Auxiliares
                # Esta lista tendra concatenado tanto el nombre o con el alias
                listaColumnas = []
                # Recorremos lista General
                contador2 = 0
                # primero llenamos el nuevo diccionario  amarrando las tuplas
                for campo in listaGeneral:
                    contador = 0
                    listaColumnas.append(campo)
                    # contador de filas
                    if (contador2 == 0):
                        for datos in listaGeneral.get(campo):
                            print("Esta es la longitud de la columna >" + str(len(ListaN)))
                            ListaN[contador] = [datos]
                            contador += 1
                            contador2 += 1
                    else:
                        for datos in listaGeneral.get(campo):
                            print("Esta es la longitud de la columna >" + str(len(ListaN)))
                            ListaN[contador].append(datos)
                            contador += 1

                # ============== Ahora ordenamos todo respecto a una columna
                object: OrderBy = tiposCuerpo
                tipo: AccesoGroupBy = object.Lista_Campos[0]
                date = tipo.Columna

                # Si viene la palabra reservada Ascendente
                if (str(tipo.Estado).upper() == 'ASC'):
                    # Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                    # tenemos el contador de columnas
                    colN = 0
                    for nombre in listaColumnas:
                        print(nombre)
                        print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                        print(date)
                        if (nombre == date):
                            colN += 1
                        else:
                            print("")
                    # tenemos el indice de la columna solicitada ahora editamos
                    # Diccionario auxiliar
                    diccionario2 = {}
                    listita = []
                    indices = 0
                    # Agarramos los datos con los que se van a ordenar los datos
                    print("Aqui estan las cosas <<<<<<")
                    print(str(colN))
                    print(ListaN)
                    for n in ListaN:
                        listita.append(ListaN.get(n)[colN - 1])
                    listt = sorted(listita)
                    print(listita)
                    # Recorremos la lista ordenada
                    for n2 in listt:
                        diccionario2[gets(ListaN, n2, colN - 1)] = ListaN.get(gets(ListaN, n2, colN - 1))
                    print(diccionario2)
                # Si viene la palabra reservada Descendente
                elif (str(tipo.Estado).upper() == 'DESC'):
                    # Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                    # tenemos el contador de columnas
                    colN = 0
                    for nombre in listaColumnas:
                        print(nombre)
                        print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                        print(date)
                        if (nombre == date):
                            colN += 1
                        else:
                            print("")
                    # tenemos el indice de la columna solicitada ahora editamos
                    # Diccionario auxiliar
                    diccionario2 = {}
                    listita = []
                    indices = 0
                    # Agarramos los datos con los que se van a ordenar los datos
                    print("Aqui estan las cosas <<<<<<")
                    print(str(colN))
                    print(ListaN)

                    for n in ListaN:
                        listita.append(ListaN.get(n)[colN - 1])
                    listt = sorted(listita, reverse=True)
                    print(listt)

                    # Recorremos la lista ordenada
                    for n2 in listt:
                        diccionario2[gets(ListaN, n2, colN - 1)] = ListaN.get(gets(ListaN, n2, colN - 1))
                    print(diccionario2)

                # Si no viene ordenamos ascendentemente
                else:
                    # Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                    # tenemos el contador de columnas
                    colN = 0
                    for nombre in listaColumnas:
                        print(nombre)
                        print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                        print(date)
                        if (nombre == date):
                            colN += 1
                        else:
                            print("")
                    # tenemos el indice de la columna solicitada ahora editamos
                    # Diccionario auxiliar
                    diccionario2 = {}
                    listita = []
                    indices = 0
                    # Agarramos los datos con los que se van a ordenar los datos
                    print("Aqui estan las cosas <<<<<<")
                    print(str(colN))
                    print(ListaN)
                    for n in ListaN:
                        listita.append(ListaN.get(n)[colN - 1])
                    listt = sorted(listita)
                    print(listita)
                    # Recorremos la lista ordenada
                    for n2 in listt:
                        diccionario2[gets(ListaN, n2, colN - 1)] = ListaN.get(gets(ListaN, n2, colN - 1))
                    print(diccionario2)

                # =============  Hacemos un contador  para gravar su numero de columnas
                listak = []
                contadorlist = 0
                for jj in diccionario2:
                    listak.append(contadorlist)
                    contadorlist += 1
                print(listak)
                # ==============  Renombramos los datos
                contadoraa = 0
                for n in diccionario2:
                    diccionario2[str(listak[contadoraa])] = diccionario2.pop(n)
                    contadoraa += 1
                print(diccionario2)
                # ============== Regresamos los datos a su posicion inicial
                diccionariof = {}
                # primero llenamos el nuevo diccionario  amarrando las tuplas
                for campo in diccionario2:
                    # contador de filas
                    contador333 = 0
                    if (len(diccionariof) == 0):
                        for datos in diccionario2.get(campo):
                            diccionariof[str(contador333)] = [datos]
                            contador333 += 1
                    else:
                        for datos in diccionario2.get(campo):
                            diccionariof[str(contador333)].append(datos)
                            contador333 += 1
                print(diccionariof)
                # ============== Ahora ordenamos Asignamos los nombres de las claves o columnas como son
                contadornn = 0
                for n in diccionariof:
                    diccionariof[listaColumnas[contadornn]] = diccionariof.pop(n)
                    contadornn += 1
                # imprimimos  la lista haber si hace lo que se piensa
                mostrarConsulta(diccionariof)
                return diccionariof

                #diccionariof.clear

            # si no trae having va a tomar directamente el objeto relacionado
            else:
                # Tomamos las Acciones de expresion
                print("Aqui se hacen Acciones con la Tabla resultante")
                imprir("GROUP BY:  Aqui tenemos un una accion <<")

        elif (isinstance(tiposCuerpo, OrderBy)):
            print("Vamos a ordenar  segun lo que venga ")

            # ====================================================================== ASC
            # ============== Aqui Amarramos las Tuplas para tomar todos los valores
            # Diccionarios auxiliares
            ListaN = {}
            # listas Auxiliares
            # Esta lista tendra concatenado tanto el nombre o con el alias
            listaColumnas = []
            # Recorremos lista General
            contador2 = 0
            # primero llenamos el nuevo diccionario  amarrando las tuplas
            for campo in listaGeneral:
                contador = 0
                listaColumnas.append(campo)
                # contador de filas
                if (contador2 == 0):
                    for datos in listaGeneral.get(campo):
                        print("Esta es la longitud de la columna >" + str(len(ListaN)))
                        ListaN[contador] = [datos]
                        contador += 1
                        contador2 += 1
                else:
                    for datos in listaGeneral.get(campo):
                        print("Esta es la longitud de la columna >" + str(len(ListaN)))
                        ListaN[contador].append(datos)
                        contador += 1

            # ============== Ahora ordenamos todo respecto a una columna
            object: OrderBy = tiposCuerpo
            tipo: AccesoGroupBy = object.Lista_Campos[0]
            date = tipo.Columna

            # Si viene la palabra reservada Ascendente
            if (str(tipo.Estado).upper() == 'ASC'):
                # Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                # tenemos el contador de columnas
                colN = 0
                for nombre in listaColumnas:
                    print(nombre)
                    print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                    print(date)
                    if (nombre == date):
                        colN += 1
                    else:
                        print("")
                # tenemos el indice de la columna solicitada ahora editamos
                # Diccionario auxiliar
                diccionario2 = {}
                listita = []
                indices = 0
                # Agarramos los datos con los que se van a ordenar los datos
                print("Aqui estan las cosas <<<<<<")
                print(str(colN))
                print(ListaN)
                for n in ListaN:
                    listita.append(ListaN.get(n)[colN - 1])
                listt = sorted(listita)
                print(listita)
                # Recorremos la lista ordenada
                for n2 in listt:
                    diccionario2[gets(ListaN, n2, colN - 1)] = ListaN.get(gets(ListaN, n2, colN - 1))
                print(diccionario2)
            # Si viene la palabra reservada Descendente
            elif (str(tipo.Estado).upper() == 'DESC'):
                # Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                # tenemos el contador de columnas
                colN = 0
                for nombre in listaColumnas:
                    print(nombre)
                    print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                    print(date)
                    if (nombre == date):
                        colN += 1
                    else:
                        print("")
                # tenemos el indice de la columna solicitada ahora editamos
                # Diccionario auxiliar
                diccionario2 = {}
                listita = []
                indices = 0
                # Agarramos los datos con los que se van a ordenar los datos
                print("Aqui estan las cosas <<<<<<")
                print(str(colN))
                print(ListaN)

                for n in ListaN:
                    listita.append(ListaN.get(n)[colN - 1])
                listt = sorted(listita, reverse=True)
                print(listt)

                # Recorremos la lista ordenada
                for n2 in listt:
                    diccionario2[gets(ListaN, n2, colN - 1)] = ListaN.get(gets(ListaN, n2, colN - 1))
                print(diccionario2)

            # Si no viene ordenamos ascendentemente
            else:
                # Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                # tenemos el contador de columnas
                colN = 0
                for nombre in listaColumnas:
                    print(nombre)
                    print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                    print(date)
                    if (nombre == date):
                        colN += 1
                    else:
                        print("")
                # tenemos el indice de la columna solicitada ahora editamos
                # Diccionario auxiliar
                diccionario2 = {}
                listita = []
                indices = 0
                # Agarramos los datos con los que se van a ordenar los datos
                print("Aqui estan las cosas <<<<<<")
                print(str(colN))
                print(ListaN)
                for n in ListaN:
                    listita.append(ListaN.get(n)[colN - 1])
                listt = sorted(listita)
                print(listita)
                # Recorremos la lista ordenada
                for n2 in listt:
                    diccionario2[gets(ListaN, n2, colN - 1)] = ListaN.get(gets(ListaN, n2, colN - 1))
                print(diccionario2)

            # =============  Hacemos un contador  para gravar su numero de columnas
            listak = []
            contadorlist = 0
            for jj in diccionario2:
                listak.append(contadorlist)
                contadorlist += 1
            print(listak)
            # ==============  Renombramos los datos
            contadoraa = 0
            for n in diccionario2:
                diccionario2[str(listak[contadoraa])] = diccionario2.pop(n)
                contadoraa += 1
            print(diccionario2)
            # ============== Regresamos los datos a su posicion inicial
            diccionariof = {}
            # primero llenamos el nuevo diccionario  amarrando las tuplas
            for campo in diccionario2:
                # contador de filas
                contador333 = 0
                if (len(diccionariof) == 0):
                    for datos in diccionario2.get(campo):
                        diccionariof[str(contador333)] = [datos]
                        contador333 += 1
                else:
                    for datos in diccionario2.get(campo):
                        diccionariof[str(contador333)].append(datos)
                        contador333 += 1
            print(diccionariof)
            # ============== Ahora ordenamos Asignamos los nombres de las claves o columnas como son
            contadornn = 0
            for n in diccionariof:
                diccionariof[listaColumnas[contadornn]] = diccionariof.pop(n)
                contadornn += 1
            # imprimimos  la lista haber si hace lo que se piensa

            mostrarConsulta(diccionariof)
            return diccionariof


        elif (isinstance(tiposCuerpo, AccesoLimit)):
            print("Bamos a elegir el limite ")
            if (str(tiposCuerpo.Reservada).lower() == "offset"):
                # codigo de offset
                # Recorremos la lista General
                print("Estoy entrando al Offset")
                for nn in listaGeneral:
                    l = listaGeneral.get(nn)
                    # Recorro la lista dentro del diccionario
                    indice = 0
                    for dato in l:
                        if (indice < int(tiposCuerpo.Expresion_Numerica)):
                            print(">>>" + l.pop(0))
                            indice += 1
            elif (str(tiposCuerpo.Reservada).lower() == "limit"):
                # Codigo de limit
                if (str(tiposCuerpo.Expresion_Numerica).lower() == "all"):
                    print("Voy a retornar todo sin limite")
                else:
                    # Recorremos la lista General
                    for nn in listaGeneral:
                        l = listaGeneral.get(nn)

                        # Recorro la lista dentro del diccionario
                        indice = 0
                        for dato in l:
                            if (indice < int(tiposCuerpo.Expresion_Numerica)):
                                print(">>>" + l.pop())
                                indice += 1

        elif (isinstance(tiposCuerpo, AccesoSubConsultas)):
            print("Bamos a ver el cuerpo de cada subconsulta")
        #print(ListaN)

        mostrarConsulta(listaGeneral)
        return listaGeneral


#une las tablas segun lo que venga en union
def DefinicionUnion(unionn):

    for uni in unionn:
        if (isinstance(uni, CamposUnions)):
            if (str(uni.Reservada).upper() == "ALL"):
                print("Viene  ALL")
                if (str(uni.Comportamiento).upper() == "UNION"):
                    print("Viene un union")
                    ank = uni.Consulta
                    if (isinstance(ank, Select)):
                        print("viene un tipo de select normal unido")
                        ank.Ejecutar()
                    elif (isinstance(ank, Select2)):
                        ank.Ejecutar()
                        print("viene un tipo de select normal con cuerpo")
                    elif (isinstance(ank, Select3)):
                        ank.Ejecutar()
                        print("Viene un tipo de Select normal con distinct")
                    elif (isinstance(ank, Select4)):
                        ank.Ejecutar()
                        print("viene un tipo de Select normal con cuerpo y distinct")
                    else:
                        print("viene otro tipo de funcion")
                elif (str(uni.Comportamiento).upper() == "INTERSECT"):
                    print("Viene un Intersect")
                    ank = uni.Consulta
                    if (isinstance(ank, Select)):
                        print("viene un tipo de select normal unido")
                        ank.Ejecutar()
                    elif (isinstance(ank, Select2)):
                        ank.Ejecutar()
                        print("viene un tipo de select normal con cuerpo")
                    elif (isinstance(ank, Select3)):
                        ank.Ejecutar()
                        print("Viene un tipo de Select normal con distinct")
                    elif (isinstance(ank, Select4)):
                        ank.Ejecutar()
                        print("viene un tipo de Select normal con cuerpo y distinct")
                    else:
                        print("viene otro tipo de funcion")
                elif (str(uni.Comportamiento).upper() == "EXCEPT"):
                    print("Viene un Except")
                    ank = uni.Consulta
                    if (isinstance(ank, Select)):
                        print("viene un tipo de select normal unido")
                        ank.Ejecutar()
                    elif (isinstance(ank, Select2)):
                        ank.Ejecutar()
                        print("viene un tipo de select normal con cuerpo")
                    elif (isinstance(ank, Select3)):
                        ank.Ejecutar()
                        print("Viene un tipo de Select normal con distinct")
                    elif (isinstance(ank, Select4)):
                        ank.Ejecutar()
                        print("viene un tipo de Select normal con cuerpo y distinct")
                    else:
                        print("viene otro tipo de funcion")
                else:
                    print("vino una palabra diferente")
            elif (str(uni.Reservada) == ","):
                print("Viene una Coma")
            else:
                if (str(uni.Comportamiento).upper() == "UNION"):
                    print("Viene un union")
                    ank = uni.Consulta
                    if (isinstance(ank, Select)):
                        print("viene un tipo de select normal unido")
                        ank.Ejecutar()
                    elif (isinstance(ank, Select2)):
                        ank.Ejecutar()
                        print("viene un tipo de select normal con cuerpo")
                    elif (isinstance(ank, Select3)):
                        ank.Ejecutar()
                        print("Viene un tipo de Select normal con distinct")
                    elif (isinstance(ank, Select4)):
                        ank.Ejecutar()
                        print("viene un tipo de Select normal con cuerpo y distinct")
                    else:
                        print("viene otro tipo de funcion")
                elif (str(uni.Comportamiento).upper() == "INTERSECT"):
                    print("Viene un Intersect")
                    ank = uni.Consulta
                    if (isinstance(ank, Select)):
                        print("viene un tipo de select normal unido")
                        ank.Ejecutar()
                    elif (isinstance(ank, Select2)):
                        ank.Ejecutar()
                        print("viene un tipo de select normal con cuerpo")
                    elif (isinstance(ank, Select3)):
                        ank.Ejecutar()
                        print("Viene un tipo de Select normal con distinct")
                    elif (isinstance(ank, Select4)):
                        ank.Ejecutar()
                        print("viene un tipo de Select normal con cuerpo y distinct")
                    else:
                        print("viene otro tipo de funcion")
                elif (str(uni.Comportamiento).upper() == "EXCEPT"):
                    print("Viene un Except")
                    ank = uni.Consulta
                    if (isinstance(ank, Select)):
                        print("viene un tipo de select normal unido")
                        ank.Ejecutar()
                    elif (isinstance(ank, Select2)):
                        ank.Ejecutar()
                        print("viene un tipo de select normal con cuerpo")
                    elif (isinstance(ank, Select3)):
                        ank.Ejecutar()
                        print("Viene un tipo de Select normal con distinct")
                    elif (isinstance(ank, Select4)):
                        ank.Ejecutar()
                        print("viene un tipo de Select normal con cuerpo y distinct")
                    else:
                        print("viene otro tipo de funcion")
                else:
                    print("vino una palabra diferente")




#----------------------------------------------------------
#           TABLA DE SIMBOLOS
#----------------------------------------------------------
#----------------------------------------------------------
from graphviz import Digraph, nohtml
from graphviz import Graph
from graphviz import escape

def tabla_simbolos():
    print("------------SIMBOLOS---------------")
    ts=ts_global
    SymbolT =  Graph('g', filename='bsimbolos.gv', format='png',node_attr={'shape': 'plaintext', 'height': '.1'})

    #DICIONARIO DATOS
    cadena=''
    for fn in ts.Datos:
        fun=ts.obtenerDato(fn)
        cadena+='<TR><TD>'+str(fun.bd)+'</TD>'+'<TD>'+str(fun.tabla)+'</TD>'+'<TD>'+str(fun.columna)+'</TD>'+'<TD>'+str(fun.valor)+'</TD>'+'<TD>'+str(fun.fila)+'</TD></TR>'

    cadena4 = ''
    for fn in ts.Tipos:
        fun:DatoTipo = ts.obtenerTipo(fn)
        cadena4 += '<TR><TD>' + str(fun.bd) + '</TD>' + '<TD>' + str(fun.tipo) + '</TD>' + '<TD>' + str(fun.valor) + '</TD>' + '<TD>' + '</TD>' + '<TD>' + '</TD></TR>'

    cadena = ''
    for fn in ts.Datos:
        fun = ts.obtenerDato(fn)
        cadena += '<TR><TD>' + str(fun.bd) + '</TD>' + '<TD>' + str(fun.tabla) + '</TD>' + '<TD>' + str(
            fun.columna) + '</TD>' + '<TD>' + str(fun.valor) + '</TD>' + '<TD>' + str(fun.fila) + '</TD></TR>'

    #DICIONARIO Tablas
    cadena2=''
    for fn in ts.Tablas:
        fun=ts.obtenerTabla(fn)
        for cuerpos in fun.cuerpo:
            if isinstance(cuerpos.tipo,valorTipo):
                cadena2+='<TR><TD>'+str(fun.id)+'</TD>'+'<TD>'+str(cuerpos.id)+'</TD>'+'<TD>'+str(cuerpos.tipo.valor)+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD></TR>'
            else:
                cadena2+='<TR><TD>'+str(fun.id)+'</TD>'+'<TD>'+str(cuerpos.id)+'</TD>'+'<TD>'+str(cuerpos.tipo)+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD></TR>'

    cadena3=''
    for fn in ts.BasesDatos:
        fun=ts.obtenerBasesDatos(fn)
        cadena3 +='<TR><TD>'+str(fun.idBase)+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD></TR>'



    SymbolT.node('table','''<<TABLE border="1" cellpadding="0" cellspacing="0"   >
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>DATOS</B> </TD>
                            </TR>
                            <TR bgcolor="#BEF781">
                                <TD bgcolor="#BEF781">BASE DATOS</TD>
                                <TD bgcolor="#BEF781">TABLA</TD>
                                <TD bgcolor="#BEF781">COLUMNA</TD>
                                <TD bgcolor="#BEF781">VALOR </TD>
                                <TD bgcolor="#BEF781">FILA</TD>
                            </TR>
                            '''
                            +cadena+
                            ''' <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"><B> TABLAS</B> </TD>
                            </TR>
                            <TR bgcolor="#BEF781">
                                <TD bgcolor="#BEF781">ID TABLA</TD>
                                <TD bgcolor="#BEF781">ID COLUMNA</TD>
                                <TD bgcolor="#BEF781">TIPO COLUMNA</TD>
                                <TD bgcolor="#BEF781">  </TD>
                                <TD bgcolor="#BEF781">  </TD>
                            </TR>'''
                             + cadena2 +
                             ''' <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>TIPOS </B></TD>
                            </TR>
                            <TR bgcolor="#BEF781">
                                <TD bgcolor="#BEF781">BASE DE DATOS</TD>
                                <TD bgcolor="#BEF781"> TIPO </TD>
                                <TD bgcolor="#BEF781">VALOR</TD>
                                <TD bgcolor="#BEF781">  </TD>
                                <TD bgcolor="#BEF781">  </TD>
                            </TR>'''
                             + cadena4 +
                             ''' <TR>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                                <TD></TD>
                            </TR>
                            <TR>
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>BASES DE DATOS</B> </TD>
                            </TR>
                            <TR>
                                <TD bgcolor="#BEF781">ID BASE DE DATOS</TD>
                                <TD bgcolor="#BEF781"></TD>
                                <TD bgcolor="#BEF781"></TD>
                                <TD bgcolor="#BEF781"></TD>
                                <TD bgcolor="#BEF781"></TD>
                            </TR>'''
                            +cadena3+
                        '''</TABLE>>''')


    #DICCIONARIO BASE DE DATOS

    SymbolT.render('g', format='png', view=True)

# Un drop table esta compuesto por el ID de la tabla que eliminara.
class DropTable(Instruccion):
    def __init__(self, id):
        self.id = id

    def Ejecutar(self):
        #validar que exista la base de datos global
        #validar que exista la tabla en la base de datos
        #eliminar

        global ts_global, baseActual
        global LisErr

        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:
            r2 = ts_global.obtenerTabla(self.id[0].val)
            if r2 is not None:
                #Eliminar Tabla
                res = Master.dropTable(baseActual,self.id[0].val)
                if res ==0:
                    #se Elimino exitosamente
                    ts_global.EliminarTabla(self.id[0].val)
                    imprir("DROP TABLE:   Exito al Eliminar ")
                elif res ==1:
                    #Error all eliminar
                    imprir("DROP TABLE:   Error Logico al eliminar")
                elif res==2:
                    #No esta la base de datos en la data
                    imprir("DROP TABLE:   Error no se encuentra la BD ")
                elif res==3:
                    #No esta la tabla en la base de datos
                    imprir("DROP TABLE:   Error no se encuentra la Tabla en la DB")
                else:
                    imprir("DROP TABLE:   Error al eliminar la Tabla!")

            else:
                imprir("DROP TABLE:   La tabla no existe!")
        else:
            imprir("DROP TABLE:   La Base de datos a eliminar no existe!")
            #colocar error semantico


class Absoluto(Instruccion) :
    def __init__(self, variable) :
        self.variable=variable

#---------------------------------------------------------------------------------------------------
class Select(Instruccion) :
    def __init__(self,  unionn, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn

    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr
        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos


        if r is not None:


           for ee in self.Nombres_Tablas:


               if(isinstance(ee,AccesoTablaSinLista)): #viene sin alias


                   #Recorremos el diccionario general para ver si existe la tabla que queremos
                   # recorremos lista General de Tablas
                   for elemento2 in ts_global.Tablas:

                       x: CreateTable = ts_global.obtenerTabla(elemento2)


                       if (str(x.id) == str(ee.NombreT)):
                          #si es la tabla validamos que tipo de campo viene



                            for ii in self.Lista_Campos:

                                if(isinstance(ii,Campo_AccedidoSinLista)): #nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                    #*  , nombrecampo,  nombrecampo alias
                                    #listaGeneral
                                    for ele in x.cuerpo: #recorremos lista de columnas
                                        y:CampoTabla = ele
                                        if (str(y.id) == str(ii.Columna)):


                                            print("LA columan "+str(ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                            #Bamos a sacar todos los datos coincidentes
                                            #recorremos datos

                                            #Vallidamos que la no venga sin datos
                                            print(ii.NombreT)
                                            if(ii.NombreT !=""):
                                                #hacemos una doble condicion para agarrar la columna que es

                                                if(str(x.id)==ii.NombreT):
                                                    print("Estoy entrando <<<<<<<<<<<<<<<<<<<<< ")
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))
                                                    listaGeneral[ii.Columna] = lista
                                                else:
                                                    print("")

                                            else:

                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))
                                                listaGeneral[ii.Columna] = lista


                                        elif(str(ii.Columna) == "*"):
                                            print("Vienen todo los datos de la tabla")

                                            #Vallidamos que la no venga sin datos
                                            if(ii.NombreT!=""):
                                                #hacemos una doble condicion para agarrar la columna que es
                                                if(str(x.id)==ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[pp.id] = Lista2

                                            #viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[pp.id] = Lista2


                                        else:
                                            print("")

                                elif(isinstance(ii,Campo_Accedido)): # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                    #listaGeneral
                                    for ele in x.cuerpo:
                                        y: CampoTabla = ele

                                        if (y.id == ii.Columna):
                                            print("LA columan "+str(ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")

                                            #verificamos el alias

                                            ListaAlias = ii.Lista_Alias
                                            #Tenemos el alias
                                            nuevoNave = ListaAlias.Alias
                                            print("ahora la columna se llama"+str(nuevoNave))

                                            # Bamos a sacar todos los datos coincidentes
                                            #Vallidamos que la no venga sin datos
                                            if(ii.NombreT !=""):
                                                #hacemos una doble condicion para agarrar la columna que es
                                                if(str(x.id)==ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = lista


                                        elif(y.id == '*'):
                                            #Recorrer todos los datos de la columna
                                            print("Vienen todo los datos  los datos de esa columna")

                                            ListaAlias = ii.Lista_Alias
                                            #Tenemos el alias
                                            nuevoNave = ListaAlias.Alias

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[str(nuevoNave)] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = Lista2
                                        else:
                                            print("")
                                elif (isinstance(ii, AccesoSubConsultas)):
                                    listaQ = {}
                                    if (ii.Lista_Alias != False):
                                        print("Bamos a ver el cuerpo de cada subconsulta")
                                        li2 = ii.Lista_Alias[0]
                                        # Cuerpo de Tipo Subconsulta
                                        sub = ii.Query
                                        if (isinstance(sub, SubSelect)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect2)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect3)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect4)):
                                            sub.Ejecutar()
                                        else:
                                            print("viene otro tipo de subconsulta")
                                    else:
                                        print("Bamos a ver el cuerpo de cada subconsulta")
                                        # Cuerpo de Tipo Subconsulta
                                        sub = ii.Query
                                        if (isinstance(sub, SubSelect)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect2)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect3)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect4)):
                                            sub.Ejecutar()
                                        else:
                                            print("viene otro tipo de subconsulta")
                                else:
                                    print("Otros posibles tipos ")
                       else:
                           print("")


#============================================================================   Acceso a las tablas con alias
               elif(isinstance(ee,AccesoTabla)): #viene con un alias

                   # verificamos el alias
                   AliasTabla = ee.Lista_Alias
                   # Tenemos el alias
                   AliasT = AliasTabla.Alias

                   # Recorremos el diccionario general para ver si existe la tabla que queremos
                   # recorremos lista General de Tablas
                   for elemento2 in ts_global.Tablas:
                       x: CreateTable = ts_global.obtenerTabla(elemento2)

                       if (str(x.id) == str(ee.NombreT)):
                           # si es la tabla validamos que tipo de campo viene
                           for ii in self.Lista_Campos:


                               if (isinstance(ii,Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                   # *  , nombrecampo,  nombrecampo alias
                                   # listaGeneral
                                   for ele in x.cuerpo:  # recorremos lista de columnas
                                       y: CampoTabla = ele
                                       if (str(y.id) == str(ii.Columna)):
                                           print("LA columan " + str(ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                           # Bamos a sacar todos los datos coincidentes
                                           # recorremos datos
                                           # Vallidamos que la no venga sin datos
                                           if (ii.NombreT != ""):
                                               if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                   i = ts_global.Datos
                                                   lista = []
                                                   for gg in ts_global.Datos:
                                                       t: DatoInsert = ts_global.obtenerDato(gg)
                                                       if (str(t.columna) == str(ii.Columna)):
                                                           print(str(t.valor))
                                                           lista.append(str(t.valor))

                                                   listaGeneral[ii.Columna] = lista

                                               else:
                                                   print("")

                                           else:
                                               i = ts_global.Datos
                                               lista = []
                                               for gg in ts_global.Datos:
                                                   t: DatoInsert = ts_global.obtenerDato(gg)
                                                   if (str(t.columna) == str(ii.Columna)):
                                                       print(str(t.valor))
                                                       lista.append(str(t.valor))
                                               listaGeneral[ii.Columna] = lista

                                       elif (str(ii.Columna) == "*"):
                                           print("Vienen todo los datos de la tabla")
                                           # Vallidamos que la no venga sin datos
                                           if (ii.NombreT != ""):

                                               # hacemos una doble condicion para agarrar la columna que es
                                               if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                   # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                   for columnas in x.cuerpo:
                                                       pp: CampoTabla = columnas
                                                       Lista2 = []
                                                       i = ts_global.Datos
                                                       for gg in i:
                                                           t: DatoInsert = ts_global.obtenerDato(gg)
                                                           if (pp.id == t.columna):
                                                               print(str(t.valor))
                                                               Lista2.append(str(t.valor))
                                                       listaGeneral[pp.id] = Lista2
                                           # viene sin referencia a tabla
                                           else:
                                               # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                               for columnas in x.cuerpo:
                                                   pp: CampoTabla = columnas
                                                   Lista2 = []
                                                   i = ts_global.Datos
                                                   for gg in i:
                                                       t: DatoInsert = ts_global.obtenerDato(gg)
                                                       if (pp.id == t.columna):
                                                           print(str(t.valor))
                                                           Lista2.append(str(t.valor))
                                                   listaGeneral[pp.id] = Lista2
                                       else:
                                           print("")

                               elif (isinstance(ii,Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                   # listaGeneral
                                   for ele in x.cuerpo:
                                       y: CampoTabla = ele
                                       if (y.id == ii.Columna):
                                           print("LA columan " + str(ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                           # verificamos el alias

                                           ListaAlias = ii.Lista_Alias
                                           # Tenemos el alias
                                           nuevoNave = ListaAlias.Alias
                                           print("ahora la columna se llama" + str(nuevoNave))

                                           # Bamos a sacar todos los datos coincidentes
                                           # Vallidamos que la no venga sin datos
                                           if (ii.NombreT != ""):
                                               # hacemos una doble condicion para agarrar la columna que es
                                               if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                   i = ts_global.Datos
                                                   lista = []
                                                   for gg in ts_global.Datos:
                                                       t: DatoInsert = ts_global.obtenerDato(gg)
                                                       if (str(t.columna) == str(ii.Columna)):
                                                           print(str(t.valor))
                                                           lista.append(str(t.valor))
                                                   listaGeneral[str(nuevoNave)] = lista
                                               else:
                                                   print("")
                                           else:
                                               i = ts_global.Datos
                                               lista = []
                                               for gg in ts_global.Datos:
                                                   t: DatoInsert = ts_global.obtenerDato(gg)
                                                   if (str(t.columna) == str(ii.Columna)):
                                                       print(str(t.valor))
                                                       lista.append(str(t.valor))
                                               listaGeneral[str(nuevoNave)] = lista

                                       elif (y.id == '*'):
                                           # Recorrer todos los datos de la columna
                                           print("Vienen todo los datos  los datos de esa columna")
                                           ListaAlias = ii.Lista_Alias
                                           # Tenemos el alias
                                           nuevoNave = ListaAlias.Alias

                                           # Vallidamos que la no venga sin datos
                                           if (ii.NombreT != ""):
                                               # hacemos una doble condicion para agarrar la columna que es
                                               if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                   # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                   for columnas in x.cuerpo:
                                                       pp: CampoTabla = columnas
                                                       Lista2 = []
                                                       i = ts_global.Datos
                                                       for gg in i:
                                                           t: DatoInsert = ts_global.obtenerDato(gg)
                                                           if (pp.id == t.columna):
                                                               print(str(t.valor))
                                                               Lista2.append(str(t.valor))
                                                       listaGeneral[str(nuevoNave)] = Lista2
                                           # viene sin referencia a tabla
                                           else:
                                               # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                               for columnas in x.cuerpo:
                                                   pp: CampoTabla = columnas
                                                   Lista2 = []
                                                   i = ts_global.Datos
                                                   for gg in i:
                                                       t: DatoInsert = ts_global.obtenerDato(gg)
                                                       if (pp.id == t.columna):
                                                           print(str(t.valor))
                                                           Lista2.append(str(t.valor))
                                                   listaGeneral[str(nuevoNave)] = Lista2
                                       else:
                                           print("")
                               elif (isinstance(ii, AccesoSubConsultas)):
                                   listaQ = {}
                                   if (ii.Lista_Alias != False):
                                       # tomamos la lista de los alias
                                       li2 = ii.Lista_Alias[0]

                                       print("Bamos a ver el cuerpo de cada subconsulta")
                                       # Cuerpo de Tipo Subconsulta
                                       sub = ii.Query
                                       if (isinstance(sub, SubSelect)):
                                           sub.Ejecutar()
                                       elif (isinstance(sub, SubSelect2)):
                                           sub.Ejecutar()
                                       elif (isinstance(sub, SubSelect3)):
                                           sub.Ejecutar()
                                       elif (isinstance(sub, SubSelect4)):
                                           sub.Ejecutar()
                                       else:
                                           print("viene otro tipo de subconsulta")

                                   else:
                                       print("Bamos a ver el cuerpo de cada subconsulta")
                                       # Cuerpo de Tipo Subconsulta
                                       sub = ii.Query
                                       if (isinstance(sub, SubSelect)):
                                           sub.Ejecutar()
                                       elif (isinstance(sub, SubSelect2)):
                                           sub.Ejecutar()
                                       elif (isinstance(sub, SubSelect3)):
                                           sub.Ejecutar()
                                       elif (isinstance(sub, SubSelect4)):
                                           sub.Ejecutar()
                                       else:
                                           print("viene otro tipo de subconsulta")
                               else:
                                   print("Otros posibles tipos ")
                       else:
                           print("")

               elif(isinstance(ee,AccesoSubConsultas)):

                   if(ee.Lista_Alias!=False):
                       #tomamos la lista de los alias
                       li2 = ee.Lista_Alias[0]

                       print("Bamos a ver el cuerpo de cada subconsulta")
                       # Cuerpo de Tipo Subconsulta
                       sub = ee.Query
                       if (isinstance(sub, SubSelect)):
                           sub.Ejecutar()
                       elif (isinstance(sub, SubSelect2)):
                           sub.Ejecutar()
                       elif (isinstance(sub, SubSelect3)):
                           sub.Ejecutar()
                       elif (isinstance(sub, SubSelect4)):
                           sub.Ejecutar()
                       else:
                           print("viene otro tipo de subconsulta")

                   else:
                       print("Bamos a ver el cuerpo de cada subconsulta")
                       # Cuerpo de Tipo Subconsulta
                       sub = ee.Query
                       if (isinstance(sub, SubSelect)):
                           sub.Ejecutar()
                       elif (isinstance(sub, SubSelect2)):
                           sub.Ejecutar()
                       elif (isinstance(sub, SubSelect3)):
                           sub.Ejecutar()
                       elif (isinstance(sub, SubSelect4)):
                           sub.Ejecutar()
                       else:
                           print("viene otro tipo de subconsulta")
               else:
                    imprir("Viene otro tipo de accion ")
        else:
            imprir("SELECT : No existe la base de datos acual")
        print(listaGeneral)
        mostrarConsulta(listaGeneral)
        #listaGeneral.clear()

#============================================================================ PROCESO UNION
        for uni in self.unionn:
            if(isinstance(uni,CamposUnions)):
                if(str(uni.Reservada).upper()=="ALL"):
                    print("Viene  ALL")
                    if(str(uni.Comportamiento).upper() =="UNION"):
                        print("Viene un union")
                        ank = uni.Consulta
                        if(isinstance(ank,Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                        elif(isinstance(ank,Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                        elif(isinstance(ank,Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                        elif(isinstance(ank,Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                        else:
                                print("viene otro tipo de funcion")
                    elif(str(uni.Comportamiento).upper()=="INTERSECT"):
                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if(isinstance(ank,Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                        elif(isinstance(ank,Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                        elif(isinstance(ank,Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                        elif(isinstance(ank,Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                        else:
                            print("viene otro tipo de funcion")
                    elif(str(uni.Comportamiento).upper()=="EXCEPT"):
                        print("Viene un Except")
                        ank = uni.Consulta
                        if(isinstance(ank,Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                        elif(isinstance(ank,Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                        elif(isinstance(ank,Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                        elif(isinstance(ank,Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                        else:
                            print("viene otro tipo de funcion")
                    else:
                        print("vino una palabra diferente")
                elif(str(uni.Reservada)==","):
                    print("Viene una Coma")
                else:
                    if(str(uni.Comportamiento).upper() =="UNION"):
                        print("Viene un union")
                        ank = uni.Consulta
                        if(isinstance(ank,Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                        elif(isinstance(ank,Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                        elif(isinstance(ank,Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                        elif(isinstance(ank,Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                        else:
                                print("viene otro tipo de funcion")
                    elif(str(uni.Comportamiento).upper()=="INTERSECT"):
                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if(isinstance(ank,Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                        elif(isinstance(ank,Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                        elif(isinstance(ank,Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                        elif(isinstance(ank,Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                        else:
                            print("viene otro tipo de funcion")
                    elif(str(uni.Comportamiento).upper()=="EXCEPT"):
                        print("Viene un Except")
                        ank = uni.Consulta
                        if(isinstance(ank,Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                        elif(isinstance(ank,Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                        elif(isinstance(ank,Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                        elif(isinstance(ank,Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                        else:
                            print("viene otro tipo de funcion")
                    else:
                        print("vino una palabra diferente")





#---------------------------------------------------------------------------------------------------
class Select2(Instruccion) :
    def __init__(self,  unionn,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn
        self.Cuerpo = Cuerpo

    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr
        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos

        if r is not None:

            for ee in self.Nombres_Tablas:

                if (isinstance(ee, AccesoTablaSinLista)):  # viene sin alias

                    # Recorremos el diccionario general para ver si existe la tabla que queremos
                    # recorremos lista General de Tablas
                    for elemento2 in ts_global.Tablas:

                        x: CreateTable = ts_global.obtenerTabla(elemento2)

                        if (str(x.id) == str(ee.NombreT)):
                            # si es la tabla validamos que tipo de campo viene

                            for ii in self.Lista_Campos:

                                if (isinstance(ii,
                                               Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                    # *  , nombrecampo,  nombrecampo alias
                                    # listaGeneral
                                    for ele in x.cuerpo:  # recorremos lista de columnas
                                        y: CampoTabla = ele
                                        if (str(y.id) == str(ii.Columna)):

                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                            # Bamos a sacar todos los datos coincidentes
                                            # recorremos datos

                                            # Vallidamos que la no venga sin datos
                                            print(ii.NombreT)
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT):
                                                    print("Estoy entrando <<<<<<<<<<<<<<<<<<<<< ")
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))
                                                    listaGeneral[ii.Columna] = lista
                                                else:
                                                    print("")

                                            else:

                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))
                                                listaGeneral[ii.Columna] = lista


                                        elif (str(ii.Columna) == "*"):
                                            print("Vienen todo los datos de la tabla")

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[pp.id] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[pp.id] = Lista2


                                        else:
                                            print("")

                                elif (isinstance(ii,
                                                 Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                    # listaGeneral
                                    for ele in x.cuerpo:
                                        y: CampoTabla = ele

                                        if (y.id == ii.Columna):
                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")

                                            # verificamos el alias

                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias
                                            print("ahora la columna se llama" + str(nuevoNave))

                                            # Bamos a sacar todos los datos coincidentes
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = lista


                                        elif (y.id == '*'):
                                            # Recorrer todos los datos de la columna
                                            print("Vienen todo los datos  los datos de esa columna")

                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[str(nuevoNave)] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = Lista2
                                        else:
                                            print("")
                                elif (isinstance(ii, AccesoSubConsultas)):
                                    listaQ = {}
                                    if (ii.Lista_Alias != False):
                                        print("Bamos a ver el cuerpo de cada subconsulta")
                                        li2 = ii.Lista_Alias[0]
                                        # Cuerpo de Tipo Subconsulta
                                        sub = ii.Query
                                        if (isinstance(sub, SubSelect)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect2)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect3)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect4)):
                                            sub.Ejecutar()
                                        else:
                                            print("viene otro tipo de subconsulta")
                                    else:
                                        print("Bamos a ver el cuerpo de cada subconsulta")
                                        # Cuerpo de Tipo Subconsulta
                                        sub = ii.Query
                                        if (isinstance(sub, SubSelect)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect2)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect3)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect4)):
                                            sub.Ejecutar()
                                        else:
                                            print("viene otro tipo de subconsulta")
                                else:
                                    print("Otros posibles tipos ")
                        else:
                            print("")


                # ============================================================================   Acceso a las tablas con alias
                elif (isinstance(ee, AccesoTabla)):  # viene con un alias

                    # verificamos el alias
                    AliasTabla = ee.Lista_Alias
                    # Tenemos el alias
                    AliasT = AliasTabla.Alias

                    # Recorremos el diccionario general para ver si existe la tabla que queremos
                    # recorremos lista General de Tablas
                    for elemento2 in ts_global.Tablas:
                        x: CreateTable = ts_global.obtenerTabla(elemento2)

                        if (str(x.id) == str(ee.NombreT)):
                            # si es la tabla validamos que tipo de campo viene
                            for ii in self.Lista_Campos:

                                if (isinstance(ii,
                                               Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                    # *  , nombrecampo,  nombrecampo alias
                                    # listaGeneral
                                    for ele in x.cuerpo:  # recorremos lista de columnas
                                        y: CampoTabla = ele
                                        if (str(y.id) == str(ii.Columna)):
                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                            # Bamos a sacar todos los datos coincidentes
                                            # recorremos datos
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))
                                                            lista.append(str(t.valor))

                                                    listaGeneral[ii.Columna] = lista

                                                else:
                                                    print("")

                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))
                                                listaGeneral[ii.Columna] = lista

                                        elif (str(ii.Columna) == "*"):
                                            print("Vienen todo los datos de la tabla")
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):

                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[pp.id] = Lista2
                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[pp.id] = Lista2
                                        else:
                                            print("")

                                elif (isinstance(ii,
                                                 Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                    # listaGeneral
                                    for ele in x.cuerpo:
                                        y: CampoTabla = ele
                                        if (y.id == ii.Columna):
                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
                                            # verificamos el alias

                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias
                                            print("ahora la columna se llama" + str(nuevoNave))

                                            # Bamos a sacar todos los datos coincidentes
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))
                                                            lista.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)
                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        lista.append(str(t.valor))
                                                listaGeneral[str(nuevoNave)] = lista

                                        elif (y.id == '*'):
                                            # Recorrer todos los datos de la columna
                                            print("Vienen todo los datos  los datos de esa columna")
                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):
                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                Lista2.append(str(t.valor))
                                                        listaGeneral[str(nuevoNave)] = Lista2
                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            Lista2.append(str(t.valor))
                                                    listaGeneral[str(nuevoNave)] = Lista2
                                        else:
                                            print("")
                                elif (isinstance(ii, AccesoSubConsultas)):
                                    listaQ = {}
                                    if (ii.Lista_Alias != False):
                                        # tomamos la lista de los alias
                                        li2 = ii.Lista_Alias[0]

                                        print("Bamos a ver el cuerpo de cada subconsulta")
                                        # Cuerpo de Tipo Subconsulta
                                        sub = ii.Query
                                        if (isinstance(sub, SubSelect)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect2)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect3)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect4)):
                                            sub.Ejecutar()
                                        else:
                                            print("viene otro tipo de subconsulta")

                                    else:
                                        print("Bamos a ver el cuerpo de cada subconsulta")
                                        # Cuerpo de Tipo Subconsulta
                                        sub = ii.Query
                                        if (isinstance(sub, SubSelect)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect2)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect3)):
                                            sub.Ejecutar()
                                        elif (isinstance(sub, SubSelect4)):
                                            sub.Ejecutar()
                                        else:
                                            print("viene otro tipo de subconsulta")
                                else:
                                    print("Otros posibles tipos ")
                        else:
                            print("")

                elif (isinstance(ee, AccesoSubConsultas)):

                    if (ee.Lista_Alias != False):
                        # tomamos la lista de los alias
                        li2 = ee.Lista_Alias[0]
                        print("Bamos a ver el cuerpo de cada subconsulta")
                        # Cuerpo de Tipo Subconsulta
                        sub = ee.Query
                        if (isinstance(sub, SubSelect)):
                            sub.Ejecutar()
                        elif (isinstance(sub, SubSelect2)):
                            sub.Ejecutar()
                        elif (isinstance(sub, SubSelect3)):
                            sub.Ejecutar()
                        elif (isinstance(sub, SubSelect4)):
                            sub.Ejecutar()
                        else:
                            print("viene otro tipo de subconsulta")

                    else:
                        print("Bamos a ver el cuerpo de cada subconsulta")
                        # Cuerpo de Tipo Subconsulta
                        sub = ee.Query
                        if (isinstance(sub, SubSelect)):
                            sub.Ejecutar()
                        elif (isinstance(sub, SubSelect2)):
                            sub.Ejecutar()
                        elif (isinstance(sub, SubSelect3)):
                            sub.Ejecutar()
                        elif (isinstance(sub, SubSelect4)):
                            sub.Ejecutar()
                        else:
                            print("viene otro tipo de subconsulta")
                else:
                    imprir("Viene otro tipo de accion ")
        else:
            imprir("SELECT : No existe la base de datos acual")
        print(listaGeneral)
        mostrarConsulta(listaGeneral)





#====================================================================   Proceso del cuerpo para editar valores en la tabla
       #procesando el cuerpo General de las tablas al insertar correctamente

        for tiposCuerpo in self.Cuerpo:
            if (isinstance(tiposCuerpo, Cuerpo_TipoWhere)):
                print("Vamos a ver condiciones y luego a mostrar datos de las condiciones")
                resultado = Inter.procesar_expresion_select(tiposCuerpo.Cuerpo, ts_global)
                if resultado is None:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SELECT: No existen registros.")
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SELECT: No existen registros.2222")
                    for r in resultado:
                        print(str(r.valor)+" "+str(r.tabla)+" "+str(r.fila))

                titulos = []
                for campo in listaGeneral:
                    titulos.append(str(campo))

                lis = []
                for t in titulos:
                    for res in resultado:
                        for item in ts_global.Datos:
                            x: DatoInsert = ts_global.obtenerDato(item)
                            if t == x.columna and x.fila == res.fila:
                                lis.append(x)

                nuevoDicc = {}
                # ingreso lista final FALTA
                for t in titulos:
                    lis2 = []
                    for u in lis:
                        if u.columna == t:
                            lis2.append(u.valor)
                    nuevoDicc[t] = lis2

                print(nuevoDicc)
                mostrarConsulta(nuevoDicc)

            elif (isinstance(tiposCuerpo, GroupBy)):
                print("Vamos a ver los tipos de grupos a realizar ")
                #si no trae having va a tomar directamente el objeto relacionado
                if (tiposCuerpo.Condiciones == False):
# ====================================================================== ASC
# ============== Aqui Amarramos las Tuplas para tomar todos los valores
                    # Diccionarios auxiliares
                    ListaN = {}
                    # listas Auxiliares
                    # Esta lista tendra concatenado tanto el nombre o con el alias
                    listaColumnas = []
                    # Recorremos lista General
                    contador2 = 0
                    # primero llenamos el nuevo diccionario  amarrando las tuplas
                    for campo in listaGeneral:
                        contador = 0
                        listaColumnas.append(campo)
                        # contador de filas
                        if (contador2 == 0):
                            for datos in listaGeneral.get(campo):
                                print("Esta es la longitud de la columna >" + str(len(ListaN)))
                                ListaN[contador] = [datos]
                                contador += 1
                                contador2 += 1
                        else:
                            for datos in listaGeneral.get(campo):
                                print("Esta es la longitud de la columna >" + str(len(ListaN)))
                                ListaN[contador].append(datos)
                                contador += 1

# ============== Ahora ordenamos todo respecto a una columna
                    object: OrderBy = tiposCuerpo
                    tipo: AccesoGroupBy = object.Lista_Campos[0]
                    date = tipo.Columna

                    # Si viene la palabra reservada Ascendente
                    if (str(tipo.Estado).upper() == 'ASC'):
                        # Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                        # tenemos el contador de columnas
                        colN = 0
                        for nombre in listaColumnas:
                            print(nombre)
                            print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                            print(date)
                            if (nombre == date):
                                colN += 1
                            else:
                                print("")
                        # tenemos el indice de la columna solicitada ahora editamos
                        # Diccionario auxiliar
                        diccionario2 = {}
                        listita = []
                        indices = 0
                        # Agarramos los datos con los que se van a ordenar los datos
                        print("Aqui estan las cosas <<<<<<")
                        print(str(colN))
                        print(ListaN)
                        for n in ListaN:
                            listita.append(ListaN.get(n)[colN - 1])
                        listt = sorted(listita)
                        print(listita)
                        # Recorremos la lista ordenada
                        for n2 in listt:
                            diccionario2[gets(ListaN, n2, colN - 1)] = ListaN.get(gets(ListaN, n2, colN - 1))
                        print(diccionario2)
                    # Si viene la palabra reservada Descendente
                    elif (str(tipo.Estado).upper() == 'DESC'):
                        # Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                        # tenemos el contador de columnas
                        colN = 0
                        for nombre in listaColumnas:
                            print(nombre)
                            print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                            print(date)
                            if (nombre == date):
                                colN += 1
                            else:
                                print("")
                        # tenemos el indice de la columna solicitada ahora editamos
                        # Diccionario auxiliar
                        diccionario2 = {}
                        listita = []
                        indices = 0
                        # Agarramos los datos con los que se van a ordenar los datos
                        print("Aqui estan las cosas <<<<<<")
                        print(str(colN))
                        print(ListaN)

                        for n in ListaN:
                            listita.append(ListaN.get(n)[colN - 1])
                        listt = sorted(listita, reverse=True)
                        print(listt)

                        # Recorremos la lista ordenada
                        for n2 in listt:
                            diccionario2[gets(ListaN, n2, colN - 1)] = ListaN.get(gets(ListaN, n2, colN - 1))
                        print(diccionario2)

                    # Si no viene ordenamos ascendentemente
                    else:
                        # Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                        # tenemos el contador de columnas
                        colN = 0
                        for nombre in listaColumnas:
                            print(nombre)
                            print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                            print(date)
                            if (nombre == date):
                                colN += 1
                            else:
                                print("")
                        # tenemos el indice de la columna solicitada ahora editamos
                        # Diccionario auxiliar
                        diccionario2 = {}
                        listita = []
                        indices = 0
                        # Agarramos los datos con los que se van a ordenar los datos
                        print("Aqui estan las cosas <<<<<<")
                        print(str(colN))
                        print(ListaN)
                        for n in ListaN:
                            listita.append(ListaN.get(n)[colN - 1])
                        listt = sorted(listita)
                        print(listita)
                        # Recorremos la lista ordenada
                        for n2 in listt:
                            diccionario2[gets(ListaN, n2, colN - 1)] = ListaN.get(gets(ListaN, n2, colN - 1))
                        print(diccionario2)

# =============  Hacemos un contador  para gravar su numero de columnas
                    listak = []
                    contadorlist = 0
                    for jj in diccionario2:
                        listak.append(contadorlist)
                        contadorlist += 1
                    print(listak)
                    # ==============  Renombramos los datos
                    contadoraa = 0
                    for n in diccionario2:
                        diccionario2[str(listak[contadoraa])] = diccionario2.pop(n)
                        contadoraa += 1
                    print(diccionario2)
# ============== Regresamos los datos a su posicion inicial
                    diccionariof = {}
                    # primero llenamos el nuevo diccionario  amarrando las tuplas
                    for campo in diccionario2:
                        # contador de filas
                        contador333 = 0
                        if (len(diccionariof) == 0):
                            for datos in diccionario2.get(campo):
                                diccionariof[str(contador333)] = [datos]
                                contador333 += 1
                        else:
                            for datos in diccionario2.get(campo):
                                diccionariof[str(contador333)].append(datos)
                                contador333 += 1
                    print(diccionariof)

# ============== Ahora ordenamos Asignamos los nombres de las claves o columnas como son
                    contadornn = 0
                    diccionarioN = {}
                    diccionarioN.update(diccionariof)

                    print(diccionariof)
                    print("ESTA ES <<<<<<<<<<<<<<<<<<<<<<<<< El que cambiamos de nombre")
                    print(listaColumnas)
                    print("ESTA ES <<<<<<<<<<<<<<<<<<<<<<<<< Estas son las columnas")

                    for n in diccionariof:
                        diccionarioN[listaColumnas[contadornn]] = diccionarioN.pop(n)
                        contadornn += 1
                    # imprimimos  la lista haber si hace lo que se piensa
                    listaGeneral.clear()
                    listaGeneral.update(diccionarioN)

                    #mostrarConsulta(diccionarioN)
                    # diccionariof.clear

                else:
                    #Tomamos las Acciones de expresion
                    print("Aqui se hacen Acciones con la Tabla resultante")
                    imprir("GROUP BY:  Aqui tenemos un una accion <<")

            elif (isinstance(tiposCuerpo, OrderBy)):
                print("Vamos a ordenar  segun lo que venga ")

#====================================================================== ASC
#============== Aqui Amarramos las Tuplas para tomar todos los valores
                #Diccionarios auxiliares
                ListaN ={}
                # listas Auxiliares
                #Esta lista tendra concatenado tanto el nombre o con el alias
                listaColumnas=[]
                #Recorremos lista General
                contador2 = 0
                #primero llenamos el nuevo diccionario  amarrando las tuplas
                for campo in listaGeneral:
                   contador = 0
                   listaColumnas.append(campo)
                   #contador de filas
                   if(contador2==0):
                       for datos in listaGeneral.get(campo):
                           print("Esta es la longitud de la columna >" + str(len(ListaN)))
                           ListaN[contador] = [datos]
                           contador += 1
                           contador2+=1
                   else:
                       for datos in listaGeneral.get(campo):
                           print("Esta es la longitud de la columna >" + str(len(ListaN)))
                           ListaN[contador].append(datos)
                           contador += 1

# ============== Ahora ordenamos todo respecto a una columna
                object:OrderBy = tiposCuerpo
                tipo:AccesoGroupBy =object.Lista_Campos[0]
                date = tipo.Columna

                #Si viene la palabra reservada Ascendente
                if(str(tipo.Estado).upper()=='ASC'):
                    #Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                    #tenemos el contador de columnas
                    colN = 0
                    for nombre in listaColumnas:
                        print(nombre)
                        print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                        print(date)
                        if(nombre == date):
                           colN+=1
                        else:
                            print("")
                    #tenemos el indice de la columna solicitada ahora editamos
                    #Diccionario auxiliar
                    diccionario2 = {}
                    listita = []
                    indices = 0
                    #Agarramos los datos con los que se van a ordenar los datos
                    print("Aqui estan las cosas <<<<<<")
                    print(str(colN))
                    print(ListaN)
                    for n in ListaN:
                        listita.append(ListaN.get(n)[colN-1])
                    listt = sorted(listita)
                    print(listita)
                    #Recorremos la lista ordenada
                    for n2 in listt:
                        diccionario2[gets(ListaN,n2,colN-1)] = ListaN.get(gets(ListaN,n2,colN-1))
                    print(diccionario2)
                # Si viene la palabra reservada Descendente
                elif(str(tipo.Estado).upper()=='DESC'):
                    #Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                    #tenemos el contador de columnas
                    colN = 0
                    for nombre in listaColumnas:
                        print(nombre)
                        print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                        print(date)
                        if(nombre == date):
                           colN+=1
                        else:
                            print("")
                    #tenemos el indice de la columna solicitada ahora editamos
                    #Diccionario auxiliar
                    diccionario2 = {}
                    listita = []
                    indices = 0
                    #Agarramos los datos con los que se van a ordenar los datos
                    print("Aqui estan las cosas <<<<<<")
                    print(str(colN))
                    print(ListaN)

                    for n in ListaN:
                        listita.append(ListaN.get(n)[colN-1])
                    listt = sorted(listita, reverse=True)
                    print(listt)

                    #Recorremos la lista ordenada
                    for n2 in listt:
                        diccionario2[gets(ListaN,n2,colN-1)] = ListaN.get(gets(ListaN,n2,colN-1))
                    print(diccionario2)

                # Si no viene ordenamos ascendentemente
                else:
                    #Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                    #tenemos el contador de columnas
                    colN = 0
                    for nombre in listaColumnas:
                        print(nombre)
                        print("<<<<<<<<<<<<<<<<<<<<<   Este essssss")
                        print(date)
                        if(nombre == date):
                           colN+=1
                        else:
                            print("")
                    #tenemos el indice de la columna solicitada ahora editamos
                    #Diccionario auxiliar
                    diccionario2 = {}
                    listita = []
                    indices = 0
                    #Agarramos los datos con los que se van a ordenar los datos
                    print("Aqui estan las cosas <<<<<<")
                    print(str(colN))
                    print(ListaN)
                    for n in ListaN:
                        listita.append(ListaN.get(n)[colN-1])
                    listt = sorted(listita)
                    print(listita)
                    #Recorremos la lista ordenada
                    for n2 in listt:
                        diccionario2[gets(ListaN,n2,colN-1)] = ListaN.get(gets(ListaN,n2,colN-1))
                    print(diccionario2)



#=============  Hacemos un contador  para gravar su numero de columnas
                listak =[]
                contadorlist = 0
                for jj in diccionario2:
                    listak.append(contadorlist)
                    contadorlist+=1
                print(listak)
#==============  Renombramos los datos
                contadoraa = 0
                for n in diccionario2:
                    diccionario2[str(listak[contadoraa])] = diccionario2.pop(n)
                    contadoraa += 1
                print(diccionario2)
#============== Regresamos los datos a su posicion inicial
                diccionariof = {}
                # primero llenamos el nuevo diccionario  amarrando las tuplas
                for campo in diccionario2:
                    # contador de filas
                    contador333 = 0
                    if (len(diccionariof) == 0):
                        for datos in diccionario2.get(campo):
                            diccionariof[str(contador333)] = [datos]
                            contador333 += 1
                    else:
                        for datos in diccionario2.get(campo):
                            diccionariof[str(contador333)].append(datos)
                            contador333 += 1
                print(diccionariof)

# ============== Ahora ordenamos Asignamos los nombres de las claves o columnas como son
                contadornn = 0
                diccionarioN={}
                diccionarioN.update(diccionariof)

                print(diccionariof)
                print("ESTA ES <<<<<<<<<<<<<<<<<<<<<<<<< El que cambiamos de nombre")
                print(listaColumnas)
                print("ESTA ES <<<<<<<<<<<<<<<<<<<<<<<<< Estas son las columnas")

                for n in diccionariof:
                    diccionarioN[listaColumnas[contadornn]] = diccionarioN.pop(n)
                    contadornn += 1
                #imprimimos  la lista haber si hace lo que se piensa
                listaGeneral.clear()
                listaGeneral.update(diccionarioN)
                #diccionariof.clear

            elif (isinstance(tiposCuerpo, AccesoLimit)):
                print("Bamos a elegir el limite ")
                if (str(tiposCuerpo.Reservada).lower() == "offset"):
                    # codigo de offset
                    # Recorremos la lista General
                    print("Estoy entrando al Offset")
                    for nn in listaGeneral:
                        l = listaGeneral.get(nn)
                        # Recorro la lista dentro del diccionario
                        indice = 0
                        for dato in l:
                            if (indice < int(tiposCuerpo.Expresion_Numerica)):
                                print(">>>" + l.pop(0))
                                indice += 1
                elif (str(tiposCuerpo.Reservada).lower() == "limit"):
                    # Codigo de limit
                    if (str(tiposCuerpo.Expresion_Numerica).lower() == "all"):
                        print("Voy a retornar todo sin limite")
                    else:
                        # Recorremos la lista General
                        for nn in listaGeneral:
                            l = listaGeneral.get(nn)

                            # Recorro la lista dentro del diccionario
                            indice = 0
                            for dato in l:
                                if (indice < int(tiposCuerpo.Expresion_Numerica)):
                                    print(">>>"+l.pop())
                                    indice += 1

            elif (isinstance(tiposCuerpo, AccesoSubConsultas)):
                print("Bamos a ver el cuerpo de cada subconsulta")
                #Cuerpo de Tipo Subconsulta
                for sub in tiposCuerpo.Query:
                    if(isinstance(sub,SubSelect)):
                        sub.Ejecutar(sub.Lista_Campos,sub.Nombres_Tablas)
                    elif(isinstance(sub,SubSelect2)):
                        sub.Ejecutar(sub.Lista_Campos,sub.Nombres_Tablas)
                    elif(isinstance(sub,SubSelect3)):
                        sub.Ejecutar(sub.Lista_Campos,sub.Nombres_Tablas)
                    elif(isinstance(sub,SubSelect4)):
                        sub.Ejecutar(sub.Lista_Campos,sub.Nombres_Tablas)
                    else:
                        print("viene otro tipo de subconsulta")


#aqui le agrega a general las listas que se generan
#=================================================================================== PROCESO UNION
            for uni in self.unionn:
                if (isinstance(uni, CamposUnions)):
                    if (str(uni.Reservada).upper() == "ALL"):
                        print("Viene  ALL")
                        if (str(uni.Comportamiento).upper() == "UNION"):
                            print("Viene un union")
                            ank = uni.Consulta
                            if (isinstance(ank, Select)):
                                print("viene un tipo de select normal unido")
                                ank.Ejecutar()
                            elif (isinstance(ank, Select2)):
                                ank.Ejecutar()
                                print("viene un tipo de select normal con cuerpo")
                            elif (isinstance(ank, Select3)):
                                ank.Ejecutar()
                                print("Viene un tipo de Select normal con distinct")
                            elif (isinstance(ank, Select4)):
                                ank.Ejecutar()
                                print("viene un tipo de Select normal con cuerpo y distinct")
                            else:
                                print("viene otro tipo de funcion")
                        elif (str(uni.Comportamiento).upper() == "INTERSECT"):
                            print("Viene un Intersect")
                            ank = uni.Consulta
                            if (isinstance(ank, Select)):
                                print("viene un tipo de select normal unido")
                                ank.Ejecutar()
                            elif (isinstance(ank, Select2)):
                                ank.Ejecutar()
                                print("viene un tipo de select normal con cuerpo")
                            elif (isinstance(ank, Select3)):
                                ank.Ejecutar()
                                print("Viene un tipo de Select normal con distinct")
                            elif (isinstance(ank, Select4)):
                                ank.Ejecutar()
                                print("viene un tipo de Select normal con cuerpo y distinct")
                            else:
                                print("viene otro tipo de funcion")
                        elif (str(uni.Comportamiento).upper() == "EXCEPT"):
                            print("Viene un Except")
                            ank = uni.Consulta
                            if (isinstance(ank, Select)):
                                print("viene un tipo de select normal unido")
                                ank.Ejecutar()
                            elif (isinstance(ank, Select2)):
                                ank.Ejecutar()
                                print("viene un tipo de select normal con cuerpo")
                            elif (isinstance(ank, Select3)):
                                ank.Ejecutar()
                                print("Viene un tipo de Select normal con distinct")
                            elif (isinstance(ank, Select4)):
                                ank.Ejecutar()
                                print("viene un tipo de Select normal con cuerpo y distinct")
                            else:
                                print("viene otro tipo de funcion")
                        else:
                            print("vino una palabra diferente")
                    elif (str(uni.Reservada) == ","):
                        print("Viene una Coma")
                    else:
                        if (str(uni.Comportamiento).upper() == "UNION"):
                            print("Viene un union")
                            ank = uni.Consulta
                            if (isinstance(ank, Select)):
                                print("viene un tipo de select normal unido")
                                ank.Ejecutar()
                            elif (isinstance(ank, Select2)):
                                ank.Ejecutar()
                                print("viene un tipo de select normal con cuerpo")
                            elif (isinstance(ank, Select3)):
                                ank.Ejecutar()
                                print("Viene un tipo de Select normal con distinct")
                            elif (isinstance(ank, Select4)):
                                ank.Ejecutar()
                                print("viene un tipo de Select normal con cuerpo y distinct")
                            else:
                                print("viene otro tipo de funcion")
                        elif (str(uni.Comportamiento).upper() == "INTERSECT"):
                            print("Viene un Intersect")
                            ank = uni.Consulta
                            if (isinstance(ank, Select)):
                                print("viene un tipo de select normal unido")
                                ank.Ejecutar()
                            elif (isinstance(ank, Select2)):
                                ank.Ejecutar()
                                print("viene un tipo de select normal con cuerpo")
                            elif (isinstance(ank, Select3)):
                                ank.Ejecutar()
                                print("Viene un tipo de Select normal con distinct")
                            elif (isinstance(ank, Select4)):
                                ank.Ejecutar()
                                print("viene un tipo de Select normal con cuerpo y distinct")
                            else:
                                print("viene otro tipo de funcion")
                        elif (str(uni.Comportamiento).upper() == "EXCEPT"):
                            print("Viene un Except")
                            ank = uni.Consulta
                            if (isinstance(ank, Select)):
                                print("viene un tipo de select normal unido")
                                ank.Ejecutar()
                            elif (isinstance(ank, Select2)):
                                ank.Ejecutar()
                                print("viene un tipo de select normal con cuerpo")
                            elif (isinstance(ank, Select3)):
                                ank.Ejecutar()
                                print("Viene un tipo de Select normal con distinct")
                            elif (isinstance(ank, Select4)):
                                ank.Ejecutar()
                                print("viene un tipo de Select normal con cuerpo y distinct")
                            else:
                                print("viene otro tipo de funcion")
                        else:
                            print("vino una palabra diferente")

        #print(ListaN)
        print(listaGeneral)
        mostrarConsulta(listaGeneral)
        listaGeneral.clear



# Con Distinct
# ---------------------------------------------------------------------------------------------------
class Select3(Instruccion):
    def __init__(self, distinct, unionn, Lista_Campos=[], Nombres_Tablas=[]):
        self.distinct = distinct
        self.Lista_Campos = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn = unionn

    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos

        if r is not None:

            for ee in self.Nombres_Tablas:

                if (isinstance(ee, AccesoTablaSinLista)):  # viene sin alias

                    ####Recorremos el diccionario general para ver si existe la tabla que queremos
                    # recorremos lista General de Tablas
                    for elemento2 in ts_global.Tablas:

                        x: CreateTable = ts_global.obtenerTabla(elemento2)
                        if (str(x.id) == str(ee.NombreT)):
                            # si es la tabla validamos que tipo de campo viene

                            for ii in self.Lista_Campos:
                                if (isinstance(ii,
                                               Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                    # *  , nombrecampo,  nombrecampo alias
                                    # listaGeneral
                                    for ele in x.cuerpo:  # recorremos lista de columnas
                                        y: CampoTabla = ele
                                        if (str(y.id) == str(ii.Columna)):

                                            ##Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            # comparamos si ya existe en la lista
                                                            miniB = False
                                                            for item in lista:
                                                                if str(item.valor) == str(t.valor):
                                                                    print(
                                                                        "------- METER EL OBJETOO COMPLETO DE DATOINSERT 1")
                                                                    miniB = True

                                                            if miniB == False:
                                                                lista.append(t)
                                                            else:
                                                                pass
                                                        else:
                                                            print("ALGUNA ESPECIE DE ERROR")
                                                            # fin comparacion insert

                                                    listaGeneral[ii.Columna] = lista
                                                else:
                                                    print("")
                                            else:  # SI EL NOMBRE O ALIAS ESTA VACIO
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    # Recorremos lista de Campos

                                                    if (str(t.columna) == str(
                                                            ii.Columna)):  # COMPARAR CADA ATRIBUTO Y SI ES LA MISMA COLUMNA ALMACENAR
                                                        print(str(t.valor))

                                                        # comparamos si ya existe en la lista
                                                        miniB = False
                                                        for item in lista:
                                                            miI: DatoInsert = item
                                                            if str(miI.valor) == str(t.valor):
                                                                miniB = True

                                                        if miniB == False:
                                                            print(" SI ALMACENA: > " + str(t.valor))
                                                            lista.append(t)
                                                        else:
                                                            pass
                                                    else:
                                                        print("ALGUNA ESPECIE DE ERROR")
                                                        # fin comparacion insert

                                                listaGeneral[ii.Columna] = lista
                                        elif (str(ii.Columna) == "*"):
                                            print("Vienen todo los datos de la tabla")

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                # comparamos si ya existe en la lista
                                                                miniB = False
                                                                for item in Lista2:
                                                                    if str(item.valor) == str(t.valor):
                                                                        print("--------YA ESTOY 2")
                                                                        miniB = True

                                                                if miniB == False:
                                                                    Lista2.append(t)
                                                                else:
                                                                    pass
                                                            else:
                                                                print("ALGUNA ESPECIE DE ERROR")
                                                                # fin comparacion insert
                                                        listaGeneral[pp.id] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            # comparamos si ya existe en la lista
                                                            miniB = False
                                                            for item in Lista2:
                                                                if str(item.valor) == str(t.valor):
                                                                    print("--------YA ESTOY 3")
                                                                    miniB = True

                                                            if miniB == False:
                                                                Lista2.append(t)
                                                            else:
                                                                pass
                                                        else:
                                                            print("ALGUNA ESPECIE DE ERROR")
                                                            # fin comparacion insert
                                                    listaGeneral[pp.id] = Lista2
                                        else:
                                            print(" ERROR NO EXISTE LA TABLA")

                                elif (isinstance(ii, Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                    # listaGeneral
                                    for ele in x.cuerpo:
                                        y: CampoTabla = ele

                                        if (y.id == ii.Columna):
                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores 4")

                                            # verificamos el alias

                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias

                                            print("ahora la columna se llama" + str(nuevoNave))

                                            # Bamos a sacar todos los datos coincidentes
                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):
                                                    i = ts_global.Datos
                                                    lista = []
                                                    for gg in ts_global.Datos:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))
                                                            # comparamos si ya existe en la lista
                                                            miniB = False
                                                            for item in lista:
                                                                if str(item.valor) == str(t.valor):
                                                                    print("--------YA ESTOY 4")
                                                                    miniB = True

                                                            if miniB == False:
                                                                lista.append(t)
                                                            else:
                                                                pass
                                                        else:
                                                            print("ALGUNA ESPECIE DE ERROR")
                                                            # fin comparacion insert
                                                    listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        # comparamos si ya existe en la lista
                                                        miniB = False
                                                        for item in lista:
                                                            if str(item.valor) == str(t.valor):
                                                                print("--------YA ESTOY 5")
                                                                miniB = True

                                                        if miniB == False:
                                                            lista.append(t)
                                                        else:
                                                            pass
                                                    else:
                                                        print("ALGUNA ESPECIE DE ERROR")
                                                        # fin comparacion insert
                                                listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = lista


                                        elif (y.id == '*'):
                                            # Recorrer todos los datos de la columna
                                            print("Vienen todo los datos  los datos de esa columna")

                                            ListaAlias = ii.Lista_Alias
                                            # Tenemos el alias
                                            nuevoNave = ListaAlias.Alias

                                            # Vallidamos que la no venga sin datos
                                            if (ii.NombreT != ""):
                                                # hacemos una doble condicion para agarrar la columna que es
                                                if (str(x.id) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                    for columnas in x.cuerpo:
                                                        pp: CampoTabla = columnas
                                                        Lista2 = []
                                                        i = ts_global.Datos
                                                        for gg in i:
                                                            t: DatoInsert = ts_global.obtenerDato(gg)
                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))
                                                                # comparamos si ya existe en la lista
                                                                miniB = False
                                                                for item in Lista2:
                                                                    if str(item.valor) == str(t.valor):
                                                                        print("--------YA ESTOY 6")
                                                                        miniB = True

                                                                if miniB == False:
                                                                    Lista2.append(t)
                                                                else:
                                                                    pass
                                                            else:
                                                                print("ALGUNA ESPECIE DE ERROR")
                                                                # fin comparacion insert
                                                        listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = Lista2

                                            # viene sin referencia a tabla
                                            else:
                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente
                                                for columnas in x.cuerpo:
                                                    pp: CampoTabla = columnas
                                                    Lista2 = []
                                                    i = ts_global.Datos
                                                    for gg in i:
                                                        t: DatoInsert = ts_global.obtenerDato(gg)
                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))
                                                            # comparamos si ya existe en la lista
                                                            miniB = False
                                                            for item in Lista2:
                                                                if str(item.valor) == str(t.valor):
                                                                    print("--------YA ESTOY 7")
                                                                    miniB = True

                                                            if miniB == False:
                                                                Lista2.append(t)
                                                            else:
                                                                pass
                                                        else:
                                                            print("ALGUNA ESPECIE DE ERROR")
                                                            # fin comparacion insert
                                                    listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = Lista2
                                        else:
                                            print("E RRRRORRR ")
                                else:
                                    print("Otros posibles tipos ")
                        else:
                            print(" LAS TABLAS NO SON CORRECTAS")

                # VIENE CON UN ALIAS
                elif (isinstance(ee, AccesoTabla)):  # viene con un alias

                    # verificamos el alias

                    AliasTabla = ee.Lista_Alias

                    # Tenemos el alias

                    AliasT = AliasTabla.Alias

                    # Recorremos el diccionario general para ver si existe la tabla que queremos

                    # recorremos lista General de Tablas

                    for elemento2 in ts_global.Tablas:

                        x: CreateTable = ts_global.obtenerTabla(elemento2)

                        if (str(x.id) == str(ee.NombreT)):

                            # si es la tabla validamos que tipo de campo viene

                            for ii in self.Lista_Campos:

                                if (isinstance(ii,Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias

                                    # *  , nombrecampo,  nombrecampo alias

                                    # listaGeneral

                                    for ele in x.cuerpo:  # recorremos lista de columnas

                                        y: CampoTabla = ele

                                        if (str(y.id) == str(ii.Columna)):

                                            print("LA columan " + str(

                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")

                                            # Bamos a sacar todos los datos coincidentes

                                            # recorremos datos

                                            # Vallidamos que la no venga sin datos

                                            if (ii.NombreT != ""):

                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):

                                                    i = ts_global.Datos

                                                    lista = []

                                                    for gg in ts_global.Datos:

                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))

                                                    listaGeneral[ii.Columna] = lista

                                                else:

                                                    print("")

                                            else:

                                                i = ts_global.Datos

                                                lista = []

                                                for gg in ts_global.Datos:

                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))

                                                listaGeneral[ii.Columna] = lista

                                        elif (str(ii.Columna) == "*"):

                                            print("Vienen todo los datos de la tabla")

                                            # Vallidamos que la no venga sin datos

                                            if (ii.NombreT != ""):

                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente

                                                    for columnas in x.cuerpo:

                                                        pp: CampoTabla = columnas

                                                        Lista2 = []

                                                        i = ts_global.Datos

                                                        for gg in i:

                                                            t: DatoInsert = ts_global.obtenerDato(gg)

                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))

                                                                Lista2.append(str(t.valor))

                                                        listaGeneral[pp.id] = Lista2

                                            # viene sin referencia a tabla

                                            else:

                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente

                                                for columnas in x.cuerpo:

                                                    pp: CampoTabla = columnas

                                                    Lista2 = []

                                                    i = ts_global.Datos

                                                    for gg in i:

                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))

                                                            Lista2.append(str(t.valor))

                                                    listaGeneral[pp.id] = Lista2

                                        else:

                                            print("")

                                elif (isinstance(ii,Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

                                    # listaGeneral

                                    for ele in x.cuerpo:

                                        y: CampoTabla = ele

                                        if (y.id == ii.Columna):

                                            print("LA columan " + str(
                                                ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")

                                            # verificamos el alias

                                            ListaAlias = ii.Lista_Alias

                                            # Tenemos el alias

                                            nuevoNave = ListaAlias.Alias

                                            print("ahora la columna se llama" + str(nuevoNave))

                                            # Bamos a sacar todos los datos coincidentes

                                            # Vallidamos que la no venga sin datos

                                            if (ii.NombreT != ""):

                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):

                                                    i = ts_global.Datos

                                                    lista = []

                                                    for gg in ts_global.Datos:

                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (str(t.columna) == str(ii.Columna)):
                                                            print(str(t.valor))

                                                            lista.append(str(t.valor))

                                                    listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = lista

                                                else:

                                                    print("")

                                            else:

                                                i = ts_global.Datos

                                                lista = []

                                                for gg in ts_global.Datos:

                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))

                                                        lista.append(str(t.valor))

                                                listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = lista

                                        elif (y.id == '*'):

                                            # Recorrer todos los datos de la columna

                                            print("Vienen todo los datos  los datos de esa columna")

                                            ListaAlias = ii.Lista_Alias

                                            # Tenemos el alias

                                            nuevoNave = ListaAlias.Alias

                                            # Vallidamos que la no venga sin datos

                                            if (ii.NombreT != ""):

                                                # hacemos una doble condicion para agarrar la columna que es

                                                if (str(x.id) == ii.NombreT or str(AliasT) == ii.NombreT):

                                                    # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente

                                                    for columnas in x.cuerpo:

                                                        pp: CampoTabla = columnas

                                                        Lista2 = []

                                                        i = ts_global.Datos

                                                        for gg in i:

                                                            t: DatoInsert = ts_global.obtenerDato(gg)

                                                            if (pp.id == t.columna):
                                                                print(str(t.valor))

                                                                Lista2.append(str(t.valor))

                                                        listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = Lista2

                                            # viene sin referencia a tabla

                                            else:

                                                # Recorremos todo de nuevo para ver si vienen las columnas propias de la tabla que estamos actualmente

                                                for columnas in x.cuerpo:

                                                    pp: CampoTabla = columnas

                                                    Lista2 = []

                                                    i = ts_global.Datos

                                                    for gg in i:

                                                        t: DatoInsert = ts_global.obtenerDato(gg)

                                                        if (pp.id == t.columna):
                                                            print(str(t.valor))

                                                            Lista2.append(str(t.valor))

                                                    listaGeneral[str(nuevoNave)+"."+str(ii.Columna)] = Lista2
                                        else:
                                            print("un posible error")
                                else:
                                    print("Otros posibles tipos ")
                        else:
                            print("un posible error")
                else:

                    imprir("Viene otro tipo de accion ")
        else:
            imprir("SELECT : No existe la base de datos acual")



        # primero obtener la primera lista
        miCuenta = 0
        titulo = []
        alias = []
        primera = []
        for lista in listaGeneral:
            if miCuenta != 1:
                primera = listaGeneral.get(lista)
                miCuenta += 1
            break

        # obtener los titulos del punto a la izquierda esto_No.ESTO_SI
        for lista in listaGeneral:
            derecha = self.quitarIzq(lista)
            sinP = derecha.replace(".", "")
            titulo.append(str(sinP))

        for listA in listaGeneral:
            derecha = self.quitarDer(listA)
            sinP = derecha.replace(".", "")
            print(sinP)

        # obtener los alias con punto
        for lista in listaGeneral:
            alias.append(str(lista))
            print(str(lista))

        nuevoDic = {}
        resdistinct = []

        for reg in primera:  # [a, b, c]
            p: DatoInsert = reg
            for t in titulo:  # [carne, apellido]
                for dat in ts_global.Datos:  # Datos
                    de: DatoInsert = ts_global.obtenerDato(dat)
                    for titu in titulo:  # [carne, apellido]
                        if de.columna == titu:
                            if p.columna == t and p.fila == de.fila:
                                resdistinct.append(de)

        print("TITULOSSSS")

        for aliasTitulo in alias:
            aliasT = self.quitarDer(aliasTitulo)
            nombre = self.quitarIzq(aliasTitulo)
            nombre = nombre.replace(".", "")
            print("Insertar en: "+str(aliasT))
            lis = []
            for u in resdistinct:
                print(str(u.columna)+str(nombre))
                if str(u.columna) == str(nombre):
                    print("Si guarda")
                    lis.append(u.valor)
                    print(lis)

            nuevoDic[aliasT] = lis

        print(nuevoDic)
        #mostrarConsulta(nuevoDic)

        mostrarConsulta(nuevoDic)
        nuevoDic.clear()
        listaGeneral.clear()

    def quitarIzq(self,Cadena):
        resultado = ""
        punto = False
        for letra in Cadena:
            if letra == '.':
                punto= True

            if punto == True:
                resultado += letra

        if punto == False:
            return Cadena
        else:
            return resultado

    def quitarDer(self,Cadena):
        resultado = ""
        punto = True
        for letra in Cadena:
            if letra == '.':
                punto= False

            if punto == True:
                resultado += letra

        return resultado

