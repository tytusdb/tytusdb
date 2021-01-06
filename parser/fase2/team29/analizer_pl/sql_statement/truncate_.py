from analizer_pl.abstract import instruction


class Truncate(instruction.Instruction):
    def __init__(self, name, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.name = name

    def execute(self, environment):
        pass
