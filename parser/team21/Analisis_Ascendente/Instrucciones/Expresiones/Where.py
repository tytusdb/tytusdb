import  math
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion,IdId
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Time import Time
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.expresion import *
import Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica as Trigonometrica
import Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math as  Math_

class Where(Instruccion):
    '''#1 not boolean
       #2 in
       #3 between
       #4 ilike
       #5 like
       #6 comparison
       #7 is not distinct
       #8 is distict
       #9 not in
       #10 not exists
       #11 exists'''
    def __init__(self, caso, boolean, columna, listaValores, valor1, valor2, comparison, fila, poscolumna):
        self.caso = caso
        self.boolean = boolean
        self.columna = columna
        self.listaValores = listaValores
        self.valor1 = valor1
        self.valor2 = valor2
        self.comparison = comparison
        self.fila = fila
        self.poscolumna = poscolumna

    #para la produccion comparisonP se usaran casos
    '''#1 IS TRUE
       #2 IS FALSE
       #3 IS UNKNOWN
       #4 IS NOT TRUE
       #5 IS NOT FALSE
       #6 IS NOT UNKNOWN
       #7 IS NULL
       #8 IS NOT NULL
       #9 NOTNULL
       #10 ISNULL'''

    def Resolver(where,Exceptions, Consola,DataSelect):


        if( isinstance(where,Where)):
            if where.caso == 1:
                # not boolean
                print('not boolean')
            elif where.caso == 2:
                #in
                listavalores=[]
                nombreCampo  = Where.ObtenerNombreCampo(where)

                print('nombreCampito22---'+nombreCampo)
                datos = []
                for val in where.listaValores:
                    if(isinstance(val,Primitivo)):
                        listavalores.append(val.valor)
                    elif(isinstance(val, Time)):
                        listavalores.append(str(val))
                num = Where.ColumnasRepetidas(DataSelect, nombreCampo)
                if  num  == 1: # existe y no hay campos repetidos no hay ambigüedad
                    datos = Where.ObtenerDatos(DataSelect, nombreCampo)
                    print('datitos')
                    print(datos)
                    #procedemos a comparar cada registro con la lista de comparacion
                    filas = Where.filtrarLista(datos,listavalores)
                    print('filaaaaaaaas')
                    print (filas)
                    return [True,filas]
                elif num == 0:
                    Exceptions.append('No existe campo ' + nombreCampo)
                    return [False,'No existe campo ' + nombreCampo ]
                else:
                    Exceptions.append ('Existe ambigüedad en el campo '+ nombreCampo)
                    return [False, 'Existe ambigüedad en el campo '+ nombreCampo]





    def ColumnasRepetidas(DataSelect,column):
        contador=0
        for columna in DataSelect:
            if str(columna[0]) == column:
                contador = contador + 1
        return contador



    def ObtenerDatos(DataSelect,column):
        # habria que buscar la columna en el arreglo que le mando desde el select
        for columna in DataSelect:
            if str(columna[0]) == column:
                print('BUSCAR COLUMNA')
                print(columna[0])
                return columna[1]
        return []


    def ObtenerNombreCampo(where):
        if isinstance(where.columna,Id):
            return str(where.columna.id)
        elif isinstance(where.columna,IdId):
            id=''
            if isinstance(where.columna.id1, Id):
                id = where.columna.id1.id

            if isinstance(where.columna.id2, Id):
                id = id +'.'+ where.columna.id2.id

            return id

    def filtrarLista(Datos,listaValores):
        cont =-1;
        filas = []
        for dato in Datos:
            if dato in listaValores:
                filas.append(cont+1) #para saber que filas o registros son los que se mostarán al final
            cont = cont + 1
        return filas

