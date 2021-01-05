from execution.abstract.querie import * 
from execution.symbol.environment import *
from execution.symbol.table import *
from execution.symbol.column import *
from execution.symbol.typ import *
from storageManager import jsonMode as admin
from TypeChecker.checker import check

class Case(Querie):

    def __init__(self,caseArr , row, column):
        Querie.__init__(self, row, column)
        self.caseArr = caseArr

    def execute(self, environment):
        #case array me devuelve un diccionario -> {'when':exp|'else', 'then':exp}
        # solamente retorna un diccionario con los datos
        result = []
        for item in self.caseArr:
            exp1 = item['when']
            exp2 = item['then']
            if not isinstance(item['exp1'],str):
                exp1 = exp1.execute(environment)
            if not isinstance(item['exp2'],str):
                exp2 = exp2.execute(environment)
            
            if not isinstance(exp1,str):
                if exp1['typ'] != Type.BOOLEAN:
                    return {'Error': 'La condicion del case no retorna un tipo booleano', 'Linea':self.row, 'Columna': self.column}
                if exp1['value'] == True:
                    return{'value':exp2['value'],'typ':exp2['typ']}
            else:
                if exp1 == 'else':
                    return{'value':exp2['value'],'typ':exp2['typ']}

        return{'value':'null','typ':Type.NULL}

            
            
            
            
