from analizer_pl.abstract.instruction import Instruction
from analizer_pl import grammar
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo


class ElseIfStmt(Instruction):
    def __init__(self, row, column, expBool, stmt) -> None:
        super().__init__(row, column)
        self.expBool = expBool
        self.stmts = stmt

    def execute(self, environment):
        try:
            cod3d = self.p_fev()
            self.p_if_sum()
            boolCode = self.expBool.execute(environment)
            cod3d += boolCode.value
            cod3d += (
                "\tif "
                + str(boolCode.temp)
                + ": goto .etiv"
                + str(grammar.current_etiq + 1)
                + "\n"
            )
            grammar.optimizer_.addIF(
                str(boolCode.temp), str("etiv" + str(grammar.current_etiq + 1)), self.row
            )
            cod3d += "\tgoto .etif" + str(grammar.current_etiq + 2) + "\n"
            grammar.optimizer_.addGoto(
                str("etif" + str(grammar.current_etiq + 2)), self.row
            )
            grammar.back_fill.insert_true(grammar.current_etiq + 1)
            grammar.back_fill.insert_false(grammar.current_etiq + 2)
            grammar.current_etiq += 2
            cod3d += self.p_iev()
            for stmt in self.stmts:
                cod3d += stmt.execute(environment).value
            cod3d += self.p_fef()
            self.p_if_rest()
            return code.C3D(cod3d, "elseif", self.row, self.column)
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error \n Hint---> Else If Statement")

    def p_if_sum(self):
        if grammar.if_stmt != 0:
            grammar.back_fill.new_lists()
        grammar.if_stmt += 1

    def p_if_rest(self):
        grammar.if_stmt -= 1

    def p_iev(self):
        return grammar.back_fill.take_out_true_list(self.row)

    def p_fev(self):
        return grammar.back_fill.take_out_false_list(self.row)

    def p_fef(self):
        val = "\tgoto .etiqS" + str(grammar.next_etiq) + "\n"
        grammar.optimizer_.addGoto(str("etiqS" + str(grammar.next_etiq)), self.row)
        val += grammar.back_fill.take_out_true_list(self.row)
        return val

    def dot(self):
        new = Nodo("ELSE_IF")
        new.addNode(self.expBool.dot())
        then = Nodo("THEN")
        new.addNode(then)
        if self.stmts:
            for s in self.stmts:
                then.addNode(s.dot())

        return new