from team29.analizer.abstract import instruction
from team29.analizer.typechecker.Metadata import Struct
from team29.analizer.reports import Nodo
# from storage.storageManager import jsonMode
import requests
import json

class Drop(instruction.Instruction):
    """
    Clase que representa la instruccion DROP TABLE and DROP DATABASE
    Esta instruccion es la encargada de eliminar una base de datos en el DBMS
    """

    def __init__(self, structure, name, exists, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.structure = structure
        self.name = name
        self.exists = exists

    def execute(self, environment):
        Struct.load()
        if self.structure == "TABLE":
            if instruction.dbtemp != "":
                form_data = {'nameDB': instruction.dbtemp, 'nameTab': self.name}
                resp = requests.post('http://127.0.0.1:9998/TABLE/dropTable', json=form_data)
                json1 = json.loads(resp.text)
                valor = json1["code"]
                if valor == 2:
                    instruction.semanticErrors.append(
                        [
                            "La base de datos "
                            + str(instruction.dbtemp)
                            + " no existe",
                            self.row,
                        ]
                    )
                    instruction.syntaxPostgreSQL.append(
                        "Error: 42000: La base de datos  "
                        + str(instruction.dbtemp)
                        + " no existe"
                    )
                    return "La base de datos no existe"
                if valor == 3:
                    instruction.semanticErrors.append(
                        ["La tabla " + str(self.name) + " no existe", self.row]
                    )
                    instruction.syntaxPostgreSQL.append(
                        "Error: 42P01: La tabla  " + str(self.name) + " no existe"
                    )
                    return "La tabla no existe en la base de datos"
                if valor == 1:
                    instruction.syntaxPostgreSQL.append(
                        "Error: XX000: Error interno"
                    )
                    return "Hubo un problema en la ejecucion de la sentencia DROP"
                if valor == 0:
                    Struct.dropTable(instruction.dbtemp, self.name)
                    return "DROP TABLE Se elimino la tabla: " + self.name
            instruction.syntaxPostgreSQL.append(
                "Error: 42000: Base de datos no especificada "
            )
            return "El nombre de la base de datos no esta especificado operacion no realizada"
        else:
            form_data = {'nameDB': self.name}
            resp = requests.post('http://127.0.0.1:9998/DB/dropDatabase', json=form_data)
            json1 = json.loads(resp.text)
            valor = json1["code"]
            if valor == 1:
                instruction.syntaxPostgreSQL.append("Error: XX000: Error interno")
                return "Hubo un problema en la ejecucion de la sentencia"
            if valor == 2:
                instruction.semanticErrors.append(
                    [
                        "La base de datos " + str(self.name) + " no existe",
                        self.row,
                    ]
                )
                instruction.syntaxPostgreSQL.append(
                    "Error: 42000: La base de datos  "
                    + str(self.name)
                    + " no existe"
                )
                return "La base de datos no existe"
            if valor == 0:
                Struct.dropDatabase(self.name)
                return "Instruccion ejecutada con exito DROP DATABASE"
        instruction.syntaxPostgreSQL.append("Error: XX000: Error interno DROPTABLE")
        return "Fatal Error: DROP TABLE"

    def dot(self):
        new = Nodo.Nodo("DROP")
        t = Nodo.Nodo(self.structure)
        n = Nodo.Nodo(self.name)
        new.addNode(t)
        new.addNode(n)
        return new
