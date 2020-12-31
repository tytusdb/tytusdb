class Function(object):

    def __init__(self, row, column):
        """Constructor de la clase abstracta Function"""
        self.row = row
        self.column = column

    def execute(self, environment):
        raise NotImplementedError
