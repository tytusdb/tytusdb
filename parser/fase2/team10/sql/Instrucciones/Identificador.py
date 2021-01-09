from sql.Instrucciones.Excepcion import Excepcion
from tkinter.constants import FALSE
from sql.Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from sql.Instrucciones.TablaSimbolos.Instruccion import *
from sql.Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from sql.Instrucciones.TablaSimbolos.Simbolo import Simbolo
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from sql.Instrucciones.Tablas.Campo import Campo
from sql.storageManager.jsonMode import *
import numpy as np
class Identificador(Instruccion):
    def __init__(self, id, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.ID),linea,columna,strGram)
        self.id = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if(arbol.getWhere() or arbol.getUpdate()):
            print("True")
            res = 0
            encontrado = 0
            #aqui deberia tener un arbol con lista de columnas
            for x in range(0,len(arbol.getColumnasActual())):
                print(x)
                valor = arbol.getColumnasActual()
                if(isinstance(valor[x],Campo)):
                    if(valor[x].nombre == self.id):
                        res = x
                        encontrado = 1
                else:
                    if(valor[x] == self.id):
                        res = x
                        encontrado = 1
            
            if(encontrado == 0):
                error = Excepcion("42P10","Semantico","La columna "+str(self.id)+" no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            else:
                return res
                #self.id
        elif arbol.comprobacionCreate:
            variable = tabla.getVariable(self.id)
            if variable == None:
                error = Excepcion("42P10","Semantico","La columna "+str(self.id)+" no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            self.tipo = variable.tipo
            arbol.columnaCheck = self.id
            return variable.valor
        else:
            # Tengo que traer la variable
            indice = arbol.devolverOrdenDeColumna(arbol.getNombreTabla(), self.id)
            #print("INDICE----------->",arbol.getNombreTabla(),indice,self.id)
            tablaSelect = extractTable(arbol.getBaseDatos(),arbol.getNombreTabla())
            col = [[item[indice]] for item in tablaSelect]
            columnas = np.array(col)
            #print(col)
            self.tipo = arbol.devolverTipoColumna(arbol.getNombreTabla(), self.id)
            return columnas

    def devolverId(self, tabla, arbol):
        return self.id

    def devolverTabla(self,tabla,arbol):
        super().ejecutar(tabla,arbol)
        valor = arbol.devolviendoTablaDeBase(self.id)
        if(valor == 0):
            print("Esto provoca un error, tabla no existe")
            return 0
        else:
            print("tabla encontrada")
            return self.id

    def comprobar(self,tabla,arbol):
        super().ejecutar(tabla,arbol)
        variable = tabla.getVariable(self.id)
        if variable == None:
            error = Excepcion("42P10","Semantico","La columna "+str(self.id)+" no existe",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        self.tipo = variable.tipo
        return variable.valor.ejecutar(tabla, arbol)

    def analizar(self, tabla, arbol):
        pass
        
    def traducir(self, tabla, arbol):
        pass