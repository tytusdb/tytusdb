
import os
from BTree import *

class nodo :
    def __init__(self,nombreDeLaTabla,numeroDeColumnasDeLaTabla) :
        self.nombre = nombreDeLaTabla
        self.columnas = numeroDeColumnasDeLaTabla
        self.elementosAB = BTree()
        self.siguiente = None
        self.anterior = None
        
class ListaDobledeArboles :
    def __init__ (self) :
        self.inicio = None
        self.fin = None
    
    #Metodo para saber si la lista esta vacia
    def estaVacia(self) :
        return self.inicio is None