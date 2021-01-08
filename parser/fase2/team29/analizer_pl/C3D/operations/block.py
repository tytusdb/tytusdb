from analizer_pl.abstract.instruction import Instruction
from analizer_pl.abstract.expression import TYPE
from analizer_pl.statement.expressions import code
from analizer_pl.abstract.environment import Environment
from analizer_pl.reports.Nodo import Nodo
from analizer_pl.C3D.operations import return_
from analizer_pl import grammar

environments = list()


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
        try:
            global environments
            newEnv = Environment(environment)
            environments.append([self.function.id, newEnv])
            decl = ""
            bl = ""
            defFunc = self.function.execute(newEnv).value
            for d in self.declaration:
                decl += d.execute(newEnv).value
            if self.function.proc == "PROCEDURE":
                for b in self.blocks:
                    if isinstance(b, return_.Return):
                        if b.exp:
                            grammar.PL_errors.append("Error P0000: Procedure no acepta return")
                            grammar.semantic_errors.append(["Procedure no acepta return",self.row])
                            # TODO: Error no puede venir return en procedure
                            pass
                        else:
                            bl += b.execute(newEnv).value
                    else:
                        bl += b.execute(newEnv).value
            else:
                for b in self.blocks:
                    bl += b.execute(newEnv).value
            grammar.optimizer_.addIgnoreString(str("stack.append(None)"), self.row, True)
            grammar.optimizer_.addLabel(str("endLabel"), self.row, True)
            return code.C3D(
                defFunc + decl + bl + "\tstack.append(None)\n" + "\tlabel .endLabel\n\n",
                "block",
                self.row,
                self.column,
            )
        except:
            grammar.PL_errors.append("Error P0000: Plpgsql fatal error ")

    def dot(self):
        new = Nodo("BLOCK")
        new.addNode(self.function.dot())

        dec = Nodo("DECLARATION")
        new.addNode(dec)
        for d in self.declaration:
            dec.addNode(d.dot())

        inst = Nodo("INSTRUCTIONS")
        new.addNode(inst)

        for b in self.blocks:
            inst.addNode(b.dot())
        return new