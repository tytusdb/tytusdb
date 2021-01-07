from abc import abstractmethod
from enum import Enum


class TYPE(Enum):
    NUMBER = 1
    STRING = 2
    BOOLEAN = 3
    TIMESTAMP = 4
    DATE = 5
    TIME = 6
    DATETIME = 7
    TYPE = 8
    NULL = 9


list_errors = list()
temp = -1


def newTemp():
    global temp
    temp += 1
    return str(temp)


def incTemp(value):
    global temp
    temp += value


class Expression:
    """
    Esta clase representa una expresión
    """

    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

    @abstractmethod
    def execute(self, environment):
        """
        Metodo que servira para ejecutar las expresiones
        """
