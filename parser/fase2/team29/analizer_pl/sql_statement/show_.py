from analizer_pl.abstract import instruction


class showDataBases(instruction.Instruction):
    def __init__(self, like, row, column):
        instruction.Instruction.__init__(self, row, column)
        if like != None:
            self.like = like[1 : len(like) - 1]
        else:
            self.like = None

    def execute(self, environment):
        pass
