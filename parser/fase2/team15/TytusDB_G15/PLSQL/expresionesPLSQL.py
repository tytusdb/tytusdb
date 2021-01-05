from enum import Enum

class TIPO_DATO(Enum) :
    INT = 1
    CHAR= 2
    DOUBLE = 3
    FLOAT = 4
    STRING = 5
    SMALLINT = 6
    BOOLEAN = 7

class OPERADOR(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    RESIDUO = 5
    NOT = 6
    AND = 7
    OR = 8
    XOR = 9
    NOTB = 10
    ANDB = 11
    ORB = 12
    XORB = 13
    SHIFTD = 14
    SHIFTI = 15
    IGUAL = 16
    DIFERENTE = 17
    MAYORIGUAL = 18
    MENORIGUAL = 19
    MAYOR = 20
    MENOR = 21
    MOD = 22


class ExpresionBinaria():
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionNumero() :
    def __init__(self, val = 0) :
        self.val = val

class ExpresionBooleana() :
    def __init__(self, val = True) :
        self.val = val

class ExpresionNegativo():
    def __init__(self, exp) :
        self.exp = exp

class ExpresionScanf():
    def __init__(self):
        ''''''

class  ExpresionNOTBIN() :
    def __init__(self, exp) :
        self.exp = exp

class  ExpresionNOT() :
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCadena() :
    def __init__(self, val) :
        self.val = val

class ExpresionIdentificador() :
    def __init__(self, id = "") :
        self.id = id

class ExpresionIncremento() :
    def __init__(self, id) :
        self.id = id


class Gramatica():
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

class ErrorLexico():
    def __init__(self, exp1, exp2, exp3):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3

class Optimizacion():
    def __init__(self, regla, exp):
        self.regla = regla
        self.exp = exp