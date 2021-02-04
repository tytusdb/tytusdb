import optimization.abstract.optimize as opt

class OptLabel(opt.OptimizedInstruction):
    """
    Label optmizado
    """
    
    def __init__(self, label, row) -> None:
        super().__init__(row)
        self.label = label

    def optimize(self,generador) -> None:
        pass

    def addToCode(self, generador) -> None:
        super().addToCode(generador)
        if self.optimizable != opt.RULES.OMISION:
            generador.addToCode(f'\tlabel {self.label}')