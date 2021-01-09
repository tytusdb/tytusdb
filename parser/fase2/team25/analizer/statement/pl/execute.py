import sys
from datetime import datetime

from analizer.abstract import instruction
from analizer.reports import Nodo
from analizer.symbol.environment import Environment
from analizer.statement.pl.procedure import envProcedure

class Execute(instruction.Instruction):
    def __init__(self, name, params, row, column) -> None:
        super().__init__(row, column)
        self.name = name
        self.params = params

    def execute(self, environment):
        pass

    def generate3d(self, environment, instanciaAux, main = False):
        try:
            proc = envProcedure.getProc(self.name)
            if proc:
                if len(proc.params) != len(self.params):
                    instruction.semanticErrors.append(
                        (f"ERROR: La cantidad de parametros ingresados en el procedimiento '{self.name}' no son los indicados",self.row)
                    )
                tipos = []
                for param in self.params:
                    tipos.append(param.execute(environment).type)

                if proc.compareParamsPrimitive() != tipos:
                    instruction.semanticErrors.append(
                        (f"ERROR: Los parametros ingresados en el procedimiento '{self.name}' no concuerdan con su tipo",self.row)
                    )

                llamado = f'\tp{self.name}('
                for param in self.params:
                    llamado += param.generate3d(environment, instanciaAux)
                llamado += ')'

                if main:
                    instanciaAux.addToMain(llamado)
                else:
                    instanciaAux.addToCode(llamado)
            else:
                instruction.semanticErrors.append(
                    (f"ERROR: El procedimiento '{self.name}' no existe",self.row)
                ) 
        except:
            instruction.semanticErrors.append(
                (f"ERROR: Error inesperado para procesamiento del procedimiento '{self.name}'",self.row)
            )

    def dot(self):
        nodo = Nodo.Nodo('Execute')
        return nodo