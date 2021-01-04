from models.instructions.shared import Instruction
from controllers.three_address_code import ThreeAddressCode
class If(Instruction):
    def __init__(self, condition, instructions, else_if, _else) :
        self.condition = condition
        self.instructions = instructions
        self.else_if = else_if
        self._else = _else

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        lbl_true = ThreeAddressCode().newLabel()
        lbl_false = ThreeAddressCode().newLabel()
        lbl_exit = ThreeAddressCode().newLabel()

        condition = self.condition.compile(environment)
        ThreeAddressCode().addCode(f"if({condition.value}): goto .{lbl_true}")
        ThreeAddressCode().addCode(f"goto .{lbl_false}")

        ThreeAddressCode().addCode(f"label .{lbl_true}")
        ThreeAddressCode().addCode(f"print(\"ETIQUETA VERDADERA\")")
        for instr in self.instructions:
            instr.compile(environment)

        ThreeAddressCode().addCode(f"goto .{lbl_exit}")
        ThreeAddressCode().addCode(f"label .{lbl_false}")
        ThreeAddressCode().addCode(f"print(\"ETIQUETA FALSA\")")    

        if self.else_if is not None:
            for else_if in self.else_if:
                else_if.compile(environment)
            ThreeAddressCode().addCode(f"goto .{lbl_exit}")

        if self._else is not None:
            for instr in self._else:
                instr.compile(environment)

        ThreeAddressCode().addCode(f"label .{lbl_exit}")
        ThreeAddressCode().addCode(f"print(\"ETIQUETA SALIDA\")")
       


    def process(self):
        pass