
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

    #Metodo para buscar una tabla
    def buscar(self,nombreTabla) :
        aux = self.inicio
        while aux != None :
            if aux.nombre == nombreTabla :
                #print("La tabla existe")
                return aux
            aux = aux.siguiente
        #print("La tabla no existe")
        return None

    #Metodo para listar los nodos
    def verNodos(self) :
        tablas = []
        aux = self.inicio
        while aux != None :
            tablas.append(aux.nombre)
            aux = aux.siguiente
        return tablas 