from team29.analizer.abstract.expression import Expression, TYPE
from team29.analizer.abstract import expression
from team29.analizer.reports import Nodo
from team29.analizer.statement.expressions.primitive import Primitive


class ExistsRelationalOperation(Expression):
    def __init__(self, subquery, row, column) -> None:
        super().__init__(row, column)
        self.subquery = subquery
        self.temp = "EXISTS( subquery )"

    def execute(self, environment):
        try:
            df1 = environment.dataFrame.copy()
            names = {}
            for n in list(df1.columns):
                names[n] = n.split(".")[1]
            df1.rename(columns=names, inplace=True)
            df2 = self.subquery.execute(environment)[0]
            y = df1.columns.intersection(df2.columns)
            lst = list(y)
            if len(lst) < 1:
                expression.list_errors.append(
                    "Error: 42P10: Referencia de columnas invalidas EXIST"
                    + "\n En la linea: "
                    + str(self.row)
                )
            value = df1[lst].apply(tuple, 1).isin(df2[lst].apply(tuple, 1))
            return Primitive(TYPE.BOOLEAN, value, self.temp, self.row, self.column)
        except:
            expression.list_errors.append(
                "Error: XX000: Error interno (Exist Relational Operation)"
                + "\n En la linea: "
                + str(self.row)
            )

    def dot(self):
        new = Nodo.Nodo("EXISTS")
        new.addNode(self.subquery.dot())
        return new
