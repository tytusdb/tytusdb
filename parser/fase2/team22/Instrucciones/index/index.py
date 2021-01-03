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

class index(Instruccion):
                  
    def __init__(self, ID, tabla , l_expresiones, where, params_crt_indx, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.QUERY),linea,columna,params_crt_indx)
        self.ID = ID
        self.tabla = tabla
        self.l_expresiones = l_expresiones
        self.where = where

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        val = self.tabla.devolverTabla(tabla, arbol)
        
        if(val == 0):
            error = Excepcion("42P01", "Semantico", "La tabla " + str(self.identificador.devolverId(tabla, arbol)) + " no existe", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            print('Error tabla no existe')
            return error

        tablaIndex = extractTable(arbol.getBaseDatos(), val)
        arbol.setTablaActual(tablaIndex)
        columnas = arbol.devolverColumnasTabla(val)
        
        data = np.array((tablaIndex))
        res = []
        # vamos a mostrar todos
        for x in range(0, len(columnas)):
            col = columnas[x].obtenerNombre()
            res.append(col)

        arbol.setColumnasActual(res)

        ## solo me quedaria buscar entre las columnas si existe la columnas 
        print(res)  

        if self.where:
            print("El where no viene vacio")

    
    def analizar(self, tabla, arbol):
        pass
        
    def traducir(self, tabla, arbol):
        pass
        
