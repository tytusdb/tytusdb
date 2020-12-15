import math

from Interpreter.environment import Environment


class Ast:
    def __init__(self, root):
        self.root = root

    def execute(self):
        print("Ejecutando el AST...")
        e = Environment(functions=self.getNativeFuncs())

        for inst in self.root:
            inst.execute(e)

        '''
        try:
            for inst in self.root:
                inst.execute(e)
            print("AST ejecutado exitosamente!")
        except:
            print("Error al ejecutar el AST!")
        '''

    def getGraph(self):
        print("Generando el grafo")

    def getNativeFuncs(self):
        functions = {
            'SQRT': lambda z: math.sqrt(z)
        }
        return functions
