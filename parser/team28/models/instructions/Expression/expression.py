import math
from abc import abstractmethod
from datetime import datetime, time
from math import *
from models.instructions.Expression.type_enum import *
import re

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
            if operator == SymbolsRelop.LESS_THAN:
                value = value1.value < value2.value
            elif operator == SymbolsRelop.GREATE_THAN:
                value = value1.value > value2.value
            elif operator == SymbolsRelop.GREATE_EQUAL:
                value = value1.value >= value2.value
            elif operator == SymbolsRelop.LESS_EQUAL:
                value = value1.value <= value2.value
            elif operator == SymbolsRelop.EQUALS:
                value = value1.value == value2.value
            elif operator == SymbolsRelop.NOT_EQUAL or operator == SymbolsRelop.NOT_EQUAL_LR:
                value = value1.value != value2.value
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

    def process(self, expression):
        name_date =  self.name_date
        type_date = ""
        name_opt = ""
        current_time = ""
        
        if isinstance(self.type_date, PrimitiveData):
            type_date = self.type_date.process(expression)
        if isinstance(self.name_opt, PrimitiveData):
            name_opt = self.name_opt.process(expression)


        if name_date == SymbolsTime.CURRENT_TIME:
            current_time = datetime.now().strftime('%H:%M:%S')
        elif name_date == SymbolsTime.CURRENT_DATE:
            current_time = datetime.now().strftime('%Y-%B-%A')
        elif name_date == SymbolsTime.NOW:
            current_time = datetime.now().strftime('%Y-%B-%A  %H:%M:%S')
        elif name_date == SymbolsTime.EXTRACT:
            if type_date.value.lower() == "YEAR".lower():
                match = re.search('\d{4}', name_opt.value)
                current_time = datetime.strptime(match.group(), '%Y').year
            elif type_date.value.lower() == "MONTH".lower():
                match = re.search('\d{4}-\d{2}-\d{2}', name_opt.value)
                current_time = datetime.strptime(match.group(), '%Y-%m-%d').month
            elif type_date.value.lower() == "DAY".lower():
                match = re.search('\d{4}-\d{2}-\d{2}', name_opt.value)
                current_time = datetime.strptime(match.group(), '%Y-%m-%d').day
            elif type_date.value.lower() == "HOUR".lower():
                match = re.search('\d{2}:\d{2}:\d{2}', name_opt.value)
                current_time = datetime.strptime(match.group(), '%H:%M:%S').hour
            elif type_date.value.lower() == "MINUTE".lower():
                match = re.search('\d{2}:\d{2}:\d{2}', name_opt.value)
                current_time = datetime.strptime(match.group(), '%H:%M:%S').minute
            elif type_date.value.lower() == "SECOND".lower():
                match = re.search('\d{2}:\d{2}:\d{2}', name_opt.value)
                current_time = datetime.strptime(match.group(), '%H:%M:%S').second
        elif name_date == SymbolsTime.DATE_PART:
            # TODO Pendiente 
            pass
        elif name_date == SymbolsTime.TIMESTAMP:
            time_data = self.method_for_timestamp(name_opt.value)
            current_time = str(datetime(time_data[0], time_data[1], time_data[2], time_data[3], time_data[4], time_data[5]))
        return PrimitiveData(DATA_TYPE.STRING, current_time)
        
    def method_for_timestamp(self, fecha):
        data_time = ""
        list_data_time = []
        for index, data in enumerate(fecha):
            if data == '\t' or data == '\r' or data == '\b' or data == '\f' or data == ' ':
                pass
            elif data != '-' and not (data == ':'):
                data_time += data
                if len(data_time) == 4:
                    list_data_time.append(int(data_time))
                    data_time = ""
                elif len(data_time) == 2 and len(list_data_time) != 0:
                    list_data_time.append(int(data_time))
                    data_time = ""
            elif data != ':' and not (data == "-"):
                data_time += data
                if len(data_time) == 2 and len(list_data_time) != 0:
                    list_data_time.append(int(data_time))
                    data_time = ""
        return list_data_time

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
    
#     def execute(self):
#         return self
    
#     def __repr__(self):
#         return str(vars(self))
