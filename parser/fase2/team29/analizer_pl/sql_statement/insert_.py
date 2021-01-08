from analizer_pl.abstract import instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.abstract.environment import Environment
from analizer_pl import grammar


class InsertInto(instruction.Instruction):
    def __init__(self, tabla, columns, parametros, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.tabla = tabla
        self.parametros = parametros
        self.columns = columns

    def execute(self, environment):
        try:
            out = "fase1.execution(dbtemp + "
            out += '" '
            out += "INSERT INTO "
            out += self.tabla + " "
            out += self.columns
            out += "VALUES ("
            parVal = ""
            j = 0
            for i in range(len(self.parametros) - 1):
                j = i + 1
                pval = self.parametros[i].execute(environment)
                parVal += pval.value
                out += pval.temp + ", "
            pval = self.parametros[j].execute(environment)
            parVal += pval.value
            out += pval.temp
            out += ");"
            out += '")\n'
            cod = out
            if isinstance(environment, Environment):
                out = "\t" + out
            out = parVal + out
            if isinstance(environment, Environment):
                grammar.optimizer_.addIgnoreString(cod, self.row, True)
            else:
                grammar.optimizer_.addIgnoreString(cod, self.row, False)
            return code.C3D(out, "insert", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: Plpgsql fatal error \n Hint---> Insert ")
    def dot(self):
        return Nodo("SQL_INSTRUCTION:_INSERT")