from analizer_pl.abstract import instruction


class CreateIndex(instruction.Instruction):
    def __init__(self, unique, idIndex, idTable, usingMethod, whereCl, optList=[]):
        self.unique = unique
        self.idIndex = idIndex
        self.idTable = idTable
        self.optList = optList
        self.whereCl = whereCl
        self.usingMethod = usingMethod
        if not idIndex:
            idIndex = "index_" + idTable
            for l in optList:
                idIndex += "_" + l[0]
            self.idIndex = idIndex

    def execute(self, environment):
        pass
