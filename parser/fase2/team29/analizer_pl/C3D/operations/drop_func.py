from os.path import extsep
from analizer_pl.abstract.instruction import Instruction
from analizer_pl.abstract.environment import Environment
from analizer_pl.statement.expressions import code
from analizer_pl import grammar
from analizer_pl.reports.Nodo import Nodo


class DropFunction(Instruction):
    def __init__(self, id, row, column) -> None:
        super().__init__(row, column)
        self.id = id

    def execute(self, environment):
        try:
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
        except:
            grammar.PL_errors.append("Error P0000: plpgsql fatal error \n Hint---> Drop Function")

    def dot(self):
        new = Nodo("DROP_FUNCTION")
        new.addNode(Nodo(str(self.id)))
        return new