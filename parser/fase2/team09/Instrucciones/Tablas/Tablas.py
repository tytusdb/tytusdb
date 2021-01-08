from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.Tablas.Campo import Campo
from storageManager.jsonMode import *

class Tablas():
    'Esta clase se utiliza para crear una tabla'

    def __init__(self, nombre, lista_de_campos):
        self.nombreDeTabla = nombre
        self.lista_de_campos = []
        self.lista_de_data = []
        #self.lista_constraint = []
        self.orden = 0

    def agregarColumna(self,nombre1,tipo1,pk1, constraint):
        res = Campo(nombre1,tipo1,pk1,self.orden, constraint)
        self.orden = self.orden + 1
        cols = self.devolverTodasLasColumnas()
        cols.append(res)
        for v in self.lista_de_campos:
            if v.tipo.toString() == "index":
                cols.append(v)
        self.lista_de_campos = cols

    def devolverColumna(self,nombre_ide):
        for x in range(0,len(self.lista_de_campos)):
            if(self.lista_de_campos[x].nombre == nombre_ide):
                return self.lista_de_campos[x].orden
        return 0

    def devolverTodasLasColumnas(self):
        campos = []
        for c in self.lista_de_campos:
            if c.tipo.toString() != "index":
                campos.append(c)
        return campos

    def devolverTipo(self,nombre_ide):
        for x in range(0,len(self.lista_de_campos)):
            if(self.lista_de_campos[x].nombre == nombre_ide):
                return self.lista_de_campos[x].tipo
        return 0

    def getColumnCount(self):
        count = 0
        for v in self.lista_de_campos:
            if v.tipo.toString() != "index":
                count = count + 1
        return count