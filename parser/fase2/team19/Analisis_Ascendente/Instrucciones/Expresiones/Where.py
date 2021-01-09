import  math
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion,IdId
from Analisis_Ascendente.Instrucciones.Time import Time
from Analisis_Ascendente.Instrucciones.expresion import *
from Analisis_Ascendente.Instrucciones.Select.select import Select
import Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica as Trigonometrica
import Analisis_Ascendente.Instrucciones.Expresiones.Math as  Math_
from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from Analisis_Ascendente.Instrucciones.Select.select1 import  selectTime
import Analisis_Ascendente.Instrucciones.Select.Select2 as Selectp3
import Analisis_Ascendente.Instrucciones.Select.Select3 as Select3
from Analisis_Ascendente.Instrucciones.Select.selectInst import Select_inst

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

    def Resolver(where,ts,Exceptions, Consola,DataSelect):


        if isinstance(where,Where):
            if where.caso == 1:
                pass# not boolean
                #print('not boolean')
            elif where.caso == 2 or where.caso == 11:
                #in
                listavalores=[]
                nombreCampo  = Where.ObtenerNombreCampo(where)

                #print('nombreCampito22---'+nombreCampo)
                datos = []

                if isinstance(where.listaValores, Select):
                    #print('Select')
                    if(where.listaValores.caso== 1):
                        a = Time.resolverTime(where.listaValores.time)
                        listavalores.append(a)
                    elif (where.listaValores.caso == 3):
                        variable = Select_inst()
                        a = Select_inst.ejecutar(variable,where.listaValores, ts, Consola, Exceptions)
                        #print('valores sin filtrar Fredy')
                        #print(a)
                        for val in a:
                            listavalores.append(val[0])
                        #print(listavalores)
                    elif(where.listaValores.caso==4):
                        a = Selectp3.Selectp3.ejecutar(where.listaValores,ts,Consola,Exceptions,False)
                        #print(a)
                        for val in a[1]:
                            listavalores.append(val[0])
                        print (listavalores)
                    elif (where.listaValores.caso==5):
                        a = Select3.Selectp4.ejecutar(where.listaValores, ts, Consola, Exceptions,False)
                        #print('resultado')
                        for val  in a[1]:
                            listavalores.append(val[0])
                        #print(listavalores)


                else:
                    for val in where.listaValores:
                        if(isinstance(val,Primitivo)):
                            listavalores.append(val.valor)
                        elif(isinstance(val, Time)):
                            v = Time.resolverTime(val)
                            listavalores.append(str(v))
                num = Where.ColumnasRepetidas(DataSelect, nombreCampo)
                if  num  == 1: # existe y no hay campos repetidos no hay ambigüedad
                    datos = Where.ObtenerDatos(DataSelect, nombreCampo)
                    #print('datitos')
                    #print(datos)
                    #procedemos a comparar cada registro con la lista de comparacion
                    filas = Where.filtrarLista(datos,listavalores,Exceptions)
                    #print('filaaaaaaaas')
                    print (filas)
                    return [True,filas, DataSelect]
                elif num == 0:
                    Exceptions.append(
                        'Error semantico - 42703 -no existe la columna , error en ' + ' - ' + where.fila + ' - ' + where.columna + '')
                    return [False,'No existe la columna ' + nombreCampo ]
                else:
                    Exceptions.append(
                        'Error semantico - 42702 -la referencia a la columna es ambigua, error en ' + ' - ' + where.fila + ' - ' + where.columna + '')

                    return [False, 'Existe ambigüedad en el campo '+ nombreCampo]

            elif where.caso == 9 or where.caso==10: # Not in
                # in
                listavalores = []
                nombreCampo = Where.ObtenerNombreCampo(where)

                #print('nombreCampito22---' + nombreCampo)
                datos = []

                if isinstance(where.listaValores, Select):
                    #print('Select')
                    if (where.listaValores.caso == 1):
                        a = Time.resolverTime(where.listaValores.time)
                        listavalores.append(a)
                    elif (where.listaValores.caso == 3):
                        variable = Select_inst()
                        a = Select_inst.ejecutar(variable,where.listaValores, ts, Consola, Exceptions)
                        #print('valores sin filtrar Fredy')
                        #print(a)
                        for val in a:
                            listavalores.append(val[0])
                        #print(listavalores)
                    elif (where.listaValores.caso == 4):
                        a = Selectp3.Selectp3.ejecutar(where.listaValores, ts, Consola, Exceptions,False)
                        #print(a)
                        for val in a[1]:
                            listavalores.append(val[0])
                        #print(listavalores)
                    elif (where.listaValores.caso == 5):
                        a = Select3.Selectp4.ejecutar(where.listaValores, ts, Consola, Exceptions,False)
                        #print('resultado')
                        #print(a)
                        for val in a[1]:
                            listavalores.append(val[0])
                else:
                    for val in where.listaValores:
                        if (isinstance(val, Primitivo)):
                            listavalores.append(val.valor)
                        elif (isinstance(val, Time)):
                            v = Time.resolverTime(val)
                            listavalores.append(str(v))
                num = Where.ColumnasRepetidas(DataSelect, nombreCampo)
                if num == 1:  # existe y no hay campos repetidos no hay ambigüedad
                    datos = Where.ObtenerDatos(DataSelect, nombreCampo)
                    #print('datitos')
                    #print(datos)
                    # procedemos a comparar cada registro con la lista de comparacion
                    filas = Where.filtrarLista2(datos, listavalores,Exceptions)
                    #print('filaaaaaaaas')
                    #print(filas)
                    return [True, filas, DataSelect]
                elif num == 0:
                    Exceptions.append(
                        'Error semantico - 42703 -no existe la columna , error en ' + ' - ' + where.fila + ' - ' + where.columna + '')

                    return [False, 'No existe campo ' + nombreCampo]
                else:
                    Exceptions.append(
                        'Error semantico - 42702 -la referencia a la columna es ambigua, error en ' + ' - ' + where.fila + ' - ' + where.columna + '')

                    return [False, 'Existe ambigüedad en el campo ' + nombreCampo]
            elif where.caso == 6: ## comparison
                pass#print('comparison')
                #print(type(where.valor1).__name__)
        elif(isinstance(where,Expresion)):
            l=Where.ResolverExpresion(where,Exceptions,Consola,DataSelect)
            #print('AJAAA')
            #print(l)
            return [True,l]





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
                #print('BUSCAR COLUMNA')
                #print(columna[0])
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

    def filtrarLista(Datos,listaValores,Exceptions):

        ##print(type(listaValores[0]).__name__)
        cont =-1;
        filas = []

        listaInt=[]
        listaFloat=[]
        for i in listaValores:
            if isinstance(i,str):
                if i.isnumeric() or i.isdecimal():
                    listaFloat.append(float(i))

        for i in listaValores:
            if isinstance(i,str):
                if i.isnumeric() or i.isdecimal():
                    listaInt.append(int(i))
        for dato in Datos:
            ##print(type(dato).__name__)
            if isinstance(dato,int) and len(listaInt)>0:
                if dato in listaInt:
                    filas.append(cont + 1)  # para saber que filas o registros son los que se mostarán al final
            elif isinstance(dato,float) and len(listaFloat)>0:
                if dato in listaFloat:
                    filas.append(cont + 1)  # para saber que filas o registros son los que se mostarán al final
            else:
                if dato in listaValores:
                    filas.append(cont+1) #para saber que filas o registros son los que se mostarán al final
            cont = cont + 1
        return filas

    def filtrarLista2(Datos,listaValores,Exceptions):

        # #print(type(listaValores[0]).__name__)
        cont = -1;
        filas = []

        listaInt = []
        listaFloat = []
        for i in listaValores:
            if isinstance(i, str):
                if i.isnumeric() or i.isdecimal():
                    listaFloat.append(float(i))

        for i in listaValores:
            if isinstance(i, str):
                if i.isnumeric() or i.isdecimal():
                    listaInt.append(int(i))
        for dato in Datos:
            # #print(type(dato).__name__)
            if isinstance(dato, int) and len(listaInt) > 0:
                if not dato in listaInt:
                    filas.append(cont + 1)  # para saber que filas o registros son los que se mostarán al final
            elif isinstance(dato, float) and len(listaFloat) > 0:
                if not dato in listaFloat:
                    filas.append(cont + 1)  # para saber que filas o registros son los que se mostarán al final
            else:
                if not dato in listaValores:
                    filas.append(cont + 1)  # para saber que filas o registros son los que se mostarán al final
            cont = cont + 1
        return filas

    def ResolverExpresion(Expr,Consola,exception,DataSelect):

        if isinstance(Expr,Expresion):


            if str(Expr.operador).upper()=='AND':
                #print('and')
                exp1 = Where.ResolverExpresion(Expr.iz, Consola, exception, DataSelect)
                exp2 = Where.ResolverExpresion(Expr.dr, Consola, exception, DataSelect)

                cont =0;
                filas = []
                if isinstance(exp1,list) and isinstance(exp2,list):

                    for fila in exp1:
                        if fila in exp2:
                            filas.append(fila)
                    return filas

            elif str(Expr.operador).upper() == 'OR':
                #print('or')
                exp1 = Where.ResolverExpresion(Expr.iz, Consola, exception, DataSelect)
                exp2 = Where.ResolverExpresion(Expr.dr, Consola, exception, DataSelect)

                cont = 0;
                filas = []
                if isinstance(exp1, list) and isinstance(exp2, list):

                    for fila in exp1:
                        if not (fila in filas):
                            filas.append(fila)

                    for fila in exp2:
                        if not (fila in filas):
                            filas.append(fila)
                    return filas
            else:
                val1 = Where.ResolverExpresion(Expr.iz, Consola, exception, DataSelect)
                val2 = Where.ResolverExpresion(Expr.dr, Consola, exception, DataSelect)
                filas = []
                if isinstance(val1, list):
                    contPos= -1
                    for valor in val1:

                        if isinstance(valor,str):
                            if str(valor).isnumeric() or str(valor).isdecimal():
                                valor= float(valor)
                        prim= Primitivo(valor,Expr.fila,Expr.columna)

                        if isinstance(val2,list):


                            if isinstance(val2[contPos+1],str):
                                n = val2[contPos+1]
                                if str(n).isnumeric() or str(n).isdecimal():
                                    n = float(n)
                            else:
                                n= val2[contPos+1]

                            prim2 = Primitivo(n, Expr.fila, Expr.columna)
                            r = Expresion(prim, prim2, Expr.operador, Expr.fila, Expr.columna)
                            b = Expresion.Resolver(r, Consola, exception, DataSelect)
                            if isinstance(b, bool):
                                if b:
                                    filas.append(contPos + 1)
                        else:

                            r = Expresion(prim,val2,Expr.operador,Expr.fila,Expr.columna)
                            #print(type(r).__name__)
                            b = Expresion.Resolver(r,Consola,exception, DataSelect)

                            if isinstance(b,bool):
                                if b:
                                    filas.append(contPos+1)

                        contPos= contPos + 1
                    return filas






        elif isinstance(Expr,Primitivo):
            return Expr
        elif isinstance(Expr,Id):
            nombreCampo = Expr.id
            num = Where.ColumnasRepetidas(DataSelect, nombreCampo)
            if num == 1:  # existe y no hay campos repetidos no hay ambigüedad
                datos = Where.ObtenerDatos(DataSelect, nombreCampo)
                #print('datitos222')
                #print(datos)
                return datos
        elif isinstance(Expr,IdId):
            #print('id.id')
            nombreCampo = ''
            if isinstance(Expr.id1,Id):
                nombreCampo= Expr.id1.id

            if isinstance(Expr.id2,Id):
                nombreCampo = nombreCampo+'.'+ Expr.id2.id

            num = Where.ColumnasRepetidas(DataSelect, nombreCampo)
            if num == 1:  # existe y no hay campos repetidos no hay ambigüedad
                datos = Where.ObtenerDatos(DataSelect, nombreCampo)
                #print('datitos222')
                #print(datos)
                return datos
        elif isinstance(Expr,Math_.Math_):
            #print(Expr.nombre)
            a = Math_.Math_.Resolver(Expr,None,Consola,exception)
            #print(type(a).__name__)
            return  Primitivo(a,Expr.fila,Expr.columna)
        elif isinstance(Expr, Trigonometrica.Trigonometrica):
            a=  Trigonometrica.Trigonometrica.Resolver(Expr,None,Consola,exception)
            return Primitivo(a,Expr.fila, Expr.columna)
        elif isinstance(Expr, Time):
            return Time.resolverTime(Expr)
        elif isinstance(Expr, Where):
            a = Where.Resolver(Expr,None,Consola,exception,DataSelect)
            if isinstance(a[0],bool):
                return a[1]
            else:
                return []


