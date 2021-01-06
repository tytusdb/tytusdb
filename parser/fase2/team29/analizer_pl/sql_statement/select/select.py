from analizer_pl.abstract import instruction


class Select(instruction.Instruction):
    def __init__(
        self,
        params,
        fromcl,
        wherecl,
        groupbyCl,
        havingCl,
        limitCl,
        orderByCl,
        distinct,
        row,
        column,
    ):
        instruction.Instruction.__init__(self, row, column)
        self.params = params
        self.wherecl = wherecl
        self.fromcl = fromcl
        self.groupbyCl = groupbyCl
        self.havingCl = havingCl
        self.limitCl = limitCl
        self.orderByCl = orderByCl
        self.distinct = distinct

    def execute(self, environment):
        pass
