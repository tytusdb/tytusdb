from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
from Instrucciones.Sql_select.OrderBy import OrderBy
from Instrucciones.Sql_select.GroupBy import GroupBy
from Instrucciones.Sql_select.Having import Having
from Instrucciones.Sql_select.Limit import Limit
from Instrucciones.Identificador import Identificador
from Instrucciones.Excepcion import Excepcion
import numpy as np

class Select(Instruccion):
                       #dist  tipo  lcol  lcol  linners where lrows
    def __init__(self, dist, lcol, lcol2, linners, where, lrows, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
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
            val = ""
            tablaSelect = ""
            for x in range(0,len(self.lcol2)):
                val = self.lcol2[x].devolverTabla(tabla,arbol)
                print(val)
                tablaSelect = extractTable(arbol.getBaseDatos(),val)

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
                        grupo = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.agruparTabla(tablaSelect,grupo)
                    if isinstance(resultado, Having):
                        print("BIENVENIDO A HAVING-BY")
                        lrows = self.lrows[x].ejecutar(tabla,arbol)
                    if isinstance(resultado, OrderBy):
                        print("BIENVENIDO A ORDER-BY")
                        orden = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.devolverTablaLimite(tablaSelect,orden)
                    if isinstance(resultado, Limit):
                        print("BIENVENIDO A LIMIT")
                        limite = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.devolverTablaLimite(tablaSelect,limite)

            return tablaSelect
        else:
            #vamos a mostrar por columna
            print("mostrar por  columna")
            val = ""
            tablaSelect = []
            #Aqui se devuelve toda la tabla
            for x in range(0,len(self.lcol2)):
                val = self.lcol2[x].devolverTabla(tabla,arbol)
                arbol.setNombreTabla(val)
                tablaSelect = extractTable(arbol.getBaseDatos(),val)
                arbol.setTablaActual(tablaSelect)
                #aqui vamos a dividir por columnas
                data = np.array((tablaSelect))
                res = []
                esExpresion = False
                for x in range(0,len(self.lcol)):
                    #obtener nombre de columna
                    if isinstance(self.lcol[x],Identificador):
                        nombreColumna = self.lcol[x].devolverId(tabla,arbol)
                        nombreTabla = val
                        #obtener la posicion
                        posicion = arbol.devolverOrdenDeColumna(nombreTabla,nombreColumna)
                        res.append(posicion)
                    else:
                        # Si la columna es una expresión
                        esExpresion = True
                        valores = self.lcol[x].ejecutar(tabla, arbol)
                        if isinstance(valores, Excepcion):
                            return valores

                        res.append(valores)
                if esExpresion:
                    listaFinal = []
                    print("resultado--------------->",res,type(res))
                    for i in res:
                        listaFinal.append(i)
                    print(listaFinal,len(listaFinal))
                    res = np.concatenate(listaFinal,axis=1)
                    #print(res)
                    return res
                nueva_Columna = data[:, res]

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
                        #tablaSelect = self.agruparTabla(grupo,grupo)

                    if isinstance(resultado, Having):
                        print("BIENVENIDO A HAVING-BY")
                        lrows = self.lrows[x].ejecutar(tabla,arbol)
                    
                    if isinstance(resultado, OrderBy):
                        print("BIENVENIDO A ORDER-BY")
                        orden = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.devolverTablaLimite(tablaSelect,orden)
                    
                    if isinstance(resultado, Limit):
                        print("BIENVENIDO A LIMIT")
                        limite = self.lrows[x].ejecutar(tabla,arbol)
                        tablaSelect = self.devolverTablaLimite(tablaSelect,limite)

                print(nueva_Columna)

            return nueva_Columna


#---------------------------GROUP BY
    def agruparTabla(self, tablaA, tablaB):
        tabla1 = tablaB
        tabla2 = tablaA
        if(len(tablaA.data)>=len(tablaB.data)):
            tabla1 = tablaA.data
            tabla2 = tablaB.data
        
        res = []
        nodo = []
        for j in range(0,len(tabla1)):
            for k in range(0,len(tabla2)): 
                if(tabla1[j] == tabla2[k]):
                    nodo.append(tabla1[j])
            res.append(nodo)
        
        return res[0]


#----------------------------ORDER BY 
    def devolverOrderBy(self,tabla,order):
        tablaRes = sorted(tabla, key=lambda a_entry: a_entry[order])
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
        if(self.lcol == "*"):
            #vamos a mostrar todos
            val = ""
            columnas = ""
            res = []
            for x in range(0,len(self.lcol2)):
                val = self.lcol2[x].devolverTabla(tabla,arbol)
                columnas = arbol.devolverColumnasTabla(val)
            print(columnas)
            for x in range(0,len(columnas)):
                col = columnas[x].obtenerNombre()
                res.append(col)
            return res
        else:
            #vamos a mostrar por columna
            print("mostrar por  columna")
            res = []
            for x in range(0,len(self.lcol)):
                if isinstance(self.lcol[x],Identificador):
                    col = self.lcol[x].devolverId(tabla,arbol)
                    res.append(col)
                else:
                    # Obtener la columna
                    #col = self.lcol[x].ejecutar(tabla,arbol)
                    res.append('col')
            return res


'''
columnas y filas
matrix = np.array(([[1,"k","t"],[2,"L","a"],[3,"N","y"]]))
nueva_Fila = lista[2]
nueva_Columna2 = matrix[:, [0, 2]]    
limite
a = sorted(a, key=lambda a_entry: a_entry[2])

'''    