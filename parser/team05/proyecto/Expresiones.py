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
    MULTIPLICACION = 3
    DIVISION = 4


# OPERACIONES LÓGICAS
class OPERACION_LOGICA(Enum):
    AND = 1
    OR = 2
    NOT = 3


# NUMERIC EXPRESSION CLASS
class NumericExpression:
    """ Numeric expression class """


# OPERACIONES BINARIAS (DOS OPERADORES, UN OPERADOR)
class BinaryExpression(NumericExpression):
    """ Binary arithmetic expression - [op1, op2, operator] """

    def __init__(self, p_op1, p_op2, p_operator):
        self.op1 = p_op1
        self.op2 = p_op2
        self.operator = p_operator

