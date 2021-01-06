from analizer_pl.abstract.instruction import Instruction
from analizer_pl import grammar
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo


class ElseStmt(Instruction):
    def __init__(self, row, column, stmt) -> None:
        super().__init__(row, column)
        self.stmts = stmt

    def execute(self, environment):
        cod3d = self.p_fev()
        for stmt in self.stmts:
            cod3d += stmt.execute(environment).value
        cod3d += self.p_fef()
        cod3d += self.p_write_next_etiq()
        cod3d += self.p_fev()
        return code.C3D(cod3d, "else", self.row, self.column)

    def p_fev(self):
        return grammar.back_fill.take_out_false_list()

    def p_fef(self):
        val = "\tgoto .etiqS" + str(grammar.next_etiq) + "\n"
        val += grammar.back_fill.take_out_true_list()
        return val

    def p_write_next_etiq(self):
        val = "\tlabel .etiqS" + str(grammar.next_etiq) + "\n"
        grammar.next_etiq += 1
        return val

    def dot(self):
        new = Nodo("ELSE")
        for s in self.stmts:
            new.addNode(s.dot())

        return new