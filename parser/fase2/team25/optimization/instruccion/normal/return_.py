import optimization.abstract.optimize as opt


class Return(opt.OptimizedInstruction):
    """
    Return que no se puede optimizar
    """
    def __init__(self, value, row) -> None:
        super().__init__(row)
        self.value = value

    def optimize(self,generador) -> None:
        pass

    def addToCode(self, generador) -> None:
        code = f'\tRETURN[0] = {self.value}'
        generador.addToCode(code)
