import sys

sys.path.append("../../..")
from  Fase1.storage.storageManager import storage
from  Fase1.analizer.typechecker.Metadata import Struct
from  Fase1.analizer.typechecker import Checker
from  Fase1.analizer.reports import Nodo
from  Fase1.analizer.abstract import instruction

# carga de datos
Struct.load()


class InsertInto(instruction.Instruction):
    def __init__(self, tabla, columns, parametros, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.tabla = tabla
        self.parametros = parametros
        self.columns = columns

    def execute(self, environment):
        try:
            lista = []
            params = []
            tab = self.tabla

            for p in self.parametros:
                params.append(p.execute(environment))

            result = Checker.checkInsert(
                instruction.dbtemp, self.tabla, self.columns, params
            )

            if result[0] == None:
                for p in result[1]:
                    if p == None:
                        lista.append(p)
                    else:
                        lista.append(p.value)
                res = storage.insert(instruction.dbtemp, tab, lista)
                if res == 2:
                    instruction.semanticErrors.append(
                        [
                            "La base de datos " + instruction.dbtemp + " no existe",
                            self.row,
                        ]
                    )
                    instruction.syntaxPostgreSQL.append(
                        "Error: 42000: La base de datos  "
                        + str(instruction.dbtemp)
                        + " no existe"
                    )
                    return "La base de datos no existe"
                elif res == 3:
                    instruction.semanticErrors.append(
                        ["La tabla " + str(tab) + " no existe", self.row]
                    )
                    instruction.syntaxPostgreSQL.append(
                        "Error: 42P01: La tabla " + str(tab) + " no existe"
                    )
                    return "No existe la tabla"
                elif res == 5:
                    instruction.semanticErrors.append(
                        [
                            "La instruccion INSERT tiene mas o menos registros que columnas",
                            self.row,
                        ]
                    )
                    instruction.syntaxPostgreSQL.append(
                        "Error: 42611: INSERT tiene mas o menos registros que columnas "
                    )
                    return "Columnas fuera de los limites"
                elif res == 4:
                    instruction.semanticErrors.append(
                        [
                            "El valor de la clave esta duplicada, viola la restriccion unica",
                            self.row,
                        ]
                    )
                    instruction.syntaxPostgreSQL.append(
                        "Error: 23505: el valor de clave esta duplicada, viola la restricción única "
                    )
                    return "Llaves primarias duplicadas"
                elif res == 1:
                    instruction.syntaxPostgreSQL.append("Error: XX000: Error interno")
                    return "Error en la operacion"
                elif res == 0:
                    return "Fila Insertada correctamente"
            else:
                return result[0]
        except:
            instruction.syntaxPostgreSQL.append(
                "Error: P0001: Error en la instruccion INSERT"
            )
            pass

    def dot(self):
        new = Nodo.Nodo("INSERT_INTO")
        t = Nodo.Nodo(self.tabla)
        par = Nodo.Nodo("PARAMS")
        new.addNode(t)
        for p in self.parametros:
            par.addNode(p.dot())

        if self.columns != None:
            colNode = Nodo.Nodo("COLUMNS")
            for c in self.columns:
                colNode.addNode(Nodo.Nodo(str(c)))
            new.addNode(colNode)

        new.addNode(par)
        return new
