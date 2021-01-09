from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class CreateDatabase(instruction.Instruction):
    """
    Clase que representa la instruccion CREATE DATABASE
    Esta instruccion es la encargada de crear una nueva base de datos en el DBMS
    """

    def __init__(self, replace, exists, name, owner, mode, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.mode = mode
        self.owner = owner
        self.replace = replace

    def execute(self, environment):
        try:
            out = "fase1.execution("
            out += '"'
            out += "CREATE "
            out += self.replace
            out += " DATABASE "
            out += self.exists + " "
            out += self.name + " "
            out += self.owner + " "
            out += self.mode + ";"
            out += '")\n'
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(out, self.row, True)
                out = "\t" + out
            else:
                grammar.optimizer_.addIgnoreString(out, self.row, False)
            return code.C3D(out, "create_db", self.row, self.column)
        except:
            grammar.PL_errors.append(
                "Error P0000: plpgsql fatal error \n Hint---> Create DataBase"
            )

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_CREATE_DATABASE")
