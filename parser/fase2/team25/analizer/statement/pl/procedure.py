import sys

sys.path.append("../../..")
from analizer.abstract import instruction
from analizer.reports import Nodo
from analizer.symbol.environment import Environment

envProcedure = Environment(for3d=True)

class Procedure(instruction.Instruction):
    def __init__(self, name, params, block, row, column) -> None:
        self.params = params
        self.block = block
        self.name = name
        super().__init__(row, column)

    def generate3d(self, environment, instanciaAux):
        header = f'\n@with_goto\ndef p{self.name}('
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

    def compareParamsTypes(self) -> list:
        types = []

        for param in self.params:
            types.append(param.type)

        return types

    def execute(self, environment):
        if not envProcedure in instruction.envVariables:
            envProcedure.functions.clear()
            instruction.envVariables.append(envProcedure)
        
        #TODO Agregar errores semanticos
        if not envProcedure.addProc(self.name, self):
            pass

    def dot(self):
        new = Nodo.Nodo('CREATE PROCEDURE')
        params = Nodo.Nodo('PARAMS')
        for param in self.params:
            nParam = Nodo.Nodo(param[0])
            nParam.addNode(Nodo.Nodo(param[1]))
            params.addNode(nParam)

        new.addNode(params)

        block = self.block.dot()
        new.addNode(block)

        return new

    
    