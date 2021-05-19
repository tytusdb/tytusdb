from team29.analizer.abstract import instruction
from team29.analizer.typechecker.Metadata import Struct
from team29.analizer.reports import Nodo
# from storage.storageManager import jsonMode
from team29.analizer.typechecker import Checker
import requests
import json

# carga de datos
Struct.load()


class AlterTable(instruction.Instruction):
    def __init__(self, table, row, column, params=[]):
        instruction.Instruction.__init__(self, row, column)
        self.table = table
        self.params = params

    def execute(self, environment):
        Struct.load()
        # alter = Struct.alterColumnsTable(instruction.dbtemp, self.table, self.params)
        if((self.params[0])[0] == "ADD"):
            form_data = {'nameDB': instruction.dbtemp, 'nameTab': self.table, 'default':self.params}
            resp = requests.post('http://127.0.0.1:9998/TABLE/alterAddColumn', json=form_data)
            json1 = json.loads(resp.text)
            valor = json1["code"]
            if valor == 0:
                alter = "Tabla alterada: " + self.table
            elif valor == 1:
                alter = "Error la modificar la tabla" + self.table
            elif valor == 2:
                alter = "La base de datos" + instruction.dbtemp + " no existe"
            elif valor == 3:
                alter = "La tabla " + self.table + " no existe en la base de datos"	
        else:
            ArraySplit = (((self.params[0])[1])[1]).split("_")
            form_data = {'nameDB': instruction.dbtemp, 'nameTab': self.table, 'numCol':int(ArraySplit[1])}
            resp = requests.post('http://127.0.0.1:9998/TABLE/alterDropColumn', json=form_data)
            json1 = json.loads(resp.text)
            valor = json1["code"]
            if valor == 0:
                alter = "Tabla alterada: " + self.table
            elif valor == 1:
                alter = "Error la modificar la tabla" + self.table
            elif valor == 2:
                alter = "La base de datos" + instruction.dbtemp + " no existe"
            elif valor == 3:
                alter = "La tabla " + self.table + " no existe en la base de datos"			
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
