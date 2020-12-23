from Instrucciones.Excepcion import Excepcion
from tkinter.constants import FALSE
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.TablaSimbolos.Instruccion import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from storageManager.jsonMode import *
import numpy as np
class Identificador(Instruccion):
    def __init__(self, id, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.ID),linea,columna)
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
        else:
            # Tengo que traer la variable
            indice = arbol.devolverOrdenDeColumna(arbol.getNombreTabla(), self.id)
            #print("INDICE----------->",arbol.getNombreTabla(),indice,self.id)
            columnas = arbol.getTablaActual()
            columnas = np.array(columnas)
            columna = columnas[:, [indice]]
            self.tipo = arbol.devolverTipoColumna(arbol.getNombreTabla(), self.id)
            return columna
            '''
            
            variable = tabla.getVariable(self.id)
            if variable == None:
                error = Excepcion("42P10","Semantico","La columna "+str(self.id)+" no existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            self.tipo = variable.tipo
            return variable.valor.ejecutar(tabla, arbol)
            '''

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