from abc import abstractmethod
from enum import Enum
import pandas as pd
from datetime import datetime

from analizer.functions import MathFunctions as mf
from analizer.functions import TrigonometricFunctions as trf
from analizer.functions import StringFunctions as strf

# import abstract.select_data as data

# Prueba para dataframe:
# df = data.dataSelect()
# df.crossJoin()


class TYPE(Enum):
    NUMBER = 1
    STRING = 2
    BOOLEAN = 3


class ERROR(Enum):
    TYPEERROR = 1
    OPERATORERROR = 2


class Expression:
    """
    Esta clase representa una expresión
    """

    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

    @abstractmethod
    def execute(self, environment):
        """
        Metodo que servira para ejecutar las expresiones
        """


class Primitive(Expression):
    """
    Esta clase contiene los tipos primitivos
    de datos como STRING, NUMBER, BOOLEAN
    """

    def __init__(self, type_, value, row, column):
        Expression.__init__(self, row, column)
        self.type = type_
        self.value = value
        self.temp = str(value)

    def execute(self, environment):
        return self


class Identifiers(Expression):
    """
    Esta clase representa los nombre de columnas
    """

    value = None
    # TODO: implementar la funcion para obtener el type de la columna
    def __init__(self, table, name, df, row, column):
        Expression.__init__(self, row, column)
        self.table = table
        self.name = name
        self.df = df
        if table == None:
            self.temp = name
        else:
            self.temp = table + "." + name
        self.type = TYPE.NUMBER

    def execute(self, environment):
        """
        TODO:Se debe hacer la logica para buscar los identificadores en la tabla
        """
        col = ""
        if self.table == None:
            col = self.name
        else:
            col = self.table + "." + self.name
        self.value = self.df[col]
        return self


class UnaryArithmeticOperation(Expression):
    """
    Esta clase recibe un parametro de expresion
    para realizar operaciones unarias
    """

    def __init__(self, exp, operator, row, column):
        Expression.__init__(self, row, column)
        self.exp = exp
        self.operator = operator
        self.temp = str(operator) + exp.temp

    def execute(self, environment):
        exp = self.exp.execute(environment)
        operator = self.operator

        if exp.type != TYPE.NUMBER:
            return ErrorUnaryOperation(exp.value, self.row, self.column)

        if operator == "+":
            value = exp.value
        elif operator == "-":
            value = exp.value * -1
        else:
            return ErrorOperatorExpression(operator, self.row, self.column)
        return Primitive(TYPE.NUMBER, value, self.row, self.column)


class BinaryArithmeticOperation(Expression):
    """
    Esta clase recibe dos parametros de expresion
    para realizar operaciones entre ellas
    """

    def __init__(self, exp1, exp2, operator, row, column):
        Expression.__init__(self, row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.temp = exp1.temp + str(operator) + exp2.temp

    def execute(self, environment):
        exp1 = self.exp1.execute(environment)
        exp2 = self.exp2.execute(environment)
        operator = self.operator

        if exp1.type != TYPE.NUMBER or exp2.type != TYPE.NUMBER:
            return ErrorBinaryOperation(exp1.value, exp2.value, self.row, self.column)
        if operator == "+":
            value = exp1.value + exp2.value
        elif operator == "-":
            value = exp1.value - exp2.value
        elif operator == "*":
            value = exp1.value * exp2.value
        elif operator == "/":
            value = exp1.value / exp2.value
        elif operator == "^":
            value = exp1.value ** exp2.value
        elif operator == "%":
            value = exp1.value % exp2.value
        else:
            return ErrorOperatorExpression(operator, self.row, self.column)
        return Primitive(TYPE.NUMBER, value, self.row, self.column)


class BinaryRelationalOperation(Expression):
    """
    Esta clase contiene las expresiones binarias de comparacion
    que devuelven un booleano.
    """

    def __init__(self, exp1, exp2, operator, row, column):
        Expression.__init__(self, row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.temp = exp1.temp + str(operator) + exp2.temp

    def execute(self, environment):
        exp1 = self.exp1.execute(environment)
        exp2 = self.exp2.execute(environment)
        operator = self.operator
        try:
            if operator == "<":
                value = exp1.value < exp2.value
            elif operator == ">":
                value = exp1.value > exp2.value
            elif operator == ">=":
                value = exp1.value >= exp2.value
            elif operator == "<=":
                value = exp1.value <= exp2.value
            elif operator == "=":
                value = exp1.value == exp2.value
            elif operator == "!=":
                value = exp1.value != exp2.value
            elif operator == "<>":
                value = exp1.value != exp2.value
            elif operator == "ISDISTINCTFROM":
                value = exp1.value != exp2.value
            elif operator == "ISNOTDISTINCTFROM":
                value = exp1.value == exp2.value
            else:
                return ErrorOperatorExpression(operator, self.row, self.column)
            return Primitive(TYPE.BOOLEAN, value, self.row, self.column)
        except TypeError:
            return ErrorBinaryOperation(exp1.value, exp2.value, self.row, self.column)
        except:
            print("Error fatal BinaryRelationalOperation")


comps = {
    "ISNULL": "IS NULL",
    "NOTNULL": "NOT NULL",
    "ISTRUE": "IS TRUE",
    "ISFALSE": "IS FALSE",
    "ISUNKNOWN": "IS UNKNOWN",
    "ISNOTNULL": "IS NOT NULL",
    "ISNOTTRUE": "IS NOT TRUE",
    "ISNOTFALSE": "IS NOT FALSE",
    "ISNOTUNKNOWN": "IS NOT UNKNOWN",
    "BETWEEN": "BETWEEN",
    "NOTBETWEEN": "NOT BETWEEN",
    "BETWEENSYMMETRIC": "BETWEEN SYMMETRIC",
}


class UnaryRelationalOperation(Expression):
    """
    Esta clase contiene las expresiones unarias de comparacion
    que devuelven un booleano.
    """

    def __init__(self, exp, operator, row, column):
        Expression.__init__(self, row, column)
        self.exp = exp
        self.operator = operator
        self.temp = exp.temp + " " + comps.get(operator)

    def execute(self, environment):
        exp = self.exp.execute(environment)
        operator = self.operator
        try:
            if operator == "ISNULL":
                value = exp.value == None
            elif operator == "NOTNULL":
                value = exp.value != None
            elif operator == "ISTRUE":
                value = exp.value == True
            elif operator == "ISFALSE":
                value = exp.value == False
            elif operator == "ISUNKNOWN":
                value = exp.value == None
            elif operator == "ISNOTNULL":
                value = exp.value != None
            elif operator == "ISNOTTRUE":
                value = exp.value != True
            elif operator == "ISNOTFALSE":
                value = exp.value != False
            elif operator == "ISNOTUNKNOWN":
                value = exp.value != None
            else:
                return ErrorOperatorExpression(operator, self.row, self.column)
            return Primitive(TYPE.BOOLEAN, value, self.row, self.column)
        except TypeError:
            return ErrorUnaryOperation(exp.value, self.row, self.column)
        except:
            print("Error fatal UnaryRelationalOperation")


class TernaryRelationalOperation(Expression):
    """
    Esta clase contiene las expresiones ternarias de comparacion
    que devuelven un booleano.
    """

    def __init__(self, exp1, exp2, exp3, operator, row, column):
        Expression.__init__(self, row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.operator = operator
        self.temp = (
            exp1.temp
            + " "
            + comps.get(operator)
            + " "
            + self.exp2.temp
            + " AND "
            + self.exp3.temp
        )

    def execute(self, environment):
        exp1 = self.exp1.execute(environment)
        exp2 = self.exp2.execute(environment)
        exp3 = self.exp3.execute(environment)
        operator = self.operator
        try:
            if operator == "BETWEEN":
                value = exp1.value > exp2.value and exp1.value < exp3.value
            elif operator == "NOTBETWEEN":
                value = not (exp1.value > exp2.value and exp1.value < exp3.value)
            elif operator == "BETWEENSYMMETRIC":
                t1 = exp1.value > exp2.value and exp1.value < exp3.value
                t2 = exp1.value < exp2.value and exp1.value > exp3.value
                value = t1 or t2
            else:
                return ErrorOperatorExpression(operator, self.row, self.column)
            return Primitive(TYPE.BOOLEAN, value, self.row, self.column)
        except TypeError:
            return ErrorTernaryOperation(
                exp1.value, exp2.value, exp3.value, self.row, self.column
            )
        except:
            print("Error fatal TernaryRelationalOperation")


class BinaryLogicalOperation(Expression):
    """
    Esta clase contiene las expresiones booleanas binarias.
    """

    def __init__(self, exp1, exp2, operator, row, column):
        Expression.__init__(self, row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.temp = exp1.temp + " " + str(operator) + " " + exp2.temp

    def execute(self, environment):
        exp1 = self.exp1.execute(environment)
        exp2 = self.exp2.execute(environment)
        operator = self.operator

        if exp1.type != TYPE.BOOLEAN or exp2.type != TYPE.BOOLEAN:
            return ErrorBinaryOperation(exp1.value, exp2.value, self.row, self.column)

        if isinstance(exp1.value, pd.core.series.Series) or isinstance(
            exp2.value, pd.core.series.Series
        ):
            if operator == "AND":
                value = exp1.value & exp2.value
            elif operator == "OR":
                value = exp1.value | exp2.value
            else:
                return ErrorOperatorExpression(operator, self.row, self.column)
        else:
            if operator == "AND":
                value = exp1.value and exp2.value
            elif operator == "OR":
                value = exp1.value or exp2.value
            else:
                return ErrorOperatorExpression(operator, self.row, self.column)
        return Primitive(TYPE.BOOLEAN, value, self.row, self.column)


class UnaryLogicalOperation(Expression):
    """
    Esta clase contiene las expresiones booleanas unarias.
    """

    def __init__(self, exp, operator, row, column):
        Expression.__init__(self, row, column)
        self.exp = exp
        self.operator = operator
        self.temp = str(operator) + " " + exp.temp

    def execute(self, environment):
        exp = self.exp.execute(environment)
        operator = self.operator
        # MOMO IF OPERADORES
        if exp.type != TYPE.BOOLEAN:
            return ErrorUnaryOperation(exp.value, self.row, self.column)

        if isinstance(exp.value, pd.core.series.Series):
            if operator == "NOT":
                value = ~exp.value
            elif operator == "ISTRUE":
                value = exp.value == True
            elif operator == "ISFALSE":
                value = exp.value == False
            elif operator == "ISUNKNOWN":
                value = exp.value == None
            elif operator == "ISNOTTRUE":
                value = exp.value != True
            elif operator == "ISNOTFALSE":
                value = exp.value != False
            elif operator == "ISNOTUNKNOWN":
                value = exp.value != None
            else:
                return ErrorOperatorExpression(operator, self.row, self.column)
        else:
            if operator == "NOT":
                value = not exp.value
            elif operator == "ISTRUE":
                value = exp.value == True
            elif operator == "ISFALSE":
                value = exp.value == False
            elif operator == "ISUNKNOWN":
                value = exp.value == None
            elif operator == "ISNOTTRUE":
                value = exp.value != True
            elif operator == "ISNOTFALSE":
                value = exp.value != False
            elif operator == "ISNOTUNKNOWN":
                value = exp.value != None
            else:
                return ErrorOperatorExpression(operator, self.row, self.column)
        return Primitive(TYPE.BOOLEAN, value, self.row, self.column)


class ErrorBinaryOperation(Expression):
    """
    Reporta error de una expresion
    """

    def __init__(self, exp1, exp2, row, column):
        Expression.__init__(self, row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.error = (
            "No se pudo concretar la operacion entre " + str(exp1) + " : " + str(exp2)
        )
        self.type = ERROR.TYPEERROR

    def execute(self, environment):
        print(self.error)


class ErrorTernaryOperation(Expression):
    """
    Reporta error de una expresion
    """

    def __init__(self, exp1, exp2, exp3, row, column):
        Expression.__init__(self, row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.error = (
            "No se pudo concretar la operacion entre "
            + str(exp1)
            + " : "
            + str(exp2)
            + " : "
            + str(exp3)
        )
        self.type = ERROR.TYPEERROR

    def execute(self, environment):
        print(self.error)


class ErrorUnaryOperation(Expression):
    """
    Reporta error de una expresion
    """

    def __init__(self, exp, row, column):
        Expression.__init__(self, row, column)
        self.exp = exp
        self.error = "No se pudo concretar la operacion con " + str(exp)
        self.type = ERROR.TYPEERROR

    def execute(self, environment):
        print(self.error)


class ErrorOperatorExpression(Expression):
    """
    Reporta error de operador
    """

    def __init__(self, operator, row, column):
        Expression.__init__(self, row, column)
        self.operator = operator
        self.error = "No se pudo encontrar el operador: " + operator
        self.type = ERROR.OPERATORERROR

    def execute(self, environment):
        print(self.error)


class FunctionCall(Expression):
    """
    Esta clase contiene las llamadas a funciones
    """

    def __init__(self, function, params, row, column):
        Expression.__init__(self, row, column)
        self.function = function.lower()
        self.params = params
        self.temp = str(function) + "("
        for t in params:
            self.temp += t.temp
        self.temp += ")"

    # TODO: Agregar un error de parametros incorrectos
    def execute(self, environment):
        try:
            valores = []
            for p in self.params:
                val = p.execute(environment).value
                if isinstance(val, pd.core.series.Series):
                    val = val.tolist()
                valores.append(val)

            if self.function == "abs":
                value = mf.absolute(*valores)
            elif self.function == "cbrt":
                value = mf.cbrt(*valores)
            elif self.function == "ceil":
                value = mf.ceil(*valores)
            elif self.function == "ceiling":
                value = mf.ceiling(*valores)
            elif self.function == "degrees":
                value = mf.degrees(*valores)
            elif self.function == "div":
                value = mf.div(*valores)
            elif self.function == "exp":
                value = mf.exp(*valores)
            elif self.function == "factorial":
                value = mf.factorial(*valores)
            elif self.function == "floor":
                value = mf.floor(*valores)
            elif self.function == "gcd":
                value = mf.gcd(*valores)
            elif self.function == "lcm":
                value = mf.lcm(*valores)
            elif self.function == "ln":
                value = mf.ln(*valores)
            elif self.function == "log":
                value = mf.log(*valores)
            elif self.function == "log10":
                value = mf.log10(*valores)
            elif self.function == "mod":
                value = mf.mod(*valores)
            elif self.function == "pi":
                value = mf.pi()
            elif self.function == "power":
                value = mf.pow(*valores)
            elif self.function == "radians":
                value = mf.radians(*valores)
            elif self.function == "round":
                value = mf.round(*valores)
            elif self.function == "sign":
                value = mf.sign(*valores)
            elif self.function == "sqrt":
                value = mf.sqrt(*valores)
            elif self.function == "trunc":
                value = mf.truncate_col(*valores)
            elif self.function == "width_bucket":
                value = mf.with_bucket(*valores)
            elif self.function == "random":
                value = mf.random_()
            elif self.function == "acos":
                value = trf.acos(*valores)
            elif self.function == "acosd":
                value = trf.acosd(*valores)
            elif self.function == "asin":
                value = trf.asin(*valores)
            elif self.function == "asind":
                value = trf.asind(*valores)
            elif self.function == "atan":
                value = trf.atan(*valores)
            elif self.function == "atand":
                value = trf.atand(*valores)
            elif self.function == "atan2":
                value = trf.atan2(*valores)
            elif self.function == "atan2d":
                value = trf.atan2d(*valores)
            elif self.function == "cos":
                value = trf.cos(*valores)
            elif self.function == "cosd":
                value = trf.cosd(*valores)
            elif self.function == "cot":
                value = trf.cot(*valores)
            elif self.function == "cotd":
                value = trf.cotd(*valores)
            elif self.function == "sin":
                value = trf.sin(*valores)
            elif self.function == "sind":
                value = trf.sind(*valores)
            elif self.function == "tan":
                value = trf.tan(*valores)
            elif self.function == "tand":
                value = trf.tand(*valores)
            elif self.function == "sinh":
                value = trf.sinh(*valores)
            elif self.function == "cosh":
                value = trf.cosh(*valores)
            elif self.function == "tanh":
                value = trf.tanh(*valores)
            elif self.function == "asinh":
                value = trf.asinh(*valores)
            elif self.function == "acosh":
                value = trf.acosh(*valores)
            elif self.function == "atanh":
                value = trf.atanh(*valores)
            elif self.function == "length":
                value = strf.length(*valores)
            elif self.function == "substring":
                value = strf.substring(*valores)
            elif self.function == "trim":
                value = strf.trim_(*valores)
            elif self.function == "get_byte":
                value = strf.get_byte(*valores)
            elif self.function == "md5":
                value = strf.md5(*valores)
            elif self.function == "set_byte":
                value = strf.set_byte(*valores)
            elif self.function == "sha256":
                value = strf.sha256(*valores)
            elif self.function == "substr":
                value = strf.substring(*valores)
            elif self.function == "convert_date":
                value = strf.convert_date(*valores)
            elif self.function == "convert_int":
                value = strf.convert_int(*valores)
            elif self.function == "encode":
                value = strf.encode(*valores)
            elif self.function == "decode":
                value = strf.decode(*valores)
            elif self.function == "now":
                value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            else:
                # TODO: Agregar un error de funcion desconocida
                value = valores[0]
            if isinstance(value, list):
                if len(value) <= 1:
                    value = value[0]
                else:
                    value = pd.Series(value)

            return Primitive(TYPE.NUMBER, value, self.row, self.column)
        except TypeError:
            print("Error de tipos en llamada a funciones")
        except:
            print("Error desconocido")


class ExtractDate(Expression):
    def __init__(self, opt, type, str, row, column):
        Expression.__init__(self, row, column)
        self.opt = opt
        self.type = type
        self.str = str.split()
        self.temp = "EXTRACT( " + opt + " FROM " + type + " " + str + " )"

    def execute(self, environment):
        try:
            if self.type == "TIMESTAMP":
                if self.str[0] == "now":
                    self.str = datetime.now().strftime("%Y/%m/%d %H:%M:%S").split()
                if self.opt == "YEAR":
                    val = self.str[0][:4]
                elif self.opt == "MONTH":
                    val = self.str[0][5:7]
                elif self.opt == "DAY":
                    val = self.str[0][8:10]
                elif self.opt == "HOUR":
                    val = self.str[1][:2]
                elif self.opt == "MINUTE":
                    val = self.str[1][3:5]
                elif self.opt == "SECOND":
                    val = self.str[1][6:8]
                else:
                    # ERROR
                    val = self.str
            elif self.type == "INTERVAL":
                if self.opt == "YEAR":
                    idx = self.str.index("years")
                    val = self.str[idx - 1]
                elif self.opt == "MONTH":
                    idx = self.str.index("months")
                    val = self.str[idx - 1]
                elif self.opt == "DAY":
                    idx = self.str.index("days")
                    val = self.str[idx - 1]
                elif self.opt == "HOUR":
                    idx = self.str.index("hours")
                    val = self.str[idx - 1]
                elif self.opt == "MINUTE":
                    idx = self.str.index("minutes")
                    val = self.str[idx - 1]
                elif self.opt == "SECOND":
                    idx = self.str.index("seconds")
                    val = self.str[idx - 1]
                else:
                    # ERROR
                    val = self.str
            else:
                val = self.str
                # ERROR
            return Primitive(TYPE.NUMBER, int(val), self.row, self.column)
        except TypeError:
            pass
        except ValueError:  # cuando no tiene el valor INTERVAL
            pass


class DatePart(Expression):
    def __init__(self, opt, type, str, row, column) -> None:
        super().__init__(row, column)
        self.opt = opt.lower()
        self.type = type
        self.str = str.split()
        self.temp = "date_part( " + opt + " , " + type + " " + str + " )"

    def execute(self, environment):
        try:
            if self.type == "TIMESTAMP":
                if self.str[0] == "now":
                    self.str = datetime.now().strftime("%Y/%m/%d %H:%M:%S").split()
                if self.opt == "years":
                    val = self.str[0][:4]
                elif self.opt == "months":
                    val = self.str[0][5:7]
                elif self.opt == "days":
                    val = self.str[0][8:10]
                elif self.opt == "hours":
                    val = self.str[1][:2]
                elif self.opt == "minutes":
                    val = self.str[1][3:5]
                elif self.opt == "seconds":
                    val = self.str[1][6:8]
                else:
                    # ERROR
                    val = self.str
            elif self.type == "DATE":
                if self.opt == "years":
                    val = self.str[0][:4]
                elif self.opt == "months":
                    val = self.str[0][5:7]
                elif self.opt == "days":
                    val = self.str[0][8:10]
                else:
                    # ERROR
                    val = self.str
            elif self.type == "TIME":
                if self.opt == "hours":
                    val = self.str[0][:4]
                elif self.opt == "minutes":
                    val = self.str[0][5:7]
                elif self.opt == "seconds":
                    val = self.str[0][8:10]
                else:
                    # ERROR
                    val = self.str
            elif self.type == "INTERVAL":
                if self.opt == "years":
                    idx = self.str.index("years")
                    val = self.str[idx - 1]
                elif self.opt == "months":
                    idx = self.str.index("months")
                    val = self.str[idx - 1]
                elif self.opt == "days":
                    idx = self.str.index("days")
                    val = self.str[idx - 1]
                elif self.opt == "hours":
                    idx = self.str.index("hours")
                    val = self.str[idx - 1]
                elif self.opt == "minutes":
                    idx = self.str.index("minutes")
                    val = self.str[idx - 1]
                elif self.opt == "seconds":
                    idx = self.str.index("seconds")
                    val = self.str[idx - 1]
                else:
                    # ERROR
                    val = self.str
            elif self.type == "NOW":
                self.str = datetime.now().strftime("%Y/%m/%d %H:%M:%S").split()
                if self.opt == "years":
                    val = self.str[0][:4]
                elif self.opt == "months":
                    val = self.str[0][5:7]
                elif self.opt == "days":
                    val = self.str[0][8:10]
                elif self.opt == "hours":
                    val = self.str[1][:2]
                elif self.opt == "minutes":
                    val = self.str[1][3:5]
                elif self.opt == "seconds":
                    val = self.str[1][6:8]
                else:
                    # ERROR
                    val = self.str
            else:
                val = self.str
                # ERROR
            return Primitive(TYPE.NUMBER, int(val), self.row, self.column)
        except TypeError:
            pass
        except ValueError:  # cuando no tiene el valor INTERVAL
            pass


class Current(Expression):
    def __init__(self, val, optStr, row, column) -> None:
        super().__init__(row, column)
        self.val = val
        self.optStr = optStr
        self.temp = val
        if optStr != None:
            self.temp += " " + optStr

    def execute(self, environment):

        try:
            if self.val == "CURRENT_DATE":
                value = datetime.now().strftime("%Y/%m/%d")
            elif self.val == "CURRENT_TIME":
                value = datetime.now().strftime("%H:%M:%S")
            elif self.val == "TIMESTAMP":
                if self.optStr == "now":
                    value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                else:
                    value = self.val
            else:
                # ERROR
                value = self.val
            return Primitive(TYPE.STRING, value, self.row, self.column)
        except:
            pass
