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

        str_value = str(self.value)
        id_value = str(id(self.value))
        graph.node(id_value, label=str_value)
        graph.edge(_id, id_value)
