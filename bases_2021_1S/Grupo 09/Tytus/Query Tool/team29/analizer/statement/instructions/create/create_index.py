from team29.analizer.abstract import instruction
from team29.analizer.reports import Nodo
from team29.analizer.typechecker.Metadata import File
from team29.analizer.typechecker.Metadata import Struct


class CreateIndex(instruction.Instruction):
    def __init__(self, unique, idIndex, idTable, usingMethod, whereCl, optList=[]):
        self.unique = unique
        self.idIndex = idIndex
        self.idTable = idTable
        self.optList = optList
        self.whereCl = whereCl
        self.usingMethod = usingMethod
        if not idIndex:
            idIndex = "index_" + idTable
            for l in optList:
                idIndex += "_" + l[0]
            self.idIndex = idIndex

    def execute(self, environment):
        Struct.load()
        name = self.idIndex
        if self.existIndex(name):
            return "Error: ya existe un index con el nombre " + name
        table = Struct.extractTable(instruction.dbtemp, self.idTable)
        if table == 1 or table == 0:
            return (
                "Error: no existe la tabla "
                + self.idTable
                + " en la base de datos "
                + instruction.dbtemp
            )
        try:
            Index = File.importFile("Index")
            indexBody = {}
            indexBody["Table"] = self.idTable
            indexBody["Unique"] = self.unique
            indexBody["Method"] = self.usingMethod
            indexBody["Columns"] = []
            for c in self.optList:
                col = {}
                col["Name"] = c[0]
                col["Order"] = c[1]
                if c[2]:
                    nulls = c[2][0]
                    if c[2][1]:
                        nulls += " " + c[2][1]
                else:
                    if col["Order"] == "DESC":
                        nulls = "NULLS FIRST"
                    else:
                        nulls = "NULLS LAST"

                col["Nulls"] = nulls
                indexBody["Columns"].append(col)

            Index[name] = indexBody
            File.exportFile(Index, "Index")
            return "Index " + name + " creado"
        except:
            return "Error fatal"

    def existIndex(self, name):
        Index = File.importFile("Index")
        exists = Index.get(name)
        if exists != None:
            return True
        return False

    def dot(self):
        new = Nodo.Nodo("CREATE_INDEX")
        if self.unique:
            uniqueNode = Nodo.Nodo("UNIQUE")
            new.addNode(uniqueNode)
        if self.usingMethod:
            uhNode = Nodo.Nodo("USING_HASH")
            new.addNode(uhNode)
        id1 = Nodo.Nodo(str(self.idIndex))
        id2 = Nodo.Nodo(str(self.idTable))
        new.addNode(id1)
        new.addNode(id2)

        listNode = Nodo.Nodo("INDEX_LIST")
        new.addNode(listNode)

        for l in self.optList:

            if l[0] != None:
                l1 = Nodo.Nodo(str(l[0]))
                listNode.addNode(l1)
            if l[1] != None:
                l2 = Nodo.Nodo(str(l[1]))
                listNode.addNode(l2)
            if l[2]:
                l3 = Nodo.Nodo("NULLS")
                listNode.addNode(l3)
                if l[2][1] != None:
                    l4 = Nodo.Nodo(str(l[2][1]))
                    listNode.addNode(l4)

        if self.whereCl != None:
            new.addNode(self.whereCl.dot())

        return new