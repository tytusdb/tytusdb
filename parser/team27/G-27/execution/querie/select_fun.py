from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from execution.symbol.typ import *
from storageManager import jsonMode as admin
from TypeChecker.checker import check

from libraries.datetime_functions import current_date

class Select_Func(Querie):

    def __init__(self,funcion,row, column):
        Querie.__init__(self, row, column)
        self.funcion = funcion

    def execute(self, environment):

        result = self.funcion.execute(environment)
        print(result)

        if isinstance(result,dict):
            if 'Error' in result:
                return result
            else:
                if 'value' in result:
                    if isinstance(result['value'],str):
                        return result['value']
                    else:
                        return str(result['value'])

        return{'Error':'Error desconocido en el select function.','row':self.row,'column':self.column}