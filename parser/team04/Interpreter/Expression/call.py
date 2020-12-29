from Interpreter.Expression.expression import Expression


class Call(Expression):
    def __init__(self, _id, expList=[]):
        self.id = _id
        self.expList = expList

    def getValue(self, env):
        values = []
        for exp in self.expList:
            values.append(exp.getValue(env))
        if self.id in env.functions:
            if(self.id == "pi"):
                return env.functions[self.id]
            else:
                print(env.functions[self.id](*values))
                return env.functions[self.id](*values)
        return ""
