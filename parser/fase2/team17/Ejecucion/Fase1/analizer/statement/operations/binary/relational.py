from  Fase1.analizer.abstract.expression import Expression, TYPE
from  Fase1.analizer.abstract import expression
from  Fase1.analizer.reports import Nodo
from  Fase1.analizer.statement.expressions import primitive


class Relational(Expression):
    """
    Esta clase contiene las expresiones binarias de comparacion
    que devuelven un booleano.
    """

    def __init__(self, exp1, exp2, operator, row, column):
        super().__init__(row, column)
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
                expression.list_errors.append(
                    "Error: 22P02: entrada invalida: "
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
                + "\n En la linea: "
                + str(self.row)
            )
            raise Exception
        except:
            raise expression.list_errors.append(
                "Error: XX000: Error interno (Binary Relational Operation)"
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