from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code


class InsertInto(instruction.Instruction):
    def __init__(self, tabla, columns, parametros, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.tabla = tabla
        self.parametros = parametros
        self.columns = columns

    def execute(self, environment):
        out = "fase1.execution(dbtemp + "
        out += '" '
        out += "INSERT "
        out += self.exists + " "
        out += self.name + " ("
        out += self.columns + " )"
        out += self.inherits + ";"
        out += '")\n'
        return code.C3D(out, "insert", self.row, self.column)
