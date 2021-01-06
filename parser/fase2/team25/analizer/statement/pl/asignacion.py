from analizer.abstract import instruction


class Asignacion(instruction.Instruction):
    def __init__(self, identificador, expresion, row , column):
        instruction.Instruction.__init__(self, row , column)
        self.identificador = identificador
        self.expresion = expresion
        
    def generate3d(self, environment, instanciaAux):
        exp = self.expresion.generate3d(environment ,instanciaAux) # t1 = 3 + 4 
        id = self.identificador
        tn = None
        instanciaAux.addToCode(f'\t{id} = {exp}')
        return tn