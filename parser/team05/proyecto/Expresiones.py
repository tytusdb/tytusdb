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


# OPERACIONES LÓGICAS
class OPERACION_LOGICA(Enum):
    IGUAL = 1
    DIF = 2
    DIF1 = 3
    MENOR = 4
    MENORIGUAL = 5
    MAYOR = 6
    MAYORIGUAL = 7
    AND = 1
    OR = 2
    NOT = 3


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
