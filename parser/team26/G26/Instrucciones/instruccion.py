class Instruccion:
    'Clase abstracta de instruccion'
    def __init__(self, type, line, column):
        self.type = type
        self.line = line
        self.column = column

    def execute(self):
        return self.val

    def __repr__(self):
        return str(self.__dict__)
