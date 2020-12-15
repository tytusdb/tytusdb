from enum import Enum


class arit(Enum):
    MAS = 1
    RES = 2
    POR = 3
    DIV = 4
    PORC = 5


class logic(Enum):
    NOT = 1
    AND = 2
    OR = 3
    XOR = 4


class relac(Enum):
    II = 1
    NI = 2
    MENI = 3
    MAYI = 4
    MAYOR = 5
    MENOR = 6


class tipod(Enum):
    INT = 1
    CHA = 2
    SMALLINT = 3
    BIGINT = 4
    DECIMAL = 5
    NUMERIC = 6
    REAL = 7
    DOUBLE = 8
    MONEY = 9
    VARYING = 10
    TEXT = 11
    DATE = 12
    BOOLEAN = 13


class Expresion:
    '''
        je je
    '''


class aritmetica(Expresion):
    def __init__(self, op1, op2, operacion, id):
        self.id = id
        self.op1 = op1
        self.op2 = op2
        self.operacion = operacion


class logica(Expresion):
    def __init__(self, op1, op2, operacion, id):
        self.id = id
        self.op1 = op1
        self.op2 = op2
        self.operacion = operacion


class relacional(Expresion):
    def __init__(self, op1, op2, operacion, id):
        self.id = id
        self.op1 = op1
        self.op2 = op2
        self.operacion = operacion


class tipo(Expresion):
    def __init__(self, tipo, id):
        self.id = id
        self.tipo = tipo


class casteo(Expresion):
    def __init__(self, tipo, valor, id):
        self.id = id
        self.tipo = tipo
        self.valor = valor