from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.simbolo import Simbolo
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from abc import ABC, abstractmethod

class NodoArbol (ABC):

    @abstractmethod
    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    @abstractmethod
    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    @abstractmethod
    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    @abstractmethod
    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    @abstractmethod
    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna
