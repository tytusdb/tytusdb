from analizer.abstract import instruction


class IfSimple(instruction.Instruction):
    def __init__(self, if_exp , if_inst, row , column, else_exp=None , else_inst = None):
        instruction.Instruction.__init__(self, row , column)
        self.if_exp = if_exp
        self.else_exp = else_exp
        self.if_inst = if_inst
        self.else_inst = else_inst

    def execute(self, environment):
        pass

    def generate3d(self, environment, instanciaAux):
        pass
