from Interpreter.Expression.expression import Expression


class Literal(Expression):
    def __init__(self, value):
        self.value = value

    def getValue(self, env):
        return self.value

    def getGraph(self, graph, idParent):
        _id = str(id(self))
        _label = self.__class__.__name__
        graph.node(_id, label=_label)
        graph.edge(idParent, _id)

        graph.node(self.value, label=self.value)
        graph.edge(_id, self.value)
