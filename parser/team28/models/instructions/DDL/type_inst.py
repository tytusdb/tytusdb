from models.instructions.shared import Instruction

class CreateType(Instruction):
    '''
        CREATE TYPE recibe un array con todas los parametros
    '''
    def __init__(self,  name, values) :
        self.name = name
        self.values = values

    def __repr__(self):
        return str(vars(self))
    
    def execute(self):
        pass