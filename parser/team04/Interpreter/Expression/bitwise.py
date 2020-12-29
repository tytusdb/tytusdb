from Interpreter.Expression.expression import Expression


class BitWise(Expression):
    def __init__(self, left, right=None):
        self.left = left
        self.right = right

    def isNumeric(self, value):
        return isinstance(value, int) or isinstance(value, float)

    def getGraph(self, graph, idParent):
        _id = str(id(self))
        _label = self.__class__.__name__
        graph.node(_id, label=_label)
        graph.edge(idParent, _id)

        self.left.getGraph(graph, _id)
        if self.right:
            self.right.getGraph(graph, _id)


class BitwiseAnd(BitWise):
    def __init__(self, left, right):
        BitWise.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue & rightValue


class BitwiseOr(BitWise):
    def __init__(self, left, right):
        BitWise.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue | rightValue


class BitwiseNot(BitWise):
    def __init__(self, left):
        BitWise.__init__(self, left)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        isNum = self.isNumeric(leftValue)

        if isNum:
            return ~ leftValue


class BitwiseXOR(BitWise):
    def __init__(self, left, right):
        BitWise.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue ^ rightValue


class BitwiseRightShift(BitWise):
    def __init__(self, left, right):
        BitWise.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue >> rightValue


class BitwiseLeftShift(BitWise):
    def __init__(self, left, right):
        BitWise.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue << rightValue
