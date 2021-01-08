from analizer.abstract import instruction
from analizer.typechecker.Metadata import File
from analizer.typechecker.Metadata import Struct
from analizer.reports.Nodo import Nodo


class AlterIndex(instruction.Instruction):
    def __init__(self, name, exists, newName, row, column, idOrNumber=None):
        instruction.Instruction.__init__(self, row, column)
        self.name = name
        self.exists = exists
        self.newName = newName
        self.id = idOrNumber

    def execute(self, environment):
        Struct.load()
        Index = File.importFile("Index")
        exists = Index.get(self.name)
        result = []
        if not exists:
            if self.exists:
                result.append("El INDEX : " + self.name + " no existe")
            else:
                result.append("Error: El INDEX : " + self.name + " no existe")
            return result

        if not self.id:
            exists = Index.get(self.newName)
            if not exists:
                Index[self.newName] = Index.pop(self.name)
                result.append(
                    "Se cambio el nombre del INDEX : "
                    + self.name
                    + " a "
                    + self.newName
                )
            else:
                result.append("Error: El INDEX : " + self.newName + " ya existe")
        else:
            column = self.newName
            index = Index[self.name]
            for c in index["Columns"]:
                if c["Name"] == column:
                    if type(self.id) == int:
                        table = index["Table"]
                        columns = Struct.extractColumns(instruction.dbtemp, table)
                        if columns:
                            if self.id > len(columns):
                                result.append(
                                    "Error fatal: INDEX "
                                    + self.name
                                    + "numero de columna invalido"
                                )
                            else:
                                col = columns[self.id - 1].name
                                c["Name"] = col
                                result.append(
                                    "INDEX : "
                                    + self.name
                                    + " cambio la columna "
                                    + column
                                    + " por "
                                    + col
                                )
                        else:
                            result.append("Error fatal: INDEX " + self.name)
                    else:
                        c["Name"] = self.id
                        result.append(
                            "INDEX : "
                            + self.name
                            + " cambio la columna "
                            + column
                            + " por "
                            + self.id
                        )

                    Index[self.name] = index
                    break
        if result == []:
            result.append(
                "Error fatal: INDEX "
                + self.name
                + " columna invalida : "
                + self.newName
            )
        File.exportFile(Index, "Index")
        return result

    def dot(self):
        new = Nodo("ALTER_INDEX")
        n = Nodo(str(self.name))
        new.addNode(n)

        if self.exists:
            ifex = Nodo("IF_EXISTS")
            new.addNode(ifex)
        nn = Nodo(str(self.newName))
        new.addNode(nn)

        if self.id:
            idornum = Nodo(str(self.id))
            new.addNode(idornum)

        return new