from analizer_pl.abstract.instruction import Instruction
from analizer_pl.abstract.expression import TYPE
from analizer_pl.statement.expressions import code
from analizer_pl.abstract.environment import Environment


class Block(Instruction):
    def __init__(
        self, function, declaration, blocks, exception, label, row, column
    ) -> None:
        super().__init__(row, column)
        self.function = function
        self.declaration = declaration
        self.blocks = blocks
        self.exception = exception
        self.label = label

    def execute(self, environment):
        newEnv = Environment(environment)
        decl = ""
        bl = ""
        defFunc = self.function.execute(newEnv).value
        for d in self.declaration:
            decl += d.execute(newEnv).value
        for b in self.blocks:
            bl += b.execute(newEnv).value
        return code.C3D(defFunc + decl + bl + "\n", "block", self.row, self.column)
