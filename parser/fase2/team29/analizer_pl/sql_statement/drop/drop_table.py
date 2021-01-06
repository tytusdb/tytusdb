from analizer_pl.abstract import instruction


class DropTable(instruction.Instruction):
    """"""

    def __init__(self, name, exists, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.name = name
        self.exists = exists

    def execute(self, environment):
        pass
