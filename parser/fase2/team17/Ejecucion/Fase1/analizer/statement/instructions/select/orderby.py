from numpy.lib.arraysetops import isin
from  Fase1.analizer.reports import Nodo
from  Fase1.analizer.abstract.instruction import Instruction
from  Fase1.analizer.statement.expressions.identifiers import Identifiers


class OrderByElement:
    def __init__(self, colName, opt, null):
        self.colName = colName
        self.opt = opt
        self.null = null


class OrderByClause(Instruction):
    def __init__(self, orderElements, row, column) -> None:
        super().__init__(row, column)
        self.elements = orderElements

    def execute(self, dataFrame, environment):
        temp = dataFrame
        order = []
        asc = []
        na = "first"
        for el in self.elements:
            # order by number
            if isinstance(el.colName, Identifiers):
                el.colName = el.colName.execute(environment).temp
            if isinstance(el.colName, int):
                order.append(temp.columns[int(el.colName) - 1])
            # order by column
            else:
                order.append(el.colName)

            if el.opt == "ASC":
                asc.append(True)
            else:
                asc.append(False)

            if el.null == "FIRST":
                na = "first"
            else:
                na = "last"

        temp = temp.sort_values(by=order, ascending=asc, na_position=na)
        return temp.reset_index()

    def dot(self):
        new = Nodo.Nodo("order_by")
        return new