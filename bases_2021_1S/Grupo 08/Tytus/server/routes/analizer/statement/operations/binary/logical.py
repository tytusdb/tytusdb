from routes.analizer.abstract.expression import Expression, TYPE
from routes.analizer.abstract import expression
from routes.analizer.reports import Nodo
from routes.analizer.statement.expressions import primitive
import pandas as pd


class Logical(Expression):
    """
    Esta clase contiene las expresiones booleanas binarias.
    """

    def __init__(self, exp1, exp2, operator, row, column):
        super().__init__(row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.temp = exp1.temp + " " + str(operator) + " " + exp2.temp

    def execute(self, environment):
        exp1 = self.exp1.execute(environment)
        exp2 = self.exp2.execute(environment)
        operator = self.operator
        try:
            if exp1.type != TYPE.BOOLEAN or exp2.type != TYPE.BOOLEAN:
                raise Exception
            if isinstance(exp1.value, pd.core.series.Series) or isinstance(
                exp2.value, pd.core.series.Series
            ):
                if operator == "AND":
                    value = exp1.value & exp2.value
                elif operator == "OR":
                    value = exp1.value | exp2.value
                else:
                    raise Exception
            else:
                if operator == "AND":
                    value = exp1.value and exp2.value
                elif operator == "OR":
                    value = exp1.value or exp2.value
                else:
                    raise Exception
            return primitive.Primitive(
                TYPE.BOOLEAN, value, self.temp, self.row, self.column
            )
        except:
            expression.list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp1.type)
                + " "
                + str(operator)
                + " "
                + str(exp2.type)
                + "\n En la linea: "
                + str(self.row)
            )

    def dot(self):
        n1 = self.exp1.dot()
        n2 = self.exp2.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        new.addNode(n2)
        return new