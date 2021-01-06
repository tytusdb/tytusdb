import sys

sys.path.append("../../..")
from analizer.abstract import instruction
from analizer.reports import Nodo
from analizer.symbol.environment import Environment

envFunction = Environment(for3d=True)

class Function(instruction.Instruction):
    def __init__(self, name, type_, params, block, row, column) -> None:
        self.params = params
        self.block = block
        self.name = name
        self.type = type_
        super().__init__(row, column)

    def generate3d(self, environment, instanciaAux):
        header = f'\n@with_goto\ndef f{self.name}('
        for param in range(len(self.params)):
            header += self.params[param][0]
            if param != len(self.params) -1:
                header += ","
        header += '):'

        eFinal = instanciaAux.getNewLabel()
        newEnv = Environment(environment)
        newEnv.addVar('eFinal',eFinal, 'Etiqueta', self.row, self.column)

        instanciaAux.addToCode(header)

        self.block.generate3d(newEnv, instanciaAux)
        instanciaAux.addToCode(f'\tlabel .{eFinal}')

    def execute(self, environment):
        if not envFunction in instruction.envVariables:
            envFunction.functions.clear()
            instruction.envVariables.append(envFunction)
        
        #TODO Agregar errores semanticos
        if not envFunction.addFunc(self.name, self):
            pass

    def compareParamsTypes(self) -> list:
        types = []

        for param in self.params:
            types.append(param.type)

        return types

        
    def dot(self):
        new = Nodo.Nodo('CREATE FUNCTION')
        returns = Nodo.Nodo('RETURNS')
        returns.addNode(Nodo.Nodo(f'{self.type}'))

        params = Nodo.Nodo('PARAMS')
        for param in self.params:
            nParam = param.dot()
            params.addNode(nParam)
        new.addNode(params)

        block = self.block.dot()
        new.addNode(block)

        return new

    
    