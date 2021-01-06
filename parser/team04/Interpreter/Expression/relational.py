from Interpreter.Expression.expression import Expression


class Relational(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getValue(self, env):
        pass

    def isNumeric(self, value):
        return isinstance(value, int) or isinstance(value, float)


class MayorQue(Relational):
    def __init__(self, left, right):
        Relational.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue > rightValue


class MenorQue(Relational):
    def __init__(self, left, right):
        Relational.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue < rightValue


class MayorIgual(Relational):
    def __init__(self, left, right):
        Relational.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue >= rightValue


class MenorIgual(Relational):
    def __init__(self, left, right):
        Relational.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue <= rightValue


class IgualQue(Relational):
    def __init__(self, left, right):
        Relational.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue == rightValue


class Distinto(Relational):
    def __init__(self, left, right):
        Relational.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue != rightValue
