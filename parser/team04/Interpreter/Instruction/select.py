from Interpreter.Instructions.instruction import Instruction


class Select(Instruction):
    def __init__(self, expression):
        self.expression = expression

    def execute(self, env):
        print("Se ejecutó la instrucción 'SELECT'")
        print(self.expression.getValue(env))
