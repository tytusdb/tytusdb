from routes.analizer.reports import Nodo
from routes.analizer.storage import BPlusMode as jsonMode
from routes.analizer.abstract import instruction


class Truncate(instruction.Instruction):
    def __init__(self, name, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.name = name

    def execute(self, environment):
        try:
            valor = jsonMode.truncate(instruction.dbtemp, self.name)
            if valor == 2:
                instruction.semanticErrors.append(
                    [
                        "La base de datos " + str(instruction.dbtemp) + " no existe ",
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
                    ["La tabla " + str(self.name) + " no existe ", self.row]
                )
                instruction.syntaxPostgreSQL.append(
                    "Error: 42P01: La tabla " + str(self.name) + " no existe"
                )
                return "El nombre de la tabla no existe"
            if valor == 1:
                instruction.syntaxPostgreSQL.append("Error: XX000: Error interno")
                return "Hubo un problema en la ejecucion de la sentencia"
            if valor == 0:
                return "Truncate de la tabla: " + self.name
        except:
            instruction.syntaxPostgreSQL.append(
                "Error: P0001: Error en la instruccion TRUNCATE"
            )

    def dot(self):
        new = Nodo.Nodo("TRUNCATE")
        n = Nodo.Nodo(self.name)
        new.addNode(n)
        return new
