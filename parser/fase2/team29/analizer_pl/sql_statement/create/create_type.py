from analizer_pl.abstract import instruction


class CreateType(instruction.Instruction):
    def __init__(self, exists, name, row, column, values=[]):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.values = values

    def execute(self, environment):
        pass
