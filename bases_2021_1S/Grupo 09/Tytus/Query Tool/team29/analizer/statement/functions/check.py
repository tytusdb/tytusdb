from team29.analizer.abstract.expression import Expression
from team29.analizer.reports import Nodo

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

    def dot(self):
        new = Nodo.Nodo("CHECK")
        new.addNode(Nodo.Nodo(str(self.value)))
        return new