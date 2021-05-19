from team29.analizer.abstract.expression import Expression
from team29.analizer.reports import Nodo


class Primitive(Expression):
    """
    Esta clase contiene los tipos primitivos
    de datos como STRING, NUMBER, BOOLEAN
    """

    def __init__(self, type_, value, temp, row, column):
        super().__init__(row, column)
        self.type = type_
        self.value = value
        self.temp = str(temp)

    def execute(self, environment):
        return self

    def dot(self):
        node = Nodo.Nodo(str(self.value))
        return node