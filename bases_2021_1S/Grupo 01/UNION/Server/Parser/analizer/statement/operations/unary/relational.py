from Parser.analizer.abstract.expression import Expression, TYPE, comps
from Parser.analizer.abstract import expression
from Parser.analizer.reports import Nodo
from Parser.analizer.statement.expressions import primitive


class Relational(Expression):
    """
    Esta clase contiene las expresiones unarias de comparacion
    que devuelven un booleano.
    """

    def __init__(self, exp, operator, row, column):
        super().__init__(row, column)
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
                raise TypeError
            return primitive.Primitive(
                TYPE.BOOLEAN, value, self.temp, self.row, self.column
            )
        except TypeError:
            expression.list_errors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(exp.type)
                + " "
                + str(operator)
                + " "
                + "\n En la linea: "
                + str(self.row)
            )
        except:
            expression.list_errors.append(
                "Error: XX000: Error interno (Unary Relational Operation)"
                + "\n En la linea: "
                + str(self.row)
            )

    def dot(self):
        n1 = self.exp.dot()
        new = Nodo.Nodo(self.operator)
        new.addNode(n1)
        return new