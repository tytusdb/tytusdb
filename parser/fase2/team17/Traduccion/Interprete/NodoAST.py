from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from abc import ABC, abstractmethod



class NodoArbol (ABC):

    @abstractmethod
    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna