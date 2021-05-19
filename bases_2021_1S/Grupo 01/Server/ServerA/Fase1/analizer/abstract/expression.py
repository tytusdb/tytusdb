from abc import abstractmethod
from enum import Enum
from Fase1.analizer.libs import MathFunctions as mf
from Fase1.analizer.libs import TrigonometricFunctions as trf
from Fase1.analizer.libs import StringFunctions as strf


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


comps = {
    "ISNULL": "IS NULL",
    "NOTNULL": "NOT NULL",
    "ISTRUE": "IS TRUE",
    "ISFALSE": "IS FALSE",
    "ISUNKNOWN": "IS UNKNOWN",
    "ISNOTNULL": "IS NOT NULL",
    "ISNOTTRUE": "IS NOT TRUE",
    "ISNOTFALSE": "IS NOT FALSE",
    "ISNOTUNKNOWN": "IS NOT UNKNOWN",
    "BETWEEN": "BETWEEN",
    "NOTBETWEEN": "NOT BETWEEN",
    "BETWEENSYMMETRIC": "BETWEEN SYMMETRIC",
}


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


def returnExpErrors():
    global list_errors
    mf.list_errors_mt += trf.list_errors_tg
    mf.list_errors_mt += list_errors
    list_ = mf.list_errors_mt
    trf.list_errors_tg = list()
    mf.list_errors_mt = list()
    list_errors = list()
    return list_