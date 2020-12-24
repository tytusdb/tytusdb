import sys
from execution.symbol.environment import Environment
from prettytable import PrettyTable

class Main(object):
    def __init__(self,queryArray):
        self.queryArray = queryArray

    
    def execute(self, environment):
        arreglo = []
        errores = []
        if isinstance(self.queryArray,list):
            for item in self.queryArray:
                env = Environment(environment)
                res = item.execute(env)
                if isinstance(res,str):
                    arreglo.append(res)
                elif isinstance(res,dict):
                    if 'Error' in res:
                        errores.append(str(res))
                    else:
                        x = PrettyTable()
                        encabezados = []
                        for value in res['table'].columns:
                            encabezados.append(value.name)
                        x.field_names = encabezados
                        for tupla in res['data']:
                            x.add_row(tupla)
                        arreglo.append(x.get_string())
                elif isinstance(res,list):
                    arreglo.append(str(res))
            return [arreglo,errores]
        else:
            return []
            



