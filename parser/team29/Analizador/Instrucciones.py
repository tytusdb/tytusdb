from abc import abstractmethod
from enum import Enum

class SELECT_MODE(Enum):
  ALL = 1
  PARAMS = 2

class Instruccion:
    """Clase abstracta"""
    @abstractmethod
    def execute(self):
        pass

class CreateDatabase(Instruccion):
    """
    Clase que representa la instruccion CREATE DATABASE
    Esta instruccion es la encargada de crear una nueva base de datos en el DBMS
    """
    def __init__(self, replace, exists, name, mode, owner):
        """
        Comment
        """
        self.replace = replace
        self.exists = exists
        self.name = name
        self.mode = mode
        self.owner = owner

class SelectOnlyParams(Instruccion):
    def __init__(self, params):
        self.params = params
    
    def execute(self):
        value = [p.execute().value for p in self.params]
        ids = [p.temp for p in self.params]
        return value
            

class SelectParams(Instruccion):
    def __init__(self, mode, params = []):
        self.mode = mode
        self.params = params
    
    def execute(self):
        pass