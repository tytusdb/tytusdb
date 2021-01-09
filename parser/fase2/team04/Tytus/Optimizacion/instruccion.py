from abc import ABC, abstractmethod

class Instruccion(ABC):
    
    @abstractmethod
    def toString(self):
        pass