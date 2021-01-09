from abc import abstractmethod
from enum import Enum
import pandas as pd
from datetime import datetime
from analizer.functions import MathFunctions as mf
from analizer.functions import TrigonometricFunctions as trf
from analizer.functions import StringFunctions as strf
from analizer.reports import Nodo
from analizer.reports import AST
from analizer.symbol.symbol import Symbol


ast = AST.AST()
root = None

list_errors = list()


class TYPE(Enum):
    NUMBER = 1
    STRING = 2
    BOOLEAN = 3
    TIMESTAMP = 4
    DATE = 5
    TIME = 6
    DATETIME = 7
    TYPE = 8
    NULL = 9


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

    @abstractmethod
    def c3d(self, environment):
        """
        Metodo que servira para obtener el codigo 3 direcciones de las expresiones
        """ 


class Primitive(Expression):
    """
    Esta clase contiene los tipos primitivos
    de datos como STRING, NUMBER, BOOLEAN
    """

    def __init__(self, type_, value, temp, row, column):
        Expression.__init__(self, row, column)
        self.type = type_
        self.value = value
        self.temp = str(temp)

    def execute(self, environment):

        return self

    def dot(self):
        nod = Nodo.Nodo(str(self.value))
        return nod

    def c3d(self, environment):

        return self


class Identifiers(Expression):
    """
    Esta clase representa los nombre de columnas
    """
    type = None
    # TODO: implementar la funcion para obtener el type de la columna
    def __init__(self, table, name, row, column):
        Expression.__init__(self, row, column)
        self.table = table
        self.name = name
        if table == None:
            self.temp = name
        else:
            self.temp = table + "." + name
        self.type = None
        self.value = name

    def execute(self, environment):
        #sacar variable
        var_ = environment.getVar(self.name)

        if var_ != None:
            return var_.value

        if not self.table:
            table = environment.ambiguityBetweenColumns(self.name)
            if table[0]:  # Si existe ambiguedad
                return
            else:
                if table[1]:
                    self.table = table[1]
                    col = self.table + "." + self.name
                    self.value = environment.dataFrame[col]
                else:
                    x = environment.getVar(self.name)
                    if not x:
                        list_errors.append(
                            "Error: 42703: columna  "
                            + str(self.name)
                            + " no existe \n En la linea: "
                            + str(self.row)
                        )
                        self.table = ""
                        self.name = ""
                        self.value = ""
                    else:
                        self.table = x[0]
                        self.name = x[1]
                        self.value = environment.getColumn(self.table, self.name)
        else:
            self.value = environment.getColumn(self.table, self.name)

        # extraer variable xd
        
        r = environment.getType(self.table, self.name)
        self.type = r

        return self

    def dot(self):
        nod = Nodo.Nodo(self.name)
        return nod

    def c3d(self, environment):
        return self


class TableAll(Expression):
    """
    Esta clase representa una tabla.*
    """

    def __init__(self, table, row, column):
        Expression.__init__(self, row, column)
        self.table = table

    def execute(self, environment):
        env = environment
        lst = []
        while env != None:
            if self.table in env.variables:
                table = env.variables[self.table].value
                for p in env.dataFrame:
                    temp = p.split(".")
                    if temp[0] == table:
                        identifier = Identifiers(
                            self.table, temp[1], self.row, self.column
                        )
                        lst.append(identifier)
                break
            env = env.previous
        return lst

    def dot(self):
        new = Nodo.Nodo(str(self.table))
        punto = Nodo.Nodo(".*")
        new.addNode(punto)
        return new


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
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(operator)
                + " "
                + str(exp.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorUnaryOperation(exp.value, self.row, self.column)

        if operator == "+":
            value = exp.value
        elif operator == "-":
            value = exp.value * -1
        else:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(operator)
                + " "
                + str(exp.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorUnaryOperation(operator, self.row, self.column)
        return Primitive(TYPE.NUMBER, value, self.temp, self.row, self.column)

    def c3d(self, environment):
        exp = self.exp.c3d(environment)
        operator = self.operator
        temp = environment.getTemp()
        if exp.type != TYPE.NUMBER:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(operator)
                + " "
                + str(exp.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorUnaryOperation(exp.value, self.row, self.column)

        if operator == "+":
            value = str(temp) + " = "+ str(exp.value)
            environment.codigo += "".join(environment.count_tabs) + value + "\n"
        elif operator == "-":
            value = str(temp) + " = -"+ str(exp.value)
            environment.codigo += "".join(environment.count_tabs) + value+"\n"
        else:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(operator)
                + " "
                + str(exp.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorUnaryOperation(operator, self.row, self.column)
        return Primitive(TYPE.NUMBER, temp, self.temp, self.row, self.column)

    def dot(self):
        n1 = self.exp.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        return new


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
        try:
            exp1 = self.exp1.execute(environment)
            exp2 = self.exp2.execute(environment)
            operator = self.operator

            if operator == "+":

               try:
                    value = exp1.value + exp2.value
               except:
                    list_errors.append(
                        "Error: 42883: la operacion no existe entre: "
                        + str(exp1.type)
                        + " "
                        + str(operator)
                        + " "
                        + str(exp2.type)
                        + "\n En la linea: "
                        + str(self.row)
                    )

                    return ErrorBinaryOperation(
                        exp1.value, exp2.value, self.row, self.column
                    )                

            elif operator == "-":
                if exp1.type != TYPE.NUMBER or exp2.type != TYPE.NUMBER:
                    list_errors.append(
                        "Error: 42883: la operacion no existe entre: "
                        + str(exp1.type)
                        + " "
                        + str(operator)
                        + " "
                        + str(exp2.type)
                        + "\n En la linea: "
                        + str(self.row)
                    )

                    return ErrorBinaryOperation(
                        exp1.value, exp2.value, self.row, self.column
                    )

                value = exp1.value - exp2.value
            elif operator == "*":
                if exp1.type != TYPE.NUMBER or exp2.type != TYPE.NUMBER:
                    list_errors.append(
                        "Error: 42883: la operacion no existe entre: "
                        + str(exp1.type)
                        + " "
                        + str(operator)
                        + " "
                        + str(exp2.type)
                        + "\n En la linea: "
                        + str(self.row)
                    )

                    return ErrorBinaryOperation(
                        exp1.value, exp2.value, self.row, self.column
                    )

                value = exp1.value * exp2.value
            elif operator == "/":
                if exp1.type != TYPE.NUMBER or exp2.type != TYPE.NUMBER:
                    list_errors.append(
                        "Error: 42883: la operacion no existe entre: "
                        + str(exp1.type)
                        + " "
                        + str(operator)
                        + " "
                        + str(exp2.type)
                        + "\n En la linea: "
                        + str(self.row)
                    )

                    return ErrorBinaryOperation(
                        exp1.value, exp2.value, self.row, self.column
                    )

                if exp2.value == 0:
                    list_errors.append("Error: 22012: No se puede dividir  por cero")
                    value = 0
                else:
                    try:
                        list_errors.append("Error: XX00L0L: Syntax Error")
                        value = exp1.value / exp2.value
                    except:
                        value = 0

            elif operator == "^":
                if exp1.type != TYPE.NUMBER or exp2.type != TYPE.NUMBER:
                    list_errors.append(
                        "Error: 42883: la operacion no existe entre: "
                        + str(exp1.type)
                        + " "
                        + str(operator)
                        + " "
                        + str(exp2.type)
                        + "\n En la linea: "
                        + str(self.row)
                    )

                    return ErrorBinaryOperation(
                        exp1.value, exp2.value, self.row, self.column
                    )

                value = exp1.value ** exp2.value
            elif operator == "%":
                if exp1.type != TYPE.NUMBER or exp2.type != TYPE.NUMBER:
                    list_errors.append(
                        "Error: 42883: la operacion no existe entre: "
                        + str(exp1.type)
                        + " "
                        + str(operator)
                        + " "
                        + str(exp2.type)
                        + "\n En la linea: "
                        + str(self.row)
                    )

                    return ErrorBinaryOperation(
                        exp1.value, exp2.value, self.row, self.column
                    )

                if exp2.value == 0:
                    list_errors.append("Error: 22012: No se puede modular por cero")
                    value = 0
                else:
                    value = exp1.value % exp2.value
            else:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)

            return Primitive(TYPE.NUMBER, value, self.temp, self.row, self.column)
        except:
            list_errors.append(
                "Error: XX000: Error interno (Binary Aritmethic Operation)"
                + "\n En la linea: "+ str(self.row)
                )
            

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        return new

    def c3d(self, environment):
        temp = environment.getTemp()
        try:
            exp1 = self.exp1.c3d(environment)
            exp2 = self.exp2.c3d(environment)
            operator = self.operator
            if exp1.type != TYPE.NUMBER or exp2.type != TYPE.NUMBER:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )

                return ErrorBinaryOperation(
                    exp1.value, exp2.value, self.row, self.column
                )
            if operator == "+":
                value = str(temp) + " = "+ str(exp1.value) + " + " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
                
            elif operator == "-":
                value = str(temp) + " = "+ str(exp1.value) + " - " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "*":
                value = str(temp) + " = "+ str(exp1.value) + " * " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "/":
                if exp2.value == 0:
                    list_errors.append("Error: 22012: No se puede dividir  por cero")
                    value = 0
                else:
                    value = str(temp) + " = "+ str(exp1.value) + " / " + str(exp2.value)
                    environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "^":
                value = str(temp) + " = "+ str(exp1.value) + " ^ " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "%":
                if exp2.value == 0:
                    list_errors.append("Error: 22012: No se puede modular por cero")
                    value = 0
                else:
                    value = str(temp) + " = "+ str(exp1.value) + " % " + str(exp2.value)
                    environment.codigo +=  "".join(environment.count_tabs) + value+"\n"
            else:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)

            return Primitive(TYPE.NUMBER, temp, self.temp, self.row, self.column)
        except:
            list_errors.append(
                "Error: XX000: Error interno (Binary Aritmethic Operation)"
                + "\n En la linea: "+ str(self.row)
                )


class BinaryStringOperation(Expression):
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
        if exp1.type != TYPE.STRING and exp2.type != TYPE.STRING:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + "\n En la linea: "
                + str(self.row)
            )

            return ErrorBinaryOperation(exp1.value, exp2.value, self.row, self.column)
        if isinstance(exp1.value, pd.core.series.Series):
            exp1.value = exp1.value.apply(str)
        else:
            exp1.value = str(exp1.value)
        if isinstance(exp2.value, pd.core.series.Series):
            exp2.value = exp2.value.apply(str)
        else:
            exp2.value = str(exp2.value)
        if operator == "||":
            value = exp1.value + exp2.value
        else:
            list_errors.append(
                "Error: 42725: el operador no es unico: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorOperatorExpression(operator, self.row, self.column)

        return Primitive(TYPE.STRING, value, self.temp, self.row, self.column)

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        return new

    def c3d(self, environment):
        exp1 = self.exp1.c3d(environment)
        exp2 = self.exp2.c3d(environment)
        operator = self.operator
        temp=environment
        if exp1.type != TYPE.STRING and exp2.type != TYPE.STRING:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + "\n En la linea: "
                + str(self.row)
            )

            return ErrorBinaryOperation(exp1.value, exp2.value, self.row, self.column)
        if isinstance(exp1.value, pd.core.series.Series):
            exp1.value = exp1.value.apply(str)
        else:
            exp1.value = str(exp1.value)
        if isinstance(exp2.value, pd.core.series.Series):
            exp2.value = exp2.value.apply(str)
        else:
            exp2.value = str(exp2.value)
        if operator == "||":
            value = str(temp) + " = "+ str(exp1.value) + " + " + str(exp2.value)
            environment.codigo += "".join(environment.count_tabs) + value+"\n"
        else:
            list_errors.append(
                "Error: 42725: el operador no es unico: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorOperatorExpression(operator, self.row, self.column)

        return Primitive(TYPE.STRING, temp, self.temp, self.row, self.column)


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
                list_errors.append(
                    "Error: 22P02: entrada invalida: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)
            return Primitive(TYPE.BOOLEAN, value, self.temp, self.row, self.column)
        except TypeError:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorBinaryOperation(exp1.value, exp2.value, self.row, self.column)
        except:
            list_errors.append(
                "Error: XX000: Error interno (Binary Relational Operation)"
                + "\n En la linea: "
                + str(self.row)
            )
            pass

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        return new

    def c3d(self, environment):
        exp1 = self.exp1.c3d(environment)
        exp2 = self.exp2.c3d(environment)

        if (str(self.exp1.type)=='TYPE.STRING'):
            #print('Pedro Hueco')
            exp1.value='\"'+str(exp1.value)+'\"'
        if (str(self.exp2.type)=='TYPE.STRING'):
            exp2.value='\"'+str(exp2.value)+'\"' 
            
        operator = self.operator
        temp = environment.getTemp()
        try:
            if operator == "<":
                value = str(temp)+ " = " + str(exp1.value) + " < " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == ">":
                value = str(temp) + " = "+ str(exp1.value) + " > " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == ">=":
                value = str(temp) + " = "+ str(exp1.value) + " >= " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "<=":
                value = str(temp) + " = "+ str(exp1.value) + " <= " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "=":
                value = str(temp) + " = "+ str(exp1.value) + " == " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "!=":
                value = str(temp) + " = "+ str(exp1.value) + " != " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "<>":
                value = str(temp) + " = "+ str(exp1.value) + " <> " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISDISTINCTFROM":
                value = str(temp) + " = "+ str(exp1.value) + " ISDISTINCTFROM " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISNOTDISTINCTFROM":
                value = str(temp) + " = "+ str(exp1.value) + " ISNOTDISTINCTFROM " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            else:                
                list_errors.append(
                    "Error: 22P02: entrada invalida: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)
            return Primitive(TYPE.BOOLEAN, temp, self.temp, self.row, self.column)
        except TypeError:
            print("error en except")
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorBinaryOperation(exp1.value, exp2.value, self.row, self.column)
        except:
            list_errors.append(
                "Error: XX000: Error interno (Binary Relational Operation)"
                + "\n En la linea: "
                + str(self.row)
            )
            pass

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
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp.type)
                    + " "
                    + str(operator)
                    + " "
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)

            return Primitive(TYPE.BOOLEAN, value, self.temp, self.row, self.column)
        except TypeError:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp.type)
                + " "
                + str(operator)
                + " "
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorUnaryOperation(exp.value, self.row, self.column)
        except:
            list_errors.append(
                "Error: XX000: Error interno (Unary Relational Operation)"
                + "\n En la linea: "
                + str(self.row)
            )
            pass

    def dot(self):
        n1 = self.exp1.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        return new

    def c3d(self, environment):
        exp = self.exp.c3d(environment)
        operator = self.operator
        temp = environment.getTemp()
        try:
            if operator == "ISNULL":
                value = str(temp) + " = "+ str(exp.value) + " == None "
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "NOTNULL":
                value = str(temp) + " = "+ str(exp.value) + " != None "
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISTRUE":
                value = str(temp) + " = "+ str(exp.value) + " == True "
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISFALSE":
                value = str(temp) + " = "+ str(exp.value) + " == False "
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISUNKNOWN":
                value = str(temp) + " = "+ str(exp.value) + " == None "
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISNOTNULL":
                value = str(temp) + " = "+ str(exp.value) + " != None "
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISNOTTRUE":
                value = str(temp) + " = "+ str(exp.value) + " != True "
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISNOTFALSE":
                value = str(temp) + " = "+ str(exp.value) + " != False "
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISNOTUNKNOWN":
                value = str(temp) + " = "+ str(exp.value) + " != None "
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            else:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp.type)
                    + " "
                    + str(operator)
                    + " "
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)

            return Primitive(TYPE.BOOLEAN, temp, self.temp, self.row, self.column)
        except TypeError:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp.type)
                + " "
                + str(operator)
                + " "
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorUnaryOperation(exp.value, self.row, self.column)
        except:
            list_errors.append(
                "Error: XX000: Error interno (Unary Relational Operation)"
                + "\n En la linea: "
                + str(self.row)
            )
            pass


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
            if (
                isinstance(exp1.value, pd.core.series.Series)
                or isinstance(exp2.value, pd.core.series.Series)
                or isinstance(exp3.value, pd.core.series.Series)
            ):
                if operator == "BETWEEN":
                    value = (exp1.value > exp2.value) & (exp1.value < exp3.value)
                elif operator == "NOTBETWEEN":
                    value = not ((exp1.value > exp2.value) & (exp1.value < exp3.value))
                elif operator == "BETWEENSYMMETRIC":
                    t1 = (exp1.value > exp2.value) & (exp1.value < exp3.value)
                    t2 = (exp1.value < exp2.value) & (exp1.value > exp3.value)
                    value = t1 | t2
                else:
                    list_errors.append(
                        "Error: 42601: Error sintactico: "
                        + "\n En la linea: "
                        + str(self.row)
                    )
                    return ErrorOperatorExpression(operator, self.row, self.column)
            else:
                if operator == "BETWEEN":
                    value = exp1.value > exp2.value and exp1.value < exp3.value
                elif operator == "NOTBETWEEN":
                    value = not (exp1.value > exp2.value and exp1.value < exp3.value)
                elif operator == "BETWEENSYMMETRIC":
                    t1 = exp1.value > exp2.value and exp1.value < exp3.value
                    t2 = exp1.value < exp2.value and exp1.value > exp3.value
                    value = t1 or t2
                else:
                    list_errors.append(
                        "Error: 42601: Error sintactico: "
                        + "\n En la linea: "
                        + str(self.row)
                    )
                    return ErrorOperatorExpression(operator, self.row, self.column)
            return Primitive(TYPE.BOOLEAN, value, self.temp, self.row, self.column)
        except TypeError:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + " y "
                + str(exp3.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorTernaryOperation(
                exp1.value, exp2.value, exp3.value, self.row, self.column
            )
        except:
            list_errors.append(
                "Error: XX000: Error interno (Ternary Relational Operation)"
                + "\n En la linea: "
                + str(self.row)
            )
            pass

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        n3 = self.exp3.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        new.addNode(n3)
        return new

    def c3d(self, environment):
        exp1 = self.exp1.c3d(environment)
        exp2 = self.exp2.c3d(environment)
        exp3 = self.exp3.c3d(environment)
        operator = self.operator
        temp = environment.getTemp()
        
        try:
            if (
                isinstance(exp1.value, pd.core.series.Series)
                or isinstance(exp2.value, pd.core.series.Series)
                or isinstance(exp3.value, pd.core.series.Series)
            ):
                if operator == "BETWEEN":
                    value = str(temp) + " = ("+ str(exp1.value) + " > "+str(exp2.value)+ " ) & ( "+ str(exp1.value) + " < "+str(exp3.value)+ " )"
                    environment.codigo += value+"\n"
                elif operator == "NOTBETWEEN":
                    value = str(temp) + " = not (("+ str(exp1.value) + " > "+str(exp2.value)+ " ) & ( "+ str(exp1.value) + " < "+str(exp3.value)+ " ))"
                    environment.codigo += value+"\n"
                elif operator == "BETWEENSYMMETRIC":
                    value = str(temp) + " = ("+ str(exp1.value) + " > "+str(exp2.value)+ " ) & ( "+ str(exp1.value) + " < "+str(exp3.value)+ " )"
                    environment.codigo += value+"\n"
                    temp2 = environment.getTemp()
                    value = str(temp2) + " = ("+ str(exp1.value) + " < "+str(exp2.value)+ " ) & ( "+ str(exp1.value) + " > "+str(exp3.value)+ " )"
                    environment.codigo += value+"\n"
                    temp3 = environment.getTemp()
                    value = str(temp3) + " = "+ str(temp) + " | "+str(temp2) 
                    environment.codigo += value+"\n"
                    temp=temp3
                else:
                    list_errors.append(
                        "Error: 42601: Error sintactico: "
                        + "\n En la linea: "
                        + str(self.row)
                    )
                    return ErrorOperatorExpression(operator, self.row, self.column)
            else:
                if operator == "BETWEEN":
                    value = str(temp) + " = "+ str(exp1.value) + " > "+str(exp2.value)+ " and  "+ str(exp1.value) + " < "+str(exp3.value)+ " "
                    environment.codigo += "".join(environment.count_tabs) + value+"\n"
                elif operator == "NOTBETWEEN":
                    value = str(temp) + " = not ("+ str(exp1.value) + " > "+str(exp2.value)+ "  and  "+ str(exp1.value) + " < "+str(exp3.value)+ " )"
                    environment.codigo += "".join(environment.count_tabs) + value+"\n"
                elif operator == "BETWEENSYMMETRIC":
                    value = str(temp) + " = "+ str(exp1.value) + " > "+str(exp2.value)+ " and "+ str(exp1.value) + " < "+str(exp3.value)+ " "
                    environment.codigo += "".join(environment.count_tabs) + value+"\n"
                    temp2 = environment.getTemp()
                    value = str(temp2) + " = "+ str(exp1.value) + " < "+str(exp2.value)+ " and "+ str(exp1.value) + " > "+str(exp3.value)+ " "
                    environment.codigo += "".join(environment.count_tabs) + value+"\n"
                    temp3 = environment.getTemp()
                    value = str(temp3) + " = "+ str(temp) + " or "+str(temp2) 
                    environment.codigo += "".join(environment.count_tabs) + value+"\n"
                    temp=temp3

                else:
                    list_errors.append(
                        "Error: 42601: Error sintactico: "
                        + "\n En la linea: "
                        + str(self.row)
                    )
                    return ErrorOperatorExpression(operator, self.row, self.column)
            return Primitive(TYPE.BOOLEAN, temp, self.temp, self.row, self.column)
        except TypeError:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + " y "
                + str(exp3.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorTernaryOperation(
                exp1.value, exp2.value, exp3.value, self.row, self.column
            )
        except:
            list_errors.append(
                "Error: XX000: Error interno (Ternary Relational Operation)"
                + "\n En la linea: "
                + str(self.row)
            )
            pass


class ExistsRelationalOperation(Expression):
    def __init__(self, subquery, row, column) -> None:
        super().__init__(row, column)
        self.subquery = subquery
        self.temp = "EXISTS( subquery )"

    def execute(self, environment):
        try:
            df1 = environment.dataFrame.copy()
            names = {}

            for n in list(df1.columns):
                names[n] = n.split(".")[1]

            df1.rename(columns=names, inplace=True)

            df2 = self.subquery.execute(environment)[0]

            y = df1.columns.intersection(df2.columns)
            lst = list(y)
            if len(lst) < 1:
                list_errors.append(
                "Error: 42P10: Referencia de columnas invalidas EXIST"
                + "\n En la linea: "+ str(self.row)
                )
               
            value = (df1[lst].apply(tuple, 1).isin(df2[lst].apply(tuple, 1)))
            return Primitive(TYPE.BOOLEAN, value, self.temp, self.row, self.column)
        except:
            list_errors.append(
                "Error: XX000: Error interno (Exist Relational Operation)"
                + "\n En la linea: "+ str(self.row)
                )

    def dot(self):
        new = Nodo.Nodo("EXISTS")
        new.addNode(self.subquery.dot())
        return new
    

class InRelationalOperation(Expression):
    def __init__(self, colData, optNot, subquery, row, column) -> None:
        super().__init__(row, column)
        self.colData = colData
        self.subquery = subquery
        self.optNot = optNot
        self.temp = colData.temp + optNot + " IN ( subquery )"

    def execute(self, environment):
        col = self.colData.execute(environment)
        df = self.subquery.execute(environment)[0]

        # TODO: Falta agregar la verificacion de types

        if len(list(df.columns)) != 1:
            list_errors.append(
                "Error: XX000: Error interno (Exist Relational Operation)"
                + "\n En la linea: "+ str(self.row)
                )
        value = col.value.isin(df.iloc[:, 0])
        if self.optNot == "NOT":
            value = ~value
        return Primitive(TYPE.BOOLEAN, value, self.temp, self.row, self.column)

    def dot(self):

        n1 = self.optNot + " IN"
        new = Nodo.Nodo(n1)
        new.addNode(self.colData.dot())
        new.addNode(self.subquery.dot())
        return new

    def cd3(self, environment):
        col = self.colData.execute(environment)
        df = self.subquery.execute(environment)[0]
        temp = environment.getTemp()
        # TODO: Falta agregar la verificacion de types

        if len(list(df.columns)) != 1:
            list_errors.append(
                "Error: XX000: Error interno (Exist Relational Operation)"
                + "\n En la linea: "+ str(self.row)
                )
        value = col.value.isin(df.iloc[:, 0])
        if self.optNot == "NOT":
            value = str(temp) + " = ~"+ str(value)
            environment.codigo += "".join(environment.count_tabs) + value+"\n"
        return Primitive(TYPE.BOOLEAN, temp, self.temp, self.row, self.column)


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
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorBinaryOperation(exp1.value, exp2.value, self.row, self.column)

        if isinstance(exp1.value, pd.core.series.Series) or isinstance(
            exp2.value, pd.core.series.Series
        ):
            if operator == "AND":
                value = exp1.value & exp2.value
            elif operator == "OR":
                value = exp1.value | exp2.value
            else:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)
        else:
            if operator == "AND":
                value = exp1.value and exp2.value
            elif operator == "OR":
                value = exp1.value or exp2.value
            else:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)
        return Primitive(TYPE.BOOLEAN, value, self.temp, self.row, self.column)

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        return new

    def c3d(self, environment):
        exp1 = self.exp1.c3d(environment)
        exp2 = self.exp2.c3d(environment)
        operator = self.operator
        temp=environment.getTemp()
        if exp1.type != TYPE.BOOLEAN or exp2.type != TYPE.BOOLEAN:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorBinaryOperation(exp1.value, exp2.value, self.row, self.column)

        if isinstance(exp1.value, pd.core.series.Series) or isinstance(
            exp2.value, pd.core.series.Series
        ):
            if operator == "AND":
                value = str(temp) + " = "+ str(exp1.value) + " & " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "OR":
                value = str(temp) + " = "+ str(exp1.value) + " | " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            else:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)
        else:
            if operator == "AND":
                value = str(temp) + " = "+ str(exp1.value) + " and " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "OR":
                value = str(temp) + " = "+ str(exp1.value) + " or " + str(exp2.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            else:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)
        return Primitive(TYPE.BOOLEAN, temp, self.temp, self.row, self.column)


class UnaryLogicalOperation(Expression):
    """
    Esta clase contiene las expresiones booleanas unarias.
    """

    def __init__(self, exp, operator, row, column):
        Expression.__init__(self, row, column)
        self.exp = exp
        self.operator = operator
        if operator == "NOT":
            self.temp = str(operator) + " " + exp.temp
        else:
            self.temp = exp.temp + " " + comps.get(operator)

    def execute(self, environment):
        exp = self.exp.execute(environment)
        operator = self.operator
        # MOMO IF OPERADORES
        if exp.type != TYPE.BOOLEAN:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp.type)
                + " y el operador "
                + str(operator)
                + "\n En la linea: "
                + str(self.row)
            )
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
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp.type)
                    + " y el operador "
                    + str(operator)
                    + "\n En la linea: "
                    + str(self.row)
                )
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
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp.type)
                    + " y el operador "
                    + str(operator)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)
        return Primitive(TYPE.BOOLEAN, value, self.temp, self.row, self.column)

    def dot(self):
        n1 = self.exp.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        return new

    def c3d(self, environment):
        exp = self.exp.c3d(environment)
        operator = self.operator
        temp = environment.getTemp()
        # MOMO IF OPERADORES
        if exp.type != TYPE.BOOLEAN:
            list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp.type)
                + " y el operador "
                + str(operator)
                + "\n En la linea: "
                + str(self.row)
            )
            return ErrorUnaryOperation(exp.value, self.row, self.column)

        if isinstance(exp.value, pd.core.series.Series):
            if operator == "NOT":
                value = str(temp)+ " = ~" + str(exp.value)
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISTRUE":
                value = str(temp)+ " = " + str(exp.value) + " == True" 
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISFALSE":
                value = str(temp)+ " = " + str(exp.value) + " == False" 
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISUNKNOWN":
                value = str(temp)+ " = " + str(exp.value) + " == None" 
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISNOTTRUE":
                value = str(temp)+ " = " + str(exp.value) + " != True" 
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "ISNOTFALSE":
                value = str(temp)+ " = " + str(exp.value) + " != False" 
                environment.codigo += "".join(environment.count_tabs) + value+"\n"
            elif operator == "".join(environment.count_tabs) + "ISNOTUNKNOWN":
                value = str(temp)+ " = " + str(exp.value) + " != None" 
                environment.codigo += value+"\n"
            else:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp.type)
                    + " y el operador "
                    + str(operator)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)
        else:
            if operator == "NOT":
                value = str(temp)+ " = ~" + str(exp.value)
                environment.codigo += value+"\n"
            elif operator == "ISTRUE":
                value = str(temp)+ " = " + str(exp.value) + " == True" 
                environment.codigo += value+"\n"
            elif operator == "ISFALSE":
                value = str(temp)+ " = " + str(exp.value) + " == False" 
                environment.codigo += value+"\n"
            elif operator == "ISUNKNOWN":
                value = str(temp)+ " = " + str(exp.value) + " == None" 
                environment.codigo += value+"\n"
            elif operator == "ISNOTTRUE":
                value = str(temp)+ " = " + str(exp.value) + " != True" 
                environment.codigo += value+"\n"
            elif operator == "ISNOTFALSE":
                value = str(temp)+ " = " + str(exp.value) + " != False" 
                environment.codigo += value+"\n"
            elif operator == "ISNOTUNKNOWN":
                value = str(temp)+ " = " + str(exp.value) + " != None" 
                environment.codigo += value+"\n"
            else:
                list_errors.append(
                    "Error: 42883: la operacion no existe entre: "
                    + str(exp.type)
                    + " y el operador "
                    + str(operator)
                    + "\n En la linea: "
                    + str(self.row)
                )
                return ErrorOperatorExpression(operator, self.row, self.column)
        return Primitive(TYPE.BOOLEAN, temp, self.temp, self.row, self.column)



class ErrorBinaryOperation(Expression):
    """
    Reporta error de una expresion
    """

    def __init__(self, exp1, exp2, row, column):
        Expression.__init__(self, row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.value = "error"
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
        i = 0
        self.temp = str(function) + "("
        for t in params:
            if i > 0:
                self.temp += ", "
            self.temp += t.temp
            i += 1
        self.temp += ")"

    # TODO: Agregar un error de parametros incorrectos
    def execute(self, environment):
        type_ = TYPE.NUMBER
        try:
            valores = []
            types = []
            for p in self.params:
                obj = p.execute(environment)
                val = obj.value
                t = obj.type
                if isinstance(val, pd.core.series.Series):
                    val = val.tolist()
                valores.append(val)
                types.append(t)
            # Se toma en cuenta que las funcines matematicas
            # y trigonometricas producen un tipo NUMBER
            type_ = TYPE.NUMBER
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
                value = strf.lenght(*valores)
            elif self.function == "substring":
                type_ = TYPE.STRING
                value = strf.substring(*valores)
            elif self.function == "trim":
                type_ = TYPE.STRING
                value = strf.trim_(*valores)
            elif self.function == "get_byte":
                value = strf.get_byte(*valores)
            elif self.function == "md5":
                type_ = TYPE.STRING
                value = strf.md5(*valores)
            elif self.function == "set_byte":
                type_ = TYPE.STRING
                value = strf.set_byte(*valores)
            elif self.function == "sha256":
                type_ = TYPE.STRING
                value = strf.sha256(*valores)
            elif self.function == "substr":
                type_ = TYPE.STRING
                value = strf.substring(*valores)
            elif self.function == "convert_date":
                type_ = TYPE.DATETIME
                value = strf.convert_date(*valores)
            elif self.function == "convert_int":
                value = strf.convert_int(*valores)
            elif self.function == "encode":
                type_ = TYPE.STRING
                value = strf.encode(*valores)
            elif self.function == "decode":
                type_ = TYPE.STRING
                value = strf.decode(*valores)
            # Se toma en cuenta que la funcion now produce tipo DATE
            elif self.function == "now":
                type_ = TYPE.DATETIME
                value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            else:
                # TODO: Agregar un error de funcion desconocida
                func_ = environment.getVar(self.function)                

                if func_ != None:                    
                    rango_param = range(len(self.params))
                    for n in rango_param:
                        valor_param = self.params[n].execute(environment)                        
                        new_sym = Symbol(
                            valor_param,
                            func_.params_func[n][1][0],
                            func_.row,
                            func_.column,
                            None,
                            None,
                            None,
                            None,
                            None,
                            valor_param
                        )
                        environment.addSymbol(func_.params_func[n][0], new_sym)
                
                value = "ERROR"
                Lista_Ejecutar = []
                try:
                    if "PROCEDURE" == environment.variables[self.function].type:
                        Lista_Ejecutar = environment.variables[self.function].bloque_func
                    else:
                        Lista_Ejecutar = environment.variables[self.function].bloque_func[1]
                except:
                    print("No existe la funcion "+self.function)
                for v in Lista_Ejecutar:
                    value = v.execute(environment)

                # BORRAR PARAMETROS CREADOS
                rango_param = range(len(self.params))
                for n in rango_param:
                    # print("vamo a borra el parametro" + str(func_.params_func[n][0]))
                    environment.dropSymbol(func_.params_func[n][0])

            if isinstance(value, list):
                if len(value) <= 1:
                    value = value[0]
                else:
                    value = pd.Series(value)



            return Primitive(type_, value, self.temp, self.row, self.column)
        except TypeError:
            list_errors.append(
                "Error: 42883: La funcion "
                + str(self.function)
                + "("
                + str(type_)
                + ") no existe"
                + "\n En la linea: "
                + str(self.row)
            )
        except:
            list_errors.append("Error: P0001: Error en funciones")

    def dot(self):
        f = Nodo.Nodo(self.function)
        p = Nodo.Nodo("PARAMS")
        new = Nodo.Nodo("CALL")
        new.addNode(f)
        new.addNode(p)
        for par in self.params:
            p.addNode(par.dot())
        return new

    def c3d(self, environment):

        cont = environment.conta_exec
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = " + str(cont) + "\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Ejecucion del procedimiento\n\n"
        #environment.conta_exec += 1


# TODO: Agregar a la gramatica DATE, TIME y Columnas (datatype)
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
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    # ERROR
                    val = self.str
            elif self.type == "DATE":
                if self.opt == "YEAR":
                    val = self.str[0][:4]
                elif self.opt == "MONTH":
                    val = self.str[0][5:7]
                elif self.opt == "DAY":
                    val = self.str[0][8:10]
                else:
                    # ERROR
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    val = self.str
            elif self.type == "TIME":
                if self.opt == "HOUR":
                    val = self.str[0][:2]
                elif self.opt == "MINUTE":
                    val = self.str[0][3:5]
                elif self.opt == "SECOND":
                    val = self.str[0][6:8]
                else:
                    # ERROR
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
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
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    val = self.str
            else:
                list_errors.append(
                    "Error: 22007: Formato de fecha invalido " + str(self.str)
                )
                val = self.str
                # ERROR

            return Primitive(TYPE.NUMBER, int(val), self.temp, self.row, self.column)
        except TypeError:
            list_errors.append("Error: 42804: discrepancia de tipo de datos ")
            pass
        except ValueError:  # cuando no tiene el valor INTERVAL
            list_errors.append(
                "Error: 22007:sintaxis de entrada no válida para el tipo 'interval' "
            )
            pass

    def dot(self):
        f = Nodo.Nodo("EXTRACT")
        p = Nodo.Nodo("PARAMS")
        new = Nodo.Nodo("CALL")
        new.addNode(f)
        new.addNode(p)
        ntype = Nodo.Nodo(str(self.type))
        nstr = Nodo.Nodo(str(self.str))
        nopt = Nodo.Nodo(str(self.opt))
        p.addNode(nopt)
        p.addNode(ntype)
        p.addNode(nstr)
        return new


class ExtractColumnDate(Expression):
    def __init__(self, opt, colData, row, column):
        Expression.__init__(self, row, column)
        self.opt = opt
        self.colData = colData
        self.temp = "EXTRACT( " + opt + " FROM " + colData.temp + " )"

    def execute(self, environment):
        try:
            valores = self.colData.execute(environment)

            if isinstance(valores.value, pd.core.series.Series):
                lst = valores.value.tolist()
                lst = [v.split() for v in lst]
            else:
                lst = [valores.split()]
            if valores.type == TYPE.TIMESTAMP or valores.type == TYPE.DATETIME:
                if self.opt == "YEAR":
                    val = [date[0][:4] for date in lst]
                elif self.opt == "MONTH":
                    val = [date[0][5:7] for date in lst]
                elif self.opt == "DAY":
                    val = [date[0][8:10] for date in lst]
                elif self.opt == "HOUR":
                    val = [date[1][:2] for date in lst]
                elif self.opt == "MINUTE":
                    val = [date[1][3:5] for date in lst]
                elif self.opt == "SECOND":
                    val = [date[1][6:8] for date in lst]
                else:
                    # ERROR
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    val = self.str
            elif valores.type == TYPE.DATE:
                if self.opt == "YEAR":
                    val = [date[0][:4] for date in lst]
                elif self.opt == "MONTH":
                    val = [date[0][5:7] for date in lst]
                elif self.opt == "DAY":
                    val = [date[0][8:10] for date in lst]
                else:
                    # ERROR
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    val = self.str
            elif valores.type == TYPE.TIME:
                if self.opt == "HOUR":
                    val = [date[0][:2] for date in lst]
                elif self.opt == "MINUTE":
                    val = [date[0][3:5] for date in lst]
                elif self.opt == "SECOND":
                    val = [date[0][6:8] for date in lst]
                else:
                    # ERROR
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    val = self.str
            else:
                val = self.str
                # ERROR
                list_errors.append(
                    "Error: 22007: Formato de fecha invalido " + str(self.str)
                )
            if isinstance(val, list):
                if len(val) <= 1:
                    val = val[0]
                else:
                    val = pd.Series(val)

            return Primitive(TYPE.NUMBER, val, self.temp, self.row, self.column)
        except TypeError:
            list_errors.append("Error: 42804: discrepancia de tipo de datos ")
            pass
        except ValueError:  # cuando no tiene el valor INTERVAL
            list_errors.append(
                "Error: 22007:sintaxis de entrada no válida para el tipo 'interval' "
            )
            pass

    def dot(self):
        f = Nodo.Nodo("EXTRACT")
        p = Nodo.Nodo("PARAMS")
        new = Nodo.Nodo("CALL")
        new.addNode(f)
        new.addNode(p)
        nstr = Nodo.Nodo(str(self.colData.temp))
        nopt = Nodo.Nodo(str(self.opt))
        p.addNode(nopt)
        p.addNode(nstr)
        return new


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
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
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
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    # ERROR
                    val = self.str
            elif self.type == "TIME":
                if self.opt == "hours":
                    val = self.str[0][:2]
                elif self.opt == "minutes":
                    val = self.str[0][3:5]
                elif self.opt == "seconds":
                    val = self.str[0][6:8]
                else:
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
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
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
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
                    list_errors.append(
                        "Error: 22007: Formato de fecha invalido " + str(self.str)
                    )
                    # ERROR
                    val = self.str
            else:
                val = self.str
                list_errors.append(
                    "Error: 22007: Formato de fecha invalido " + str(self.str)
                )
                # ERROR
            return Primitive(TYPE.NUMBER, int(val), self.temp, self.row, self.column)
        except TypeError:
            list_errors.append("Error: 42804: discrepancia de tipo de datos ")
            pass
        except ValueError:  # cuando no tiene el valor INTERVAL
            list_errors.append(
                "Error: 22007:sintaxis de entrada no válida para el tipo 'interval' "
            )
            pass

    def dot(self):
        f = Nodo.Nodo("date_part")
        p = Nodo.Nodo("PARAMS")
        new = Nodo.Nodo("CALL")
        new.addNode(f)
        new.addNode(p)
        ntype = Nodo.Nodo(str(self.type))
        nstr = Nodo.Nodo(str(self.str))
        nopt = Nodo.Nodo(str(self.opt))
        p.addNode(nopt)
        p.addNode(ntype)
        p.addNode(nstr)
        return new


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
                    value = self.optStr
            else:
                # ERROR
                list_errors.append(
                    "Error: 22007: Formato de fecha invalido " + str(self.str)
                )
                value = self.val
            return Primitive(TYPE.STRING, value, self.temp, self.row, self.column)
        except:
            list_errors.append("Error: P0001: Error en expresiones de fechas")
            pass

    def dot(self):
        new = Nodo.Nodo(self.val)
        return new


class CheckValue(Expression):
    """
    Clase que representa un valor del la condicion a desarrollar
    en el CHECK
    """

    def __init__(self, value, type_, row, column):
        self.value = value
        self.type = type_
        self.row = row
        self.column = column

    def execute(self, environment):
        return self


class AggregateFunction(Expression):
    """
    Esta clase representa las funciones de agregacion utilizadas en el Group By
    """

    def __init__(self, func, colData, row, column) -> None:
        super().__init__(row, column)
        self.func = func.lower()
        self.colData = colData
        if colData == "*":
            self.temp = func + "(*)"
        else:
            self.temp = func + "(" + colData.temp + ")"

    def execute(self, environment):
        countGr = environment.groupCols
        if countGr == 0:
            if self.colData != "*":
                c = self.colData.execute(environment).value
                if self.func == "sum":
                    newDf = c.sum()
                elif self.func == "count":
                    newDf = c.count()
                elif self.func == "prom":
                    newDf = c.mean()
                else:
                    newDf = None
                    list_errors.append(
                "Error: 42725: Error en la funcion "+str(self.func)
                + "\n En la linea: "+ str(self.row)
                )
            else:
                c = environment.dataFrame.iloc[:, -1:]
                if self.func == "count":
                    newDf = len(c)
                else:
                    newDf = None
                    list_errors.append(
                "Error: 42725: Error en la funcion "+str(self.func)
                + "\n En la linea: "+ str(self.row)
                )
            return Primitive(TYPE.NUMBER, newDf, self.temp, self.row, self.column)
        if self.colData != "*":
            # Obtiene las ultimas columnas metidas (Las del group by)
            df = environment.dataFrame.iloc[:, -countGr:]
            c = self.colData.execute(environment)
            x = c.value
            x = pd.DataFrame(x)
            x.rename(columns={x.columns[0]: c.temp}, inplace=True)
            if len(list(x.columns)) > 1:
                df = pd.concat([df, x.iloc[:, :1]], axis=1)
            else:
                df = pd.concat([df, x], axis=1)
            cols = list(df.columns)[:-1]
            if self.func == "sum":
                newDf = df.groupby(cols).sum().reset_index()
            elif self.func == "count":
                newDf = df.groupby(cols).count().reset_index()
            elif self.func == "prom":
                newDf = df.groupby(cols).mean().reset_index()
            else:
                newDf = None
                list_errors.append(
                "Error: 42725: Error en la funcion "+str(self.func)
                + "\n En la linea: "+ str(self.row)
                )

            value = newDf.iloc[:, -1:]
        else:
            # Obtiene las ultimas columnas metidas (Las del group by)
            df = environment.dataFrame.iloc[:, -countGr:]

            x = df.iloc[:, -1:]
            x = pd.DataFrame(x)
            x.rename(columns={x.columns[0]: "count(*)"}, inplace=True)
            df = pd.concat([df, x], axis=1)
            cols = list(df.columns)[:-1]
            if self.func == "count":

                newDf = df.groupby(cols).count().reset_index()
            else:
                newDf = None
                list_errors.append(
                "Error: 42725: Error en la funcion "+str(self.func)
                + "\n En la linea: "+ str(self.row)
                )
            value = newDf.iloc[:, -1:]

        return Primitive(TYPE.NUMBER, value, self.temp, self.row, self.column)

    def dot(self):
        f = Nodo.Nodo(self.func)
        p = Nodo.Nodo("PARAMS")
        new = Nodo.Nodo("CALL")
        new.addNode(f)
        new.addNode(p)

        #p.addNode(self.colData.dot()) #ERROR
        return new


def returnExpErrors():
    global list_errors
    mf.list_errors_mt += trf.list_errors_tg
    mf.list_errors_mt += list_errors
    list_ = mf.list_errors_mt
    trf.list_errors_tg = list()
    mf.list_errors_mt = list()
    list_errors = list()
    return list_

def makeAst():
    ast.makeAst(root)
