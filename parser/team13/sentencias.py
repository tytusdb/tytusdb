from enum import Enum


class Aritmetica(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5
    POTENCIA = 6


class Relacionales(Enum):
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    DIFERENTE = 4
    MAYORIGUAL_QUE=5
    MENORIGUAL_QUE=6


class Logicas(Enum):
    AND = 1
    OR = 2
    NOT = 3


class Expresion(Enum):
    ID = 1
    BOOLEAN = 2
    DECIMAL = 3
    ENTERO = 4
    CADENA = 5
    TABATT = 6
    NEGATIVO = 7


class Sentencia:
    '''clase abstracta'''


class SCrearBase(Sentencia):
    def __init__(self, owner, mode, replace, exists, id):
        self.id = id
        self.owner = owner
        self.mode = mode
        self.replace = replace
        self.exists = exists


class SShowBase(Sentencia):
    def __init__(self, like, cadena):
        self.like = like
        self.cadena = cadena


class SAlterBase(Sentencia):
    def __init__(self, id, rename, owner, idnuevo):
        self.id = id
        self.rename = rename
        self.owner = owner
        self.idnuevo = idnuevo


class SDropBase(Sentencia):
    def __init__(self, exists, id):
        self.exists = exists
        self.id = id


class STypeEnum(Sentencia):
    def __init__(self, id, lista=[]):
        self.id = id
        self.lista = lista


class SExpresion(Sentencia):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo


class SOperacion(Sentencia):
    def __init__(self, opIzq, opDer, operador):
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador


class SUpdateBase(Sentencia):
    def __init__(self, id, listaSet=[], listaWhere=[]):
        self.id = id
        self.listaSet = listaSet
        self.listaWhere = listaWhere


class SValSet(Sentencia):
    def __init__(self, columna, valor):
        self.columna = columna
        self.valor = valor


class SValWhere(Sentencia):
    def __init__(self, columna, valor):
        self.columna = columna
        self.columna = valor

