from analizer_pl.abstract.instruction import Instruction
from analizer_pl import grammar
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo


class If_Statement(Instruction):
    def __init__(self, row, column, expBool, elseif_list, else_, stmts) -> None:
        super().__init__(row, column)
        self.expBool = expBool
        self.elseif_list = elseif_list
        self.else_ = else_
        self.stmts = stmts

    def execute(self, environment):
        self.p_if_sum()
        boolCode = self.expBool.execute(environment)
        cod3d = boolCode.value
        cod3d += (
            "\tif "
            + str(boolCode.temp)
            + ": goto .etiv"
            + str(grammar.current_etiq + 1)
            + "\n"
        )
        cod3d += "\tgoto .etif" + str(grammar.current_etiq + 2) + "\n"
        grammar.back_fill.insert_true(grammar.current_etiq + 1)
        grammar.back_fill.insert_false(grammar.current_etiq + 2)
        grammar.current_etiq += 2
        cod3d += self.p_iev()
        codeElseif = ""
        for stmt in self.stmts:
            cod3d += stmt.execute(environment).value
        if len(self.elseif_list) > 0:
            for elseif in self.elseif_list:
                codeElseif += elseif.execute(environment).value
        cod3d += self.p_fef()
        cod3d += codeElseif
        if self.else_ != None:
            cod3d += self.else_.execute(environment).value
        else:
            cod3d += self.p_write_next_etiq()
            cod3d += self.p_fev()
        self.p_if_rest()
        return code.C3D(cod3d, "if", self.row, self.column)

    def p_if_sum(self):
        if grammar.if_stmt != 0:
            grammar.back_fill.new_lists()
        grammar.if_stmt += 1

    def p_if_rest(self):
        grammar.if_stmt -= 1

    def p_iev(self):
        return grammar.back_fill.take_out_true_list()

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
        new = Nodo("IF")
        new.addNode(self.expBool.dot())
        then = Nodo("THEN")
        new.addNode(then)
        for s in self.stmts:
            then.addNode(s.dot())
        for eif in self.elseif_list:
            new.addNode(eif.dot())

        if self.else_:
            new.addNode(self.else_.dot())
        return new