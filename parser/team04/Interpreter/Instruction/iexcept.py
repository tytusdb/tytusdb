from Interpreter.Instruction.instruction import Instruction


class iexcept_all(Instruction):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def execute(self, env):
        print("Se ejecutó la instrucción 'EXCEPT ALL'")


class iexcept(Instruction):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def execute(self, env):
        print("Se ejecutó la instrucción 'EXCEPT'")
