from team29.analizer.abstract.expression import Expression, TYPE, comps
from team29.analizer.abstract import expression
from team29.analizer.reports import Nodo
from team29.analizer.statement.expressions import primitive
import pandas as pd


class Relational(Expression):
    """
    Esta clase contiene las expresiones ternarias de comparacion
    que devuelven un booleano.
    """

    def __init__(self, exp1, exp2, exp3, operator, row, column):
        super().__init__(row, column)
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
                    expression.list_errors.append(
                        "Error: 42601: Error sintactico: "
                        + "\n En la linea: "
                        + str(self.row)
                    )
                    return AssertionError
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
                    expression.list_errors.append(
                        "Error: 42601: Error sintactico: "
                        + "\n En la linea: "
                        + str(self.row)
                    )
                    return AssertionError
            return primitive.Primitive(
                TYPE.BOOLEAN, value, self.temp, self.row, self.column
            )
        except TypeError:
            expression.list_errors.append(
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
            return AssertionError
        except:
            expression.list_errors.append(
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