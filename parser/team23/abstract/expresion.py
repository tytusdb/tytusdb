from abc import ABC, abstractmethod

class expresion(ABC):
    def __init__(self, line, column):
        self.line = line
        self.column = column

    @abstractmethod
    def ejecutar(self):
        pass