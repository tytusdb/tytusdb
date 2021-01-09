import optimization.abstract.optimize as opt

class Invoke(opt.OptimizedInstruction):
    """
    Invoke que no se puede optimizar xd
    """
    def __init__(self, id, params, row) -> None:
        super().__init__(row)
        self.id = id
        self.params = params

    def optimize(self,generador) -> None:
        pass

    def addToCode(self, generador) -> None:
        code = f'{self.id}('
        #Para cada parametro
        for index in range(len(self.params)):
            code += str(self.params[index])
            #Coma si es necesaria
            if index != len(self.params) - 1:
                code += ','
        code += ')'

        if self.id != 'principal':
            code = '\t' + code
        
        generador.addToCode(code)

