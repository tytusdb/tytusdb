from team29.analizer.reports import Nodo
from team29.analizer.abstract import instruction
from team29.analizer.symbol.environment import Environment
from team29.analizer.statement.instructions.select.select import Select
import pandas as pd


class Union(Select):
    """
    Clase encargada de la instruccion CHECK que almacena la condicion
    a desarrollar en el CHECK
    """

    def __init__(self, s1, s2, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.s1 = s1
        self.s2 = s2

    def execute(self, environment):
        newEnv = Environment(environment, instruction.dbtemp)
        instruction.envVariables.append(newEnv)
        s1 = self.s1.execute(newEnv)
        s2 = self.s2.execute(newEnv)
        df1 = s1[0]
        df2 = s2[0]
        types1 = list(s1[1].values())
        types2 = list(s2[1].values())
        if len(df1.columns) != len(df2.columns):
            instruction.syntaxPostgreSQL.append(
                "Error: 42611: UNION definicion en numero de columnas invalida "
            )
            return "Error Union: El numero de columnas no coinciden"
        for i in range(len(types1)):
            if types1[i] != types2[i]:
                instruction.semanticErrors.append(
                    [
                        "Error Union: discrepancia de tipo de datos entre columnas",
                        self.row,
                    ]
                )
                instruction.syntaxPostgreSQL.append(
                    "Error: 42804: Union discrepancia de tipo de datos entre columnas "
                )
                return "Error: Los tipos de columnas no coinciden"
        df2.columns = df1.columns.tolist()
        df = pd.concat([df1, df2], ignore_index=True)
        return [df, types1]

    def dot(self):
        new = Nodo.Nodo("UNION")
        new.addNode(self.s1.dot())
        new.addNode(self.s2.dot())
        return new


class Intersect(Select):
    """
    Clase encargada de la instruccion CHECK que almacena la condicion
    a desarrollar en el CHECK
    """

    def __init__(self, s1, s2, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.s1 = s1
        self.s2 = s2

    def execute(self, environment):
        newEnv = Environment(environment, instruction.dbtemp)
        instruction.envVariables.append(newEnv)
        s1 = self.s1.execute(newEnv)
        s2 = self.s2.execute(newEnv)
        df1 = s1[0]
        df2 = s2[0]
        types1 = list(s1[1].values())
        types2 = list(s2[1].values())
        if len(df1.columns) != len(df2.columns):
            instruction.syntaxPostgreSQL.append(
                "Error: 42611: INTERSEC definicion en numero de columnas invalida "
            )

            return "Error: El numero de columnas no coinciden"
        for i in range(len(types1)):
            if types1[i] != types2[i]:
                instruction.semanticErrors.append(
                    ["Error discrepancia de tipo de datos entre columnas", self.row]
                )
                instruction.syntaxPostgreSQL.append(
                    "Error: 42804: discrepancia de tipo de datos entre columnas "
                )
                return "Error: Los tipos de columnas no coinciden"
        df = df1.merge(df2).drop_duplicates(ignore_index=True)
        return [df, types1]

    def dot(self):
        new = Nodo.Nodo("INTERSECT")
        new.addNode(self.s1.dot())
        new.addNode(self.s2.dot())
        return new


class Except_(Select):
    """
    Clase encargada de la instruccion CHECK que almacena la condicion
    a desarrollar en el CHECK
    """

    def __init__(self, s1, s2, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.s1 = s1
        self.s2 = s2

    def execute(self, environment):
        newEnv = Environment(environment, instruction.dbtemp)
        instruction.envVariables.append(newEnv)
        s1 = self.s1.execute(newEnv)
        s2 = self.s2.execute(newEnv)
        df1 = s1[0]
        df2 = s2[0]
        types1 = list(s1[1].values())
        types2 = list(s2[1].values())
        if len(df1.columns) != len(df2.columns):
            instruction.syntaxPostgreSQL.append(
                "Error: 42611: EXCEPT definicion en numero de columnas invalida "
            )
            return "Error: El numero de columnas no coinciden"
        for i in range(len(types1)):
            if types1[i] != types2[i]:
                instruction.semanticErrors.append(
                    ["Error discrepancia de tipo de datos entre columnas", self.row]
                )
                instruction.syntaxPostgreSQL.append(
                    "Error: 42804: discrepancia de tipo de datos entre columnas"
                )
                return "Error: Los tipos de columnas no coinciden"
        df = df1.merge(df2, how="outer", indicator=True).loc[
            lambda x: x["_merge"] == "left_only"
        ]
        del df["_merge"]
        return [df, types1]

    def dot(self):
        new = Nodo.Nodo("EXCEPT")
        new.addNode(self.s1.dot())
        new.addNode(self.s2.dot())
        return new
