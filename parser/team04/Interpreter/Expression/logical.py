from Interpreter.Expression.expression import Expression


class Logical(Expression):
    def __init__(self, left, right=None):
        self.left = left
        self.right = right

    def getValue(self, env):
        pass

    def isBool(self, value):
        return isinstance(value, bool)

    def getGraph(self, graph, idParent):
        _id = str(id(self))
        _label = self.__class__.__name__
        graph.node(_id, label=_label)
        graph.edge(idParent, _id)

        self.left.getGraph(graph, _id)
        if self.right:
            self.right.getGraph(graph, _id)


class And_class(Logical):
    def __init__(self, left, right):
        Logical.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areBools = self.isBool(leftValue) and self.isBool(rightValue)

        if areBools:
            return leftValue and rightValue


class Or_class(Logical):
    def __init__(self, left, right):
        Logical.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areBools = self.isBool(leftValue) and self.isBool(rightValue)

        if areBools:
            return leftValue or rightValue


class Not_class(Logical):
    def __init__(self, left):
        Logical.__init__(self, left)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        isBool = self.isBool(leftValue)

        if isBool:
            return not(leftValue)
