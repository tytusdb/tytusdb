from analizer.abstract import instruction
from analizer.reports.Nodo import Nodo

class Return_(instruction.Instruction):
    def __init__(self, exp , row , column):
        instruction.Instruction.__init__(self, row , column)
        self.exp = exp

    def execute(self, environment):
        pass

    def generate3d(self, environment, instanciaAux):
        if self.exp:
            exp = self.exp.generate3d(environment,instanciaAux)
            instanciaAux.addToCode(f'{instanciaAux.getTabulaciones()}RETURN[0] = {exp}')
        eFinal = environment.getVar('eFinal').value
        instanciaAux.addToCode(f'\tgoto .{eFinal}')

    def dot(self):
        return_texto = "RETURN"
        return_nodo = Nodo(return_texto)
        expresion_texto = "EXPRESION"
        expresion_nodo = Nodo(expresion_texto)
        expresion_nodo.addNode(self.exp.dot())
        return_nodo.addNode(expresion_nodo)
        return return_nodo
