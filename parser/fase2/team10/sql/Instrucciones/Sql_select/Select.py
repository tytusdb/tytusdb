from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.storageManager.jsonMode import *
from sql.Instrucciones.Sql_select.OrderBy import OrderBy
from sql.Instrucciones.Sql_select.GroupBy import GroupBy
from sql.Instrucciones.Sql_select.Having import Having
from sql.Instrucciones.Sql_select.Limit import Limit
from sql.Instrucciones.Identificador import Identificador
from sql.Instrucciones.Excepcion import Excepcion
from sql.Instrucciones.Sql_select import SelectLista 
from sql.Instrucciones.TablaSimbolos.Simbolo import Simbolo
import numpy as np
import pandas as pd
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class Select(Instruccion):
                       #dist  tipo  lcol  lcol  linners where lrows
    def __init__(self, dist, lcol, lcol2, linners, where, lrows, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.QUERY),linea,columna,strGram)
        self.dist = dist
        self.lcol = lcol
        self.lcol2 = lcol2
        self.linners = linners
        self.where = where
        self.lrows = lrows

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if(self.lcol == "*"):
            #vamos a mostrar todos
            #haremos un for 
            print('select');
            val = ""
            tablaSelect = ""
            tablaSelect2 = ""
            tablaX = []
            for x in range(0,len(self.lcol2)):
                if(x==0):
                    # Cuando viene un Alias
                    if isinstance(self.lcol2[x], SelectLista.Alias):
                        #print(self.lcol2[x].id,self.lcol2[x].expresion.id)
                        val = self.lcol2[x].expresion.devolverTabla(tabla,arbol)
                        variable = Simbolo(self.lcol2[x].id,None,val,0,0)
                        tabla.setVariable(variable)
                    # Cuando viene una columna normal
                    else:
                        val = self.lcol2[x].devolverTabla(tabla,arbol)
                    
                    tablaSelect = extractTable(arbol.getBaseDatos(),val)
                else:
                    if isinstance(self.lcol2[x], SelectLista.Alias):
                        #print(self.lcol2[x].id,self.lcol2[x].expresion.id)
                        val = self.lcol2[x].expresion.devolverTabla(tabla,arbol)
                        variable = Simbolo(self.lcol2[x].id,None,val,0,0)
                        tabla.setVariable(variable)
                    # Cuando viene una columna normal
                    else:
                        val = self.lcol2[x].devolverTabla(tabla,arbol)

                    tablaSelect2 = extractTable(arbol.getBaseDatos(),val)
                    tablaSelect = self.unirTablas(tablaSelect,tablaSelect2)

            if(self.where != None):
                arbol.setTablaActual(tablaSelect)
                arbol.setColumnasActual(arbol.devolverColumnasTabla(val))
                tablaSelect = self.where.ejecutar(tabla,arbol)
                columnas = self.devolverColumnas(tabla,arbol)
            
            if(self.lrows != None):
                for x in range(0,len(self.lrows)):
                    resultado = self.lrows[x]
                    #BUENO AQUI VIENE LO OTRO (O-w-O)
                    #ORDER_BY
                    #aqui va por orden
                    #FROM---> WHERE--->GROUPBY---->HAVING---->SELECT--->DISTINCT--->ORDERBY---->LIMIT
                    if isinstance(resultado, GroupBy):
                        print("BIENVENIDO A GROUP-BY")
                        grupo = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.agruparTabla(tablaSelect,grupo)
                    if isinstance(resultado, Having):
                        print("BIENVENIDO A HAVING-BY")
                        lrows = self.lrows[x].ejecutar(tabla,arbol)
                    if isinstance(resultado, OrderBy):
                        print("BIENVENIDO A ORDER-BY")
                        orden = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.devolverOrderBy(tablaSelect,orden,arbol)
                    if isinstance(resultado, Limit):
                        print("BIENVENIDO A LIMIT")
                        limite = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.devolverTablaLimite(tablaSelect,limite)
            print (tablaSelect)
            return tablaSelect
        else:
            #vamos a mostrar por columna
            print("mostrar por  columna")
            val = ""
            tablaSelect = []
            tablaSelect2 = []
            #Aqui se devuelve toda la tabla
            for x in range(0,len(self.lcol2)):
                if(x == 0):
                    # Cuando viene un Alias
                    if isinstance(self.lcol2[x], SelectLista.Alias):
                        #print(self.lcol2[x].id,self.lcol2[x].expresion.id)
                        val = self.lcol2[x].expresion.devolverTabla(tabla,arbol)
                        variable = Simbolo(self.lcol2[x].id,None,val,0,0)
                        tabla.setVariable(variable)
                    # Cuando viene una columna normal
                    else:
                        val = self.lcol2[x].devolverTabla(tabla,arbol)
                    
                    arbol.setNombreTabla(val)
                    tablaSelect = extractTable(arbol.getBaseDatos(),val)
                    '''
                    val = self.lcol2[x].devolverTabla(tabla,arbol)
                    arbol.setNombreTabla(val)
                    tablaSelect = extractTable(arbol.getBaseDatos(),val)
                    '''
                else:
                    if isinstance(self.lcol2[x], SelectLista.Alias):
                        #print(self.lcol2[x].id,self.lcol2[x].expresion.id)
                        val = self.lcol2[x].expresion.devolverTabla(tabla,arbol)
                        variable = Simbolo(self.lcol2[x].id,None,val,0,0)
                        tabla.setVariable(variable)
                    # Cuando viene una columna normal
                    else:
                        val = self.lcol2[x].devolverTabla(tabla,arbol)

                    tablaSelect2 = extractTable(arbol.getBaseDatos(),val)
                    tablaSelect = self.unirTablas(tablaSelect,tablaSelect2)

            arbol.setTablaActual(tablaSelect)
            #aqui vamos a dividir por columnas
            data = np.array((tablaSelect))
            res = []
            esExpresion = False
            tamAnterior = 0
            arr = []
            for x in range(0,len(self.lcol)):
                #obtener nombre de columna
                if isinstance(self.lcol[x],Identificador):
                    nombreColumna = self.lcol[x].devolverId(tabla,arbol)
                    nombreTabla = val
                    #obtener la posicion
                    posicion = arbol.devolverOrdenDeColumna(nombreTabla,nombreColumna)
                    arr.append(posicion)
                elif isinstance(self.lcol[x], SelectLista.Alias):
                    print(self.lcol[x].id,self.lcol[x].expresion)
                    valor = tabla.getVariable(self.lcol[x].id)
                    print(valor)
                    valores = arbol.devolverColumnasTabla(valor.valor)
                    #valores = self.lcol[x].expresion.devolverTabla(tabla,arbol)

                    #valores = self.lcol[x].ejecutar(tabla, arbol)
                    if isinstance(valores, Excepcion):
                        return valores
                    
                    #arr = []
                    if(x == 0):
                        if(self.lcol[x].expresion == "*"):
                            for m in range(0,len(valores)):
                                tal = valores[m].orden
                                arr.append(tal)
                        else:
                            for m in range(0,len(valores)):
                                if(valores[m].nombre == self.lcol[x].expresion):
                                    tal = valores[m].orden
                                    arr.append(tal)
                        tamAnterior = len(valores)
                    else:
                        if(self.lcol[x].expresion == "*"):
                            #arr = arr.copy()
                            for m in range(0,len(valores)):
                                tal = tamAnterior + valores[m].orden
                                arr.append(tal)
                        else:
                            #arr = arr.copy()
                            for m in range(0,len(valores)):
                                if(valores[m].nombre == self.lcol[x].expresion):
                                    tal = tamAnterior + valores[m].orden
                                    arr.append(tal)
                else:
                    # Si la columna es una expresión
                    esExpresion = True
                    valores = self.lcol[x].ejecutar(tabla, arbol)
                    if isinstance(valores, Excepcion):
                        return valores

                    res.append(valores)
            
            if esExpresion:
                listaFinal = []
                #print("resultado--------------->",res,type(res))
                for i in res:
                    listaFinal.append(i)
                #print(listaFinal,len(listaFinal))
                res = np.concatenate(listaFinal,axis=1)
                #print(res)
                return res
            else:
                res = arr

            tablaSelect = data[:, res]

            if(self.where != None):
                arbol.setTablaActual(tablaSelect)
                columnas = self.devolverColumnas(tabla,arbol)
                arbol.setColumnasActual(columnas)
                tablaSelect = self.where.ejecutar(tabla,arbol)

            if(self.lrows != None):
                for x in range(0,len(self.lrows)):
                    resultado = self.lrows[x]
                    #BUENO AQUI VIENE LO OTRO (O-w-O)
                    #ORDER_BY
                    #aqui va por orden
                    #FROM---> WHERE--->GROUPBY---->HAVING---->SELECT--->DISTINCT--->ORDERBY---->LIMIT
                    if isinstance(resultado, GroupBy):
                        print("BIENVENIDO A GROUP-BY")
                        #TO DO VALIDAR EL NUMERO DE COLUMNAS DEL GROUP 
                        grupo = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.agruparTabla(grupo)

                    if isinstance(resultado, Having):
                        print("BIENVENIDO A HAVING-BY")
                        lrows = self.lrows[x].ejecutar(tabla,arbol)
                    
                    if isinstance(resultado, OrderBy):
                        print("BIENVENIDO A ORDER-BY")
                        self.lrows[x].setTabla(val)
                        orden = self.lrows[x].ejecutar(tabla,arbol)
                        #orden = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.devolverOrderBy(tablaSelect,orden,arbol)
                    
                    if isinstance(resultado, Limit):
                        print("BIENVENIDO A LIMIT")
                        limite = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.devolverTablaLimite(tablaSelect,limite)

                print(tablaSelect)

            return tablaSelect

#---------------------------GROUP BY
    def agruparTabla(self, tab):
        #tab = np.array(tab)
        tab = np.ascontiguousarray(tab) 
        unique_a = np.unique(tab.view([('', tab.dtype)]*tab.shape[1]))
        return unique_a.view(tab.dtype).reshape((unique_a.shape[0], tab.shape[1])) 

#----------------------------ORDER BY 
    def devolverOrderBy(self,tabla,order,arbol):
        #aqui vamos a hacer los indices
        '''
        ind = []
        for x in range(0, len(tabla)):
            ind.append(x)
        
        tam = tabla.shape
        fila = tam[0]
        columna = tam[1]
        '''
        arr2D = tabla
        t = []
        for x in range(0,len(arr2D)):
            val = arr2D[x]
            nodo = []
            for y in range(0,len(val)):
                nodo.append(val[y])
            t.append(nodo)
        
        arr2D = t
        columnIndex = order
        if(arbol.getOrder() == 'DESC'):
            # Sort 2D numpy array by 2nd Column
            sortedArr = np.sort(arr2D, axis = 0)
            sortedArr = sortedArr[::-1]
            print('Sorted 2D Numpy Array')
            print(sortedArr)
            tablaRes = sortedArr
        else:
            sort = np.sort(arr2D,axis=0)
            #sort = np.sort(arr2D, axis = 0)
            #sort = np.sort(arr2D)
            #sort = sort[::1]
            print(sort)
            tablaRes = sort

        #vamos a volverlo otra ves una tabla
        '''
        tablaRes = sorted(tabla, key=lambda a_entry: a_entry[order])
        '''
        return tablaRes 

#-----------------------------LIMIT
    def devolverTablaLimite(self,tabla,numeroLimite):
        if(len(tabla)>numeroLimite):
            nueva_lista = tabla[0:numeroLimite]
        else:
            nueva_lista = tabla[0:len(tabla)]
        return nueva_lista

#-----------------------------COLUMNAS
    def devolverColumnas(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #vamos a mostrar todos
        val = ""
        columnas = ""
        columnas2 = ""
        res = []
        esExpresion = False
        tamAnterior = 0
        arr = []
        for x in range(0,len(self.lcol)):
            if(self.lcol == "*"):
                if isinstance(self.lcol2[x],Identificador):
                    valores = arbol.devolverColumnasTabla(self.lcol2[x].id)
                    for m in range(0,len(valores)):
                        tal = valores[m].nombre
                        arr.append(tal)
                else:
                    valor = tabla.getVariable(self.lcol2[x].id)
                    valores = arbol.devolverColumnasTabla(valor.valor)
                    for m in range(0,len(valores)):
                        tal = valores[m].nombre
                        arr.append(tal)
            else:
                if isinstance(self.lcol[x],Identificador):
                    col = self.lcol[x].devolverId(tabla,arbol)
                    arr.append(col)
                elif isinstance(self.lcol[x], SelectLista.Alias):
                    print(self.lcol[x].id,self.lcol[x].expresion)
                    valor = tabla.getVariable(self.lcol[x].id)
                    print(valor)
                    valores = arbol.devolverColumnasTabla(valor.valor)
                    #valores = self.lcol[x].expresion.devolverTabla(tabla,arbol)

                    #valores = self.lcol[x].ejecutar(tabla, arbol)
                    if isinstance(valores, Excepcion):
                        return valores
                    
                    #arr = []
                    if isinstance(self.lcol[x], SelectLista.Alias):
                        if(x == 0):
                            if(self.lcol[x].expresion == "*"):
                                for m in range(0,len(valores)):
                                    tal = valores[m].nombre
                                    arr.append(tal)
                            else:
                                for m in range(0,len(valores)):
                                    if(valores[m].nombre == self.lcol[x].expresion):
                                        tal = valores[m].nombre
                                        arr.append(tal)
                        else:
                            if(self.lcol[x].expresion == "*"):
                                #arr = arr.copy()
                                for m in range(0,len(valores)):
                                    tal = valores[m].nombre
                                    arr.append(tal)
                            else:
                                #arr = arr.copy()
                                for m in range(0,len(valores)):
                                    if(valores[m].nombre == self.lcol[x].expresion):
                                        tal = valores[m].nombre
                                        arr.append(tal)
                else:
                    arr.append("columna")

        res = arr
        return res


    def unirTablas(self, tabla1, tabla2):
        tablaRes = []
        tablaRes2 = []
        for x in range(0,len(tabla1)):
            va = tabla1[x]
            #a = np.array(tabla1[x])
            for y in range(0,len(tabla2)):
                nodo = va.copy()
                res = tabla2[y]
                for z in range(0,len(res)):
                    nodo.append(res[z])
                    #nodo = np.insert(a, a.shape[1], np.array((res[z])), 1)
                #print(nodo)
                if(nodo != []):
                   tablaRes2.append(nodo)
                print(nodo)
        return tablaRes2

'''
columnas y filas
matrix = np.array(([[1,"k","t"],[2,"L","a"],[3,"N","y"]]))
nueva_Fila = lista[2]
nueva_Columna2 = matrix[:, [0, 2]]    
Numero de Filas
a.shape[0]
Numero de columnas
a.shape[1]
limite
a = sorted(a, key=lambda a_entry: a_entry[2])

'''    