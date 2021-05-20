from utilities.analisys_parser.analizer.reports import Nodo
from utilities.analisys_parser.analizer.abstract import instruction
from utilities.analisys_parser.analizer.statement.instructions.select.select import Select
from utilities.analisys_parser.analizer.symbol.symbol import Symbol
from utilities.analisys_parser.analizer.abstract.expression import Expression
from utilities.storage import avlMode
from utilities.analisys_parser.analizer.typechecker.Metadata import Struct

import pandas as pd


class FromClause(instruction.Instruction):
    """
    Clase encargada de la clausa FROM para la obtencion de datos
    """

    def __init__(self, tables, aliases, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.tables = tables
        self.aliases = aliases

    def crossJoin(self, tables):
        if len(tables) <= 1:
            return tables[0]
        for t in tables:
            t["____tempCol"] = 1

        new_df = tables[0]
        i = 1
        while i < len(tables):
            new_df = pd.merge(new_df, tables[i], on=["____tempCol"])
            i += 1

        new_df = new_df.drop("____tempCol", axis=1)
        return new_df

    def execute(self, environment):
        Struct.load()
        tempDf = None
        for i in range(len(self.tables)):
            exec = self.tables[i].execute(environment)
            data = exec[0]
            types = exec[1]
            if isinstance(self.tables[i], Select):
                newNames = {}
                subqAlias = self.aliases[i]
                for (columnName, columnData) in data.iteritems():
                    colSplit = columnName.split(".")
                    if len(colSplit) >= 2:
                        newNames[columnName] = subqAlias + "." + colSplit[1]
                        types[subqAlias + "." + colSplit[1]] = columnName
                    else:
                        newNames[columnName] = subqAlias + "." + colSplit[0]
                        types[subqAlias + "." + colSplit[0]] = columnName
                data.rename(columns=newNames, inplace=True)
                environment.addVar(subqAlias, subqAlias, "TABLE", self.row, self.column)
            else:
                sym = Symbol(
                    self.tables[i].name,
                    None,
                    self.tables[i].row,
                    self.tables[i].column,
                )
                environment.addSymbol(self.tables[i].name, sym)
                if self.aliases[i]:
                    environment.addSymbol(self.aliases[i], sym)
            if i == 0:
                tempDf = data
            else:
                tempDf = self.crossJoin([tempDf, data])
            environment.dataFrame = tempDf
            try:
                environment.types.update(types)
            except:
                instruction.syntaxPostgreSQL.append(
                    "Error: P0001: Error en la instruccion SELECT clausula FROM"
                )
        return

    def dot(self):
        new = Nodo.Nodo("FROM")
        for t in self.tables:
            if isinstance(t, Select):
                n = t.dot()
                new.addNode(n)
            else:
                t1 = Nodo.Nodo(t.name)
                new.addNode(t1)
        for a in self.aliases:
            a1 = Nodo.Nodo(a)
            new.addNode(a1)
        return new


class TableID(Expression):
    """
    Esta clase representa un objeto abstracto para el manejo de las tablas
    """

    type_ = None

    def __init__(self, name, row, column):
        Expression.__init__(self, row, column)
        self.name = name

    def execute(self, environment):
        result = avlMode.extractTable(instruction.dbtemp, self.name)
        if result == None:
            instruction.semanticErrors.append(
                [
                    "La tabla "
                    + str(self.name)
                    + " no pertenece a la base de datos "
                    + instruction.dbtemp,
                    self.row,
                ]
            )
            instruction.syntaxPostgreSQL.append(
                "Error: 42P01: la relacion "
                + instruction.dbtemp
                + "."
                + str(self.name)
                + " no existe"
            )
            return "FATAL ERROR TABLE ID"
        # Almacena una lista con con el nombre y tipo de cada columna
        lst = Struct.extractColumns(instruction.dbtemp, self.name)
        columns = [l.name for l in lst]
        newColumns = [self.name + "." + col for col in columns]
        df = pd.DataFrame(result, columns=newColumns)
        environment.addTable(self.name)
        tempTypes = {}
        for i in range(len(newColumns)):
            tempTypes[newColumns[i]] = lst[i].type
        return [df, tempTypes]
