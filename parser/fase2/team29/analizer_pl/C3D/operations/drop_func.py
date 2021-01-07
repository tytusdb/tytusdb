from analizer_pl.abstract.instruction import Instruction
from analizer_pl.abstract.environment import Environment
from analizer_pl.statement.expressions import code


class DropFunction(Instruction):
    def __init__(self, id, row, column) -> None:
        super().__init__(row, column)
        self.id = id

    def execute(self, environment):
        c3d = ""
        tab = ""
        if isinstance(environment, Environment):
            tab += "\t"
            func = environment.globalEnv.dropFunction(self.id)
        else:
            func = environment.dropFunction(self.id)
        if func:
            c3d += tab + "del " + self.id + "\n"
        return code.C3D(c3d, "drop_func", self.row, self.column)
