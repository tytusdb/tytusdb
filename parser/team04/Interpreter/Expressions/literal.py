from Interpreter.Expressions.expression import Expression


class Literal(Expression):
    def __init__(self, value):
        self.value = value

    def getValue(self, env):
        return self.value
