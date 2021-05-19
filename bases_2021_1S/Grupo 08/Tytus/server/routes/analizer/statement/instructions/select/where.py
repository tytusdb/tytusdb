from routes.analizer.reports import Nodo
from routes.analizer.abstract.instruction import Instruction


class WhereClause(Instruction):
    def __init__(self, series, row, column):
        super().__init__(row, column)
        self.series = series

    def execute(self, environment):
        filt = self.series.execute(environment)
        df = environment.dataFrame.loc[filt.value]
        environment.dataFrame = df.reset_index(drop=True)
        return df

    def dot(self):
        new = Nodo.Nodo("WHERE")
        new.addNode(self.series.dot())
        return new
