from analizer_pl.abstract.instruction import Instruction
from analizer_pl.statement.expressions import code
from analizer_pl.reports.Nodo import Nodo


class FunctionDeclaration(Instruction):
    def __init__(self, proc, id, params, returns, row, column) -> None:
        super().__init__(row, column)
        self.id = id
        self.params = params
        self.returns = returns
        self.proc = proc

    def execute(self, environment):
        if not self.params:
            self.params = []
        environment.globalEnv.addFunction(self.id, self.returns, len(self.params))
        cd = "\n@with_goto\ndef " + self.id + "():\n"
        for p in self.params:
            cd += "\t" + p.execute(environment).temp + " = stack.pop()\n"

        if self.params:
            for p in self.params:
                p.execute(environment)

        # TODO: Codigo 3d
        return code.C3D(cd, self.id, self.row, self.column)

    def dot(self):
        new = Nodo("FUNCTION")
        idNode = Nodo(str(self.id))
        new.addNode(idNode)

        if self.params:
            paramsNode = Nodo("PARAMS")
            new.addNode(paramsNode)
            for p in self.params:
                paramsNode.addNode(p.dot())
        if self.returns:
            returnsNode = Nodo("RETURN")
            new.addNode(returnsNode)
            typ = Nodo(str(self.returns))
            returnsNode.addNode(typ)

        return new