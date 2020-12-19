from abc import ABC, abstractmethod

class InstruccionAbstracta(ABC):

    
    
    def setearValores(self, fila,columna,nombreNodo,numeroNodo,valor,hijos = []):
        self.fila = fila
        self.columna = columna
        self.nombreNodo = nombreNodo
        self.numeroNodo = numeroNodo
        self.valor = valor    
        self.hijos = hijos


    @abstractmethod
    def ejecutar(self):
        pass
    


