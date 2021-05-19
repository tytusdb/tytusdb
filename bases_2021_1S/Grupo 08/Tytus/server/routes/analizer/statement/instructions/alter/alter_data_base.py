from routes.analizer.abstract import instruction
from routes.analizer.typechecker.Metadata import Struct
from routes.analizer.reports import Nodo
from routes.analizer.storage import BPlusMode as jsonMode


# carga de datos
Struct.load()


class AlterDataBase(instruction.Instruction):
    def __init__(self, option, name, newname, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.option = option  # define si se renombra o se cambia de dueño
        self.name = name  # define el nombre nuevo de la base de datos o el nuevo dueño
        self.newname = newname

    def execute(self, environment):
        Struct.load()
        try:
            if self.option == "RENAME":
                valor = jsonMode.alterDatabase(self.name, self.newname)
                if valor == 2:
                    instruction.semanticErrors.append(
                        ["La base de datos " + str(self.name) + " no existe", self.row]
                    )
                    instruction.syntaxPostgreSQL.append(
                        "Error: 42000: La base de datos  "
                        + str(self.name)
                        + " no existe"
                    )
                    return "La base de datos no existe: '" + self.name + "'."
                if valor == 3:
                    instruction.semanticErrors.append(
                        [
                            "La base de datos " + str(self.newname) + " ya existe",
                            self.row,
                        ]
                    )
                    instruction.syntaxPostgreSQL.append(
                        "Error: 42P04: La base de datos  "
                        + str(self.newname)
                        + " ya existe"
                    )
                    return "El nuevo nombre para la base de datos existe"
                if valor == 1:
                    instruction.syntaxPostgreSQL.append("Error: XX000: Error interno")
                    return "Hubo un problema en la ejecucion de la sentencia"
                if valor == 0:
                    Struct.alterDatabaseRename(self.name, self.newname)
                    return (
                        "Base de datos renombrada: " + self.name + " - " + self.newname
                    )
                return "Error ALTER DATABASE RENAME: " + self.newname
            elif self.option == "OWNER":
                valor = Struct.alterDatabaseOwner(self.name, self.newname)
                if valor == 0:
                    return "Instruccion ejecutada con exito ALTER DATABASE OWNER"
                instruction.syntaxPostgreSQL.append("Error: XX000: Error interno")
                return "Error ALTER DATABASE OWNER"
            instruction.syntaxPostgreSQL.append("Error: XX000: Error interno")
            return "Fatal Error ALTER DATABASE: " + self.newname
        except:
            instruction.syntaxPostgreSQL.append(
                "Error: P0001: Error en la instruccion ALTER DATABASE"
            )

    def dot(self):
        new = Nodo.Nodo("ALTER_DATABASE")
        iddb = Nodo.Nodo(self.name)
        new.addNode(iddb)

        optionNode = Nodo.Nodo(self.option)
        new.addNode(optionNode)
        valOption = Nodo.Nodo(self.newname)
        optionNode.addNode(valOption)

        return new
