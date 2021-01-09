from analizer_pl.abstract.expression import Expression
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class Ternary(Expression):
    def __init__(self, temp, exp1, exp2, exp3, operator, row, column):
        super().__init__(row, column)
        self.temp = int(temp) - 1
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.operator = operator

    def execute(self, environment):
        try:
            exp1 = self.exp1.execute(environment)
            exp2 = self.exp2.execute(environment)
            exp3 = self.exp3.execute(environment)
            operator = self.operator

            if operator == "BETWEEN":
                exp1_ = Binary(self.newTemp(), exp1, exp2, ">", self.row, self.column)
                exp2_ = Binary(self.newTemp(), exp1, exp3, "<", self.row, self.column)
                return Binary(
                    self.newTemp(), exp1_, exp2_, "AND", self.row, self.column
                ).execute(environment)
            elif operator == "NOTBETWEEN":
                exp1_ = Binary(self.newTemp(), exp1, exp2, ">", self.row, self.column)
                exp2_ = Binary(self.newTemp(), exp1, exp3, "<", self.row, self.column)
                exp3 = Binary(
                    self.newTemp(), exp1_, exp2_, "AND", self.row, self.column
                )
                return Unary(
                    self.newTemp(), exp3, "NOT", self.row, self.column
                ).execute(environment)
            else:  # operator == "BETWEENSYMMETRIC"
                exp4 = Binary(self.newTemp(), exp1, exp2, ">", self.row, self.column)
                exp5 = Binary(self.newTemp(), exp1, exp3, "<", self.row, self.column)
                exp6 = Binary(self.newTemp(), exp4, exp5, "AND", self.row, self.column)
                exp4 = Binary(self.newTemp(), exp1, exp2, "<", self.row, self.column)
                exp5 = Binary(self.newTemp(), exp1, exp3, ">", self.row, self.column)
                exp7 = Binary(self.newTemp(), exp4, exp5, "AND", self.row, self.column)
                return Binary(
                    self.newTemp(), exp6, exp7, "OR", self.row, self.column
                ).execute(environment)
        except:
            grammar.PL_errors.append(
                "Error P0000: plpgsql fatal error \n Hint---> Ternary Expression"
            )

    def newTemp(self):
        self.temp += 1
        return str(self.temp)

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        n3 = self.exp3.dot()
        new = Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        new.addNode(n3)
        return new


class Binary(Expression):
    """
    Esta clase recibe dos parametros de expresion
    para realizar el  C3D
    """

    def __init__(self, temp, exp1, exp2, operator, row, column):
        super().__init__(row, column)
        self.temp = "t" + temp
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator

    def execute(self, environment):
        try:
            tab = ""
            tab1 = False
            if isinstance(environment, Environment):
                tab = "\t"
                tab1 = True
            exp1 = self.exp1.execute(environment)
            exp2 = self.exp2.execute(environment)
            if self.operator == "<>":
                self.operator = "!="
            elif self.operator == "=":
                self.operator = "=="
            elif self.operator == "||":
                self.operator = "+"
            exp1.temp = values.get(exp1.temp, exp1.temp)
            exp2.temp = values.get(exp2.temp, exp2.temp)
            exp = (
                exp1.value
                + exp2.value
                + tab
                + self.temp
                + " = "
                + str(exp1.temp)
                + " "
                + self.operator.lower()
                + " "
                + str(exp2.temp)
                + "\n"
            )
            grammar.optimizer_.addAritOp(
                self.temp,
                str(exp1.temp),
                exp2.temp,
                self.operator.lower(),
                self.row,
                tab1,
            )
            return code.C3D(exp, self.temp, self.row, self.column)
        except:
            grammar.PL_errors.append(
                "Error P0000: plpgsql fatal error \n Hint---> Binary Expression"
            )

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        new = Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        return new


class Unary(Expression):
    """
    Esta clase recibe un parametro de expresion
    para realizar el  C3D
    """

    def __init__(self, temp, exp, operator, row, column):
        super().__init__(row, column)
        self.temp = "t" + temp
        self.exp = exp
        self.operator = operator

    def execute(self, environment):
        try:
            tab = ""
            tab1 = False
            if isinstance(environment, Environment):
                tab = "\t"
                tab1 = True
            exp = self.exp.execute(environment)
            if self.operator == "+":
                grammar.optimizer_.addScalarAsig(
                    self.temp, str(exp.temp), None, "=", self.row, tab1
                )
                exp = exp.value + tab + self.temp + " = " + str(exp.temp) + "\n"

            elif self.operator == "-":
                grammar.optimizer_.addAritOp(
                    self.temp, "-1 ", exp.temp, "*", self.row, tab1
                )
                exp = exp.value + tab + self.temp + " = -1 * " + str(exp.temp) + "\n"

            elif self.operator == "NOTNULL":
                grammar.optimizer_.addAritOp(
                    self.temp, str(exp.temp), "None", "!=", self.row, tab1
                )
                exp = (
                    exp.value
                    + tab
                    + self.temp
                    + " = "
                    + str(exp.temp)
                    + " != None "
                    + "\n"
                )

            elif self.operator == "NOT":
                grammar.optimizer_.addScalarAsig(
                    self.temp, str(exp.temp), None, "= not", self.row, tab1
                )
                exp = exp.value + tab + self.temp + " = not " + str(exp.temp) + "\n"

            else:
                if "NOT" in self.operator:
                    exp2 = self.operator[5:]
                    self.operator = " != "
                else:
                    exp2 = self.operator[2:]
                    self.operator = " == "
                grammar.optimizer_.addAritOp(
                    self.temp, exp.temp, exp2, self.operator, self.row, tab1
                )
                exp2 = values.get(exp2, exp2)
                exp = (
                    exp.value
                    + tab
                    + self.temp
                    + " = "
                    + str(exp.temp)
                    + self.operator
                    + exp2
                    + "\n"
                )
            return code.C3D(exp, self.temp, self.row, self.column)
        except:
            grammar.PL_errors.append(
                "Error P0000: plpgsql fatal error \n Hint---> Unary Expression"
            )

    def dot(self):
        n = self.exp.dot()
        new = Nodo(self.operator)
        new.addNode(n)
        return new


values = {
    "TRUE": "True",
    "FALSE": "False",
    "UNKNOWN": "None",
    "NULL": "None",
}