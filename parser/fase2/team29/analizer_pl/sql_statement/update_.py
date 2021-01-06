from analizer_pl.abstract import instruction


class Update(instruction.Instruction):
    def __init__(self, fromcl, values, wherecl, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.wherecl = wherecl
        self.fromcl = fromcl
        self.values = values

    def execute(self, environment):
        pass
