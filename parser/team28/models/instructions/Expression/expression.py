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

class DATA_TYPE(Enum):
    NUMBER = 1
    STRING = 2
    CHAR = 3
    BOOLEANO = 4

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
    def execute(self):
        pass
    
class PrimitiveData(Expression):
    """
    Esta clase contiene los tipos primitivos
    de datos como STRING, NUMBER, BOOLEAN
    """

    def __init__(self, data_type, value):
        self.data_type = data_type
        self.value = value

    def execute(self, environment):
        return self

class ArithmeticBinaryOperation(Expression):
    '''
        Una operacion binaria recibe, sus dos operandos y el operador
    '''
    def __init__(self, value1, value2, operador) :
        self.value1 = value1
        self.value2 = value2
        self.operador = operador
    
    def __repr__(self):
        return str(vars(self))
    
    def execute(self, expression):
        value1 = self.value1.execute(expression)
        value2 = self.value2.execute(expression)
        operador = self.operador
        try:
            if value1.type == DATA_TYPE.NUMBER and value2.type == DATA_TYPE.NUMBER: #OPERACIONES MATEMATICAS
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
                return PrimitiveData(DATA_TYPE.NUMBER, value)
            else:
                print("Error de tipo")
                print(self)
                return   
        except:
            print("FATAL ERROR, ni idea porque murio, F")

        
class Relop(Expression):
    '''
    Relop contiene los operadores logicos
    == != >= ...
    Devuelve un valor booleano
    '''
    def __init__(self, value1, operator, value2):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2

    def __repr__(self):
        return str(vars(self))

    def execute(self, expression):
        value1 = self.value1.execute(expression)
        value2 = self.value2.execute(expression)
        operator = self.operator
        try:
            value = 0
            if operator == "<":
                value = value1 < value2
            elif operator == ">":
                value = value1 > value2
            elif operator == ">=":
                value = value1 >= value2
            elif operator == "<=":
                value = value1 <= value2
            elif operator == "=":
                value = value1 == value2
            elif operator == "!=":
                value = value1 != value2
            elif operator == "<>":
                value = value1 != value2
            else:
                print("Operador no valido: " + operator)
                return
            return PrimitiveData(DATA_TYPE.BOOLEANO, value)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Relop")

    
class LogicalOperators(Expression):
    '''
        LogicalOperators
    '''
    def __init__(self, value1, operator, value2):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2

    def __repr__(self):
        return str(vars(self))
    def execute(self, expression):
        value1 = self.value1.execute(expression)
        value2 = self.value2.execute(expression)
        operator = self.operator
        try:
            value = 0
            if operator == "AND":
                value = value1 & value2
            elif operator == "OR":
                value = value1 | value2
            else:
                print("Operador no valido: " + operator)
                return
            return PrimitiveData(DATA_TYPE.BOOLEANO, value)
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- LogicalOperators")

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

class UnaryOrSquareExpressions(Expression):
    '''
    UnaryOrSquareExpressions
    '''
    def __init__(self, sign, expression_list):
        self.sign = sign
        self.expression_list = expression_list
    
    def __repr__(self):
        return str(vars(self))

# class StringExpression(Expression):
#     def __init__(self, type, value):
#         self.type = type
#         self.value = value
    
#     def execute(self):
#         return self
    
#     def __repr__(self):
#         return str(vars(self))