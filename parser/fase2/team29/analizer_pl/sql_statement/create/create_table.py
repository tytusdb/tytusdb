from analizer_pl.abstract import instruction


class CreateTable(instruction.Instruction):
    def __init__(self, exists, name, inherits, row, column, columns=[]):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.columns = columns
        self.inherits = inherits

    def execute(self, environment):
        pass
