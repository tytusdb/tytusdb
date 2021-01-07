from Interpreter.Expression.expression import Expression


class As(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)

        if isinstance(leftValue, list):
            leftValue[0] = [rightValue]
            return leftValue
        else:
            return [[rightValue], [leftValue]]

    def getGraph(self, graph, idParent):
        _id = str(id(self))
        _label = self.__class__.__name__
        graph.node(_id, label=_label)
        graph.edge(idParent, _id)

        self.left.getGraph(graph, _id)
        self.right.getGraph(graph, _id)
