from Interpreter.node import Node


class Expression(Node):
    def getValue(self, env):
        pass

    def getGraph(self, graph, idParent):
        _id = str(id(self))
        _label = self.__class__.__name__
        graph.node(_id, label=_label)
        graph.edge(idParent, _id)
