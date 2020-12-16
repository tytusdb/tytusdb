from Interpreter.Expressions.expression import Expression


class Call(Expression):
    def __init__(self, _id, exp):
        self.id = _id
        self.exp = exp

    def getValue(self, env):
        expValue = self.exp.getValue(env)
        return env.functions[self.id](expValue)
