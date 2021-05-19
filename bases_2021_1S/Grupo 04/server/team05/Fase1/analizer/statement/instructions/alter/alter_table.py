from  Fase1.analizer.abstract import instruction
from  Fase1.analizer.typechecker.Metadata import Struct
from  Fase1.analizer.reports import Nodo
from  Fase1.storage.storageManager import jsonMode
from  Fase1.storage import avlMode
from  Fase1.analizer.typechecker import Checker

# carga de datos
Struct.load()


class AlterTable(instruction.Instruction):
    def __init__(self, table, row, column, params=[]):
        instruction.Instruction.__init__(self, row, column)
        self.table = table
        self.params = params

    def execute(self, environment):
        alter = Struct.alterColumnsTable(instruction.dbtemp, self.table, self.params)
        if alter == None:
            alter = Checker.checkValue(instruction.dbtemp, self.table)
            Struct.save()
        if alter == None:
            alter = "Tabla alterada: " + self.table
        return alter

    def dot(self):
        new = Nodo.Nodo("ALTER_TABLE")
        idNode = Nodo.Nodo(str(self.table))
        new.addNode(idNode)

        for p in self.params:
            operacion = Nodo.Nodo(p[0])
            new.addNode(operacion)
            if p[0] == "ADD":
                if not p[1][0]:
                    col = Nodo.Nodo(p[1][1])
                    operacion.addNode(col)
                    typ = Nodo.Nodo(str(p[1][2][0]))
                    operacion.addNode(typ)
                    if p[1][2][1][0] != None:
                        parNode = Nodo.Nodo("PARAMS")
                        typ.addNode(parNode)
                        for p2 in p[1][2][1]:
                            lit = Nodo.Nodo(str(p2))
                            parNode.addNode(lit)
                else:
                    if p[1][1][0] == "PRIMARY":
                        primNode = Nodo.Nodo("PRIMARY_KEY")
                        operacion.addNode(primNode)
                        idlist = p[1][1][1]
                        for il in idlist:
                            nl = Nodo.Nodo(str(il))
                            primNode.addNode(nl)
                    elif p[1][1][0] == "FOREIGN":
                        forNode = Nodo.Nodo("FOREIGN_KEY")
                        operacion.addNode(forNode)
                        idlist = p[1][1][1]
                        for il in idlist:
                            nl = Nodo.Nodo(str(il))
                            forNode.addNode(nl)
                        refNode = Nodo.Nodo("REFERENCES")
                        forNode.addNode(refNode)
                        idNode = Nodo.Nodo(str(p[1][1][2]))
                        refNode.addNode(idNode)
                        idlist2 = p[1][1][3]
                        for il2 in idlist2:
                            nl2 = Nodo.Nodo(str(il2))
                            refNode.addNode(nl2)
                    elif p[1][1][0] == "UNIQUE":
                        uniqueNode = Nodo.Nodo("UNIQUE")
                        operacion.addNode(uniqueNode)
                        if p[1][1][2] != None:
                            const = Nodo.Nodo("CONSTRAINT")
                            uniqueNode.addNode(const)
                            idcont = Nodo.Nodo(str(p[1][1][2]))
                            const.addNode(idcont)
                        id2const = Nodo.Nodo(str(p[1][1][1][0]))
                        uniqueNode.addNode(id2const)
            elif p[0] == "DROP":
                subOper = Nodo.Nodo(str(p[1][0]))
                idDrop = Nodo.Nodo(str(p[1][1]))
                operacion.addNode(subOper)
                operacion.addNode(idDrop)
            elif p[0] == "RENAME":
                rename1 = Nodo.Nodo(str(p[1][0]))
                rename2 = Nodo.Nodo(str(p[1][1]))
                operacion.addNode(rename1)
                operacion.addNode(rename2)
            elif p[0] == "ALTER":
                idAlter = Nodo.Nodo(str(p[1][1]))
                operacion.addNode(idAlter)
                if p[1][0] == "SET":
                    setNode = Nodo.Nodo("SET")
                    operacion.addNode(setNode)
                    if p[1][2][0] == "DEFAULT":
                        defNode = Nodo.Nodo("DEFAULT")
                        defNode.addNode(p[1][2][1].dot())
                        setNode.addNode(defNode)
                    elif p[1][2][1]:
                        notnullN = Nodo.Nodo("NOT_NULL")
                        setNode.addNode(notnullN)
                    elif not p[1][2][1]:
                        nullN = Nodo.Nodo("NULL")
                        setNode.addNode(nullN)
                elif p[1][0] == "TYPE":
                    typeNode = Nodo.Nodo("TYPE")
                    typ2 = Nodo.Nodo(str(p[1][2][0]))
                    typeNode.addNode(typ2)
                    operacion.addNode(typeNode)
                    if p[1][2][1][0] != None:
                        parNode2 = Nodo.Nodo("PARAMS")
                        typ2.addNode(parNode2)
                        for p3 in p[1][2][1]:
                            lit2 = Nodo.Nodo(str(p3))
                            parNode2.addNode(lit2)
        return new
