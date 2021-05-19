from parserT28.models.instructions.shared import Instruction
from parserT28.controllers.three_address_code import ThreeAddressCode


class If(Instruction):
    def __init__(self, condition, instructions, else_if, _else):
        self.condition = condition
        self.instructions = instructions
        self.else_if = else_if
        self._else = _else

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):

        lbl_true = ThreeAddressCode().newLabel()
        lbl_false = ThreeAddressCode().newLabel()

        condition = None
        if type(self.condition) is not list:
            condition = self.condition.compile(environment)
        else:
            condition = self.condition[0].compile(environment)

        ThreeAddressCode().addCode(f"if({condition.value}): goto .{lbl_true}")
        ThreeAddressCode().addCode(f"goto .{lbl_false}")

        ThreeAddressCode().addCode(
            f"label .{lbl_true}    # {condition.value} ---- True")
        for instr in self.instructions:
            instr.compile(environment)

        if self._else is not None:

            lbl_exit = ThreeAddressCode().newLabel()
            ThreeAddressCode().addCode(f"goto .{lbl_exit}")
            ThreeAddressCode().addCode(
                f"label .{lbl_false}    # {condition.value} ---- False")

            if isinstance(self._else, If):
                self._else.compile(environment)
            else:
                for instr in self._else:
                    instr.compile(environment)

            ThreeAddressCode().addCode(
                f"label .{lbl_exit}    # {condition.value} ---- Salida")

        else:

            ThreeAddressCode().addCode(
                f"label .{lbl_false}    # {condition.value} ---- False")

    def process(self):
        pass


def anidarIFs(counter, arr_ifs, _else):
    newIF = None
    if arr_ifs is not None and counter < len(arr_ifs)-1:
        newIF = If(arr_ifs[counter].condition, arr_ifs[counter].instructions,
                   None, anidarIFs(counter+1, arr_ifs, _else))
    else:
        newIF = If(arr_ifs[counter].condition,
                   arr_ifs[counter].instructions, None, _else)
    return newIF
