from abc import abstractmethod
from enum import Enum

from analizer.functions import MathFunctions as mf
from analizer.functions import TrigonometricFunctions as trf


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
    Esta clase XD
    """

    def __init__(self, table, value, row, column):
        Expression.__init__(self, row, column)
        self.table = table
        self.value = value
        # self.temp = tabla + "." + value
        self.temp = str(value)

    def execute(self, environment):
        """
        TODO:Se debe hacer la logica para buscar los identificadores en la tabla
        """
        return Primitive(TYPE.NUMBER, 0, self.row, self.column)


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

        if exp.type != TYPE.BOOLEAN:
            return ErrorUnaryOperation(exp.value, self.row, self.column)

        if operator == "NOT":
            value = not exp.value
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
        self.function = function
        self.params = params
        self.temp = str(function) + "("
        for t in params:
            self.temp += t.temp
        self.temp += ")"

    # TODO: Quitar los corchetes iniciales de valores
    def execute(self, environment):
        try:
            valores = [[p.execute(environment).value for p in self.params]]

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
            else:
                value = valores[0]
            if isinstance(value, list):
                if len(value) <= 1:
                    value = value[0]
            return Primitive(TYPE.NUMBER, value, self.row, self.column)
        except TypeError:
            print("Error de tipos")
        except:
            print("Error desconocido")
