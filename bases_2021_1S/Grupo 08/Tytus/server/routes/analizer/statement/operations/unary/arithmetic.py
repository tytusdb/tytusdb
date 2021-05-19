from routes.analizer.abstract.expression import Expression, TYPE
from routes.analizer.abstract import expression
from routes.analizer.reports import Nodo
from routes.analizer.statement.expressions import primitive


class Arithmetic(Expression):
    """
    Esta clase recibe un parametro de expresion
    para realizar operaciones unarias
    """

    def __init__(self, exp, operator, row, column):
        super().__init__(row, column)
        self.exp = exp
        self.operator = operator
        self.temp = str(operator) + exp.temp

    def execute(self, environment):
        exp = self.exp.execute(environment)
        operator = self.operator
        if exp.type != TYPE.NUMBER:
            expression.list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(operator)
                + " "
                + str(exp.type)
                + "\n En la linea: "
                + str(self.row)
            )
            return ArithmeticError
        if operator == "+":
            value = exp.value
        elif operator == "-":
            value = exp.value * -1
        else:
            expression.list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(operator)
                + " "
                + str(exp.type)
                + "\n En la linea: "
                + str(self.row)
            )
            raise Exception
        return primitive.Primitive(TYPE.NUMBER, value, self.temp, self.row, self.column)

    def dot(self):
        n1 = self.exp.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        return new