from Interpreter.Instruction.instruction import Instruction


class union_all(Instruction):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def execute(self, env):
        print("Se ejecutó la instrucción 'UNION ALL'")


class union(Instruction):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def execute(self, env):
        print("Se ejecutó la instrucción 'UNION'")
