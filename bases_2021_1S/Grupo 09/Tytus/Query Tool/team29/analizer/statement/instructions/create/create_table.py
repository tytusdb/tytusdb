from team29.analizer.abstract import instruction
from team29.analizer.abstract import instruction
from team29.analizer.typechecker.Metadata import Struct
from team29.analizer.reports import Nodo
# from storage.storageManager import jsonMode
from team29.analizer.typechecker import Checker
import requests
import json
from team29.analizer import variables

class CreateTable(instruction.Instruction):
    def __init__(self, exists, name, inherits, row, column, columns=[]):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.columns = columns
        self.inherits = inherits

    def execute(self, environment):
        Struct.load()
        # insert = [posiblesErrores,noColumnas]
        insert = Struct.insertTable(
            instruction.dbtemp, self.name, self.columns, self.inherits
        )
        error = insert[0]
        nCol = insert[1]
        if not error:
            error = True
        """
        Result
        0: insert
        1: error
        2: not found database
        3: exists table
        """
        if True:
            form_data = {'nameDB': instruction.dbtemp, 'nameTab': self.name, 'numCol': nCol}
            resp = requests.post('http://127.0.0.1:9998/TABLE/createTable', json=form_data)
            json1 = json.loads(resp.text)
            result = json1["code"]
            if result == 0:
                pass
            elif result == 1:
                instruction.syntaxPostgreSQL.append("Error: XX000: Error interno")
                return "Error: No se puede crear la tabla: " + self.name
            elif result == 2:
                instruction.semanticErrors.append(
                    "La base de datos " + instruction.dbtemp + " no existe"
                )
                instruction.syntaxPostgreSQL.append(
                    "Error: 3F000: base de datos" + instruction.dbtemp + " no existe"
                )
                return "Error: Base de datos no encontrada: " + instruction.dbtemp
            elif result == 3 and self.exists:
                instruction.semanticErrors.append(
                    ["La tabla " + str(self.name) + " ya existe", self.row]
                )
                instruction.syntaxPostgreSQL.append(
                    "Error: 42P07: La tabla  " + str(self.name) + " ya existe"
                )
                return "La tabla ya existe en la base de datos"
            else:
                instruction.semanticErrors.append(
                    ["La tabla " + str(self.name) + " ya existe", self.row]
                )
                instruction.syntaxPostgreSQL.append("Error: 42P07: tabla duplicada")
                return "Error: ya existe la tabla " + self.name
            pk = ""
            addPK = 0
            if pk:
                addPK = jsonMode.alterAddPK(instruction.dbtemp, self.name, pk)
            if addPK != 0:
                instruction.syntaxPostgreSQL.append(
                    "Error: 23505: Error en llaves primarias de la instruccion CREATE TABLE de la tabla "
                    + str(self.name)
                )
            return "Tabla " + self.name + " creada"
        else:
            # Struct.dropTable(instruction.dbtemp, self.name)
            return error

    def dot(self):
        new = Nodo.Nodo("CREATE_TABLE")

        if self.exists:
            ex = Nodo.Nodo("EXISTS")
            new.addNode(ex)
        n = Nodo.Nodo(self.name)
        new.addNode(n)
        c = Nodo.Nodo("COLUMNS")
        new.addNode(c)

        for cl in self.columns:
            if not cl[0]:
                id = Nodo.Nodo(cl[1])
                c.addNode(id)
                typ = Nodo.Nodo("TYPE")
                c.addNode(typ)
                typ1 = Nodo.Nodo(cl[2][0])
                typ.addNode(typ1)
                par = cl[2][1]
                if par[0] != None:
                    params = Nodo.Nodo("PARAMS")
                    typ.addNode(params)
                    for parl in par:
                        parl1 = Nodo.Nodo(str(parl))
                        params.addNode(parl1)

                colOpts = cl[3]
                if colOpts != None:
                    coNode = Nodo.Nodo("OPTIONS")
                    c.addNode(coNode)
                    for co in colOpts:
                        if co[0] == "NULL":
                            if co[1]:
                                notNullNode = Nodo.Nodo("NOT_NULL")
                            else:
                                notNullNode = Nodo.Nodo("NULL")
                            coNode.addNode(notNullNode)
                        elif co[0] == "DEFAULT":
                            defaultNode = Nodo.Nodo("DEFAULT")
                            coNode.addNode(defaultNode)
                            litDefaultNode = Nodo.Nodo(str(co[1]))
                            defaultNode.addNode(litDefaultNode)

                        elif co[0] == "PRIMARY":
                            primaryNode = Nodo.Nodo("PRIMARY_KEY")
                            coNode.addNode(primaryNode)

                        elif co[0] == "REFERENCES":
                            referencesNode = Nodo.Nodo("REFERENCES")
                            coNode.addNode(referencesNode)
                            idReferences = Nodo.Nodo(str(co[1]))
                            referencesNode.addNode(idReferences)
                        else:
                            constNode = Nodo.Nodo("CONSTRAINT")
                            coNode.addNode(constNode)
            else:
                if cl[1][0] == "UNIQUE":
                    uniqueNode = Nodo.Nodo("UNIQUE")
                    c.addNode(uniqueNode)
                    idlist = cl[1][1]

                    for il in idlist:
                        nl = Nodo.Nodo(str(il))
                        uniqueNode.addNode(nl)

                if cl[1][0] == "PRIMARY":
                    primNode = Nodo.Nodo("PRIMARY_KEY")
                    c.addNode(primNode)
                    idlist = cl[1][1]

                    for il in idlist:
                        nl = Nodo.Nodo(str(il))
                        primNode.addNode(nl)
                if cl[1][0] == "FOREIGN":
                    forNode = Nodo.Nodo("FOREIGN_KEY")
                    c.addNode(forNode)
                    idlist = cl[1][1]
                    for il in idlist:
                        nl = Nodo.Nodo(str(il))
                        forNode.addNode(nl)
                    refNode = Nodo.Nodo("REFERENCES")
                    forNode.addNode(refNode)
                    idNode = Nodo.Nodo(str(cl[1][2]))
                    refNode.addNode(idNode)
                    idlist2 = cl[1][3]
                    for il2 in idlist2:
                        nl2 = Nodo.Nodo(str(il2))
                        refNode.addNode(nl2)

        if self.inherits != None:
            inhNode = Nodo.Nodo("INHERITS")
            new.addNode(inhNode)
            inhNode2 = Nodo.Nodo(str(self.inherits))
            inhNode.addNode(inhNode2)
        return new
