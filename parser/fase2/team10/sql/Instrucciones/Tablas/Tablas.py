from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Expresiones.Primitivo import Primitivo
from sql.Instrucciones.Tablas.Campo import Campo
from sql.storageManager.jsonMode import *

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
        self.lista_de_campos.append(res)

    def devolverColumna(self,nombre_ide):
        for x in range(0,len(self.lista_de_campos)):
            if(self.lista_de_campos[x].nombre == nombre_ide):
                return self.lista_de_campos[x].orden
        return 0

    def devolverTodasLasColumnas(self):
        return self.lista_de_campos

    def devolverTipo(self,nombre_ide):
        for x in range(0,len(self.lista_de_campos)):
            if(self.lista_de_campos[x].nombre == nombre_ide):
                return self.lista_de_campos[x].tipo
        return 0