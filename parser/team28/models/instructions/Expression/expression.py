from enum import Enum

from abc import abstractmethod

class SymbolsAritmeticos(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVISON = 4
    EXPONENT = 5
    MODULAR = 6
    BITWISE_SHIFT_RIGHT = 7
    BITWISE_SHIFT_LEFT = 8
    BITWISE_AND = 9
    BITWISE_OR = 10
    BITWISE_XOR = 11

class SymbolsTipoDato(Enum):
    INTEGER = 1
    FLOAT = 2
    STRING = 3
    CHAR = 4
    BOOLEANO = 5

class SymbolsRelop(Enum):
    EQUALS = 1
    NOT_EQUAL = 2
    GREATE_EQUAL = 3
    GREATE_THAN = 4
    LESS_THAN = 5
    LESS_EQUAL = 6
    NOT_EQUAL_LR = 7

class SymbolsUnaryOrOthers(Enum):
    UMINUS = 1
    UPLUS = 2
    BITWISE_NOT = 3
    SQUARE_ROOT = 4
    CUBE_ROOT = 5


class Expression:
    @abstractmethod
    def procces(self):
        pass

class BinaryOperation(Expression):
    '''
        Una operacion binaria recibe, sus dos operandos y el operador
    '''
    def __init__(self, value1, value2, operador) :
        self.value1 = value1
        self.value2 = value2
        self.operador = operador
    
    def __repr__(self):
        return str(vars(self))
    
    def procces(self, expression):
        value1 = self.value1.procces(expression)
        value2 = self.value2.procces(expression)
        operador = self.operador
        if value1.type != SymbolsTipoDato.INTEGER and value2.type != SymbolsTipoDato.INTEGER:
            print('error de ejecucion')
            return
        value = 0
        if operador == SymbolsAritmeticos.PLUS:
            value = round(value1.value + value2.value, 2)
        elif operador == SymbolsAritmeticos.MINUS:
            value = round(value1.value - value2.value, 2)
        elif operador == SymbolsAritmeticos.TIMES:
            value = round(value1.value * value2.value, 2)
        elif operador == SymbolsAritmeticos.DIVISON:
            value = round(value1.value / value2.value, 2)
        elif operador == SymbolsAritmeticos.EXPONENT:
            value = round(value1.value ** value2.value, 2)
        elif operador == SymbolsAritmeticos.MODULAR:
            value = round(value1.value % value2.value, 2)
        elif operador == SymbolsAritmeticos.BITWISE_SHIFT_LEFT:
            value = round(value1.value << value2.value, 2)
        elif operador == SymbolsAritmeticos.BITWISE_SHIFT_RIGHT:
            value = round(value1.value >> value2.value, 2)
        elif operador == SymbolsAritmeticos.BITWISE_AND:
            value = round(value1.value & value2.value)
        elif operador == SymbolsAritmeticos.BITWISE_OR:
            value = round(value1.value | value2.value)
        elif operador == SymbolsAritmeticos.BITWISE_XOR:
            value = round(value1.value ^ value2.value)
        return NumberExpression(SymbolsTipoDato.INTEGER, value)

# TODO JUAN MARCOS 
class Relop(Expression):
    '''
    Relop contiene los operadores logicos
    == != >= ...
    '''
    def __init__(self, value1, operador_logico, value2):
        self.value1 = value1
        self.operador_logico = operador_logico
        self.value2 = value2

    def __repr__(self):
        return str(vars(self))

class ExpressionsTime(Expression):
    '''
        ExpressionsTime
    '''
    def __init__(self, name_date, type_date, name_opt):
        self.name_date = name_date
        self.type_date = type_date
        self.name_opt = name_opt

    def __repr__(self):
        return str(vars(self))

class ExpressionsTrigonometric(Expression):
    '''
        ExpressionsTrigonometric
    '''
    def __init__(self, type_trigonometric, expression1, optional_expression2):
        self.type_trigonometric = type_trigonometric
        self.expression1 = expression1
        self.optional_expression2 = optional_expression2

    def __repr__(self):
        return str(vars(self))
# TODO JUAN MARCOS 
class ExpressionsGreastLeast(Expression):
    '''
        ExpressionsGreastLeast
    '''
    def __init__(self, type_expression, lista_arr):
        self.type_expression = type_expression
        self.lista_arr = lista_arr
    def __repr__(self):
        return str(vars(self))
# TODO JUAN MARCOS 
class MathematicalExpressions(Expression):
    '''
        MathematicalExpressions
    '''
    def __init__(self, type_expression, lista_arr, optional_alias):
        self.type_expression = type_expression
        self.lista_arr = lista_arr
        self.optiona_alias = optional_alias
    
    def __repr__(self):
        return str(vars(self))

class UnaryOrSquareExpressions(Expression):
    '''
    UnaryOrSquareExpressions
    '''
    def __init__(self, sign, expression_list):
        self.sign = sign
        self.expression_list = expression_list
    
    def __repr__(self):
        return str(vars(self))


class LogicalOperators(Expression):
    '''
    LogicalOperators
    '''
    def __init__(self, value1, logical_operator, value2):
        self.value1 = value1
        self.logical_operator = logical_operator
        self.value2 = value2

    def __repr__(self):
        return str(vars(self))


class NumberExpression(Expression):
    def __init__(self, type, value):
        self.value = value
        self.type = type
    def procces(self, object):
        return self

    def __repr__(self):
        return str(vars(self))

class StringExpression(Expression):
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def procces(self):
        return self
    
    def __repr__(self):
        return str(vars(self))