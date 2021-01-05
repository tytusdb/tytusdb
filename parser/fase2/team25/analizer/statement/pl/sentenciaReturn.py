from analizer.abstract import instruction


class Return_(instruction.Instruction):
    def __init__(self, exp , row , column):
        instruction.Instruction.__init__(self, row , column)
        self.exp = exp

    def execute(self, environment):
        pass

    def generate3d(self, environment, instanciaAux):
        exp = self.exp.generate3d(0,instanciaAux)
        instanciaAux.addToCode(f'{instanciaAux.getTabulaciones()}return {exp}')

