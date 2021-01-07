from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment


class InsertInto(instruction.Instruction):
    def __init__(self, tabla, columns, parametros, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.tabla = tabla
        self.parametros = parametros
        self.columns = columns

    def execute(self, environment):
        tab = ""
        if isinstance(environment, Environment):
            tab += "\t"
        out = tab+"fase1.execution(dbtemp + "
        out += '" '
        out += "INSERT INTO "
        out += self.tabla + " "
        out += self.columns
        out += "VALUES ("
        parVal = ""
        j = 0
        for i in range(len(self.parametros)-1):
            j = i + 1
            pval = self.parametros[i].execute(environment)
            parVal += pval.value
            out += pval.temp + ", "
        pval = self.parametros[j].execute(environment)
        parVal += pval.value
        out += pval.temp
        out += ");"
        out += '")\n'
        out = parVal + out
        return code.C3D(out, "insert", self.row, self.column)

    def dot(self):
        return Nodo("SQL_INSTRUCTION:_INSERT")