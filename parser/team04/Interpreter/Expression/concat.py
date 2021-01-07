from Interpreter.Expression.expression import Expression


class Concat(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)

        return str(leftValue) + str(rightValue)
