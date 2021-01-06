from analizer_pl.abstract import instruction


class Delete(instruction.Instruction):
    def __init__(self, fromcl, wherecl, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.wherecl = wherecl
        self.fromcl = fromcl

    def execute(self, environment):
        pass
