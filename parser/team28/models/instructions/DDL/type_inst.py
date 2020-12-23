from models.instructions.shared import Instruction
from models.type import *
from controllers.symbol_table import * 


class CreateType(Instruction):
    '''
        CREATE TYPE recibe un array con todas los parametros
    '''
    def __init__(self,  name, values) :
        self._name = name
        self._values = values

    def __repr__(self):
        return str(vars(self))
    
    def process(self,instrucction):
        typeNew = Type(self._name.alias)
        for valor in self._values:
            typeNew._values.append(valor.alias)

        SymbolTable().add(typeNew._name,str(typeNew._values),'TYPE','DB',None,'0','0')
        print(typeNew)