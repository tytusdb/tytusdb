import sys
from execution.symbol.environment import Environment

class Main(object):
    def __init__(self,queryArray):
        self.queryArray = queryArray

    
    def execute(self, environment):
        arreglo = []
        errores = []
        for item in self.queryArray:
            env = Environment(environment)
            res = item.execute(env)
            if isinstance(res,str):
                arreglo.append(res)
            elif isinstance(res,dict) or isinstance(res,list):
                errores.append(str(res))
        return [arreglo,errores]
            



