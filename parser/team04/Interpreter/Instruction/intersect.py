from Interpreter.Instruction.instruction import Instruction


class intersect_all(Instruction):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def execute(self, env):
        print("Se ejecutó la instrucción 'INTERSECT ALL'")


class intersect(Instruction):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def execute(self, env):
        print("Se ejecutó la instrucción 'INTERSECT'")
