import sys

sys.path.append("../../..")
# from storage.storageManager import jsonMode
from team29.analizer.typechecker.Metadata import Struct
from team29.analizer.typechecker import Checker
from team29.analizer.reports import Nodo
from team29.analizer.abstract import instruction
import requests
import json

# carga de datos
Struct.load()


class InsertInto(instruction.Instruction):
    def __init__(self, tabla, columns, parametros, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.tabla = tabla
        self.parametros = parametros
        self.columns = columns

    def execute(self, environment):
        
        Struct.load()
        lista = []
        params = []
        tab = self.tabla

        for p in self.parametros:
            params.append(p.execute(environment))
            
        if True:
            for p in params:
                if p == None:
                    lista.append(p)
                else:
                    lista.append(p.value)
            form_data = {'nameDB': instruction.dbtemp, 'nameTab': tab, 'registrer': lista}
            resp = requests.post('http://127.0.0.1:9998/TUPLA/insert', json=form_data)
            json1 = json.loads(resp.text)
            res = json1["code"]
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
            return res
        
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
