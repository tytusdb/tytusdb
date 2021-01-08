import optimization.abstract.optimize as opt

class PushStack(opt.OptimizedInstruction):
    """
    PushStack 
    """
    def __init__(self, value, row) -> None:
        super().__init__(row)
        self.value = value

    def optimize(self,generador) -> None:
        pass

    def addToCode(self, generador) -> None:
        generador.addToCode(f'\tstack.push({self.value})')
