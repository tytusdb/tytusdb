from  Fase1.analizer.abstract.expression import Expression


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
