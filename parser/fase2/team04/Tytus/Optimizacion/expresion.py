from abc import ABC, abstractmethod

class Expresion(ABC):
    
    @abstractmethod
    def toString(self):
        pass