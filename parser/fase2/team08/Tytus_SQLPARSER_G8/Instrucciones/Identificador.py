from Instrucciones.Excepcion import Excepcion
from tkinter.constants import FALSE
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.TablaSimbolos.Instruccion import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from Instrucciones.Tablas.Campo import Campo
from storageManager.jsonMode import *
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
                #print(x)
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
            #print("tabla encontrada")
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
        super().analizar(tabla,arbol)
        variable = tabla.getSimboloVariable(self.id)
        if variable == None:
            error = Excepcion("42P10","Semantico","La columna "+str(self.id)+" no existe",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        return variable.tipo
        
    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        variable = tabla.getSimboloVariable(self.id)
        retorno = Nodo3D()
        temporal1 = tabla.getTemporal()
        arbol.addComen(f"Obtiene id: {self.id}")
        arbol.addc3d(f"{temporal1} = P + {variable.posicion}")
        temporal2 = tabla.getTemporal()
        arbol.addc3d(f"{temporal2} = Pila[{temporal1}]")
        retorno.temporalAnterior = temporal2

        return retorno

    def concatenar(self, tabla, arbol):
        return f"{self.id}"
