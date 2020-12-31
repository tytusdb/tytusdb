from abc import ABC, abstractmethod
from tools.tabla_tipos import *

class expresion(ABC):
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def tipo_dominante(self, tipo1, tipo2):
        return tipos_tabla[tipo1][tipo2]

    @abstractmethod
    def ejecutar(self):
        pass