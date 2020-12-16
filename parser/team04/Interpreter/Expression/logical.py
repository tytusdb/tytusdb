from Interpreter.Expressions.expression import Expression


class Logical(Expression):
    def __init__(self, value):
        self.value = value   

    def getValue(self, env):
        pass

    def isNumeric(self, value):
        return isinstance(value, int) or isinstance(value, float)



class And_class(Logical):
    def __init__(self, left, right):
        Logical.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue and rightValue

class Or_class(Logical):
    def __init__(self, left, right):
        Logical.__init__(self, left, right)

    def getValue(self, env):
        leftValue = self.left.getValue(env)
        rightValue = self.right.getValue(env)
        areNums = self.isNumeric(leftValue) and self.isNumeric(rightValue)

        if areNums:
            return leftValue or rightValue

class Not_class(Logical):
    def __init__(self, right):
        Logical.__init__(self, right)

    def getValue(self, env):
        rightValue = self.right.getValue(env)
        areNum = self.isNumeric(rightValue) 

        if areNum:
            return not(rightValue)
