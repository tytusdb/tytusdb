from models.objects.columns_select import ColumnsSelect
from models.objects.id import Id
from models.objects.table_select import TablaSelect
from models.instructions.DML.special_functions import search_duplicate_symbol, search_symbol
from controllers.symbol_table import SymbolTable
import math
from abc import abstractmethod
from datetime import datetime, time
from math import *
from models.instructions.Expression.type_enum import *
import re

class Expression:
    @abstractmethod
    def process(self):
        pass

class ArithmeticBinaryOperation(Expression):
    '''
        Una operacion binaria recibe, sus dos operandos y el operador
    '''
    def __init__(self, value1, value2, operador, op, line, column) :
        self.value1 = value1
        self.value2 = value2
        self.operador = operador
        self.line = line 
        self.column = column
        self.alias = str(self.value1.alias) + str(op) + str(self.value2.alias)

    def __repr__(self):
        return str(vars(self))
    
    def process(self, expression):
        value1 = self.value1.process(expression)
        value2 = self.value2.process(expression)
        operador = self.operador
        if value1.data_type != DATA_TYPE.NUMBER and value2.data_type != DATA_TYPE.NUMBER:
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
        
        return PrimitiveData(DATA_TYPE.NUMBER, value, self.line, self.column)

    
class Relop(Expression):
    '''
    Relop contiene los operadores logicos
    == != >= ...
    Devuelve un valor booleano
    '''
    def __init__(self, value1, operator, value2, op, line, column):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2
        self.op = op
        self.line = line
        self.column = column
        self.alias = f'{str(self.value1.alias)}  {str(op)}  {str(self.value2.alias)}'

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        value1 = self.value1.process(expression)
        value2 = self.value2.process(expression)
        operator = self.operator
        try:
            value = 0
            if isinstance(value1,PrimitiveData) and isinstance(value2, PrimitiveData):
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
                return PrimitiveData(DATA_TYPE.BOOLEANO, value, self.line, self.column)
            else:
                data = ""
                if isinstance(value1, list):
                    if isinstance(value2.value, int):
                        if self.op == "=":
                            data = f'{value1[1]} {self.op}= {str(value2.value)}'
                            return data
                        else:
                            data = f'{value1[1]} {self.op} {str(value2.value)}'
                            return data
                    else:
                        if self.op == "=":
                            data = f'{value1[1]} {self.op}= "{str(value2.value)}"'
                            return data
                        else:
                            data = f'{value1[1]} {self.op} {str(value2.value)}'
                            return data
                elif isinstance(value2, list):
                    if isinstance(value1.value, int):
                        if self.op == "=":
                            data = f'{value2[1]} {self.op}= {str(value1.value)}'
                            return data
                        else:
                            data = f'{value2[1]} {self.op} {str(value1.value)}'
                            return data
                    else:
                        if self.op == "=":
                            data = f'{value2[1]} {self.op}= "{str(value1.value)}"'
                            return data
                        else:
                            data = f'{value2[1]} {self.op} {str(value1.value)}'
                            return data
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- Relop")


class Identifiers(Expression):
    def __init__(self, value, line, column):
        self.value = value
        self.line = line
        self.column = column
        self.alias = f'{self.value}'
        
    def __repr__(self):
        return str(vars(self))
    
    def process(self, expression):
        symbol = search_symbol(self.value)
        if symbol == None:
            if search_duplicate_symbol(self.value, None):
                return PrimitiveData(DATA_TYPE.STRING,self.value, self.line, self.column)
            else:
                SymbolTable().add(Id(self.value), self.value,'ID', None, None, self.line, self.column)
                return PrimitiveData(DATA_TYPE.STRING,self.value, self.line, self.column)
        else:
            if isinstance(symbol.name, TablaSelect):
                return PrimitiveData(DATA_TYPE.STRING, self.value, self.line, self.column)
            elif isinstance(symbol.name, ColumnsSelect):
                return [symbol.name.values, symbol.value]
        return None
    
class ExpressionsTime(Expression):
    '''
        ExpressionsTime
    '''
    def __init__(self, name_date, type_date, name_opt,name_date2,line, column):
        self.name_date = name_date
        self.type_date = type_date
        self.name_opt = name_opt
        self.line = line
        self.column = column
        self.alias = f'{name_date2}'


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
            if name_opt.value == 'now':
                current_time = datetime.now().strftime('%Y-%B-%A  %H:%M:%S')
            else:
                time_data = self.method_for_timestamp(name_opt.value)
                current_time = str(datetime(time_data[0], time_data[1], time_data[2], time_data[3], time_data[4], time_data[5]))
        return PrimitiveData(DATA_TYPE.STRING, current_time, self.line, self.column)
        
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
    def __init__(self, type_trigonometric, expression1, optional_expression2,line, column):
        self.type_trigonometric = type_trigonometric
        self.expression1 = expression1
        self.optional_expression2 = optional_expression2
        self.line = line
        self.column = column
        self.alias = str(self.type_trigonometric)
        
    def __repr__(self):
        return str(vars(self))
    def process(self, expression):
        type_trigo = self.type_trigonometric
        exp1 = None
        exp2 = None
        result = 0
        if isinstance(self.expression1, PrimitiveData):
            exp1 = self.expression1.process(expression)
        if isinstance(self.optional_expression2, PrimitiveData):
            exp2 = self.optional_expression2.process(expression)
        if type_trigo.lower() == "acos":
            result = round(acos(float(exp1.value)), 4)
        elif type_trigo.lower() == 'acosd':
            result = round(degrees(acos(float(exp1.value))), 4)
        elif type_trigo.lower() == 'asin':
            result = round(asin(float(exp1.value)), 4)
        elif type_trigo.lower() == 'asind':
            result = round(degrees(asin(float(exp1.value))), 4)
        elif type_trigo.lower() == 'atan':
            result = round(atan(float(exp1.value)), 4)
        elif type_trigo.lower() == 'atand':
            result = round(degrees(atan(float(exp1.value))), 4)
        elif type_trigo.lower() == 'atan2':
            result = round(atan2(float(exp1.value), float(exp2.value)), 4)
        elif type_trigo.lower() == 'atan2d':
            result = round(degrees(atan2(float(exp1.value), float(exp2.value))), 4)
        elif type_trigo.lower() == 'cos':
            result = round(cos(float(exp1.value)), 4)
        elif type_trigo.lower() == 'cosd':
            result = round(degrees(cos(float(exp1.value))), 4)
        elif type_trigo.lower() == 'cot':
            result = round(1/(tan(float(exp1.value))), 4)
        elif type_trigo.lower() == 'cotd':
            result = round(degrees(1/(tan(float(exp1.value)))), 4)
        elif type_trigo.lower() == 'sin':
            result = round(sin(float(exp1.value)), 4)
        elif type_trigo.lower() == 'sind':
            result = round(degrees(sin(float(exp1.value))), 4)
        elif type_trigo.lower() == 'tan':
            result = round(tan(float(exp1.value)), 4)
        elif type_trigo.lower() == 'tand':
            result = round(degrees(tan(float(exp1.value))), 4)
        elif type_trigo.lower() == 'cosh':
            result = round(cosh(float(exp1.value)), 4)
        elif type_trigo.lower() == 'sinh':
            result = round(sinh(float(exp1.value)), 4)
        elif type_trigo.lower() == 'tanh':
            result = round(tanh(float(exp1.value)), 4)
        elif type_trigo.lower() == 'acosh':
            result = round(acosh(float(exp1.value)),4)
        elif type_trigo.lower() == 'asinh':
            result = round(asinh(float(exp1.value)),4)
        elif type_trigo.lower() == 'atanh':
            result = round(atanh(float(exp1.value)),4)
        return PrimitiveData(DATA_TYPE.NUMBER, result, self.line, self.column)


class UnaryOrSquareExpressions(Expression):
    '''
    UnaryOrSquareExpressions
    '''
    def __init__(self, sign, value,line, column, sign1):
        self.sign = sign
        self.value = value
        self.line = line
        self.column = column
        self.alias = str(sign1) + str(self.value.alias)
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, expression):
        expression1 = self.value.process(expression)
        type_unary_or_other = self.sign
        if expression1.data_type != DATA_TYPE.NUMBER:
            print('error')
            return
        result = 0
        if type_unary_or_other == SymbolsUnaryOrOthers.UMINUS or type_unary_or_other == SymbolsUnaryOrOthers.BITWISE_NOT:
            result = expression1.value * -1
        elif type_unary_or_other == SymbolsUnaryOrOthers.UPLUS:
            result = expression1.value * 1
        elif type_unary_or_other == SymbolsUnaryOrOthers.SQUARE_ROOT:
            result = round(math.sqrt(expression1.value), 2)
        elif type_unary_or_other == SymbolsUnaryOrOthers.CUBE_ROOT:
            result = round(expression1.value**(1/3), 2)
        return PrimitiveData(DATA_TYPE.NUMBER, result, self.line, self.column)


class LogicalOperators(Expression):
    '''
        LogicalOperators
    '''
    def __init__(self, value1, operator, value2,line, column):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2
        self.line = line
        self.column = column
        self.alias = f'{str(self.value1.alias)}  {str(self.operator)}  {str(self.value2.alias)}'

    def __repr__(self):
        return str(vars(self))
        
    def process(self, expression):
        value1 = self.value1.process(expression)
        value2 = self.value2.process(expression)
        operator = self.operator
        try:
            value = 0
            if isinstance(value1, PrimitiveData) and isinstance(value2, PrimitiveData):
                if operator.lower() == "and":
                    value = value1.value and value2.value
                elif operator.lower() == "or":
                    value = value1.value or value2.value
                else:
                    print("Operador no valido: " + operator)
                    return
                return PrimitiveData(DATA_TYPE.BOOLEANO, value, self.line, self.column)
            else:
                data = ""
                if operator.lower() == 'and':
                    data = f'({value1}) and ({value2})'
                    return data
                elif operator.lower() == 'or':
                    data = f'({value1})  or ({value2})'
                    return data
                else:
                    print("Operador no valido: " + operator)
                    return
        except TypeError:
            print("Error de tipo")
            print(self)
            return
        except:
            print("FATAL ERROR, ni idea porque murio, F --- LogicalOperators")


class PrimitiveData(Expression):
    """
    Esta clase contiene los tipos primitivos
    de datos como STRING, NUMBER, BOOLEAN
    """

    def __init__(self, data_type, value, line, column):
        self.data_type = data_type
        self.value = value
        self.alias = str(self.value)
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        return self