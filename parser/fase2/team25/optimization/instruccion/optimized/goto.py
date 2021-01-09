import optimization.abstract.optimize as opt

class OptGoto(opt.OptimizedInstruction):
    """
    Goto sin poderse optimizar :(
    """
    def __init__(self, label, row) -> None:
        super().__init__(row)
        self.label = label
    
    def optimize(self,generador) -> None:
        pass

    def addToCode(self, generador) -> None:
        if self.optimizable != opt.RULES.OMISION:
            generador.addToCode(f'\tgoto {self.label}')