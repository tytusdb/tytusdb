from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


class DropDatabase(instruction.Instruction):
    """
    Clase que representa la instruccion DROP TABLE and DROP DATABASE
    Esta instruccion es la encargada de eliminar una base de datos en el DBMS
    """

    def __init__(self, name, exists, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.name = name
        self.exists = exists

    def execute(self, environment):
        out = "fase1.execution("
        out += '"'
        out += "DROP DATABASE "
        out += self.exists
        out += self.name + ";"
        out += '")\n'
        return code.C3D(out, "drop_db", self.row, self.column)
