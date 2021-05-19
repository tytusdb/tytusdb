from team29.analizer.reports import Nodo
from team29.analizer.abstract.instruction import Instruction


class LimitClause(Instruction):
    def __init__(self, num, offset, row, column) -> None:
        super().__init__(row, column)
        self.num = num
        self.offset = offset

    def execute(self, dataFrame, environment):
        temp = dataFrame
        if self.offset != None:
            temp = dataFrame[self.offset :]
        if self.num == "ALL":
            return temp
        return temp.head(self.num)

    def dot(self):
        new = Nodo.Nodo("LIMIT")
        numN = Nodo.Nodo(str(self.num))
        new.addNode(numN)
        if self.offset != None:
            off = Nodo.Nodo("OFFSET")
            new.addNode(off)
            offId = Nodo.Nodo(str(self.offset))
            off.addNode(offId)
        return new
