from analizer.abstract.expression import Expression


class C3D(Expression):
    """
    Esta clase contiene el codigo de 3 direcciones
    """

    def __init__(self, value, temp, row, column):
        super().__init__(row, column)
        self.value = value
        self.temp = str(temp)

    def execute(self, environment):
        return self
