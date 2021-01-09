from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
from Instrucciones.Sql_select.OrderBy import OrderBy
from Instrucciones.Sql_select.GroupBy import GroupBy
from Instrucciones.Sql_select.Having import Having
from Instrucciones.Sql_select.Limit import Limit
from Instrucciones.Identificador import Identificador
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Sql_select import SelectLista 
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
import numpy as np
import pandas as pd
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class Index(Instruccion):
                       #dist  tipo  lcol  lcol  linners where lrows
    def __init__(self, idIndex, idTabla , lcol, where, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.QUERY),linea,columna,strGram)
        self.idIndex = idIndex
        self.idTabla = idTabla
        self.lcol = lcol
        self.where = where





    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        val = self.idTabla.devolverTabla(tabla, arbol)
        print("El wkkkkkkene vacio")

        if(val == 0):
            error = Excepcion("42P01", "Semantico", "La tabla " + str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            print('Error tabla no existe')
            return error
        print("Eiiiiiiiviene vacio")

        tablaIndex = extractTable(arbol.getBaseDatos(), val)
        arbol.setTablaActual(tablaIndex)
        columnas = arbol.devolverColumnasTabla(val)
        print("El jjjjjjjjene vacio")

        data = np.array((tablaIndex))
        res = []
        # vamos a mostrar todos
        for x in range(0, len(columnas)):
            col = columnas[x].obtenerNombre()
            res.append(col)

        arbol.setColumnasActual(res)

        ## solo me quedaria buscar entre las columnas si existe la columnas 
        print(res)  
        print("El wheracio")

        if self.where:
            print("El where no viene vacio")

    
    def analizar(self, tabla, arbol):
        pass
        
    def traducir(self, tabla, arbol):
        tabla.setIndex(self)
        cadena = ""
        funcname = ""


       
        h=0
        val2param=""
        val1param=""
        try:
                print("actuaparam in self.parametros") 

           


        except Exception as e:
            print(e) 
        
        

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