from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Arbol import Arbol
from sql.storageManager.jsonMode import *

class BaseDeDatos(Instruccion):
    'Esta clase se utiliza para crear una base de datos'

    def __init__(self, nombre):
        self.nombreTabla = nombre
        self.tablas = []

    def agregarTabla(self, nombre):
        self.tablas.append(nombre)
        print("se agrego la tabla")

    def getTabla(self,ptabla):
        for tabla in self.tablas:
            if tabla.nombreDeTabla==ptabla:
                return tabla
                
        return None

    def eliminarTabla(self, nombre):
        for x in range(0, len(self.tablas)):
            if self.tablas[x].nombreDeTabla == nombre :
                self.tablas.pop(x)
                return 1
        
        return 0

    def devolverTabla(self, nombre):
        for x in range(0, len(self.tablas)):
            if self.tablas[x].nombreDeTabla == nombre :
                return self.tablas[x]
        return 0

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
