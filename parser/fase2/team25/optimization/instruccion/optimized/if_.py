import optimization.abstract.optimize as opt

class OptIf(opt.OptimizedInstruction):
    """
    If optimizado
    """
    def __init__(self, type_, condition, goto, row) -> None:
        super().__init__(row)
        self.type = type_
        self.condition = condition
        self.goto = goto
        
    def optimize(self,generador):
        if self.type == opt.TEVAL.SINGLE:
            pass
        elif self.type == opt.TEVAL.OPERATION:
            pass

    def addToCode(self, generador):
        super().addToCode(generador)
        if self.type == opt.TEVAL.SINGLE:
            generador.addToCode(f'\tif {self.condition}: goto {self.goto.label}')
        else:
            generador.addToCode(f'\tif {self.condition[0]} {self.condition[1]} {self.condition[2]}: goto {self.goto.label}')
        
