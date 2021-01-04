# GRUPO 5
# 201213062 - Mónica Raquel Calderon Muñoz
# 201213223 - Astrid Edith Hernandez Gonzalez
# 201213255 - Leonel Eduardo Avila Calvillo
# 201220159 - Diego Ahtohil Noj Armira
# 201220165 - Oscar Rolando Bernard Peralta

# IMPORT SECTION
from enum import Enum


# OPERACIONES
class OPERACIONES(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5
    EXP = 6
    IS = 7
    ISNULL = 8
    NOTNULL = 9
    BETWEEN = 10
    NOTBETWEEN = 11
    BETWEENSIMMETRIC = 12
    NOTBETWEENSIMMETRIC = 13
    ISDISTINCT = 14
    ISNOTDISTINCT = 15


# OPERACIONES LÓGICAS
class OPERACION_LOGICA(Enum):
    IGUAL = 1
    DIF = 2
    DIF1 = 3
    MENOR = 4
    MENORIGUAL = 5
    MAYOR = 6
    MAYORIGUAL = 7
    AND = 8
    OR = 9
    NOT = 10
    BETWEEN = 11
    NOTBETWEEN = 12
    BETWEENSIMMETRIC = 13
    NOTBETWEENSIMMETRIC = 14
    ISDISTINCT = 15
    ISNOTDISTINCT = 16

class OPERACION_STRING(Enum):
    BAND = 1
    BOR = 2
    BXOR = 3
    DESPLAZAI = 4
    DESPLAZAD = 5
    BNOT = 6
    RAIZCUADRADA = 7
    RAIZCUBICA = 8

# CLASE DE EXPRESION NUMERICA
class Expresion:
    """ Numeric expression class """


# OPERACIONES BINARIAS (DOS OPERANDOS, UN OPERADOR)
class ExpresionBinaria(Expresion):
    """ Expresión de operación binaria - [op1, op2, operator] """

    def __init__(self, p_op1, p_op2, p_operador):
        self.op1 = p_op1
        self.op2 = p_op2
        self.operador = p_operador


# OPERACIONES UNARIAS (UN OPERANDO, UN OPERADOR)
class ExpresionUnaria(Expresion):
    """ Expresión de operación unaria - [oper1, operador] """

    def __init__(self, p_op1, p_operador):
        self.op1 = p_op1
        self.operador = p_operador


# EXPRESIONES DE VALOR
class ExpresionDeValor(Expresion):
    """ Expresión de valor - [número, decimal, cadena, true, false, date, time, datetime] """

    def __init__(self, p_valor):
        self.valor = p_valor

#Clase para guardar id y el alias del mismo 
class Id(Expresion):
    def __init__(self, valor, alias):
        self.alias = alias
        self.valor = valor

class Numero(Expresion):
    def __init__(self, valor):
        self.valor = valor

class Decimal(Expresion):
    def __init__(self, valor):
        self.valor = valor

class Cadena(Expresion):
    def __init__(self, valor):
        self.valor = valor

class Booleano(Expresion):
    def __init__(self, valor):
        self.valor = valor

class Date(Expresion):
    def __init__(self, valor):
        self.valor = valor

class Null(Expresion):
    def __init__(self):
        """ 
        CLASE PARA GUARDAR VALOR NULL
        """

class Unknow(Expresion):
    def __init__(self):
        """
        CLASE PARA GUARDAR EL VALOR UNKNOW
        """