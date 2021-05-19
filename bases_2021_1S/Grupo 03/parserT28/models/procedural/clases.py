from parserT28.models.instructions.shared import Instruction
from parserT28.controllers.three_address_code import ThreeAddressCode


class BodyDeclaration(Instruction):
    def __init__(self,  declare, begin):
        self.declare = declare
        self.begin = begin

    def __repr__(self):
        return str(vars(self))

    def compile(self, enviroment):

        if self.declare is not None:
            for declaration in self.declare:
                # print(declaration)
                declaration.compile(enviroment)

        if self.begin is not None:
            if type(self.begin) is list:
                for instr in self.begin:
                    print(instr)
                    instr.compile(enviroment)
            else:
                self.begin.compile(enviroment)

    def process(self):
        pass


class Call(Instruction):
    def __init__(self, id_func, params):
        self.id_func = id_func
        self.params = params

    def __repr__(self):
        return str(vars(self))

    def compile(self, enviroment):
        pass

    def process(self):
        pass


class ReturnFuncProce(Instruction):
    def __init__(self, val_return):
        self.val_return = val_return

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        if self.val_return is not None:
            value = self.val_return.compile(environment)
            pos = ThreeAddressCode().stackCounter
            # Metiendo el valor a retornar al Stack
            ThreeAddressCode().addStack(value.value)
            ThreeAddressCode().addCode(f"P = {pos}")

        # Poniendo salto incondicional
        lbl_return = environment.getReturn()
        ThreeAddressCode().addCode(f"goto .{lbl_return}")

    def process(self):
        pass
