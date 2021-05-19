from parserT28.controllers.error_controller import ErrorController
from parserT28.controllers.three_address_code import ThreeAddressCode
from parserT28.models.objects.columns_select import ColumnsSelect
from parserT28.models.objects.id import Id
from parserT28.models.objects.table_select import TablaSelect
from parserT28.models.instructions.DML.special_functions import search_duplicate_symbol, search_symbol
from parserT28.controllers.symbol_table import SymbolTable
import math
from abc import abstractmethod
from datetime import datetime, time
from math import *
from parserT28.models.instructions.Expression.type_enum import *
import re


class Expression:
    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def compile(self):
        pass


def getOperador(operador):
    value = 0
    if operador == SymbolsAritmeticos.PLUS:
        value = "+"
    elif operador == SymbolsAritmeticos.MINUS:
        value = "-"
    elif operador == SymbolsAritmeticos.TIMES:
        value = "*"
    elif operador == SymbolsAritmeticos.DIVISON:
        value = "/"
    elif operador == SymbolsAritmeticos.EXPONENT:
        value = "**"
    elif operador == SymbolsAritmeticos.MODULAR:
        value = "%"
    elif operador == SymbolsAritmeticos.BITWISE_SHIFT_LEFT:
        value = "<<"
    elif operador == SymbolsAritmeticos.BITWISE_SHIFT_RIGHT:
        value = ">>"
    elif operador == SymbolsAritmeticos.BITWISE_AND:
        value = "&"
    elif operador == SymbolsAritmeticos.BITWISE_OR:
        value = "|"
    elif operador == SymbolsAritmeticos.BITWISE_XOR:
        value = "^"
    elif operador == SymbolsRelop.LESS_THAN:
        value = "<"
    elif operador == SymbolsRelop.GREATE_THAN:
        value = ">"
    elif operador == SymbolsRelop.GREATE_EQUAL:
        value = ">="
    elif operador == SymbolsRelop.LESS_EQUAL:
        value = "<="
    elif operador == SymbolsRelop.EQUALS:
        value = "=="
    elif operador == SymbolsRelop.NOT_EQUAL or operador == SymbolsRelop.NOT_EQUAL_LR:
        value = "!="
    return value


class ArithmeticBinaryOperation(Expression):
    '''
        Una operacion binaria recibe, sus dos operandos y el operador
    '''

    def __init__(self, value1, value2, operador, op, line, column):
        self.value1 = value1
        self.value2 = value2
        self.operador = operador
        self.line = line
        self.column = column
        self.alias = str(self.value1.alias) + str(op) + str(self.value2.alias)
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        value1 = self.value1.compile(environment)
        value2 = self.value2.compile(environment)
        try:
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = {value1.value} {getOperador(self.operador)} {value2.value}")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Error de tipo"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
        except:
            desc = "FATAL ERROR, ArithmeticBinaryOperation, no acepta ids"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def process(self, expression):
        value1 = self.value1.process(expression)
        value2 = self.value2.process(expression)
        operador = self.operador
        try:
            if value1.data_type != DATA_TYPE.NUMBER and value2.data_type != DATA_TYPE.NUMBER:
                desc = "FATAL ERROR, ArithmeticBinaryOperation, no acepta ids"
                ErrorController().add(34, 'Execution', desc, self.line, self.column)
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
        except TypeError:
            desc = "Error de tipo"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
        except:
            desc = "FATAL ERROR, ArithmeticBinaryOperation, no acepta ids"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


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
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        value1 = self.value1.compile(environment)
        value2 = self.value2.compile(environment)
        if isinstance(value1, PrimitiveData):
            if value1.data_type == DATA_TYPE.STRING:
                value1.value = f"\'{value1.value}\'"
        if isinstance(value1, PrimitiveData):
            if value2.data_type == DATA_TYPE.STRING:
                value2.value = f"\'{value2.value}\'"
        try:
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(
                f"{temporal} = {value1.value} {getOperador(self.operator)} {value2.value}")

            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except TypeError:
            desc = "Error de tipo"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
        except:
            desc = "FATAL ERROR, Relop, no acepta ids"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def process(self, expression):
        value1 = self.value1.process(expression)
        value2 = self.value2.process(expression)
        operator = self.operator
        try:
            value = 0
            if isinstance(value1, PrimitiveData) and isinstance(value2, PrimitiveData):
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
                if isinstance(value1, list) and isinstance(value2, list):
                    if self.op == "=":
                        lista_aux = []
                        lista_aux.append(value1[0])
                        lista_aux.append(value2[0])
                        data = f'{value1[1]}_y {self.op}= {value2[1]}_x'
                        return [lista_aux, data, value1[1]]
                    else:
                        lista_aux = []
                        lista_aux.append(value1[0])
                        lista_aux.append(value2[0])
                        data = f'{value1[1]}_y {self.op} {value2[1]}_x'
                        return [lista_aux, data, value1[1]]
                elif isinstance(value1, list):
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
                            data = f'{value1[1]} {self.op} "{str(value2.value)}"'
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
                            data = f'{value2[1]} {self.op} "{str(value1.value)}"'
                            return data
        except TypeError:
            desc = "Error de tipo"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
        except:
            desc = "FATAL ERROR, ni idea porque murio, F --- Relop"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class Identifiers(Expression):
    def __init__(self, value, line, column):
        self.value = value
        self.line = line
        self.column = column
        self.alias = f'{self.value}'
        self._tac = ''

    def __repr__(self):
        return str(vars(self))

    def compile(self, expression):
        return self.alias

    def process(self, expression):
        try:
            symbol = search_symbol(self.value)
            if symbol == None:
                if search_duplicate_symbol(self.value, None):
                    return PrimitiveData(DATA_TYPE.STRING, self.value, self.line, self.column)
                else:
                    SymbolTable().add(Id(self.value), self.value, 'ID',
                                      None, None, self.line, self.column)
                    return PrimitiveData(DATA_TYPE.STRING, self.value, self.line, self.column)
            else:
                if isinstance(symbol.name, TablaSelect):
                    return PrimitiveData(DATA_TYPE.STRING, self.value, self.line, self.column)
                elif isinstance(symbol.name, ColumnsSelect):
                    return [symbol.name.values, symbol.value]
        except:
            desc = "FATAL ERROR --- Identifiers"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class ExpressionsTime(Expression):
    '''
        ExpressionsTime
    '''

    def __init__(self, name_date, type_date, name_opt, name_date2, line, column):
        self.name_date = name_date
        self.type_date = type_date
        self.name_opt = name_opt
        self.line = line
        self.column = column
        self.alias = f'{name_date2}'
        self._tac = ""

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        name_date = self.name_date
        type_date = ""
        name_opt = ""
        current_time = ""
        try:
            if isinstance(self.type_date, PrimitiveData):
                type_date = self.type_date.process(expression)
            if isinstance(self.name_opt, PrimitiveData):
                name_opt = self.name_opt.process(expression)

            if name_date == SymbolsTime.CURRENT_TIME:
                current_time = datetime.now().strftime('%H:%M:%S')
            elif name_date == SymbolsTime.CURRENT_DATE:
                current_time = datetime.now().strftime('%Y-%B-%A')
            elif name_date == SymbolsTime.NOW:
                current_time = datetime.now().strftime('%Y/%m/%d  %H:%M:%S')
            elif name_date == SymbolsTime.EXTRACT:
                if type_date.value.lower() == "YEAR".lower():
                    match = re.search('\d{4}', name_opt.value)
                    current_time = datetime.strptime(match.group(), '%Y').year
                elif type_date.value.lower() == "MONTH".lower():
                    match = re.search('\d{4}-\d{2}-\d{2}', name_opt.value)
                    current_time = datetime.strptime(
                        match.group(), '%Y-%m-%d').month
                elif type_date.value.lower() == "DAY".lower():
                    match = re.search('\d{4}-\d{2}-\d{2}', name_opt.value)
                    current_time = datetime.strptime(
                        match.group(), '%Y-%m-%d').day
                elif type_date.value.lower() == "HOUR".lower():
                    match = re.search('\d{2}:\d{2}:\d{2}', name_opt.value)
                    current_time = datetime.strptime(
                        match.group(), '%H:%M:%S').hour
                elif type_date.value.lower() == "MINUTE".lower():
                    match = re.search('\d{2}:\d{2}:\d{2}', name_opt.value)
                    current_time = datetime.strptime(
                        match.group(), '%H:%M:%S').minute
                elif type_date.value.lower() == "SECOND".lower():
                    match = re.search('\d{2}:\d{2}:\d{2}', name_opt.value)
                    current_time = datetime.strptime(
                        match.group(), '%H:%M:%S').second
            elif name_date == SymbolsTime.DATE_PART:
                # TODO Pendiente
                if type_date.value.lower() == 'years':
                    new_value = type_date.value + ",  " + name_opt.value
                    new_value = new_value.split()
                    current_time = new_value.index('years')
                    current_time = new_value[current_time - 1]
                elif type_date.value.lower() == 'months':
                    new_value = type_date.value + ",  " + name_opt.value
                    new_value = new_value.split()
                    current_time = new_value.index('months')
                    current_time = new_value[current_time - 1]
                elif type_date.value.lower() == 'days':
                    new_value = type_date.value + ",  " + name_opt.value
                    new_value = new_value.split()
                    current_time = new_value.index('days')
                    current_time = new_value[current_time - 1]
                elif type_date.value.lower() == 'hours':
                    new_value = type_date.value + ",  " + name_opt.value
                    new_value = new_value.split()
                    current_time = new_value.index('hours')
                    current_time = new_value[current_time - 1]
                elif type_date.value.lower() == 'minutes':
                    new_value = type_date.value + ",  " + name_opt.value
                    new_value = new_value.split()
                    current_time = new_value.index('minutes')
                    current_time = new_value[current_time - 1]
                elif type_date.value.lower() == 'seconds':
                    new_value = type_date.value + ",  " + name_opt.value
                    new_value = new_value.split()
                    current_time = new_value.index('seconds')
                    current_time = new_value[current_time - 1]
            elif name_date == SymbolsTime.TIMESTAMP:
                if name_opt.value == 'now':
                    current_time = datetime.now().strftime('%Y/%m/%d  %H:%M:%S')
                else:
                    time_data = self.method_for_timestamp(name_opt.value)
                    current_time = str(datetime(
                        time_data[0], time_data[1], time_data[2], time_data[3], time_data[4], time_data[5]))
            return PrimitiveData(DATA_TYPE.STRING, current_time, self.line, self.column)
        except:
            desc = "FATAL ERROR, ExpressionsTime, error con las fechas"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

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


class UnaryOrSquareExpressions(Expression):
    '''
    UnaryOrSquareExpressions
    '''

    def __init__(self, sign, value, line, column, sign1):
        self.sign = sign
        self.value = value
        self.line = line
        self.column = column
        self.alias = str(sign1) + str(self.value.alias)
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        expression1 = self.value.process(expression)
        type_unary_or_other = self.sign
        try:
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
        except:
            desc = "FATAL ERROR --- UnaryOrSquareExpressions"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self, expression):
        expression1 = self.value.compile(expression)
        type_unary_or_other = self.sign
        temporal = ThreeAddressCode().newTemp()

        try:
            if expression1.data_type != DATA_TYPE.NUMBER:
                print('error')
                return
            dataTemp = f"{temporal} = 0"

            if type_unary_or_other == SymbolsUnaryOrOthers.UMINUS or type_unary_or_other == SymbolsUnaryOrOthers.BITWISE_NOT:
                dataTemp = f"{temporal} = -{expression1.value}"

            elif type_unary_or_other == SymbolsUnaryOrOthers.UPLUS:
                dataTemp = f"{temporal} = {expression1.value}"

            elif type_unary_or_other == SymbolsUnaryOrOthers.SQUARE_ROOT:
                dataTemp = f"{temporal} = sqrt({expression1.value})  # |/"

            elif type_unary_or_other == SymbolsUnaryOrOthers.CUBE_ROOT:
                temporal1 = ThreeAddressCode().newTemp()
                ThreeAddressCode().addCode(f"{temporal1} = 1 / 3")
                dataTemp = f"{temporal} = {expression1.value} ** {temporal1} # ||/"

            ThreeAddressCode().addCode(dataTemp)
            return PrimitiveData(DATA_TYPE.NUMBER, temporal, self.line, self.column)
        except:
            desc = "FATAL ERROR --- UnaryOrSquareExpressions"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)


class LogicalOperators(Expression):
    '''
        LogicalOperators
    '''

    def __init__(self, value1, operator, value2, line, column):
        self.value1 = value1
        self.operator = operator
        self.value2 = value2
        self.line = line
        self.column = column
        self.alias = f'{str(self.value1.alias)}  {str(self.operator)}  {str(self.value2.alias)}'
        self._tac = self.alias

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        value1 = self.value1.compile(environment)
        value2 = self.value2.compile(environment)
        operator = self.operator

        temporal = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(
            f"{temporal} = {value1.value} {operator} {value2.value}")
        return PrimitiveData(DATA_TYPE.BOOLEANO, temporal, self.line, self.column)

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
                if isinstance(value1, list) and isinstance(value2, list):
                    if operator.lower() == 'and':
                        lista_temp = []
                        lista_temp.append(value1[2])
                        lista_temp.append(value2[2])
                        lista_temp = self.convert_unic_list2(lista_temp)
                        name_list = self.convert_unic_list(
                            value1[0], value2[0])
                        data = f'({value1[1]}) and ({value2[1]})'
                        return [name_list, data, lista_temp]
                    elif operator.lower() == 'or':
                        lista_temp = []
                        lista_temp.append(value1[2])
                        lista_temp.append(value2[2])
                        lista_temp = self.convert_unic_list2(lista_temp)
                        name_list = self.convert_unic_list(
                            value1[0], value2[0])
                        data = f'({value1[1]})  or ({value2[1]})'
                        return [name_list, data, lista_temp]
                    else:
                        print("Operador no valido: " + operator)
                        return
                else:
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
            desc = "FATAL ERROR --- LogicalOperators"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
        except:
            desc = "FATAL ERROR --- LogicalOperators"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def convert_unic_list(self, value1, value2):
        lista = []
        for data in value1:
            lista.append(data)
        for data in value2:
            lista.append(data)
        return lista

    def convert_unic_list2(self, list_temp):
        lista = []
        for data in list_temp:
            if isinstance(data, list):
                for data1 in data:
                    lista.append(data1)
            else:
                lista.append(data)
        return lista


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
        self._tac = self.alias

        if self.data_type == DATA_TYPE.STRING:
            self.alias = "\'" + self.alias + "\'"

    def __repr__(self):
        return str(vars(self))

    def process(self, expression):
        return self

    def compile(self, expression):
        return self
