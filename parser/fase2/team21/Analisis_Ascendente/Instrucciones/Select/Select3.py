from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select as Select
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.select import GroupBy,Having
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Time import  Time
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import  *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import  Trigonometrica
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.IdAsId import  IdAsId,Id,IdId
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import  Math_
from prettytable import PrettyTable
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Where as Where
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion

class Selectp4(Instruccion):

    def ejecutar(Select,ts,Consola, Exceptions,mostrar):




        tablasRef = {}
        cont=0
        x = PrettyTable()
        x.clear()
        en=[]
        DataSelect=[]
        DataSelectInicial= []
        columnasT = len(Select.columnas)
        Error = False;
        if (ts.validar_sim("usedatabase1234") == 1 and cont <= columnasT):

            simboloBD = ts.buscar_sim(ts.buscar_sim("usedatabase1234").valor)
            resultado = FROM(Select, tablasRef, Exceptions, DataSelectInicial,simboloBD.id,(simboloBD.Entorno).simbolos)  # leemos las tablas

            if resultado[0]:
                DataSelectInicial= resultado[3]
                #print(DataSelectInicial)
                DataSelectInicial = EvaluarWhere(ts, Select, DataSelectInicial, Exceptions, Consola,tablasRef,(simboloBD.Entorno).simbolos)

                DataAux = DataSelectInicial.copy()
                DataSelectInicial=[]

                for i in range(len(DataAux[0])):
                    columnas = []
                    for fila in DataAux[1]:
                        columnas.append(fila[i])
                    DataSelectInicial.append([str(DataAux[0][i][0]),columnas,str(DataAux[0][i][1])])
            else:
                Error = True



        for i in tablasRef.items():
            print(i)
        for columna in Select.columnas:
            #print('what -- ' + str(len(Select.columnas)))
            Permutar = False

            if (ts.validar_sim("usedatabase1234")==1 and cont<=columnasT):
                cont=cont+1
                simboloBD = ts.buscar_sim(ts.buscar_sim("usedatabase1234").valor)
                #print(simboloBD.id)
                entornoBD = simboloBD.Entorno
                listado_tablas = entornoBD.simbolos
                listadoCampo = {}




                if resultado[0]: #si vienen valores de ids de tablas validos

                    if not Error:

                        if isinstance(columna, str):  # todos los campitos es decir *
                            DataSelect = DataSelectInicial

                        elif isinstance(columna, Id):
                            nombreCampo = columna.id
                            #print('campo'+nombreCampo)

                            Frecuencia = CamposRepetidos(tablasRef,Exceptions,listado_tablas,nombreCampo)
                            #print('Frecuencia <<<->>>'+str(Frecuencia))
                            if (Frecuencia == 1):
                                referencia = BuscarCampoTablas(tablasRef, Exceptions, listado_tablas, nombreCampo)
                                #print(referencia)
                                DataSelectAux=[]
                                if(referencia[0]):#quiere decir que existe en una de las tablas del from
                                    columna = ExtraerColumna(DataSelectInicial,nombreCampo,referencia[1],tablasRef)
                                    #print(columna)
                                    if columna[0]:
                                        DataSelect.append(columna[1])
                                    #x.add_column(nombreCampo,columna)
                            elif Frecuencia == 0 :
                                Exceptions.append(
                                    'Error semantico - 42703 -no existe la columna, error en ' + ' - ' + str(Select.fila) + ' - ' + str(Select.columna) + '')
                                print('No existe campo en tablas de referencia')
                                Error = True
                                break;
                            else:
                                Exceptions.append(
                                    'Error semantico - 42702 -la referencia a la columna es ambigua, error en ' + ' - ' + str(Select.fila) + ' - ' + str(Select.columna) + '')
                                print('Existe ambigüedad en campos de tablas de referencia campo'+ nombreCampo)
                                Error = True
                                break;



                        elif isinstance(columna, IdId): #cuando viene con puntito id.id la columna
                            nombreCampo = columna.id2
                            #print( 'campito bebé-->'+str(nombreCampo))

                            if isinstance(columna.id1,Id):
                                nombreTabla = columna.id1.id #alias de la tabla
                                if isinstance(columna.id2,Id) :
                                    nombreCampo = columna.id2.id


                                    Tabla = existeAliasTabla(tablasRef,nombreTabla) #nombre de tabla con ese alias

                                    if Tabla[0]: # existe un alias para una tabla en ese select

                                        if nombreCampo == '*':

                                            en = []
                                            ContT = []
                                            ContT = encabezados(str(Tabla[1]), tablasRef, listado_tablas, en)
                                            #DataJson = extractTable(simboloBD.id, str(Tabla[1]))

                                            for enca in ContT[2]:
                                                Frecuencia = CamposRepetidos(tablasRef, Exceptions, listado_tablas,enca)
                                                if Frecuencia > 1:
                                                    columna = ExtraerColumna(DataSelectInicial, nombreTabla+'.'+enca, str(Tabla[1]),tablasRef)
                                                elif Frecuencia==1:
                                                    columna = ExtraerColumna(DataSelectInicial, enca,str(Tabla[1]), tablasRef)
                                                if columna[0]:
                                                    DataSelect.append(columna[1])

                                            #DataSelect = agregarData(x, DataJson, ContT[0], ContT[2], DataSelect, nombreTabla,
                                            #                           Permutar, str(Tabla[1]))

                                        else:
                                            referencia = existeCampo(nombreCampo,(listado_tablas.get(Tabla[1]).Entorno).simbolos)
                                            DataSelectAux = []
                                            if (referencia[0]):  # quiere decir que existe en una de las tablas del from

                                                Frecuencia = CamposRepetidos(tablasRef, Exceptions, listado_tablas,nombreCampo)

                                                if Frecuencia>1: #buscarlo con alias
                                                    columna = ExtraerColumna(DataSelectInicial,
                                                                             nombreTabla + '.' + nombreCampo,
                                                                             str(Tabla[1]), tablasRef)
                                                else:#buscar solo el nombre del campo
                                                    columna = ExtraerColumna(DataSelectInicial,
                                                                             nombreCampo,
                                                                             str(Tabla[1]), tablasRef)
                                                if columna[0]:
                                                    DataSelect.append(columna[1])


                                            else:
                                                Exceptions.append(
                                                    'Error semantico - 42703 -no existe la columna, error en ' + ' - ' + str(Select.fila) + ' - ' + str(Select.columna) + '')
                                                print('no existe campo  en tabla' + Tabla[1])
                                                Error = True
                                                break;

                                    else:
                                        Exceptions.append(
                                            'Error semantico - 42P01 -falta una entrada para la tabla en la cláusula FROM, error en ' + ' - ' + str(Select.fila) + ' - ' + str(Select.columna) + '')
                                        print('no existe tabla con ese alias' + nombreTabla)
                                        Error = True
                                        break;

                            else:
                                Exceptions.append(
                                    'Error semantico - 42P01 -tipo invalido de id campo , error en ' + ' - ' + str(Select.fila) + ' - ' + str(Select.columna) + '')

                                Error = True
                                break;
                        else:
                            if isinstance(columna,Math_) and  not isinstance(Select.complementS,GroupBy) and len(Select.columnas)==1:

                                if(columna.nombre == 'COUNT' ) :

                                    if isinstance(columna.E1,Id): #para que no de error de tipos de la Expresion1
                                        if str(columna.E1.id)=='*':
                                            if len(DataSelectInicial)>0: #verifico que ya hayan datos en la DataFiltrada
                                                contador= str(len(DataSelectInicial[0][1]))
                                                encab = 'COUNT(*)'
                                                DataSelect = [[encab,contador]]
                                                #print(DataSelectInicial)
                                else:
                                    val=OpAgregacion(Select,columna,DataSelectInicial,tablasRef,Exceptions,listado_tablas)
                                    #print('probando')
                                    #print(val)
                                    if(val[0]):
                                        DataSelect = [val[1]]
                                        #print(DataSelect)


                            elif isinstance(columna,Time):
                                print()

                    else:
                        Error = True
                        break
                else:
                    Error = True
                    break
            else:
                print("no se seleciona una bd")

        if (not Error):

            for i in DataSelect:
                columna=[]
                for row in i[1]:
                    columna.append(row)
                x.add_column(i[0],columna)

            if mostrar:
                Consola.append('\n' + x.get_string() + '\n')

            DataSelectFilas=[]

            enc=[]
            try:
                for  i in range(len(DataSelect[0][1])):
                    fila = []
                    enc = []
                    for columna in DataSelect:
                        fila.append(columna[1][i])
                        enc.append(columna[0])
                    DataSelectFilas.append(fila)

                DataSelectAux=[]
                DataSelectAux.append(enc)
                DataSelectAux.append(DataSelectFilas)
                #print('LO QUE RETORNA--><3')
                #print(DataSelectAux)
            except:
                DataSelectAux=[]

            return DataSelectAux

    def traducir(Sel, ts, consola, lista, tv):
        # iniciar traduccion
        # iniciar traduccion
        info = ""  # info contiene toda el string a mandar como parametros

        # print("concatena \n")
        # print(Select.concatena)

        for data in Sel.concatena:

            info += " " + data
        print('concatena' + str(Sel.concatena))

        info = obtenerTraduccion2(Sel, ts, consola, lista, tv)

        # info = Sel.concatena[0]
        contador = tv.Temp()
        consola.append(f"\n\t{contador} = f\"{info}\"")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")


def obtenerTraduccion2(Sel,ts,consola, lista,tv):
    fromt = Select.select.Select.obtenerCadenaInner(Sel.inner, lista)
    order = ''
    subq = ''

    where = ''
    where = ' WHERE ' + str(Select.select.Select.obtenerCadenaWhere(Sel.complementS, lista)) + ' '
    if Sel.orderby != None:
        order = ' ORDER BY ' + str(Select.select.Select.obtenerCadenalistColumn(Sel.orderby, lista)) + ' '

    if Sel.subquery != None and Sel.subquery.caso != 4:
        subq = '( ' + (Sel.subquery).concatena[0].replace(";", "") + ' ) '

    if isinstance(Sel.columnas, str):
        info = (f"SELECT  * FROM  {subq}{fromt} {where}{order};")
    else:
        cols = Select.select.Select.obtenerCadenalistColumna(Sel.columnas, lista)

        info = (f"SELECT  {cols} FROM  {subq}{fromt}{where}{order};")
    # t[0] = Select(5, False, None, t[2], t[4], t[5], t[8], t[9], t[7], concatenaTime, lexer.lineno, columna)
    return info



def existeTabla(listadoTablas,tablaBuscar):

        for tablita in listadoTablas:
            if listadoTablas.get(tablita).id == tablaBuscar:
                return True
        return  False


def existeAliasTabla(tablasRef, Alias):

    for k in tablasRef.keys():
        if k == Alias:
            return [True, tablasRef.get(k)]
    return [False,False]

def encabezados(tablaR,tablasRef,listado_tablas,en):

        contadorCampos = 0
        campos = []

        for elemento in listado_tablas: #tablas en ts

            if listado_tablas.get(elemento).id == tablaR:
                entornoTabla = listado_tablas.get(elemento).Entorno
                lista_campos = entornoTabla.simbolos
                for campito in lista_campos:
                    nombreCampo = str(lista_campos.get(campito).id)
                    enc = ''
                    if nombreCampo in en:
                        for k in tablasRef.keys():
                            if tablasRef.get(k) == tablaR:
                                enc = k
                                break

                        en.append(enc + '.' + nombreCampo)
                        campos.append(nombreCampo)

                    else:
                        en.append(nombreCampo)
                        campos.append(nombreCampo)
                    contadorCampos = contadorCampos + 1

                return [contadorCampos,campos,en]
        return  [0,campos,en]

def ActualizarTabla(x,DataJson,rango,en,DataSelect3, alias):
    filas = len(DataJson)
    #print('filas nueva tabla'+str(filas))
    DataSelectAux =[]
    row = []

    for columna in DataSelect3: #3
        row = []

        for fila in columna[1]: #2
            for i in range(filas):
                row.append(str(fila))
        DataSelectAux.append([str(columna[0]),row,columna[2]])

    return DataSelectAux




def agregarData(x,DataJson,rango,en,DataSelect3,alias,Permutar,tabla):

    if Permutar:
        for i in range(rango):
            columna = []
            #print(len(DataSelect3[0][1]))
            if(len(DataJson)>0):
                for j in range(int(len(DataSelect3[0][1])/len(DataJson))):
                    for row in DataJson:
                        columna.append(row[i])
            if alias != None:
                DataSelect3.append([alias+'.'+en[i], columna,tabla])
            else:
                DataSelect3.append([en[i], columna, tabla])

        return DataSelect3

    else:
        for i in range(rango):
            columna = []
            for column in DataJson:
                columna.append(column[i])
            if alias != None:
                DataSelect3.append([alias + '.' + en[i], columna, tabla])
            else:
                DataSelect3.append([en[i], columna, tabla])
            #x.add_column(en[i], columna)

        return  DataSelect3

        #x.add_column(en[i], columna)


def FROM(Select,tablasRef,Exceptions,DataSelectInicial,BD,listado_tablas):
    if Select.subquery != None:  # resolver subquery primero que de aca saldrían los datos
        print('what -- ' + type(Select.subquery).__name__)
    else:  # las tablas vendrían en inner
        for tablas in Select.inner:  # nada mas obteniendo los id de las tablas solicitadas
           # print('tablas55555 -- ' + tablas.id1.id)
            if isinstance(tablas, Id):
                tablasRef[str(tablas.id)] = tablas.id
            elif isinstance(tablas, IdAsId):
                if isinstance(tablas.id1, Id) and isinstance(tablas.id2, Id):

                    if str(tablas.id2.id) in tablasRef.keys():
                        Exceptions.append(
                            'Error semantico - 42712 -  el nombre de tabla  fue especificado más de una vez, error en ' + ' - ' + str(Select.fila) + ' - ' + str(Select.columna) + '')

                        #print('alias repetidos-->'+ tablas.id2.id)
                        return [False,tablasRef]
                    tablasRef[str(tablas.id2.id)] = str(tablas.id1.id)
                else:
                    Exceptions.append(
                        'Error semantico - 42712 -  alias de tipo invalidos, error en ' + ' - ' + str(Select.fila) + ' - ' + str(Select.columna) + '')
                    return [False,tablasRef]

        Error = False
        for k in tablasRef.keys():
            if not existeTabla(listado_tablas, tablasRef.get(k)):
                Exceptions.append(
                    f'Error semantico - 42P01 - no existe la relación, error en  - {Select.fila} - {Select.columna}')
                Error = True
                break;
        if not Error:
            cont22 = 0
            NombreAnterior = ''
            Permutar =False
            encabezaditos=[]
            for k in tablasRef.keys():
                if cont22 > 0:
                    Permutar = True
                    DataAux = []
                    DataAux = DataSelectInicial.copy()
                    DataSelect = []
                    DataJson = extractTable(BD, tablasRef.get(k))
                    #DataJson = DataSelectInicial.get(tablasRef.get(k))
                    DataSelectInicial = ActualizarTabla(None, DataJson, Contt[0], Contt[2], DataAux, None)
                    #print("sad-->" + str((DataSelectInicial)))

                en = []
                Contt = []
                Contt = encabezados(tablasRef.get(k), tablasRef, listado_tablas, en)
                # listadoCampo[tablasRef.get(k)] = Cont
                DataJson= extractTable(BD,tablasRef.get(k))
                #DataJson = DataSelectInicial.get(tablasRef.get(k))
                encaAux=[]
                #print(listado_tablas)
                for enca in Contt[2]:
                    Frecuencia = CamposRepetidos(tablasRef, Exceptions, listado_tablas, enca)

                    if Frecuencia>1 and k != tablasRef.get(k):
                        encaAux.append(k+'.'+enca)
                    else:
                        encaAux.append(enca)

                DataSelectInicial = agregarData(None, DataJson, Contt[0], encaAux, DataSelectInicial, None, Permutar, tablasRef.get(k))
                cont22 = cont22 + 1
                #print('agregar---' + str(DataSelectInicial))

            return [True,tablasRef,Exceptions,DataSelectInicial]
        else:
            return [False, tablasRef, Exceptions, DataSelectInicial]


def BuscarCampoTablas(tablasRef,Exceptions,listado_tablas,campobuscar):
    for ref in tablasRef.keys():
        entornoTabla = listado_tablas.get(tablasRef.get(ref)).Entorno
        lista_campos = entornoTabla.simbolos
        contadorPosicion= 0

        for campo in lista_campos:
            if campobuscar == lista_campos.get(campo).id:
                return [True,tablasRef.get(ref),contadorPosicion]
            contadorPosicion = contadorPosicion + 1
    return [False,False,False]

def ObtenerTipoCampo(tablasRef,Exceptions,listado_tablas,campobuscar,tabla):
    for ref in tablasRef.keys():
        entornoTabla = listado_tablas.get(tablasRef.get(ref)).Entorno
        lista_campos = entornoTabla.simbolos

        for campo in lista_campos:
            if campobuscar == lista_campos.get(campo).id and tablasRef.get(ref) == tabla:
                tipo = lista_campos.get(campo).tipo
                tipo=str(tipo).split("-")
                tip=str(str(tipo[0]).strip())#1 INT #2 FLOAT #3 STRING INVALIDO
                #print('esto')
                #print(tip)
                if tip == 'SMALLINT' or tip=='INTEGER' or tip=='BIGINT':
                    tip=1
                elif tip=='DECIMAL' or tip=='NUMERIC' or tip=='REAL' or tip=='DOUBLE' or tip=='MONEY':
                    tip=2
                else:
                    tip = 3
                return [True, tip]
    return [False,False]

def CamposRepetidos(tablasRef,Exceptions,listado_tablas,campobuscar):

    contador = 0
    for ref in tablasRef.keys():
        #print(tablasRef.get(ref))
        entornoTabla = listado_tablas.get(tablasRef.get(ref)).Entorno
        lista_campos = entornoTabla.simbolos


        for campo in lista_campos:
            if campobuscar == lista_campos.get(campo).id:
                contador = contador + 1
    return contador

def existeCampo(nombreCampo,lista):
    contador = 0
    for campo in lista:
        if nombreCampo == lista.get(campo).id:
            return [True,contador]
        contador += 1
    return [False,contador]


def EvaluarWhere(ts,Select,DataSelect,Exceptions,Consola,tablasRef,listado_tablas):
    #print(type(Select.complementS).__name__)
    #print(DataSelect)
    l = []
    filas=[False,[]]
    if isinstance(Select.complementS,Where.Where) or isinstance(Select.complementS,Expresion.Expresion):
        filas = Where.Where.Resolver(Select.complementS,ts,Exceptions,Consola,DataSelect,tablasRef, listado_tablas)

    elif isinstance(Select.complementS,GroupBy):
        filas = Where.Where.Resolver(Select.complementS.listaC, ts, Exceptions, Consola, DataSelect,tablasRef, listado_tablas)
    '''for c in DataSelect:
        l.append(str(c[0]))
    x.field_names= l'''
    #print(filas)
    DataSelectAux = []
    row = []
    if filas[0] and filas[1]!=None and len(filas[1])>0:
        registros=[]
        columnas=[]
        for i in filas[1]:

            registros=[]
            columnas=[]
            for column in DataSelect:

                registros.append(column[1][i])
                columnas.append([column[0],column[2]])
            row.append(registros)
            #x.add_row(registros)

        #print('rows')
        #print(row)
        return [columnas,row]
    else:
        #print(filas[1])
        columnas=[]
        for column in DataSelect:
            columnas.append([column[0],column[2]])
        return [columnas,[]]



def PermutarData(DataSelect3, DataSelectAux):

    if len(DataSelect3)>0: # hay más entonces
        # buscar si hay una columna de la misma tabla
        veces =-1
        columnaAux = []
        contcolumna=0
        for columna in DataSelect3:
            if columna[2] == DataSelectAux[2]:
                if len(DataSelectAux[1])>0:
                    veces = int(len(columna[1])/len(DataSelectAux[1]))

                break;
            contcolumna = contcolumna + 1
        #print('veces' + str(veces))
        if veces>0:

            if DataSelect3[contcolumna][1][0] == DataSelect3[contcolumna][1][1]:
                for row in DataSelectAux[1]:
                    for i in range(veces):
                        columnaAux.append(row)
                DataSelect3.append([DataSelectAux[0],columnaAux,DataSelectAux[2]])
            else:
                for i in range(veces):
                    for row in DataSelectAux[1]:
                        columnaAux.append(row)
                DataSelect3.append([DataSelectAux[0], columnaAux, DataSelectAux[2]])
            return DataSelect3

        else:
            DataSelect3 = ActualizarTabla(None,DataSelectAux[1],None,None,DataSelect3,None) # permutado la data existente hasta el momento

            columna = []
            #print(len(DataSelect3[0][1]))
            if len(DataSelectAux[1])>0:
                for j in range(int(len(DataSelect3[0][1]) / len(DataSelectAux[1]))):
                    for row in DataSelectAux[1]:
                        columna.append(row)
            DataSelect3.append([DataSelectAux[0], columna, DataSelectAux[2]])
            return  DataSelect3


    else:
        #print('lo que llega')
        #print(DataSelectAux)
        DataSelect3.append([DataSelectAux[0],DataSelectAux[1],DataSelectAux[2]])
        return DataSelect3


def ExtraerColumna(DataSelect3,campo,tabla, tablasRef):

    for columna in DataSelect3:
        if str(columna[0])==campo and str(columna[2])== tabla:
            return [True,columna]
    return [False,[]]


#----------------------------------------------------------------------------------------------------------------
def OpAgregacion(Select,columna,DataSelect3,tablasRef,Exceptions,listado_tablas):
    Error=False
    valores=[]
    valoresAux=[]
    if isinstance(columna,Math_):
        if isinstance(columna.E1, Id):
            nombreCampo = columna.E1.id
            #print('campo' + nombreCampo)

            Frecuencia = CamposRepetidos(tablasRef, Exceptions, listado_tablas, nombreCampo)
            #print('Frecuencia <<<->>>' + str(Frecuencia))
            if (Frecuencia == 1):
                referencia = BuscarCampoTablas(tablasRef, Exceptions, listado_tablas, nombreCampo)
                #print(referencia)
                DataSelectAux = []
                if (referencia[0]):  # quiere decir que existe en una de las tablas del from referencia[1] contiene el nombre de la tabla
                    columnaa = ExtraerColumna(DataSelect3, nombreCampo, referencia[1], tablasRef)
                    tipo = ObtenerTipoCampo(tablasRef,Exceptions,listado_tablas,nombreCampo,referencia[1]) #1 INT #2 FLOAT #3 STRING INVALIDO

                    if columnaa[0]:
                        valoresAux=[]
                        #valores = columnaa[1][1]
                        if tipo[1] == 1:#convertir a int
                            for val in columnaa[1][1]:
                                valoresAux.append(int(float(val)))
                        elif tipo[1]==2: # convertir a float
                            for val in columnaa[1][1]:
                                valoresAux.append(float(val))
                        else:
                            Exceptions.append(
                                'Error semantico - 42883 -Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos. ' + ' - ' + str(
                                    Select.fila) + ' - ' + str(
                                    Select.columna) + '')
                            print('Error semantico - 42883 -Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos.')
                            Error = True
                            return [False, [[]]]



            elif Frecuencia == 0:
                Exceptions.append(
                    'Error semantico - 42703 -no existe la columna, error en ' + ' - ' + str(Select.fila) + ' - ' + str(
                        Select.columna) + '')
                print('No existe campo en tablas de referencia')
                Error = True
                return [False,[[]]]
            else:
                Exceptions.append(
                    'Error semantico - 42702 -la referencia a la columna es ambigua, error en ' + ' - ' + str(
                        Select.fila) + ' - ' + str(Select.columna) + '')
                print('Existe ambigüedad en campos de tablas de referencia campo' + nombreCampo)
                Error = True
                return [False,[[]]]

        elif isinstance(columna.E1, IdId):  # cuando viene con puntito id.id la columna
            nombreCampo = columna.E1.id2
            #print('campito bebé-->' + str(nombreCampo))

            if isinstance(columna.E1.id1, Id):
                nombreTabla = columna.E1.id1.id  # alias de la tabla
                if isinstance(columna.E1.id2, Id):
                    nombreCampo = columna.E1.id2.id

                    Tabla = existeAliasTabla(tablasRef, nombreTabla)  # nombre de tabla con ese alias

                    if Tabla[0]:  # existe un alias para una tabla en ese select

                        referencia = existeCampo(nombreCampo, (listado_tablas.get(Tabla[1]).Entorno).simbolos)
                        DataSelectAux = []
                        if (referencia[0]):  # quiere decir que existe en una de las tablas del from

                            Frecuencia = CamposRepetidos(tablasRef, Exceptions, listado_tablas, nombreCampo)
                            columnaa=[]
                            tipo=-1
                            if Frecuencia > 1:  # buscarlo con alias
                                columnaa = ExtraerColumna(DataSelect3,
                                                             nombreTabla + '.' + nombreCampo,
                                                             str(Tabla[1]), tablasRef)

                                tipo = ObtenerTipoCampo(tablasRef, Exceptions, listado_tablas, nombreCampo,
                                                             str(Tabla[1]))  # 1 INT #2 FLOAT #3 STRING INVALIDO

                            else:  # buscar solo el nombre del campo
                                columnaa = ExtraerColumna(DataSelect3,
                                                             nombreCampo,
                                                             str(Tabla[1]), tablasRef)
                                tipo = ObtenerTipoCampo(tablasRef, Exceptions, listado_tablas,
                                                        nombreCampo,
                                                        str(Tabla[1]))  # 1 INT #2 FLOAT #3 STRING INVALIDO

                            if columnaa[0]:
                                valoresAux = []
                                # valores = columnaa[1][1]

                                if tipo[1] == 1:  # convertir a int
                                    for val in columnaa[1][1]:
                                        valoresAux.append(int(float(val)))
                                elif tipo[1] == 2:  # convertir a float
                                    for val in columnaa[1][1]:
                                        valoresAux.append(float(val))
                                else:
                                    Exceptions.append(
                                        'Error semantico - 42883 -Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos. ' + ' - ' + str(
                                            Select.fila) + ' - ' + str(
                                            Select.columna) + '')
                                    print(
                                        'Error semantico - 42883 -Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos.')
                                    Error = True
                                    return [False, [[]]]



                            else:
                                Exceptions.append(
                                    'Error semantico - 42703 -no existe la columna, error en ' + ' - ' + str(
                                        Select.fila) + ' - ' + str(Select.columna) + '')
                                print('no existe campo  en tabla' + Tabla[1])
                                Error = True
                                return [False,[[]]]

                    else:
                        Exceptions.append(
                            'Error semantico - 42P01 -falta una entrada para la tabla en la cláusula FROM, error en ' + ' - ' + str(
                                Select.fila) + ' - ' + str(Select.columna) + '')
                        print('no existe tabla con ese alias' + nombreTabla)
                        Error = True
                        return [False,[[]]]
            else:
                Exceptions.append(
                    'Error semantico - 42P01 -tipo invalido de id campo , error en ' + ' - ' + str(Select.fila) + ' - ' + str(
                        Select.columna) + '')

                Error = True
                return [False,[[]]]


        resultado=0
        if columna.nombre =='SUM':
            for i in valoresAux:
                resultado+= i
            return [True, ['SUM',[resultado]]]
        elif columna.nombre == 'AVG':
            for i in valoresAux:
                resultado += i
            promedio = resultado/len(DataSelect3)
            return [True, ['AVG', [promedio]]]
        elif columna.nombre == 'MAX':
            maxx = max(valoresAux)
            return [True,['MAX',[maxx]]]
        elif columna.nombre == 'MIN':
            minn= min(valoresAux)
            return [True,['MIN',[minn]]]

        return [True, valores]
