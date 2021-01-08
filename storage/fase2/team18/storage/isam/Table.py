from .ISAM import ISAM
from .ISAM import Tuple


class Table:
    def __init__(self, name, numberColumns):
        self.name = name
        self.numberColumns = numberColumns
        self.PK = []
        self.hiddenPK = 1
        self.tuples = ISAM()
        self.PKDefined = False
        self.droppdedPK = False

    def insert(self, PK, register):
        tup = Tuple(PK, register)
        return self.tuples.insert(tup)

    def extractTable(self):
        return self.tuples.extractAll()

    def extractRangeTable(self, lower, upper, column):
        return self.tuples.extractRange(lower, upper, column)

    def chart(self):
        self.tuples.chart()

    def truncate(self):
        self.tuples.truncate()

    def search(self, PK):
        return self.tuples.search(str(PK))

    def delete(self, PK):
        return self.tuples.delete(str(PK))

    def update(self, register, cols):
        if self.PKDefined:
            PKCols = self.PK
        else:
            PKCols = self.hiddenPK
            self.hiddenPK += 1
        return self.tuples.update(register, cols, PKCols)

