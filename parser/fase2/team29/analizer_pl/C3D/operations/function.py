from analizer_pl.abstract.instruction import Instruction
from analizer_pl.statement.expressions import code


class FunctionDeclaration(Instruction):
    def __init__(self, id, params, returns, row, column) -> None:
        super().__init__(row, column)
        self.id = id
        self.params = params
        self.returns = returns

    def execute(self, environment):
        environment.globalEnv.addFunction(self.id, self.returns, len(self.params))
        cd = "\ndef " + self.id + "():\n"
        for p in self.params:
            cd += "\t" + p.execute(environment).temp + " = stack.pop()\n"

        if self.params:
            for p in self.params:
                p.execute(environment)

        # TODO: Codigo 3d
        return code.C3D(cd, self.id, self.row, self.column)
