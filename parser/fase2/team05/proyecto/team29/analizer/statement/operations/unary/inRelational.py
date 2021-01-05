from analizer.abstract.expression import Expression, TYPE
from analizer.abstract import expression
from analizer.reports import Nodo
from analizer.statement.expressions.primitive import Primitive


class InRelationalOperation(Expression):
    def __init__(self, colData, optNot, subquery, row, column) -> None:
        super().__init__(row, column)
        self.colData = colData
        self.subquery = subquery
        self.optNot = optNot
        self.temp = colData.temp + optNot + " IN ( subquery )"

    def execute(self, environment):
        col = self.colData.execute(environment)
        df = self.subquery.execute(environment)[0]
        # TODO: Falta agregar la verificacion de types
        if len(list(df.columns)) != 1:
            expression.list_errors.append(
                "Error: XX000: Error interno (Exist Relational Operation)"
                + "\n En la linea: "
                + str(self.row)
            )
        value = col.value.isin(df.iloc[:, 0])
        if self.optNot == "NOT":
            value = ~value
        return Primitive(TYPE.BOOLEAN, value, self.temp, self.row, self.column)

    def dot(self):

        n1 = self.optNot + " IN"
        new = Nodo.Nodo(n1)
        new.addNode(self.colData.dot())
        new.addNode(self.subquery.dot())
        return new
