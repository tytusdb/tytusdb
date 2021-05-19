from team29.analizer.abstract.expression import Expression, TYPE
from team29.analizer.abstract import expression
from team29.analizer.reports import Nodo
from team29.analizer.statement.expressions import primitive
import pandas as pd


class String(Expression):
    """
    Esta clase recibe dos parametros de expresion
    para realizar operaciones entre ellas
    """

    def __init__(self, exp1, exp2, operator, row, column):
        super().__init__(row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator
        self.temp = exp1.temp + str(operator) + exp2.temp

    def execute(self, environment):
        try:
            exp1 = self.exp1.execute(environment)
            exp2 = self.exp2.execute(environment)
            operator = self.operator
            if exp1.type != TYPE.STRING and exp2.type != TYPE.STRING:
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
                raise Exception
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
                expression.list_errors.append(
                    "Error: 42725: el operador no es unico: "
                    + str(exp1.type)
                    + " "
                    + str(operator)
                    + " "
                    + str(exp2.type)
                    + "\n En la linea: "
                    + str(self.row)
                )
                raise Exception
            return primitive.Primitive(
                TYPE.STRING, value, self.temp, self.row, self.column
            )
        except:
            expression.list_errors.append(
                "Error: XX000: Error interno (Binary String Operation)"
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