from Parser.analizer.abstract.expression import Expression, TYPE
from Parser.analizer.abstract import expression
from Parser.analizer.reports import Nodo
from Parser.analizer.statement.expressions.primitive import Primitive
import pandas as pd


class AggregateFunction(Expression):
    """
    Esta clase representa las funciones de agregacion utilizadas en el Group By
    """

    def __init__(self, func, colData, row, column) -> None:
        super().__init__(row, column)
        self.func = func.lower()
        self.colData = colData
        if colData == "*":
            self.temp = func + "(*)"
        else:
            self.temp = func + "(" + colData.temp + ")"

    def execute(self, environment):
        countGr = environment.groupCols
        if countGr == 0:
            if self.colData != "*":
                c = self.colData.execute(environment).value
                if self.func == "sum":
                    newDf = c.sum()
                elif self.func == "count":
                    newDf = c.count()
                elif self.func == "prom":
                    newDf = c.mean()
                else:
                    newDf = None
                    expression.list_errors.append(
                        "Error: 42725: Error en la funcion "
                        + str(self.func)
                        + "\n En la linea: "
                        + str(self.row)
                    )
            else:
                c = environment.dataFrame.iloc[:, -1:]
                if self.func == "count":
                    newDf = len(c)
                else:
                    newDf = None
                    expression.list_errors.append(
                        "Error: 42725: Error en la funcion "
                        + str(self.func)
                        + "\n En la linea: "
                        + str(self.row)
                    )
            return Primitive(TYPE.NUMBER, newDf, self.temp, self.row, self.column)
        if self.colData != "*":
            # Obtiene las ultimas columnas metidas (Las del group by)
            df = environment.dataFrame.iloc[:, -countGr:]
            c = self.colData.execute(environment)
            x = c.value
            x = pd.DataFrame(x)
            x.rename(columns={x.columns[0]: c.temp}, inplace=True)
            if len(list(x.columns)) > 1:
                df = pd.concat([df, x.iloc[:, :1]], axis=1)
            else:
                df = pd.concat([df, x], axis=1)
            cols = list(df.columns)[:-1]
            if self.func == "sum":
                newDf = df.groupby(cols).sum().reset_index()
            elif self.func == "count":
                newDf = df.groupby(cols).count().reset_index()
            elif self.func == "prom":
                newDf = df.groupby(cols).mean().reset_index()
            else:
                newDf = None
                expression.list_errors.append(
                    "Error: 42725: Error en la funcion "
                    + str(self.func)
                    + "\n En la linea: "
                    + str(self.row)
                )

            value = newDf.iloc[:, -1:]
        else:
            # Obtiene las ultimas columnas metidas (Las del group by)
            df = environment.dataFrame.iloc[:, -countGr:]

            x = df.iloc[:, -1:]
            x = pd.DataFrame(x)
            x.rename(columns={x.columns[0]: "count(*)"}, inplace=True)
            df = pd.concat([df, x], axis=1)
            cols = list(df.columns)[:-1]
            if self.func == "count":

                newDf = df.groupby(cols).count().reset_index()
            else:
                newDf = None
                expression.list_errors.append(
                    "Error: 42725: Error en la funcion "
                    + str(self.func)
                    + "\n En la linea: "
                    + str(self.row)
                )
            value = newDf.iloc[:, -1:]

        return Primitive(TYPE.NUMBER, value, self.temp, self.row, self.column)

    def dot(self):
        f = Nodo.Nodo(self.func)
        p = Nodo.Nodo("PARAMS")
        new = Nodo.Nodo("CALL")
        new.addNode(f)
        new.addNode(p)

        if self.colData != "*":
            p.addNode(self.colData.dot())
        else:
            p.addNode(Nodo.Nodo("*"))
        return new
