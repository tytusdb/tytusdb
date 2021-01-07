from analizer_pl.abstract.instruction import Instruction
from analizer_pl.abstract.environment import Environment
from analizer_pl.statement.expressions import code
from analizer_pl import grammar


class DropFunction(Instruction):
    def __init__(self, id, row, column) -> None:
        super().__init__(row, column)
        self.id = id

    def execute(self, environment):
        c3d = ""
        tab = ""
        tab1 = False
        if isinstance(environment, Environment):
            tab += "\t"
            tab1 = True
            func = environment.globalEnv.dropFunction(self.id)
        else:
            func = environment.dropFunction(self.id)
        if func:
            c3d += tab + "del " + self.id + "\n"
            grammar.optimizer_.addIgnoreString(str("del " + self.id), self.row, tab1)
        return code.C3D(c3d, "drop_func", self.row, self.column)
