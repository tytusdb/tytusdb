import ts as TS
import jsonMode as Master
import interprete as Inter
from six import string_types
from errores import *
from random import *
from expresiones import *

from prettytable import PrettyTable


LisErr = TablaError([])
ts_global = TS.TablaDeSimbolos()
Lista = []
ListaTablasG = []
baseN = []
baseActual = ""
Ejecucion  = ">"
listaGeneral = {}

listaGeneralSubQuery = []

#Lista los datos retornados pode cada una de las posibles condiciones
Modificaciones={}



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



def ExisteInList(lista,valor):
    for ss in lista:
        if(str(ss)==str(valor)):
            return  False

    return True



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
    listaGeneral ={}
    listaConsultados=[]
    contadorCol = 0

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
                                        print(ii.NombreT)

                                        if (ii.NombreT != ""):
                                            # hacemos una doble condicion para agarrar la columna que es
                                            if (str(x.id) == ii.NombreT):
                                                print("Estoy entrando <<<<<<<<<<<<<<<<<<<<< ")
                                                i = ts_global.Datos
                                                lista = []

                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna) and str(t.tabla) == str(
                                                            ii.NombreT)):

                                                        print(str(t.columna) + "Estos vienen" + str(t.tabla))
                                                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

                                                        nombreGen = ""
                                                        if (ExisteInList(listaConsultados,
                                                                         t.columna) == False):  # Existe

                                                            print("Campo ya existe se creara un nuevo nombre")
                                                            nombreGen += str(t.columna) + str(contadorCol)
                                                            print(str(t.valor))
                                                            listaGeneralSubQuery.append(t)
                                                            lista.append(str(t.valor))

                                                        else:
                                                            listaConsultados.append(t.columna)
                                                            print(str(t.valor))
                                                            listaGeneralSubQuery.append(t)
                                                            lista.append(str(t.valor))
                                                            nombreGen += str(ii.Columna)
                                                listaGeneral[nombreGen] = lista
                                                contadorCol += 1


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
                                                            listaGeneralSubQuery.append(t)
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
                                                        listaGeneralSubQuery.append(t)
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
                                            if (str(x.id) == ii.NombreT):
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        listaGeneralSubQuery.append(t)
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
                                                    listaGeneralSubQuery.append(t)
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
                                                            listaGeneralSubQuery.append(t)
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
                                                        listaGeneralSubQuery.append(t)
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

                                        imprir("SELECT : Tipo Distinto de Subconsulta")
                                        er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                        LisErr.agregar(er)
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
                                        imprir("SELECT : Tipo Distinto de Subconsulta")
                                        er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                        LisErr.agregar(er)

# ============================ Agregamos la produccion de Cases en los campos
                            elif (isinstance(ii, CaseCuerpo)):
                                lis = {}
                                lis = VerificaciontipoWhen(ii.Lista_When)
                                Modificaciones.update(lis)
                                print(Modificaciones)
# ============================ Termina Instruccion de Cases en los campos
                            else:
                                imprir("SELECT : Tipo Distinto de Ejecucion")
                                er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
                                LisErr.agregar(er)
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
                                                        listaGeneralSubQuery.append(t)
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
                                                    listaGeneralSubQuery.append(t)
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
                                                            listaGeneralSubQuery.append(t)
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
                                                        listaGeneralSubQuery.append(t)
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
                                                        listaGeneralSubQuery.append(t)
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
                                                    listaGeneralSubQuery.append(t)
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
                                                            listaGeneralSubQuery.append(t)
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
                                                        listaGeneralSubQuery.append(t)
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
                                        imprir("SELECT : Tipo Distinto de Subconsulta")
                                        er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                        LisErr.agregar(er)

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
                                        imprir("SELECT : Tipo Distinto de Subconsulta")
                                        er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                        LisErr.agregar(er)

 # ============================ Agregamos la produccion de Cases en los campos
                            elif (isinstance(ii, CaseCuerpo)):
                                lis = {}
                                lis = VerificaciontipoWhen(ii.Lista_When)
                                Modificaciones.update(lis)
                                print(Modificaciones)
# ============================ Termina Instruccion de Cases en los campos
                            else:
                                imprir("SELECT : Tipo Distinto de Ejecucion")
                                er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
                                LisErr.agregar(er)
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
                        imprir("SELECT : Tipo Distinto de Subconsulta")
                        er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                        LisErr.agregar(er)

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
                        imprir("SELECT : Tipo Distinto de Subconsulta")
                        er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                        LisErr.agregar(er)
            else:
                imprir("SELECT : Viene otro tipo de Funcion ")
                er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                LisErr.agregar(er)
    else:
        imprir("SELECT : No existe la base de datos acual")
        er = ErrorRep('Semantico', 'No Existe la Base de Datos Actual', 0)
        LisErr.agregar(er)
    print(listaGeneral)
#    mostrarConsulta(listaGeneral)

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
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SELECT: No existen registros.")
            elif isinstance(resultado, list):
                if len(resultado) == 0:
                    banderilla = True
            elif isinstance(resultado, bool):
                banderilla = False
            else:
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SELECT: No existen registros.2222")
                for r in resultado:
                    print(str(r.valor) + " " + str(r.tabla) + " " + str(r.fila))

            titulos = []
            for campo in listaGeneral:
                titulos.append(str(campo))

            lis = []
            if (isinstance(resultado, list)):
                for t in titulos:
                    for res in resultado:
                        for item in ts_global.Datos:
                            x: DatoInsert = ts_global.obtenerDato(item)
                            if t == x.columna and x.fila == res.fila:
                                lis.append(x)

            nuevoDicc = {}
            # ingreso lista final FALTA
            # counter = 0
            for t in titulos:
                lis2 = []
                for u in lis:
                    if u.columna == t:
                        lis2.append(u.valor)
                nuevoDicc[t] = lis2

                dicci = {}
                dicci.update(nuevoDicc)

                for nn in nuevoDicc:
                    if (len(nuevoDicc.get(nn)) > 0):
                        print("")
                    else:
                        if banderilla:
                            print("")
                        else:
                            del dicci[nn]
                listaGeneral.update(dicci)
                dicci.clear()

            print("Aqui vienee la salida <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print(nuevoDicc)
            # mostrarConsulta(nuevoDicc)


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

                diccionarioN2 = {}
                diccionarioN2.update(diccionario2)

                contadoraa = 0
                for n in diccionario2:
                    diccionarioN2[str(listak[contadoraa])] = diccionarioN2.pop(n)
                    contadoraa += 1
                print(diccionarioN2)

                diccionario2.clear()
                diccionario2.update(diccionarioN2)

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

                for n in diccionariof:
                    diccionarioN[listaColumnas[contadornn]] = diccionarioN.pop(n)
                    contadornn += 1
                # imprimimos  la lista haber si hace lo que se piensa
                listaGeneral.clear()
                listaGeneral.update(diccionarioN)

                return listaGeneral



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
                    listita.append(int(ListaN.get(n)[colN - 1]))
                listt = sorted(listita)
                print(listita)
                # Recorremos la lista ordenada
                for n2 in listt:
                    diccionario2[gets(ListaN, str(n2), colN - 1)] = ListaN.get(gets(ListaN,str(n2), colN - 1))
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
                    listita.append(int(ListaN.get(n)[colN - 1]))
                listt = sorted(listita, reverse=True)
                print(listt)

                # Recorremos la lista ordenada
                for n2 in listt:
                    diccionario2[gets(ListaN, str(n2), colN - 1)] = ListaN.get(gets(ListaN,str(n2), colN - 1))
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
                    listita.append(int(ListaN.get(n)[colN - 1]))
                listt = sorted(listita)
                print(listita)
                # Recorremos la lista ordenada
                for n2 in listt:
                    diccionario2[gets(ListaN, str(n2), colN - 1)] = ListaN.get(gets(ListaN,str(n2), colN - 1))
                print(diccionario2)

            # =============  Hacemos un contador  para gravar su numero de columnas
            listak = []
            contadorlist = 0
            for jj in diccionario2:
                listak.append(contadorlist)
                contadorlist += 1
            print(listak)
# ==============  Renombramos los datos
            diccionarioN2 = {}
            diccionarioN2.update(diccionario2)

            contadoraa = 0
            for n in diccionario2:
                diccionarioN2[str(listak[contadoraa])] = diccionarioN2.pop(n)
                contadoraa += 1
            print(diccionarioN2)

            diccionario2.clear()
            diccionario2.update(diccionarioN2)
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

            for n in diccionariof:
                diccionarioN[listaColumnas[contadornn]] = diccionarioN.pop(n)
                contadornn += 1
            # imprimimos  la lista haber si hace lo que se piensa
            listaGeneral.clear()
            listaGeneral.update(diccionarioN)

            return listaGeneral


        elif (isinstance(tiposCuerpo, AccesoLimit)):
            print("Bamos a elegir el limite ")

            lista = Limites(listaGeneral, tiposCuerpo)
            listaGeneral.update(lista)

        elif (isinstance(tiposCuerpo, AccesoSubConsultas)):
            print("Bamos a ver el cuerpo de cada subconsulta")
        #print(ListaN)

#        mostrarConsulta(listaGeneral)
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


#Con este Bamos a Procesar las Expresiones y vamos a devolver una lista de las coincidencias
def ProcesoExpresion(Expresion):
    global ts_global
    ListaGenerica =[]
    ListaGenerica_ = []

    ListaGenerica = Inter.procesar_expresion_select(Expresion, ts_global)
    ListaGenerica_ = set(ListaGenerica)

    if ListaGenerica_ is None:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SELECT: No existen registros.")
        return None
    else:
        return ListaGenerica_


def VerificaciontipoWhen(Lista_When):
    ValorSust=""
    retorno ={}

    listaResultado=[]
    listwhen=[]

    for sss in Lista_When:
        if (isinstance(sss, TiposWhen)):
            # When ListaExpresiones1 then listaExpresiones3
            if ((sss.Reservada != "")  and (sss.ListaExpresiones1 != False) and
                (sss.Reservada2 == "") and (sss.ListaExpresiones2 == False) and
                (sss.Reservada3 != "") and (sss.ListaExpresiones3 != False)):

                print("El primer tipo de when <<<<<<<<<<<<<<<<<<<<<<<")
                # Procesando la primera lista de instrucciones
                listaResultado = ProcesoExpresion(sss.ListaExpresiones1)
                # Procesando la Segunda lista de instrucciones valor a sustituir

                listwhen = []
                if listaResultado is None:
                    print("No hay coincidencias")
                else:
                    for r in listaResultado:
                        print(str(r.valor) + " " + str(r.tabla) + " " + str(r.fila))
                        listwhen.append(r.valor)


                li:ExpresionValor = sss.ListaExpresiones3
                ValorSust += str(li.val)

                retorno[li.val]=listwhen


                #return listaResultado,ValorSust

            # ========================================   AQUI BAMOS sacar el valor y setearle el nombre de la tabl a nombre.campo
            # When ListaExpresiones1 Else listaExpresiones2 then ListaExpresiones3
            elif ((sss.Reservada != "") and (sss.ListaExpresiones1 != False) and
                  (sss.Reservada2 != "") and (sss.ListaExpresiones2 != False) and
                  (sss.Reservada3 != "") and (sss.ListaExpresiones3 != False)):
                print("El Segundo tipo de when <<<<<<<<<<<<<<<<<<<<<<<<<")
                print("El primer tipo de when <<<<<<<<<<<<<<<<<<<<<<<")
                # Procesando la primera lista de instrucciones
                listaResultado = ProcesoExpresion(sss.ListaExpresiones1)
                # Procesando la Segunda lista de instrucciones valor a sustituir
                listwhen = []
                if listaResultado is None:
                    print("No hay coincidencias")
                else:
                    for r in listaResultado:
                        print(str(r.valor) + " " + str(r.tabla) + " " + str(r.fila))
                        listwhen.append(r.valor)

                li = sss.ListaExpresiones3
                ValorSust += str(li.val)

                retorno[li.val] = listwhen



            # When ListaExpresiones1
            elif ((sss.Reservada != "") and (sss.ListaExpresiones1 != False) and
                  (sss.Reservada2 == "") and (sss.ListaExpresiones2 == False) and
                  (sss.Reservada3 == "") and (sss.ListaExpresiones3 == False)):
                print("El Tercer tipo de when <<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("El primer tipo de when <<<<<<<<<<<<<<<<<<<<<<<")
                # Procesando la primera lista de instrucciones
                listaResultado = ProcesoExpresion(sss.ListaExpresiones1)
                listwhen = []
                if listaResultado is None:
                    print("No hay coincidencias")
                else:
                    for r in listaResultado:
                        print(str(r.valor) + " " + str(r.tabla) + " " + str(r.fila))
                        listwhen.append(r.valor)


                retorno[0] = listwhen


            # When ListaExpresiones1 Else listaExpresiones2
            elif ((sss.Reservada != "") and (sss.ListaExpresiones1 != False) and
                  (sss.Reservada2 != "") and (sss.ListaExpresiones2 != False) and
                  (sss.Reservada3 == "") and (sss.ListaExpresiones3 == False)):
                print("El Cuarto tipo de when <<<<<<<<<<<<<<<<<<<<<<<<<<")
                # Procesando la primera lista de instrucciones
                listaResultado = ProcesoExpresion(sss.ListaExpresiones1)
                # Procesando la Segunda lista de instrucciones valor a sustituir
                listwhen = []
                if listaResultado is None:
                    print("No hay coincidencias")
                else:
                    for r in listaResultado:
                        print(str(r.valor) + " " + str(r.tabla) + " " + str(r.fila))
                        listwhen.append(r.valor)


                li = sss.ListaExpresiones2
                ValorSust += str(li.val)
                retorno[ValorSust] = listwhen

            else:
                print("Verificar Errores Sintacticos")
                return  False,"None"
                retorno[li.val] = listwhen
        else:
            imprir("CASE: Error de tipo ")

    return  retorno


#Alineamos la cantidad de datos si una lista trae menos
def AlinearDatos(listaGeneral):
    nes ={}
    dataa=0
    p = None
    listaling=[]

#Calculamos la talla maxima de los datos
    for data in listaGeneral:
        maxi = 0
        for jo in listaGeneral.get(data):
            maxi+=1
        listaling.append(maxi)
    dataa = max(listaling)

#Rellenamos si no tiene la norma General
    for date in listaGeneral:
        for jo in listaGeneral.get(date):
            if(len(listaGeneral.get(date))<dataa):
                listaGeneral.get(date).append(p)

    print(listaGeneral)

    return listaGeneral


#Interseccion entre dos tablas
def Interseccion(listaGeneral):

    # Recorremos cada dato en los diccionarios opcion2
    listi  =[]  #datos1
    listi2 =[]  #datos2
    listR =[]
    contador=0

    # sacamos las dos listas de cada tabla a intersectar
    for ni in listaGeneral:
        if(contador==0):
            listi = listaGeneral.get(ni)[:]
        else:
            listi2 = listaGeneral.get(ni)[:]
        contador += 1

    #ELIMINAMOS LOS NULOS PARA COMBERTIR TODO A ENTERO


    print(listi)
    print(listi2)
    #comparamos y los que sean igual los metemos a una lista aparte
    for kl in listi:
        for km in listi2:
            if(str(kl)==str(km)):
                listR.append(km)

    print(listR)
    #ahora seteamos el nuevo valor a la lista general
    for ji in listaGeneral:
        listaGeneral[ji]=listR

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(listaGeneral)
    return  listaGeneral


#Excepcion de tablas
def Excepcion(listaGeneral):

    # Recorremos cada dato en los diccionarios opcion2
    listi  =[]  #datos1
    listi2 =[]  #datos2
    listR =[]

    listNone=[]
    contador=0

    # sacamos las dos listas de cada tabla a intersectar
    for ni in listaGeneral:
        if(contador==0):
            listi = listaGeneral.get(ni)[:]
        else:
            listi2 = listaGeneral.get(ni)[:]
        contador += 1

    print(listi)
    print(listi2)
    banderita=False
    #comparamos y los que sean igual los metemos a una lista aparte
    for kl in listi:
        banderita = False
        for km in listi2:
            if(str(kl)==str(km)):
                banderita=True
        if(banderita==False):
            listR.append(kl)

    #llenamos lista none
    for ii in listR:
        listNone.append(None)


    print(listR)
    #ahora seteamos el nuevo valor a la lista general
    conta2=0
    for ji in listaGeneral:
        if(conta2==0):
            listaGeneral[ji]=listR
        else:
            listaGeneral[ji] =listNone
        conta2+=1
    print(listaGeneral)


    return  listaGeneral



def ProcesoSub(Cuerpo,ts):

    global listaGeneralSubQuery

    ii=Cuerpo
    if (isinstance(ii, AccesoSubConsultas)):

        listaQ = {}
        if (ii.Lista_Alias != False):
            print("Bamos a ver el cuerpo de cada subconsulta")
            li2 = ii.Lista_Alias[0]
            # Cuerpo de Tipo Subconsulta
            sub = ii.Query
            if (isinstance(sub, SubSelect)):
                listaQ= sub.Ejecutar()
            elif (isinstance(sub, SubSelect2)):
                listaQ=sub.Ejecutar()
            elif (isinstance(sub, SubSelect3)):
                listaQ=sub.Ejecutar()
            elif (isinstance(sub, SubSelect4)):
                listaQ=sub.Ejecutar()
            else:
                imprir("SELECT : Tipo Distinto de Subconsulta")
                er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                LisErr.agregar(er)
        else:
            print("Bamos a ver el cuerpo de cada subconsulta")
            # Cuerpo de Tipo Subconsulta
            sub = ii.Query
            if (isinstance(sub, SubSelect)):
                listaQ=sub.Ejecutar()


            elif (isinstance(sub, SubSelect2)):
                listaQ=sub.Ejecutar()
            elif (isinstance(sub, SubSelect3)):
                listaQ=sub.Ejecutar()
            elif (isinstance(sub, SubSelect4)):
                listaQ=sub.Ejecutar()
            else:
                imprir("SELECT : Tipo Distinto de Subconsulta")
                er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                LisErr.agregar(er)
    else:
        imprir("SELECT : Tipo Distinto de Ejecucion")
        er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
        LisErr.agregar(er)


    for n in listaQ:
        n2= listaQ.get(n)



    return  listaGeneralSubQuery




#Proceso Limit
def Limites(listaGeneral,tiposCuerpo):

    if (str(tiposCuerpo.Reservada).lower() == "offset"):
        # codigo de offset
        # Recorremos la lista General
        print("Estoy entrando al Offset")
        for nn in listaGeneral:
            l = listaGeneral.get(nn)
            # Recorro la lista dentro del diccionario
            indice = 0
            listan = l[:]

            for dato in l:
                if (indice > int(tiposCuerpo.Expresion_Numerica)-1):
                    print(">>>" + str(dato)+"<<<<<<<< Dato Pasado ")
                    indice+=1
                    print(str(indice)+"<< Este indice va")
                else:
                    print("><><><><> DAto Eliminado >>>> "+str(dato))
                    listan.remove(dato)
                    indice += 1

            listaGeneral[nn]=listan

        return listaGeneral



    elif (str(tiposCuerpo.Reservada).lower() == "limit"):
        # Codigo de limit
        if (str(tiposCuerpo.Expresion_Numerica).lower() == "all"):
            print("Voy a retornar todo sin limite")
            return listaGeneral
        else:
            # Recorremos la lista General
            print("ESTA es la lista wey >>???>??>   ")
            print(listaGeneral)

            for nn in listaGeneral:
                l = listaGeneral.get(nn)

                # Recorro la lista dentro del diccionario
                indice = 0
                listan = l[:]

                for dato in l:
                    if (indice > int(tiposCuerpo.Expresion_Numerica)-1):
                        print(">>>" + str(dato)+"<<<<<<<< Dato eliminado ")
                        listan.remove(dato)
                        indice+=1
                        print(str(indice)+"<< Este indice va")
                    else:
                        print("><><><><> DAto paso >>>> "+str(dato))
                        indice += 1

                listaGeneral[nn]=listan

            return listaGeneral




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

    cadena5 = ''
    for fn in ts.Validaciones:
        fun = ts.Validaciones.get(fn)
        if isinstance(fun, constraintTabla):
            print("ESTE SI LO IMPRIMEEEeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            cadena5 += '<TR><TD>' + str(fun.idRef) + '</TD>' + '<TD>' + str(fun.listas_id) + '</TD>' + '<TD>' + str(fun.valor) + '</TD>' + '<TD>' + str(fun.id) + '</TD>' + '<TD>' + '</TD></TR>'
        else:
            cadena5 += '<TR><TD>' + str(fun.tabla) + '</TD>' + '<TD>' + str(fun.campo) + '</TD>' + '<TD>' + str(fun.validacion) + '</TD>' + '<TD>' + str(fun.id) + '</TD>' + '<TD>' + '</TD></TR>'


    cadena = ''
    for fn in ts.Datos:
        fun = ts.obtenerDato(fn)
        cadena += '<TR><TD>' + str(fun.bd) + '</TD>' + '<TD>' + str(fun.tabla) + '</TD>' + '<TD>' + str(
            fun.columna) + '</TD>' + '<TD>' + str(fun.valor) + '</TD>' + '<TD>' + str(fun.fila) + '</TD></TR>'

    #DICIONARIO Tablas
    cadena2=''
    for fn in ts.Tablas:
        fun=ts.obtenerTabla(fn)

        if fun.inhe == None:
            print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT INHE VACIO")
            cadena2 += '<TR><TD COLSPAN="5" bgcolor="#A9F5E1"> </TD></TR>'
        else:
            print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT INHE SI TIENE")
            cadena2 += '<TR><TD COLSPAN="5" bgcolor="#A9F5E1"> HERENCIA: '+ fun.inhe.id +'</TD></TR>'

        for cuerpos in fun.cuerpo:
            if isinstance(cuerpos, CampoTabla):
                if isinstance(cuerpos.tipo, valorTipo):
                    cadena2+='<TR><TD>'+str(fun.id)+'</TD>'+'<TD>'+str(cuerpos.id)+'</TD>'+'<TD>'+str(cuerpos.tipo.valor)+'('+str(cuerpos.tipo.expresion.val)+')'+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD></TR>'
                else:
                    cadena2+='<TR><TD>'+str(fun.id)+'</TD>'+'<TD>'+str(cuerpos.id)+'</TD>'+'<TD>'+str(cuerpos.tipo)+'</TD>'+'<TD>'+'</TD>'+'<TD>'+'</TD></TR>'
            else:
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> UN C")
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
                                <TD COLSPAN="5" bgcolor="#FA8258"> <B>VALIDACIONES</B> </TD>
                            </TR>
                            <TR bgcolor="#BEF781">
                                <TD bgcolor="#BEF781">TABLA</TD>
                                <TD bgcolor="#BEF781">CAMPO</TD>
                                <TD bgcolor="#BEF781">TIPO</TD>
                                <TD bgcolor="#BEF781">ID</TD>
                                <TD bgcolor="#BEF781"> </TD>
                            </TR>
                            '''
                            +cadena5+
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
                res = Master.dropTable(baseActual, self.id[0].val)
                if res ==0:
                    #se Elimino exitosamente
                    ts_global.EliminarTabla(self.id[0].val)

                    #por cada dato que tenga el valor tabla eliminarlo.
                    listaE = []
                    for dato in ts_global.Datos:
                        actual:DatoInsert = ts_global.obtenerDato(dato)
                        if actual.tabla == self.id[0].val:
                            listaE.append(dato)

                    for d in listaE:
                        ts_global.EliminarDato(d)

                    listaV = []
                    for vali in ts_global.Validaciones:
                        actual = ts_global.Validaciones.get(vali)
                        if isinstance(actual ,constraintTabla):
                            if actual.idRef == self.id[0].val:
                                listaV.append(vali)
                        else:
                            if actual.tabla == self.id[0].val:
                                listaV.append(vali)

                    for d in listaE:
                        ts_global.EliminarDato(d)

                    for v in listaV:
                        del ts_global.Validaciones[v]


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

        global ts_global, baseActual, ListaTablasG
        global LisErr
        listaConsultados = []
        contadorCol = 0

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        casee =False

        if r is not None:


           for ee in self.Nombres_Tablas:


               if(isinstance(ee,AccesoTablaSinLista)): #viene sin alias


                   #Recorremos el diccionario general para ver si existe la tabla que queremos
                   # recorremos lista General de Tablas
                   for elemento2 in ts_global.Tablas:

                       x: CreateTable = ts_global.obtenerTabla(elemento2)


                       if (str(x.id) == str(ee.NombreT)):
                           ListaTablasG.append(x.id)
                           #si es la tabla validamos que tipo de campo viene


                           numeroExpresion = 1
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

                                                        if (str(t.columna) == str(ii.Columna) and str(t.tabla)==str(ii.NombreT)):

                                                            print(str(t.columna) +"Estos vienen"+str(t.tabla))
                                                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

                                                            nombreGen = ""
                                                            if(ExisteInList(listaConsultados,t.columna)==False):  #Existe

                                                                print("Campo ya existe se creara un nuevo nombre")
                                                                nombreGen += str(t.columna) + str(contadorCol)
                                                                print(str(t.valor))
                                                                listaGeneralSubQuery.append(t)
                                                                lista.append(str(t.valor))

                                                            else:
                                                                listaConsultados.append(t.columna)
                                                                print(str(t.valor))
                                                                listaGeneralSubQuery.append(t)
                                                                lista.append(str(t.valor))
                                                                nombreGen+=str(ii.Columna)
                                                    listaGeneral[nombreGen] = lista
                                                    contadorCol += 1


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
                                            if not isinstance(ii.Columna, string_types):
                                                print("Se intentara procesar una expresion")

                                                result = Inter.procesar_expresion_columna(ii.Columna, ts_global)
                                                if isinstance(result, list):
                                                    listaGeneral["Expresion" + str(numeroExpresion)] = result
                                                    print('resultado expresion')
                                                else:
                                                    listaGeneral["Expresion"+str(numeroExpresion)] = [result]
                                                numeroExpresion += 1
                                                break


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
                                            if not isinstance(ii.Columna, string_types):
                                                print("Se intentara procesar una expresion")
                                                nuevoNave = ii.Lista_Alias.Alias

                                                result = Inter.procesar_expresion_columna(ii.Columna, ts_global)
                                                if isinstance(result, list):
                                                    listaGeneral[nuevoNave] = result
                                                    print('resultado expresion')
                                                else:
                                                    listaGeneral[nuevoNave] = [result]

                                                break
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
                                            imprir("SELECT : Tipo Distinto de Subconsulta")
                                            er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                            LisErr.agregar(er)
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
                                            imprir("SELECT : Tipo Distinto de Subconsulta")
                                            er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                            LisErr.agregar(er)

# ============================ Agregamos la produccion de Cases en los campos
                                elif (isinstance(ii, CaseCuerpo)):
                                    lis={}
                                    lis  = VerificaciontipoWhen(ii.Lista_When)
                                    Modificaciones.update(lis)
                                    print(Modificaciones)
                                    casee = True
# ============================ Termina Instruccion de Cases en los campos
                                else:
                                    imprir("SELECT : Viene otro tipo de Ejecucion ")
                                    er = ErrorRep('Semantico','No es un tipo Correcto de ejecucion', 0)
                                    LisErr.agregar(er)
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
                                           imprir("SELECT : Tipo Distinto de Subconsulta")
                                           er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                           LisErr.agregar(er)

# ============================ Agregamos la produccion de Cases en los campos
                               elif (isinstance(ii, CaseCuerpo)):
                                   lis = {}
                                   lis = VerificaciontipoWhen(ii.Lista_When)
                                   Modificaciones.update(lis)
                                   print(Modificaciones)
                                   casee = True
# ============================ Termina Instruccion de Cases en los campos
                               else:
                                   print("")
                                   #imprir("SELECT : Tipo Distinto de Ejecucion")
                                   #er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
                                   #LisErr.agregar(er)
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
                           imprir("SELECT : Tipo Distinto de Subconsulta")
                           er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                           LisErr.agregar(er)
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
                           imprir("SELECT : Tipo Distinto de Subconsulta")
                           er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                           LisErr.agregar(er)
               else:
                   imprir("SELECT : Tipo Distinto de Ejecucion")
                   er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
                   LisErr.agregar(er)
        else:
            imprir("SELECT : No existe la base de datos acual")
            er = ErrorRep('Semantico', 'No Existe la Base de Datos Actual', 0)
            LisErr.agregar(er)


# ========================================================================== Proceso para Sustituir datos en las lista
        if(casee == True):
            #recorremos Lista General
            diccAux = {}
            contador = 0

            for uni in listaGeneral:
                print("Entre 1")
                for ele2 in listaGeneral.get(uni): #lista de data de el diccionario
                    contador+=1
                    print("Entre 2")

                    for ene in Modificaciones:   #Recorremos el diccionario con los datos que llevaran cambio
                        print("Entre 3")
                        for ele3 in Modificaciones.get(ene):
                            print("Entre 4")
                            print("este>" + str(ele2) + "ESTOS TENGO ACTUALMENTE" + str(ele3))
                            print("y le bamos a poner este>>>>" + str(ene))

                            if(ele2==ele3):
                                print("este >>>>>"+str(ele2)+"Se va a reemplazar por este >>>>>"+str(ene))
                                listaGeneral.get(uni)[contador-1] = ene

            diccAux.update(listaGeneral)
            listaGeneral.clear()
            listaGeneral.update(diccAux)
        else:
            print("Nada")









#============================================================================ PROCESO UNION
        #Nos va a decir si se realizo alguna union para evitar graficar 2 veces

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
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif(str(uni.Comportamiento).upper()=="INTERSECT"):
                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)



                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                           #mostrarConsulta(list2)


                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)


                    elif(str(uni.Comportamiento).upper()=="EXCEPT"):

                        print("Viene un Except")
                        ank = uni.Consulta
                        if(isinstance(ank,Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        elif(isinstance(ank,Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        elif(isinstance(ank,Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        elif(isinstance(ank,Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    else:
                        imprir("SELECT : Viene otro tipo de Funcion ")
                        er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                        LisErr.agregar(er)


                elif(str(uni.Reservada)==";"):
                    print("Fin ")

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
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif(str(uni.Comportamiento).upper()=="INTERSECT"):

                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if(isinstance(ank,Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)


                        elif(isinstance(ank,Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)


                        elif(isinstance(ank,Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        elif(isinstance(ank,Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif(str(uni.Comportamiento).upper()=="EXCEPT"):

                        print("Viene un Except")
                        ank = uni.Consulta
                        if(isinstance(ank,Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        elif(isinstance(ank,Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)

                        elif(isinstance(ank,Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)


                        elif(isinstance(ank,Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 =Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            #mostrarConsulta(list2)
                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    else:
                        imprir("SELECT : Palabra Reservada No encontrada")
                        er = ErrorRep('Semantico', 'No Se Encontro la Palabra reservada', 0)
                        LisErr.agregar(er)


        print(listaGeneral)
        print("<<<<<<<<<<<<<<<<<<<<<<<<  estaaaa")
        liste = AlinearDatos(listaGeneral)
        mostrarConsulta(liste)


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
        listaConsultados = []
        contadorCol = 0

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        casee = False

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

                                if (isinstance(ii, Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
                                    # *  , nombrecampo,  nombrecampo alias
                                    # listaGeneral
                                    for ele in x.cuerpo:  # recorremos lista de columnas
                                        y: CampoTabla = ele

                                        if (str(y.id) == str(ii.Columna)):

                                            print("LA columan " + str(ii.Columna) + "Esta en la tabla y bamos a retornar sus valores")
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

                                                        if (str(t.columna) == str(ii.Columna) and str(t.tabla)==str(ii.NombreT)):

                                                            print(str(t.columna) +"Estos vienen"+str(t.tabla))
                                                            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

                                                            nombreGen = ""
                                                            if(ExisteInList(listaConsultados,t.columna)==False):  #Existe

                                                                print("Campo ya existe se creara un nuevo nombre")
                                                                nombreGen += str(t.columna) + str(contadorCol)
                                                                print(str(t.valor))
                                                                listaGeneralSubQuery.append(t)
                                                                lista.append(str(t.valor))

                                                            else:
                                                                listaConsultados.append(t.columna)
                                                                print(str(t.valor))
                                                                listaGeneralSubQuery.append(t)
                                                                lista.append(str(t.valor))
                                                                nombreGen+=str(ii.Columna)
                                                    listaGeneral[nombreGen] = lista
                                                    contadorCol += 1


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
                                            imprir("SELECT : Tipo Distinto de Subconsulta")
                                            er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                            LisErr.agregar(er)
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
                                            imprir("SELECT : Tipo Distinto de Subconsulta")
                                            er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                            LisErr.agregar(er)

# ============================ Agregamos la produccion de Cases en los campos
                                elif (isinstance(ii, CaseCuerpo)):
                                    lis = {}
                                    lis = VerificaciontipoWhen(ii.Lista_When)
                                    Modificaciones.update(lis)
                                    print(Modificaciones)
                                    casee = True
# ============================ Finaliza Agregacion de  la produccion de Cases en los campos
                                else:
                                    imprir("SELECT : Tipo Distinto de Ejecucion")
                                    er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
                                    LisErr.agregar(er)
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

                                if (isinstance(ii, Campo_AccedidoSinLista)):  # nombrecampo   #nombretabla.nombrecampo     # select * from tabla1;    sin alias
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
                                            imprir("SELECT : Tipo Distinto de Subconsulta")
                                            er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                            LisErr.agregar(er)

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
                                            imprir("SELECT : Tipo Distinto de Subconsulta")
                                            er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                                            LisErr.agregar(er)
# ============================ Agregamos la produccion de Cases en los campos
                                elif (isinstance(ii, CaseCuerpo)):
                                    lis = {}
                                    lis = VerificaciontipoWhen(ii.Lista_When)
                                    Modificaciones.update(lis)
                                    print(Modificaciones)
                                    casee = True
# ============================ Finaliza la produccion de Cases en los campos
                                else:
                                    imprir("SELECT : Tipo Distinto de Ejecucion")
                                    er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
                                    LisErr.agregar(er)
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
                            imprir("SELECT : Tipo Distinto de Subconsulta")
                            er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                            LisErr.agregar(er)

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
                            imprir("SELECT : Tipo Distinto de Subconsulta")
                            er = ErrorRep('Semantico', 'No es un tipo Correcto de Subconsulta', 0)
                            LisErr.agregar(er)

                else:
                    imprir("SELECT : Tipo Distinto de Ejecucion")
                    er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
                    LisErr.agregar(er)
        else:
            imprir("SELECT : No existe la base de datos acual")
            er = ErrorRep('Semantico', 'No Existe la Base de Datos Actual', 0)
            LisErr.agregar(er)



# ========================================================================== Proceso para Sustituir datos en las lista
        if (casee == True):
            # recorremos Lista General
            diccAux = {}
            contador = 0

            for uni in listaGeneral:
                print("Entre 1")
                for ele2 in listaGeneral.get(uni):  # lista de data de el diccionario
                    contador += 1
                    print("Entre 2")

                    for ene in Modificaciones:  # Recorremos el diccionario con los datos que llevaran cambio
                        print("Entre 3")
                        for ele3 in Modificaciones.get(ene):
                            print("Entre 4")
                            print("este>" + str(ele2) + "ESTOS TENGO ACTUALMENTE" + str(ele3))
                            print("y le bamos a poner este>>>>" + str(ene))

                            if (ele2 == ele3):
                                print("este >>>>>" + str(ele2) + "Se va a reemplazar por este >>>>>" + str(ene))
                                listaGeneral.get(uni)[contador - 1] = ene

            diccAux.update(listaGeneral)
            listaGeneral.clear()
            listaGeneral.update(diccAux)
        else:
            print("Nada")

#====================================================================   Proceso del cuerpo para editar valores en la tabla
       #procesando el cuerpo General de las tablas al insertar correctamente
        banderilla = False
        for tiposCuerpo in self.Cuerpo:
            if (isinstance(tiposCuerpo, Cuerpo_TipoWhere)):

                print("Vamos a ver condiciones y luego a mostrar datos de las condiciones")
                resultado = Inter.procesar_expresion_select(tiposCuerpo.Cuerpo, ts_global)

                if resultado is None:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SELECT: No existen registros.")
                elif isinstance(resultado, list):
                    if len(resultado) == 0:
                        banderilla = True
                elif isinstance(resultado,bool):
                        banderilla = False
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SELECT: No existen registros.2222")
                    for r in resultado:
                        print(str(r.valor)+" "+str(r.tabla)+" "+str(r.fila))


                titulos = []
                for campo in listaGeneral:
                    titulos.append(str(campo))

                lis = []
                if(isinstance(resultado,list)):
                    for t in titulos:
                        for res in resultado:
                            for item in ts_global.Datos:
                                x: DatoInsert = ts_global.obtenerDato(item)
                                if t == x.columna and x.fila == res.fila:
                                    lis.append(x)



                nuevoDicc = {}
                # ingreso lista final FALTA
                #counter = 0
                for t in titulos:
                    lis2 = []
                    for u in lis:
                        if u.columna == t:
                            lis2.append(u.valor)
                    nuevoDicc[t] = lis2

                    dicci={}
                    dicci.update(nuevoDicc)

                    for nn in nuevoDicc:
                        if(len(nuevoDicc.get(nn))>0):
                            print("")
                        else:
                            if banderilla:
                                print("")
                            else:
                                del dicci[nn]
                    listaGeneral.update(dicci)
                    dicci.clear()


                print("Aqui vienee la salida <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print(nuevoDicc)
                #mostrarConsulta(nuevoDicc)

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
                        for n2 in sorted(listita):
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
                        for n2 in sorted(listita, reverse=True):
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


                    diccionarioN2 = {}
                    diccionarioN2.update(diccionario2)


                    contadoraa = 0
                    for n in diccionario2:
                        diccionarioN2[str(listak[contadoraa])] = diccionarioN2.pop(n)
                        contadoraa += 1
                    print(diccionarioN2)

                    diccionario2.clear()
                    diccionario2.update(diccionarioN2)



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

                    for n in diccionariof:
                        diccionarioN[listaColumnas[contadornn]] = diccionarioN.pop(n)
                        contadornn += 1
                    # imprimimos  la lista haber si hace lo que se piensa
                    #listaGeneral.clear()
                    #listaGeneral.update(diccionarioN)
                    imprir("SELECT: Operacion Group by ")
                    mostrarConsulta(diccionarioN)
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


                    print("ESTOY  En ASC <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
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
                        listita.append(int(ListaN.get(n)[colN-1]))
                    listt = sorted(listita)
                    print(listita)
                    #Recorremos la lista ordenada

                    for n2 in sorted(listita):
                        diccionario2[gets(ListaN,str(n2),colN-1)] = ListaN.get(gets(ListaN,str(n2),colN-1))
                    print(diccionario2)
                # Si viene la palabra reservada Descendente
                elif(str(tipo.Estado).upper()=='DESC'):
                    #Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                    #tenemos el contador de columnas

                    print("ESTOY  En DESC <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
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
                        listita.append(int(ListaN.get(n)[colN-1]))
                    listt = sorted(listita, reverse=True)
                    print(listt)

                    #Recorremos la lista ordenada
                    for n2 in sorted(listita, reverse=True):
                        diccionario2[gets(ListaN,str(n2),colN-1)] = ListaN.get(gets(ListaN,str(n2),colN-1))
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
                    print("Aqui Vienen listas A Ordenat <<<<<<")
                    print(str(colN))
                    print(ListaN)

                    for n in ListaN:
                        listita.append(int(ListaN.get(n)[colN-1]))
                    listt = sorted(listita)
                    print(listita)

                    print("ESTA  ES LA LISTA ORDENADA ----->    ")
                    print(listt)
                    #Recorremos la lista ordenada
                    for n2 in listt:
                        diccionario2[gets(ListaN,str(n2),colN-1)] = ListaN.get(gets(ListaN,str(n2),colN-1))
                    print(diccionario2)



#=============  Hacemos un contador  para gravar su numero de columnas
                listak =[]
                contadorlist = 0
                for jj in diccionario2:
                    listak.append(contadorlist)
                    contadorlist+=1
                print(listak)
#==============  Renombramos los datos

                diccionarioN2 = {}
                diccionarioN2.update(diccionario2)

                contadoraa = 0
                for n in diccionario2:
                    diccionarioN2[str(listak[contadoraa])] = diccionarioN2.pop(n)
                    contadoraa += 1
                print(diccionarioN2)

                diccionario2.clear()
                diccionario2.update(diccionarioN2)

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

                for n in diccionariof:
                    diccionarioN[listaColumnas[contadornn]] = diccionarioN.pop(n)
                    contadornn += 1
                #imprimimos  la lista haber si hace lo que se piensa
                #listaGeneral.clear()
                #listaGeneral.update(diccionarioN)
                imprir("ESTO SALE AL HACER EL ORDER BY ")
                mostrarConsulta(diccionarioN)
                #diccionariof.clear

            elif (isinstance(tiposCuerpo, AccesoLimit)):
                print("Bamos a elegir el limite ")

                lista = Limites(listaGeneral,tiposCuerpo);
                mostrarConsulta(lista)

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
            else:
                imprir("SELECT : Tipo Distinto de Ejecucion")
                er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
                LisErr.agregar(er)



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
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif (str(uni.Comportamiento).upper() == "INTERSECT"):
                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)



                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                        # mostrarConsulta(list2)

                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)


                    elif (str(uni.Comportamiento).upper() == "EXCEPT"):

                        print("Viene un Except")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    else:
                        imprir("SELECT : Viene otro tipo de Funcion ")
                        er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                        LisErr.agregar(er)


                elif (str(uni.Reservada) == ";"):
                    print("Fin ")

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
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif (str(uni.Comportamiento).upper() == "INTERSECT"):

                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)


                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)


                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif (str(uni.Comportamiento).upper() == "EXCEPT"):

                        print("Viene un Except")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)


                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)
                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    else:
                        imprir("SELECT : Palabra Reservada No encontrada")
                        er = ErrorRep('Semantico', 'No Se Encontro la Palabra reservada', 0)
                        LisErr.agregar(er)

        listaling = AlinearDatos(listaGeneral)
        print("<<<<<<<<<<<<<<<<<<<<<<<<   ES LA SALIDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  ")
        print(listaling)

        mostrarConsulta(listaling)


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
                                                            # =============================================================  data oscar
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
                                                # =============================================================  data oscar
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
                                                        # =============================================================  data oscar
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
                                                # =============================================================  data oscar
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

                                                                # =============================================================  data oscar
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
                                                        # =============================================================  data oscar
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

                                                            # =============================================================  data oscar
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
                                                    # =============================================================  data oscar
                                                    listaGeneral[pp.id] = Lista2
                                        else:
                                            print(" ERROR NO EXISTE LA TABLA")

                                elif (isinstance(ii,
                                                 Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

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

                                                            # =============================================================  data oscar
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
                                                    # =============================================================  data oscar
                                                    listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        # =============================================================  data oscar
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
                                                # =============================================================  data oscar
                                                listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = lista


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
                                                                # =============================================================  data oscar
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
                                                        # =============================================================  data oscar
                                                        listaGeneral[
                                                            str(nuevoNave) + "." + str(ii.Columna)] = Lista2

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
                                                            # =============================================================  data oscar
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
                                                    # =============================================================  data oscar
                                                    listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = Lista2
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

                                                    listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = lista

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

                                                listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = lista

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

                                                        listaGeneral[
                                                            str(nuevoNave) + "." + str(ii.Columna)] = Lista2

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

                                                    listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = Lista2
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

        # ============================================================================  Aqui vienen acciones del distinct =================================================

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
            print("Insertar en: " + str(aliasT))
            lis = []
            for u in resdistinct:
                print(str(u.columna) + str(nombre))
                if str(u.columna) == str(nombre):
                    print("Si guarda")
                    lis.append(u.valor)
                    print(lis)

            nuevoDic[aliasT] = lis

        print(nuevoDic)
        # mostrarConsulta(nuevoDic)
        imprir("DISTINCT: DISTINCT REALIZADO CON EXISTO")
        listaAlinear = AlinearDatos(nuevoDic)
        mostrarConsulta(listaAlinear)
        listaGeneral.clear()

        listaGeneral.update(listaAlinear)



        # aqui le agrega a general las listas que se generan
        # =================================================================================== PROCESO UNION
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
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif (str(uni.Comportamiento).upper() == "INTERSECT"):
                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)



                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                        # mostrarConsulta(list2)

                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)


                    elif (str(uni.Comportamiento).upper() == "EXCEPT"):

                        print("Viene un Except")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    else:
                        imprir("SELECT : Viene otro tipo de Funcion ")
                        er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                        LisErr.agregar(er)


                elif (str(uni.Reservada) == ";"):
                    print("Fin ")

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
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif (str(uni.Comportamiento).upper() == "INTERSECT"):

                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            print(list2)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)


                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)


                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif (str(uni.Comportamiento).upper() == "EXCEPT"):

                        print("Viene un Except")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)


                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)
                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    else:
                        imprir("SELECT : Palabra Reservada No encontrada")
                        er = ErrorRep('Semantico', 'No Se Encontro la Palabra reservada', 0)
                        LisErr.agregar(er)

        listaling = AlinearDatos(listaGeneral)
        print("<<<<<<<<<<<<<<<<<<<<<<<<   ES LA SALIDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  ")
        print(listaling)

        mostrarConsulta(listaling)
    # ================================================= AQUI VIENE UNION ==============================================

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


class Select4(Instruccion) :
    def __init__(self,distinct,  unionn,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.distinct = distinct
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.unionn         = unionn
        self.Cuerpo = Cuerpo

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
                                                            # =============================================================  data oscar
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
                                                # =============================================================  data oscar
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
                                                        # =============================================================  data oscar
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
                                                # =============================================================  data oscar
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

                                                                # =============================================================  data oscar
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
                                                        # =============================================================  data oscar
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

                                                            # =============================================================  data oscar
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
                                                    # =============================================================  data oscar
                                                    listaGeneral[pp.id] = Lista2
                                        else:
                                            print(" ERROR NO EXISTE LA TABLA")

                                elif (isinstance(ii,
                                                 Campo_Accedido)):  # nombre alias ssj      #nombretabla.nombrecampo alias  tss

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

                                                            # =============================================================  data oscar
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
                                                    # =============================================================  data oscar
                                                    listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = lista
                                                else:
                                                    print("")
                                            else:
                                                i = ts_global.Datos
                                                lista = []
                                                for gg in ts_global.Datos:
                                                    t: DatoInsert = ts_global.obtenerDato(gg)

                                                    if (str(t.columna) == str(ii.Columna)):
                                                        print(str(t.valor))
                                                        # =============================================================  data oscar
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
                                                # =============================================================  data oscar
                                                listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = lista


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
                                                                # =============================================================  data oscar
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
                                                        # =============================================================  data oscar
                                                        listaGeneral[
                                                            str(nuevoNave) + "." + str(ii.Columna)] = Lista2

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
                                                            # =============================================================  data oscar
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
                                                    # =============================================================  data oscar
                                                    listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = Lista2
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

                                                    listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = lista

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

                                                listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = lista

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

                                                        listaGeneral[
                                                            str(nuevoNave) + "." + str(ii.Columna)] = Lista2

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

                                                    listaGeneral[str(nuevoNave) + "." + str(ii.Columna)] = Lista2
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

        # ============================================================================  Aqui vienen acciones del distinct =================================================

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
            print("Insertar en: " + str(aliasT))
            lis = []
            for u in resdistinct:
                print(str(u.columna) + str(nombre))
                if str(u.columna) == str(nombre):
                    print("Si guarda")
                    lis.append(u.valor)
                    print(lis)

            nuevoDic[aliasT] = lis

        print(nuevoDic)
        # mostrarConsulta(nuevoDic)
        imprir("DISTINCT: DISTINCT REALIZADO CON EXISTO")
        listaGeneral.clear()

        listaGeneral.update(nuevoDic)

# ========================================================================== Proceso para El distinct

#====================================================================   Proceso del cuerpo para editar valores en la tabla
       #procesando el cuerpo General de las tablas al insertar correctamente
        for tiposCuerpo in self.Cuerpo:
            if (isinstance(tiposCuerpo, Cuerpo_TipoWhere)):

                print("Vamos a ver condiciones y luego a mostrar datos de las condiciones")
                resultado = Inter.procesar_expresion_select(tiposCuerpo.Cuerpo, ts_global)

                if resultado is None:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SELECT: No existen registros.")
                elif isinstance(resultado, list):
                    if len(resultado) == 0:
                        banderilla = True
                elif isinstance(resultado,bool):
                        banderilla = False
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++SELECT: No existen registros.2222")
                    for r in resultado:
                        print(str(r.valor)+" "+str(r.tabla)+" "+str(r.fila))


                titulos = []
                for campo in listaGeneral:
                    titulos.append(str(campo))

                lis = []
                if(isinstance(resultado,list)):
                    for t in titulos:
                        for res in resultado:
                            for item in ts_global.Datos:
                                x: DatoInsert = ts_global.obtenerDato(item)
                                if t == x.columna and x.fila == res.fila:
                                    lis.append(x)



                nuevoDicc = {}
                # ingreso lista final FALTA
                #counter = 0
                for t in titulos:
                    lis2 = []
                    for u in lis:
                        if u.columna == t:
                            lis2.append(u.valor)
                    nuevoDicc[t] = lis2

                    dicci={}
                    dicci.update(nuevoDicc)

                    for nn in nuevoDicc:
                        if(len(nuevoDicc.get(nn))>0):
                            print("")
                        else:
                            if banderilla:
                                print("")
                            else:
                                del dicci[nn]
                    listaGeneral.update(dicci)
                    dicci.clear()


                print("Aqui vienee la salida <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print(nuevoDicc)
                #mostrarConsulta(nuevoDicc)


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
                        for n2 in sorted(listita):
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
                        for n2 in sorted(listita, reverse=True):
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


                    diccionarioN2 = {}
                    diccionarioN2.update(diccionario2)


                    contadoraa = 0
                    for n in diccionario2:
                        diccionarioN2[str(listak[contadoraa])] = diccionarioN2.pop(n)
                        contadoraa += 1
                    print(diccionarioN2)

                    diccionario2.clear()
                    diccionario2.update(diccionarioN2)



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

                    for n in diccionariof:
                        diccionarioN[listaColumnas[contadornn]] = diccionarioN.pop(n)
                        contadornn += 1
                    # imprimimos  la lista haber si hace lo que se piensa
                    #listaGeneral.clear()
                    #listaGeneral.update(diccionarioN)
                    imprir("SELECT: Operacion Group by ")
                    mostrarConsulta(diccionarioN)
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


                    print("ESTOY  En ASC <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
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
                        listita.append(int(ListaN.get(n)[colN-1]))
                    listt = sorted(listita)
                    print(listita)
                    #Recorremos la lista ordenada

                    for n2 in sorted(listita):
                        diccionario2[gets(ListaN,str(n2),colN-1)] = ListaN.get(gets(ListaN,str(n2),colN-1))
                    print(diccionario2)
                # Si viene la palabra reservada Descendente
                elif(str(tipo.Estado).upper()=='DESC'):
                    #Recorremos la fila de las columnas para ver que numero tenemos la solicitada
                    #tenemos el contador de columnas

                    print("ESTOY  En DESC <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
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
                        listita.append(int(ListaN.get(n)[colN-1]))
                    listt = sorted(listita, reverse=True)
                    print(listt)

                    #Recorremos la lista ordenada
                    for n2 in sorted(listita, reverse=True):
                        diccionario2[gets(ListaN,str(n2),colN-1)] = ListaN.get(gets(ListaN,str(n2),colN-1))
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
                    print("Aqui Vienen listas A Ordenat <<<<<<")
                    print(str(colN))
                    print(ListaN)

                    for n in ListaN:
                        listita.append(int(ListaN.get(n)[colN-1]))
                    listt = sorted(listita)
                    print(listita)

                    print("ESTA  ES LA LISTA ORDENADA ----->    ")
                    print(listt)
                    #Recorremos la lista ordenada
                    for n2 in listt:
                        diccionario2[gets(ListaN,str(n2),colN-1)] = ListaN.get(gets(ListaN,str(n2),colN-1))
                    print(diccionario2)



#=============  Hacemos un contador  para gravar su numero de columnas
                listak =[]
                contadorlist = 0
                for jj in diccionario2:
                    listak.append(contadorlist)
                    contadorlist+=1
                print(listak)
#==============  Renombramos los datos

                diccionarioN2 = {}
                diccionarioN2.update(diccionario2)

                contadoraa = 0
                for n in diccionario2:
                    diccionarioN2[str(listak[contadoraa])] = diccionarioN2.pop(n)
                    contadoraa += 1
                print(diccionarioN2)

                diccionario2.clear()
                diccionario2.update(diccionarioN2)

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

                for n in diccionariof:
                    diccionarioN[listaColumnas[contadornn]] = diccionarioN.pop(n)
                    contadornn += 1
                #imprimimos  la lista haber si hace lo que se piensa
                #listaGeneral.clear()
                #listaGeneral.update(diccionarioN)
                imprir("ESTO SALE AL HACER EL ORDER BY ")
                mostrarConsulta(diccionarioN)
                #diccionariof.clear

            elif (isinstance(tiposCuerpo, AccesoLimit)):
                print("Bamos a elegir el limite ")

                lista = Limites(listaGeneral,tiposCuerpo);
                mostrarConsulta(lista)

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
            else:
                imprir("SELECT : Tipo Distinto de Ejecucion")
                er = ErrorRep('Semantico', 'No es un tipo Correcto de Ejecucion', 0)
                LisErr.agregar(er)

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
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif (str(uni.Comportamiento).upper() == "INTERSECT"):
                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)



                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                        # mostrarConsulta(list2)

                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)


                    elif (str(uni.Comportamiento).upper() == "EXCEPT"):

                        print("Viene un Except")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    else:
                        imprir("SELECT : Viene otro tipo de Funcion ")
                        er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                        LisErr.agregar(er)


                elif (str(uni.Reservada) == ";"):
                    print("Fin ")

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
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif (str(uni.Comportamiento).upper() == "INTERSECT"):
                        print("<<<<<<<<<<<<<<<<<<<<<<<<   ES LA SALIDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  ")
                        print("Viene un Intersect")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("<<<<<<<<<<<<<<<<<<<<<<<<   ES LA SALIDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  ***")

                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            print("**********************************************************************************")
                            print(listaling)
                            print("**********************************************************************************")
                            #mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            print("**********************************************************************************")
                            print(list2)
                            print("**********************************************************************************")
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)


                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)


                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Interseccion(listaling)
                            imprir("SELECT: Comando INTERSECT con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    elif (str(uni.Comportamiento).upper() == "EXCEPT"):
                        print("<<<<<<<<<<<<<<<<<<<<<<<<   ES LA SALIDAAAAAAAAAAAAAAAAAAAAAAAAAAAAEXCEPT  ")
                        print("Viene un Except")
                        ank = uni.Consulta
                        if (isinstance(ank, Select)):
                            print("viene un tipo de select normal unido")
                            ank.Ejecutar()
                            print("Tenemos el diccionario ya unido ")
                            print(listaGeneral)
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select2)):
                            ank.Ejecutar()
                            print("viene un tipo de select normal con cuerpo")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)

                        elif (isinstance(ank, Select3)):
                            ank.Ejecutar()
                            print("Viene un tipo de Select normal con distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)


                        elif (isinstance(ank, Select4)):
                            ank.Ejecutar()
                            print("viene un tipo de Select normal con cuerpo y distinct")
                            listaling = AlinearDatos(listaGeneral)
                            mostrarConsulta(listaling)
                            list2 = Excepcion(listaling)
                            imprir("SELECT: Comando Except con Exito")
                            listaGeneral.update(list2)
                            # mostrarConsulta(list2)
                        else:
                            imprir("SELECT : Viene otro tipo de Funcion ")
                            er = ErrorRep('Semantico', 'No Es el correcto tipo de funcion ', 0)
                            LisErr.agregar(er)

                    else:
                        imprir("SELECT : Palabra Reservada No encontrada")
                        er = ErrorRep('Semantico', 'No Se Encontro la Palabra reservada', 0)
                        LisErr.agregar(er)

        listaling = AlinearDatos(listaGeneral)
        print("<<<<<<<<<<<<<<<<<<<<<<<<   ES LA SALIDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  ")
        print(listaling)

        mostrarConsulta(listaling)



class SelectExpresion(Instruccion):
    def __init__(self, listaCampos = []):
        self.listaCampos = listaCampos

    def Ejecutar(self):
        global ts_global
        numero = 1
        for campo in self.listaCampos:

            if isinstance(campo, Campo_AccedidoSinLista):
                if isinstance(campo.Columna, string_types):
                    if campo.Columna.isnumeric() or campo.Columna.isdecimal():
                        result = int(campo.Columna)
                        listaGeneral['Expresion' + str(numero)] = [result]
                        numero += 1
                else:
                    result = Inter.procesar_expresion(campo.Columna, ts_global)
                    listaGeneral['Expresion' + str(numero)] = [result]
                    numero += 1
            if isinstance(campo, Campo_Accedido):
                columna = campo.Columna
                alias = campo.Lista_Alias.Alias
                if isinstance(columna, string_types):
                    if columna.isnumeric() or columna.isdecimal():
                        result = int(columna)
                        listaGeneral[alias] = [result]
                        numero += 1
                else:
                    result = Inter.procesar_expresion(columna, ts_global)
                    listaGeneral[alias] = [result]
                    numero += 1




        mostrarConsulta(listaGeneral)
        listaGeneral.clear()



#subSelect sin cuerpo
#---------------------------------------------------------------------------------------------------
class SubSelect(Instruccion) :
    def __init__(self, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas

    def Ejecutar(self):
        #Listas Auxiliares
        Lista = {}
        Lista = GenerarTablaQuery(self.Lista_Campos, self.Nombres_Tablas)
        print(Lista)
        listaGeneral.update(Lista)

        imprir("Ejecute una Subconsulta <<<<<<<<<<<<<")
        return Lista


#subSelect con cuerpo
#---------------------------------------------------------------------------------------------------
class SubSelect2(Instruccion) :
    def __init__(self,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.Cuerpo = Cuerpo
    def Ejecutar(self):

        #Generamos el Query
        Lista = GenerarTablaQuery(self.Lista_Campos, self.Nombres_Tablas)
        #Filtramos el cuerpo
        print("Esto devuelve la Generacion de Tabla ")
        print(Lista)

        listi = FiltrarCuerpo(Lista, self.Cuerpo)
        print(listi)
        listaGeneral.update(listi)
        #Rellenamos campos si no son suficientes
        listaling = AlinearDatos(listaGeneral)
        mostrarConsulta(listaling)


#subSelect sin cuerpo con distict
#---------------------------------------------------------------------------------------------------

class SubSelect3(Instruccion) :
    def __init__(self,Distict, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Distict       = Distict
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas

    def Ejecutar(self):
        Lista = {}

        Lista = GenerarTablaQuery(self.Lista_Campos, self.Nombres_Tablas)
        print(Lista)
        listaGeneral.update(Lista)
        print(Lista)

#subSelect con cuerpo con distict
#---------------------------------------------------------------------------------------------------
class SubSelect4(Instruccion) :
    def __init__(self,Distict,Cuerpo, Lista_Campos=[], Nombres_Tablas=[] ) :
        self.Distict       = Distict
        self.Lista_Campos   = Lista_Campos
        self.Nombres_Tablas = Nombres_Tablas
        self.Cuerpo = Cuerpo


    def Ejecutar(self):
        Lista = {}
        # Generamos el Query
        Lista = GenerarTablaQuery(self.Lista_Campos, self.Nombres_Tablas)
        # Filtramos el cuerpo
        print("Esto devuelve la Generacion de Tabla ")
        print(Lista)

        listi = FiltrarCuerpo(Lista, self.Cuerpo)
        print(listi)
        listaGeneral.update(listi)
        # Rellenamos campos si no son suficientes
        listaling = AlinearDatos(listaGeneral)
        mostrarConsulta(listaling)



# Campos Accedidos
#---------------------------------------------------------------------------------------------------

#Campos Accedidos por Lista
class Campo_Accedido(Instruccion): #Nombre.columna  Lista_Posible

    def __init__(self, NombreT, Columna, Lista_Alias=[]):
        self.NombreT       = NombreT
        self.Columna       = Columna
        self.Lista_Alias   = Lista_Alias

    def Ejecutar(self):
        print("")

#Campos Accedidos por Lista
class Campo_AccedidoSinLista(Instruccion): #Nombre.columna  Lista_Posible

    def __init__(self, NombreT, Columna):
        self.NombreT       = NombreT
        self.Columna       = Columna

#---------------------------------------------------------------------------------------------------
#Nombre Tabla Accedidos
#---------------------------------------------------------------------------------------------------

class AccesoTabla(Instruccion): #Tabla Lista

    def __init__(self, NombreT,Lista_Alias=[]):
        self.NombreT     = NombreT
        self.Lista_Alias = Lista_Alias

#Accediendo sin lista
class AccesoTablaSinLista(Instruccion): #Tabla

    def __init__(self, NombreT):
        self.NombreT     = NombreT

#---------------------------------------------------------------------------------------------------

#Campos Accedidos desde Group By
#---------------------------------------------------------------------------------------------------

class AccesoGroupBy(Instruccion): #Tabla Lista

    def __init__(self, NombreT,Columna,Estado,Lista_Alias=[]):
        self.NombreT      = NombreT
        self.Columna      = Columna
        self.Lista_Alias  = Lista_Alias
        self.Estado       = Estado



#---------------------------------------------------------------------------------------------------

# Campos Limit
#---------------------------------------------------------------------------------------------------

class AccesoLimit(Instruccion):

    def __init__(self,Reservada,Expresion_Numerica):
        self.Reservada = Reservada
        self.Expresion_Numerica  =  Expresion_Numerica


#Campos Accedidos desde Las Subconsultas
#---------------------------------------------------------------------------------------------------

class AccesoSubConsultas(Instruccion):

    def __init__(self, AnteQuery=[],Query=[],Lista_Alias=[]):
        self.AnteQuery      = AnteQuery
        self.Query          = Query
        self.Lista_Alias  = Lista_Alias


#---------------------------------------------------------------------------------------------------

#Campos de los unions
#---------------------------------------------------------------------------------------------------

class CamposUnions(Instruccion):
    def __init__(self,Reservada,Comportamiento,Consulta=[]):
        self.Reservada      = Reservada
        self.Comportamiento = Comportamiento
        self.Consulta       = Consulta


# Alias
#---------------------------------------------------------------------------------------------------
#Alias Campos
#---------------------------------------------------------------------------------------------------

#Alias Campos sin lista
class Alias_Campos_ListaCamposSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias
#Alias Tablas
#---------------------------------------------------------------------------------------------------
#Alias campos Sin Lista
class Alias_Table_ListaTablasSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias
#Alias Group By
#---------------------------------------------------------------------------------------------------
#Alias campos Sin Lista
class Alias_Tablas_GroupSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias

#Alias SUB QUERYS
#---------------------------------------------------------------------------------------------------
class Alias_SubQuerysSinLista(Instruccion):
    def __init__(self, Alias):
        self.Alias = Alias

# FIN ALIAS
#---------------------------------------------------------------------------------------------------


#Cuerpo Consulta
#---------------------------------------------------------------------------------------------------
#where Condiciones

class Cuerpo_Condiciones(Instruccion):
    def __init__(self,Cuerpo=[]):
        self.Cuerpo = Cuerpo

#Cuerpo Tipo Where condiciones
#---------------------------------------------------------------------------------------------------
class Cuerpo_TipoWhere(Instruccion):
    def __init__(self,Cuerpo=[]):
        self.Cuerpo = Cuerpo
#TIPOS DE GROUP BY
#---------------------------------------------------------------------------------------------------
#Group By  Con Having y condiciones
class GroupBy(Instruccion):
    def __init__(self,Lista_Campos=[],Condiciones=[]):
        self.Lista_Campos = Lista_Campos
        self.Condiciones  = Condiciones


#Group By  Con Having y condiciones
class OrderBy(Instruccion):
    def __init__(self,Lista_Campos=[],Condiciones=[]):
        self.Lista_Campos = Lista_Campos
        self.Condiciones  = Condiciones


#TIPOS DE CASES
#---------------------------------------------------------------------------------------------------
class CaseCuerpo(Instruccion):
    def __init__(self,Cuerpo,Lista_When=[]):
        self.Lista_When = Lista_When
        self.Cuerpo     = Cuerpo


class ExpresionesCase(Instruccion):
    def __init__(self,Reservada,ListaExpresiones=[]):
        self.Reservada            = Reservada
        self.ListaExpresiones     = ListaExpresiones

class TiposWhen(Instruccion):
    def __init__(self,Reservada,Reservada2,Reservada3,ListaExpresiones1=[],ListaExpresiones2=[],ListaExpresiones3=[]):
        self.Reservada    = Reservada
        self.Reservada2   = Reservada2
        self.Reservada3   = Reservada3
        self.ListaExpresiones1 = ListaExpresiones1
        self.ListaExpresiones2 = ListaExpresiones2
        self.ListaExpresiones3 = ListaExpresiones3

#---------------------------------------------------------------------------------------------------
#INSERTAR DATOS CESAR
class DatoInsert(Instruccion):
    def __init__(self, bd, tabla, columna, valor, fila):
        self.bd = bd
        self.tabla = tabla
        self.columna = columna
        self.valor = valor
        self.fila = fila
        self.calculado = valor

class Insert_Datos(Instruccion):
    def __init__(self, id_table, valores):
        self.id_table = id_table
        self.valores = valores

    def Ejecutar(self):
        print("ENTRA AL INSERT -----------------------------------------------------------------------")
        FilaG = randint(1,500)
        print("Ejecucion")
        global ts_global, baseActual
        global LisErr
        r = ts_global.obtenerBasesDatos(baseActual)

        if r is None:
            imprir("INSERT BD:  No existe la BD para insertar.")
        else:
            r2:CreateTable = ts_global.obtenerTabla(self.id_table[0].val)
            if r2 is None:
                imprir("INSERT BD:  No existe la Tabla para insertar.")
            else:
                # Obtener tabla actual
                rT:CreateTable = ts_global.obtenerTabla(self.id_table[0].val)
                #print(">>>>>>>"+str(rT.id))

                temporal:CampoTabla = rT.cuerpo
                print("ENTRA AL INSERT 2-----------------------------------------------------------------------")
                # borre un for incesesario de impresion

                cC = 0
                for c in rT.cuerpo:
                    if isinstance(c, constraintTabla):
                        pass
                    else:
                        cC += 1

                cV = 0
                for v in self.valores:
                    cV += 1

                if cC == cV:
                    print(" >> Parametros exactos. +++++++++++++++++++++++++++++++++++++++++++")
                    index = 0
                    banderaInsert = False

                    for cc in self.valores:
                        if isinstance(temporal[index], constraintTabla):
                            pass
                        else:
                            if isinstance(temporal[index].tipo, valorTipo):

                                resultado = Inter.procesar_expresion(cc, None)
                                print(" Mi proceso: "+str(resultado))

                                if isinstance(resultado, string_types) and (str(temporal[index].tipo.valor).upper() == 'VARCHAR' or str(temporal[index].tipo.valor).upper() == 'CHARACTER' or str(temporal[index].tipo.valor).upper() == 'CHAR'):
                                    print(" >>> Parametros correctos, insertar, Validar la exprecion.")
                                    banderaInsert = True
                                else:
                                    imprir("INSERT BD: Parametros incorrectos. ")
                                    banderaInsert = False
                            else:
                                resultado = Inter.procesar_expresion(cc, None)
                                print(" Mi proceso: "+str(resultado))
                                #print(" Valor: >>>" + str(cc.val))
                                if isinstance(resultado, string_types) and  str(temporal[index].tipo).upper() == 'TEXT' or str(temporal[index].tipo).upper() == 'DATE':
                                    print(" >>> Parametros correctos, insertar")
                                    banderaInsert = True
                                elif str(temporal[index].tipo).upper() == 'BOOLEAN'and (str(cc.val).upper() == 'TRUE' or str(cc.val).upper() == 'FALSE'):
                                    imprir("INSERT BD: Parametros correctos, insertar")
                                    banderaInsert = True
                                elif int(resultado) > 0 and (str(temporal[index].tipo).upper() == 'SMALLINT' or str(temporal[index].tipo).upper() == 'INTEGER' or str(temporal[index].tipo).upper() == 'INT' or str(temporal[index].tipo).upper() == 'BIGINT' or str(temporal[index].tipo).upper() == 'DECIMAL' or str(temporal[index].tipo).upper() == 'REAL' or str(temporal[index].tipo).upper() == 'FLOAT' or str(temporal[index].tipo).upper() == 'MONEY'):
                                    print(" >>> Parametros correctos, insertar")
                                    banderaInsert = True
                                else:
                                    imprir("INSERT BD: Parametros incorrectos. ")
                                    banderaInsert = False

                            index += 1

                    # INSERTANDO DATOS
                    ix = 0
                    if banderaInsert is True:
                        listaTemp = []

                        for ccc in self.valores:
                            resultado = Inter.procesar_expresion(ccc, None)
                            d = DatoInsert(baseActual, r2.id, str(temporal[ix].id), resultado, FilaG)
                            ts_global.agregarDato(d)
                            listaTemp.append(resultado)
                            ix += 1

                        sr = Master.insert(baseActual, str(self.id_table[0].val), listaTemp)
                        print(baseActual + str(self.id_table[0].val) + str(len(listaTemp)))
                        if sr is 0:
                            imprir("INSERT BD:  Insert realizado con exito.")
                        else:
                            imprir("INSERT BD:  No se realizo el insert.")
                else:
                    imprir("INSERT BD:  Parametros insuficientes.")

# ***************************** CREATE TABLE Y INHERITS ****************************************
class Inherits(Instruccion):
    def __init__(self, id):
        self.id = id

class ObjetoValidacion():
    def __init__(self, tabla, campo, validacion, id):
        self.tabla = tabla
        self.campo = campo
        self.validacion = validacion
        self.id = id

class CreateTable(Instruccion):
    def __init__(self, id, cuerpo, inhe):
        self.id = id
        self.cuerpo = cuerpo
        self.inhe = inhe

    def Ejecutar(self):
        global ts_global, baseActual
        global LisErr

        # SI la tabla ya existe en el diccionario.
        r = ts_global.obtenerTabla(self.id)

        if r is None:
            imprir("INSERT BD: Creando tabla. ")

            # se cuenta el numero de columnas
            columnas = 0

            for campos in self.cuerpo:
                if isinstance(campos, constraintTabla):
                    pass
                else:
                    columnas += 1

            rM = Master.createTable(baseActual, self.id, columnas)

            #Insertamos las validaciones que tengan.
            for v in self.cuerpo:
                x:CampoTabla = v
                if isinstance(v, CampoTabla):
                    for vali in x.validaciones:
                        if isinstance(vali, CampoValidacion):
                            val: CampoValidacion = vali
                            if vali.id is None:
                                print("nada")
                                pass
                            else:
                                print(str(val.id) + str(val.valor))
                                temporal2 = constraintTabla(str(val.id), "auto", None, x.id, None, self.id)
                                ts_global.agregarValidacion(temporal2)

                        elif isinstance(vali, constraintTabla):
                            val: constraintTabla = vali
                            if val is None:
                                pass
                            else:
                                print(val.valor+val.id+val.listas_id+val.idRef)
                else:
                    print(">>> ES OTRO TIPO DE CAMPO")
                    vv: constraintTabla = v
                    Vcion = ObjetoValidacion(self.id, vv.id, vv.valor, vv.id)
                    ts_global.agregarValidacion(Vcion)

            if rM == 0:
                ts_global.agregarTabla(self)
                print(" > Se creo la tabla en la base de datos.")

            elif rM == 1:
                print("> 1")
                er =  ErrorRep('Semantico', 'No se encontro el archivo data.',0)
                LisErr.agregar(er)

            elif rM == 2:
                print("> 2")
                er =  ErrorRep('Semantico', 'No existe la base de datos actual.',0)
                LisErr.agregar(er)

            elif rM == 3:
                print( "> 3")
                er =  ErrorRep('Semantico', 'La tabla ya existe en la base de datos.',0)
                LisErr.agregar(er)
        else:
            imprir("INSERT BD: La tabla ya esta en la TS. ")
            er = ErrorRep('Semantico', 'La tabla ya existe en la base de datos.', 0)
            LisErr.agregar(er)

# --------------------------------------------------------
class CampoTabla(Instruccion):
    def __init__(self, id, tipo, validaciones):
        self.id = id
        self.tipo = tipo
        self.validaciones = validaciones

#---------------------------------------------------------
class CampoValidacion(Instruccion):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor

#---------------------------------------------------------------------------------------------------
class Delete_Datos(Instruccion):
    def __init__(self, id_table, valore_where):
        self.id_table = id_table
        self.valore_where = valore_where

    def Ejecutar(self):
        global ts_global, baseActual, ListaTablasG
        global LisErr

        ListaTablasG.append(self.id_table[0].val)
        rb = ts_global.obtenerBasesDatos(baseActual)
        if rb is None:
            imprir("DELETE: No existe la base de datos. ")
            er = ErrorRep('Semantico', 'No existe la base de datos indicada.', 0)
            LisErr.agregar(er)
        else:
            rt = ts_global.obtenerTabla(self.id_table[0].val)
            if rt is None:
                imprir("DELETE: No existe la tabla de datos. ")
                er = ErrorRep('Semantico', 'No existe la tabla indicada.', 0)
                LisErr.agregar(er)
            else:
                resultado = Inter.procesar_expresion(self.valore_where, ts_global)
                listaEliminar = []
                # recorrer lista de valores a eliminar.
                if len(resultado) is 0:
                    imprir("DELETE: No existen registros.")

                    er = ErrorRep('Semantico', 'No existen registros que cumplan la condicion para eliminar.', 0)
                    LisErr.agregar(er)
                else:
                    for i in resultado:
                        ii:DatoInsert = i

                        #recorrer tabla de simbolos.
                        for item in ts_global.Datos:
                            v: DatoInsert = ts_global.obtenerDato(item)
                            bandera = False
                            if str(ii.fila) == str(v.fila):

                                for p in listaEliminar:
                                    if item == p:
                                        bandera = True
                                    else:
                                        bandera = False

                                if bandera is False:
                                    listaEliminar.append(item)

                    for d in listaEliminar:
                        r = ts_global.EliminarDato(d)
                        if r is None:
                            pass
                        else:
                            pass
                    imprir(" DELETE: Se eliminaron los registros.")
# --------------------------------------------------------------------------------------------------
class constraintTabla(Instruccion):
    def __init__(self, valor, id, condiciones, listas_id, referencia, idRef):
        self.valor = valor
        self.id = id
        self.condiciones = condiciones
        self.listas_id = listas_id
        self.referencia = referencia
        self.idRef = idRef


class CreateDataBase(Instruccion):
    def __init__(self, replace, exists, idBase, idOwner, Modo ):
        self.replace = replace
        self.exists = exists
        self.idBase = idBase
        self.idOwner = idOwner
        self.Modo = Modo


    def Ejecutar(self):
        global ts_global, baseActual
        global LisErr,Ejecucion

        if self.replace == "":
            r = ts_global.obtenerBasesDatos(self.idBase)
            if r is None:
                rM = Master.createDatabase(str(self.idBase))
                imprir("CREATE DB:  Base de datos creada con exito!")
                if rM == 0:
                    ts_global.agregarBasesDatos(self)
                    print(" > Base de datos creada con exito!")
                elif rM == 1 or rM == 2:
                    print("> Base de datos ya existe.")
                    er = ErrorRep('Semantico', 'La Base de datos ya existe', 0)
                    LisErr.agregar(er)
            else:
                print("Si encontre la BD. ")
                imprir("CREATE DB:  La Base de Datos No se Creo ya que existe!")
                er = ErrorRep('Semantico', 'La Base de datos ya existe', 0)
                LisErr.agregar(er)
        else:
            r = ts_global.obtenerBasesDatos(self.idBase)
            if r is None:

                rM = Master.createDatabase(str(self.idBase))
                imprir("CREATE DB:    Base de datos creada con exito!")
                baseActual = str(self.idBase)
                baseN.append(self.idBase)
                if rM == 0:
                    ts_global.agregarBasesDatos(self)
                    print(" > Base de datos creada con exito!")
                elif rM == 1 or rM == 2:
                    print("> Base de datos ya existe Se va a Reemplazar ")
            else:
                imprir("CREATE DB:  Se encontro la BD Bamos a Reemplazar!")
                Lista.clear();
                Lista.append(Ejecucion)
                print("Si encontre la BD. Bamos a Reemplazar la Misma! ")

class ShowDatabases(Instruccion):
    def __init__(self, cadenaLike):
        self.cadenaLike = cadenaLike

    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion
        #idDB = self.cadenaLike.replace("\"","")

        r  = Master.showDatabases()
        if r  is not None:  #si lo encuentra
            for element in r:
                print(str(element))
                imprir("SHOW DB:>"+ str(element))
        else:
            imprir("SHOW DB: No se encontro la BD")
            er = ErrorRep('Semantico', 'No Encontre la Base de Datos', 0)
            LisErr.agregar(er)


class AlterDataBase(Instruccion):
    def __init__(self, idDB, opcion):
        self.idDB = idDB
        self.opcion = opcion

    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion


        c1 = False
        c2 = False
        error=""

        opcion  = self.opcion.replace("\"", "")
        opcionf = self.opcion.replace("\'", "")

        r =  ts_global.obtenerBasesDatos(self.idDB)
        r2 = ts_global.obtenerBasesDatos(opcionf)

        if r is not None:  #si lo encuentra
            c1 = True
        else:
            error += "No se Encontro la Base De datos "
        if r2 is  None:  #No Esta el Nombre para definirlo en la bd
            c2 = True
        else:
            error += "  Se encontro el Valor a Setear"

        if (c1 and c2):
            print("Excelente se puede editar")
            #Editamos nuestro diccionario
            ts_global.actualizarCreateDataBase(str(self.idDB),str(self.opcion))
            imprir("ALTER DB: Edicion base de Datos Exitosa!")
            #Editamos en base de datos fisica
            rM = Master.alterDatabase(str(self.idDB),str(self.opcion))
            if rM==2:
                print("No se encuentra la BD")
            elif rM==3:
                print("Ya se encuentra la BD con el nombre a tratar")
            elif rM==1:
                print("Verificar Ocurrio Error Al editar")
            elif rM==0:
                print("Se Edito la Base de Datos con exito")
            else:
                print( "No llega nunca pero por si las moscas ")
        else:
            print("No encontre la BD.")
            imprir("ALTER DB:  No se encontro la base de datos! :( ")
            er = ErrorRep('Semantico', error, 0)
            LisErr.agregar(er)


class DropDataBase(Instruccion):

    def __init__(self, id, existe):
        self.id = id
        self.existe = existe



    def Ejecutar(self):
        global ts_global
        global LisErr,Ejecucion

        r = ts_global.obtenerBasesDatos(self.id)

        if r == None:  #si lo encuentra
            imprir("DROP DB:  No se encontro la base de datos! :( ")
            er = ErrorRep('Semantico', 'No Encontre la Base de Datos', 0)
            LisErr.agregar(er)
        else:
            ts_global.EliminarBD(str(self.id))
            imprir("DROP DB:  Se elimino correctamente la base de Datos! :) ")
            rM = Master.dropDatabase(str(self.id))
            if rM==0:
                print("Exito")
            elif rM==1:
                print("Fracaso al escribir en bd")
            elif rM==2:
                print("No existe el elemento en la BD")
            else:
                print("No llega nunca pero por si las moscas")

# Crear funciones de ejecucion ----------------------------------
class SelectExtract(Instruccion):
    def __init__(self, tipoTiempo, cadenaFecha):
        self.tipoTiempo = tipoTiempo
        self.cadenaFecha = cadenaFecha

    def Ejecutar(self):
        pass


class SelectDatePart(Instruccion):
    def __init__(self, cadena, cadenaIntervalo):
        self.cadena = cadena
        self.cadenaIntervalo = cadenaIntervalo

class SelectTipoCurrent(Instruccion):
    def __init__(self, tipoCurrent):
        self.tipoCurrent = tipoCurrent

class SelectStamp(Instruccion):
    def __init__(self, cadena):
        self.cadena = cadena

class Selectnow(Instruccion):
    def __init__(self, constru):
        self.constru = constru

class CreacionEnum(Instruccion):
    def __init__(self, id, listaCadenas):
        self.listaCadenas = listaCadenas
        self.id = id

    def Ejecutar(self):
        global ts_global, baseActual, ListaTablasG
        global LisErr

        if self.listaCadenas.__len__() != 0:
            for cadena in self.listaCadenas:

                if str(cadena) not in ts_global.Tipos:
                    mi = DatoTipo(baseActual, str(self.id), str(cadena))
                    ts_global.agregarTipo(mi)
                    imprir("TYPE: Tipo agregado")
                else:
                    imprir("TYPE: Ya existe este tipo.")
                    er = ErrorRep('Semantico', 'El tipo creado ya existe.', 0)
                    LisErr.agregar(er)
        else:
            imprir("TYPE: Los parametros son incorrectos.")
            er = ErrorRep('Semantico', 'Se necesitan cadenas para crearlos..', 0)
            LisErr.agregar(er)

        print("AQUI ESTAN")
        for ca in ts_global.Tipos:
            a = ts_global.Tipos.get(ca)
            print(str(a.tipo))

# Crear funciones de ejecucion ----------------------------------
#Prueba clase errores
class ErrorSintactico():
    def __init__(self, valor, error, linea):
        self.valor = valor
        self.error = error
        self.linea = linea

    def imprimirError(self):
        return " Error " + str(self.error) + ", no se esperaba el token: " + str(self.valor) + ", Linea: " + str(self.linea)

#---------------------------------------------------------------------------------------------------
class Update_Datos(Instruccion):
    def __init__(self, id_table, valores_set, valor_where):
        self.id_table = id_table
        self.valores_set = valores_set
        self.valor_where = valor_where


    def Ejecutar(self):
        global ts_global, baseActual, ListaTablasG
        global LisErr

        ListaTablasG.append(self.id_table[0].val)
        rb = ts_global.obtenerBasesDatos(baseActual)
        if rb is None:
            imprir("UPDATE: No existe la base de datos.")
            er = ErrorRep('Semantico', 'No existe la base de datos.', 0)
            LisErr.agregar(er)
        else:
            rt = ts_global.obtenerTabla(self.id_table[0].val)
            if rt is None:
                imprir("UPDATE: No existe la tabla indicada.")
                er = ErrorRep('Semantico', 'No existe la tabla indicada.', 0)
                LisErr.agregar(er)
            else:
                resultado = Inter.procesar_expresion(self.valor_where, ts_global)
                listaUpdate = []
                if len(resultado) is 0:
                    imprir("UPDATE: No existen registros.")
                    er = ErrorRep('Semantico', 'No existen registros que cumplan la condicion para actualizar.', 0)
                    LisErr.agregar(er)
                else:
                    listaSet = []
                    # Valores SET
                    for i in self.valores_set:
                        p: ExpresionAritmetica = i
                        listaSet.append(p)

                    # recorrer lista de valores a actualizar.
                    for i in resultado:
                        ii:DatoInsert = i

                        #recorrer tabla de simbolos.
                        for item in ts_global.Datos:
                            v: DatoInsert = ts_global.obtenerDato(item)
                            bandera = False
                            if str(ii.fila) == str(v.fila):
                                for p in listaUpdate:
                                    if item == p:
                                        bandera = True
                                    else:
                                        bandera = False

                                if bandera is False:
                                    listaUpdate.append(v)

                    for i in listaUpdate:
                        ii: DatoInsert = i
                        for s in listaSet:
                            ss: ExpresionAritmetica = s
                            if str(ss.exp1.id) == str(ii.columna):
                                ii.valor = str(ss.exp2.val)
                            else:
                                pass
                imprir("UPDATE: Se actualizaron los registros.")

#Clase para el Alter Table----------------------------
class Alter_Table_AddColumn(Instruccion):
    def __init__(self, id_table, id_columnas):
        self.id_table = id_table
        self.id_columnas = id_columnas

        """ def Ejecutar(self):
        #Verificar que existe la base de datos
        #Verificar que existe la tabla
        #Verificar que existe la columna en la tabla
        global ts_global, baseActual
        global LisErr
        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)
            print(self.id_table)



            if r2 is not None:

                for elemento in self.id_columnas:


                    if isinstance(elemento,ExpresionValor2):

                        rc =  Master.alterAddColumn(baseActual,self.id_table,elemento.val)

                        if rc == 0:

                            #Se ingreso correctamente el valor
                            temporal2 = CampoValidacion(None, None)
                            temporal  = CampoTabla(elemento.val, elemento.tipo, temporal2)
                            r2.cuerpo.append(temporal)


                            for elemento in ts_global.Tablas:
                                x:CreateTable = ts_global.obtenerTabla(elemento)
                                for ele in x.cuerpo:
                                    y:CampoTabla  = ele
                                    print(y.id+"<<<<<<<<<<<<<<<<<<<<<<")
                            imprir("ALTER TABLE: Se Agrego correctamente la Columna")
                        elif rc==1:
                            #Error al escribir en la base de datos
                            imprir("ALTER TABLE: Error al Escribir en la Base de Datos")
                        elif rc==2:
                            #No esta la base de datos  en las listas
                            imprir("ALTER TABLE: No existe la BD")
                        elif rc==3:
                            #no esta la tabla en la base de datos
                            imprir("ALTER TABLE: La tabla no existe en la BD")
                        else:
                            #Error logico
                            imprir("ALTER TABLE: Error logico en la operacion")
                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            #colocar error semantico
            """

    def Ejecutar(self):
        print("EJECUTAR ALTER TABLE ADD COLUMN")
        # Verificar que existe la base de datos
        # Verificar que existe la tabla
        # Verificar que existe la columna en la tabla
        global ts_global, baseActual
        global LisErr
        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2: CreateTable = ts_global.obtenerTabla(self.id_table)
            print(self.id_table)

            if r2 is not None:

                for elemento in self.id_columnas:

                    if isinstance(elemento, ExpresionValor2):

                        bandera = False
                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)
                            print(str(x.id) + " ÑÑÑ " +str(self.id_table))
                            if (x.id == self.id_table):
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    print(str(y.id) + str(elemento.val))
                                    if y.id != elemento.val:
                                        print("BANDERA ES TRUE")
                                        bandera = True
                            else:
                                print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")


                        if bandera == True:
                            print("SI ES TRUE")
                            rc = Master.alterAddColumn(baseActual, self.id_table, elemento.val)

                            if rc == 0:
                                # Se ingreso correctamente el valor
                                temporal2 = CampoValidacion(None, None)
                                temporal = CampoTabla(elemento.val, elemento.tipo, temporal2)
                                print("CAMPO  TABLA: "+str(elemento.val)+str(elemento.tipo)+str(temporal2))
                                r2.cuerpo.append(temporal)

                                imprir("ALTER TABLE: Se Agrego correctamente la Columna")

                                for elemento2 in ts_global.Tablas:
                                    x: CreateTable = ts_global.obtenerTabla(elemento2)
                                    print("TABLA: ")
                                    if (x.id == self.id_table):
                                        for ele in x.cuerpo:
                                            y = ele
                                            if isinstance(ele, CampoTabla):
                                                print(str(y.id)+str(y.tipo))

                            elif rc == 1:
                                # Error al escribir en la base de datos
                                imprir("ALTER TABLE: Error al Escribir en la Base de Datos")
                            elif rc == 2:
                                # No esta la base de datos  en las listas
                                imprir("ALTER TABLE: No existe la BD")
                            elif rc == 3:
                                # no esta la tabla en la base de datos
                                imprir("ALTER TABLE: La tabla no existe en la BD")
                            else:
                                # Error logico
                                imprir("ALTER TABLE: Error logico en la operacion")
                        else:
                            imprir("ALTER TABLE: La columna a insertar ya existe ")
                    else:
                        imprir("ALTER TABLE: Error de tipo.")
            else:
                imprir("ALTER TABLE:   La tabla no existe.")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe.")

class Alter_COLUMN(Instruccion):
    def __init__(self, idtabla,columnas):
        self.idtabla = idtabla
        self.columnas = columnas

    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2: CreateTable = ts_global.obtenerTabla(self.idtabla)

            if r2 is not None:


                for tt in self.columnas:

                    if isinstance(tt, ExpresionValor2):


                        #recorremos lista General de Tablas
                        for elemento2 in ts_global.Tablas:

                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if (x.id == self.idtabla):
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele

                                    print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")
                                    if (y.id == tt.val):

                                        y.tipo = tt.tipo
                                        imprir("ALTER TABLE: Se Actualizo correctamente El Tipo de Dato")
                                    else:
                                        print("")
                            else:
                                print("")

                        # imprimir valores actualizados
                        # for elemento2 in ts_global.Tablas:
                        #    x: CreateTable = ts_global.obtenerTabla(elemento2)
                        #    for ele in x.cuerpo:
                        #        y: CampoTabla = ele
                        #       print(y.id + "<<<<<<<<<<<<<<<<<<<<<< EEEEEEEEEEEE")

                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                    imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            # colocar error semantico

class Alter_Table_Drop_Column(Instruccion):
    def __init__(self, id_table, columnas):
        self.id_table = id_table
        self.columnas = columnas


    def Ejecutar(self):

        #Verificar que existe la base de datos
        #Verificar que existe la tabla
        #Verificar que existe la columna en la tabla

        global ts_global, baseActual
        global LisErr
        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)

            if r2 is not None:

                for elemento in self.columnas:

                    if isinstance(elemento,ExpresionValor):
                        #Agarramos el valor de la lista de elementos
                        #Recorremos para buscar la columna en la lista
                          contador=0
                          for elemento2 in ts_global.Tablas:
                             x:CreateTable = ts_global.obtenerTabla(elemento2)

                             if(x.id == self.id_table):

                                 for ele in x.cuerpo:
                                   y:CampoTabla  = ele
                                   print(y.id+"<<<<<<<<<<<<<<<<<<<<<<")

                                   if (y.id==elemento.val):
                                       contador += 1

                                       #mandamos a eliminar y verificamos la respuesta
                                       print(str(baseActual)+str(self.id_table)+str(contador))
                                       rc = Master.alterDropColumn(str(baseActual), str(self.id_table), int(contador))
                                       if rc == 0:
                                           # Se elimino correctamente el elemento
                                           #Eliminamos de nuestro diccionario
                                           r2.cuerpo.remove(y.id)
                                           imprir("ALTER TABLE: Se Elimino correctamente la Columna")
                                       elif rc == 1:
                                           # Error al escribir en la base de datos
                                           imprir("ALTER TABLE: Error al Eliminar en la Base de Datos")
                                       elif rc == 2:
                                           # No esta la base de datos  en las listas
                                           imprir("ALTER TABLE: No existe la BD")
                                       elif rc == 3:
                                           # no esta la tabla en la base de datos
                                           imprir("ALTER TABLE: La tabla no existe en la BD")
                                       elif rc == 4:
                                           # no esta la tabla en la base de datos
                                           imprir("ALTER TABLE: La Columna no esta ")

                                       elif rc == 5:
                                           # no esta la tabla en la base de datos
                                           imprir("ALTER TABLE: Excedio los Limites ")

                                       else:
                                           # Error logico
                                           imprir("ALTER TABLE: Error logico en la operacion")
                                   else:
                                       contador+=1

                             else:
                                 print("Next!")

                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            #colocar error semantico


class Alter_Table_Rename_Column(Instruccion):
    def __init__(self, id_table, old_column, new_column):
        self.id_table = id_table
        self.old_column = old_column
        self.new_column = new_column

    def Ejecutar(self):

        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)

            if r2 is not None:

                elementoo  = self.old_column
                elementoo2 = self.new_column

                if isinstance(elementoo, ExpresionValor) and isinstance(elementoo2, ExpresionValor):

                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if(x.id == self.id_table):
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")
                                    if (y.id == elementoo.val):
                                        y.id = elementoo2.val
                                        imprir("ALTER TABLE: Se Actualizo correctamente la Columna")
                                    else:
                                        print("")
                            else:
                                print("")
                        #imprimir valores actualizados
                        #for elemento2 in ts_global.Tablas:
                        #    x: CreateTable = ts_global.obtenerTabla(elemento2)
                        #    for ele in x.cuerpo:
                        #        y: CampoTabla = ele
                        #       print(y.id + "<<<<<<<<<<<<<<<<<<<<<< EEEEEEEEEEEE")

                else:
                    imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            # colocar error semantico

class Alter_Table_Drop_Constraint(Instruccion):
    def __init__(self, id_table, id_constraint):
        self.id_tabla = id_table
        self.id_constraint = id_constraint


    def Ejecutar(self):
        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)

            if r2 is not None:

                elementoo  = self.id_constraint

                if isinstance(elementoo, ExpresionValor):

                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if(x.id == self.id_tabla):
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    print(y.id + "<<<<<<<<<<<<<<<<<<<<<<")
                                    if (y.id == elementoo.val):

                                        for validacion in y.validaciones:
                                            validacion:CampoValidacion
                                            if validacion.valor=="CONSTRAINT_UNIQUE":
                                                validacion.valor = " "
                                                imprir("ALTER TABLE: CONSTRAINT ELIMINADO CORRECTAMENTE")
                                    else:
                                        print("")
                            else:
                                print("")


                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if(x.id == self.id_tabla):
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    if (y.id == elementoo.val):

                                        for validacion in y.validaciones:
                                            validacion: CampoValidacion
                                            print("VALIDACIONES CAMPO >>>>"+str(validacion.id)+"<->"+str(validacion.valor))
                                    else:
                                        print("")
                            else:
                                print("")

                elif isinstance(elementoo,constraintTabla):




                    for elemento2 in ts_global.Tablas:

                        x: CreateTable = ts_global.obtenerTabla(elemento2)
                        if (x.id == self.id_tabla):

                            for ele in x.cuerpo:

                                y: CampoTabla = ele

                                if (y.id == elementoo.val):

                                    for validacion in y.validaciones:
                                        validacion:constraintTabla

                                        validacion.valor      = None
                                        validacion.id         = None
                                        validacion.condiciones= None
                                        validacion.listas_id  = None
                                        validacion.referencia = None
                                        validacion.idRef      = None


                                        imprir("ALTER TABLE: CONSTRAINT ELIMINADO CORRECTAMENTE")
                                else:
                                    print("")
                        else:
                            print("")


                    for elemento2 in ts_global.Tablas:
                        x: CreateTable = ts_global.obtenerTabla(elemento2)

                        if (x.id == self.id_tabla):
                            for ele in x.cuerpo:
                                y: CampoTabla = ele

                                if (y.id == elementoo.val):
                                    for validacion in y.validaciones:
                                        validacion:constraintTabla
                                        var="VALIDACIONES CAMPO >>>>"+str(validacion.valor)+str(validacion.id)+str(validacion.condiciones )+str(validacion.listas_id  )+str(validacion.referencia  )+str(validacion.idRef)
                                        print(var)
                                else:
                                    print("")
                        else:
                            print("")
                else:
                    imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            # colocar error semantico

class Alter_table_Alter_Column_Set(Instruccion):
    def __init__(self, id_table, id_column):
        self.id_tabla = id_table
        self.id_column = id_column
    def Ejecutar(self):
        print(">>>>> SI HACE EL COLUMN SET")
        global ts_global, baseActual
        global LisErr

        r = ts_global.obtenerBasesDatos(baseActual)  # buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_tabla)

            if r2 is not None:
                print("!!! SI EXISTE TABLA ALTER TABLE SET COLUMN")
                elementoo = self.id_column

                if isinstance(elementoo, ExpresionValor):

                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if x.id == self.id_tabla:
                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    print(y.id + "<<<<COLUMN SETT SI ENTRA....")
                                    if (y.id == elementoo.val):

                                        bandera = False
                                        for validacion in y.validaciones:
                                            validacion:CampoValidacion

                                            if validacion.id == "NOT" and validacion.valor=="NULL":
                                                imprir("ALTER TABLE: YA TIENE LA VALIDACION NOT NULL")
                                                bandera= True

                                        if(bandera==False):
                                            # Se ingreso correctamente el valor
                                            # validar que exista ese esa columna en alguna tabla
                                            temporal2 = constraintTabla("NOT NULL", "not_null_n", None, self.id_column.val, None, self.id_tabla)
                                            ts_global.agregarValidacion(temporal2)

                                            # EN LA TABLA PEDIDA QUE ES elemento2.val
                                            laTabla: CreateTable = ts_global.obtenerTabla(self.id_tabla)

                                            y.validaciones.append(temporal2)
                                            imprir("ALTER TABLE: SE SETEO NOT NULL CORRECTAMENTE")
                                    else:
                                        print("")

                            else:
                                print("")


                        for elemento2 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento2)

                            if x.id == self.id_tabla:

                                for ele in x.cuerpo:
                                    y: CampoTabla = ele
                                    if (y.id == elementoo.val):

                                        for validacion in y.validaciones:
                                            validacion: CampoValidacion
                                            print("VALIDACIONES CAMPO >>>>"+str(validacion.id)+"<->"+str(validacion.valor))
                                    else:
                                        print("")
                            else:
                                print("")
                else:
                    imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            # colocar error semantico


class Alter_table_Add_Foreign_Key(Instruccion):
    def __init__(self, id_table, id_column, id_column_references, idforeign):
        self.id_table = id_table
        self.id_column = id_column
        self.idforeign = idforeign
        self.id_column_references = id_column_references


    def Ejecutar(self):
        print("por que entra aca.")
        #Verificar que existe la base de datos
        #Verificar que existe la tabla
        #Verificar que existe la columna en la tabla
        global ts_global, baseActual
        global LisErr
        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)
            print(self.id_table)



            if r2 is not None:
                    elemento       = self.id_column
                    elemento2      = self.id_column_references
                    tipoReferencia = ""

                    if isinstance(elemento,ExpresionValor) and isinstance(elemento,ExpresionValor):
                        bandera = False
                        bandera2 = False


                        for elemento22 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento22)

                            if x.id == self.id_table:
                                for ele in x.cuerpo:
                                    if isinstance(ele, constraintTabla):
                                        pass
                                    else:
                                        y: CampoTabla = ele

                                        if y.id != elemento2.val:
                                            bandera=True
                                        if y.id == elemento.val:
                                            bandera2=True
                                            tipoReferencia=y.tipo


                                if (bandera==True) and (bandera2 ==True):
                                        # Se ingreso correctamente el valor
                                        #validar que exista ese esa columna en alguna tabla

                                        #### PRUEBA CAMBIO A INSERTAR TIPO CONSTRAIN AL CUERPO DE LA TABLA
                                        temporal2 = constraintTabla("FOREIGN KEY", self.idforeign, None, elemento.val, None, self.id_table)
                                        ts_global.agregarValidacion(temporal2)

                                        print(ts_global.Validaciones)

                                        #EN LA TABLA PEDIDA QUE ES elemento2.val
                                        laTabla:CreateTable = ts_global.obtenerTabla(self.id_table)

                                        #por cada campo que tenga hasta que encontremos elemento.val
                                        for campo in laTabla.cuerpo:
                                            if isinstance(campo, constraintTabla):
                                                pass
                                            else:
                                                tt: CampoTabla = campo
                                                if elemento.val == tt.id:
                                                    tt.validaciones.append(temporal2)

                                        #r2.cuerpo.append(temporal)
                                        imprir("ALTER TABLE: En Hora Buena Se Ingreso la Llave Foranea Correctamente")
                                else:
                                    imprir("ALTER TABLE: No se Ejecuto la Accion ")
                            else:
                                print("")
                        else:
                            imprir("ALTER TABLE: La columna a insertar ya existe ")

                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            #colocar error semantico

class Alter_Table_Add_Constraint(Instruccion):
    def __init__(self, id_table, id_constraint, id_column):
        self.id_table = id_table
        self.id_constraint = id_constraint
        self.id_column = id_column

    def Ejecutar(self):
        global ts_global, baseActual
        global LisErr
        r  = ts_global.obtenerBasesDatos(baseActual)  #buscamos en el diccionario de la base de datos
        if r is not None:

            r2:CreateTable = ts_global.obtenerTabla(self.id_table)
            print(self.id_table)



            if r2 is not None:

                    elemento       = self.id_constraint
                    elemento2      = self.id_column

                    tipoReferencia = ""


                    if isinstance(elemento,ExpresionValor) and isinstance(elemento,ExpresionValor):


                        bandera = False
                        bandera2 = False

                        for elemento22 in ts_global.Tablas:
                            x: CreateTable = ts_global.obtenerTabla(elemento22)

                            if x.id == self.id_table:

                                for ele in x.cuerpo:
                                    y: CampoTabla = ele

                                    if y.id == elemento2.val:
                                        bandera=True
                                        tipoReferencia = y.tipo

                                    if y.id != elemento.val:
                                        bandera2=True

                                if (bandera==True) and (bandera2 ==True):
                                        # Se ingreso correctamente el valor
                                        #validar que exista ese esa columna en alguna tabla
                                        temporal2 = constraintTabla("UNIQUE",self.id_constraint.val,None, elemento.val, None, self.id_table)
                                        ts_global.agregarValidacion(temporal2)

                                        # EN LA TABLA PEDIDA QUE ES elemento2.val
                                        laTabla: CreateTable = ts_global.obtenerTabla(self.id_table)

                                        # por cada campo que tenga hasta que encontremos elemento.val
                                        for campo in laTabla.cuerpo:
                                            if isinstance(campo, constraintTabla):
                                                pass
                                            else:
                                                tt: CampoTabla = campo
                                                if elemento.val == tt.id:
                                                    tt.validaciones.append(temporal2)
                                        imprir("ALTER TABLE: En Hora Buena Se Ingreso El Constraint UNIQUE")

                                else:
                                    imprir("ALTER TABLE: No se Ejecuto la Accion ")
                            else:
                                print("")
                    else:
                        imprir("ALTER TABLE: ERROR DE TIPO")
            else:
                imprir("ALTER TABLE:   La tabla no existe!   ")
        else:
            imprir("ALTER TABLE:   La Base de datos no existe")
            #colocar error semantico

class useClase(Instruccion):
    def __init__(self,id):
        self.id = id

    def Ejecutar(self):
        imprir("USE: Se usara la base de datos " + str(self.id))


class DatoTipo(Instruccion):
    def __init__(self, bd, tipo, valor):
        self.bd = bd
        self.tipo = tipo
        self.valor = valor
