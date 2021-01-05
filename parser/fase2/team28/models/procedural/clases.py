from models.instructions.shared import Instruction

class BodyDeclaration(Instruction):
    def __init__(self,  declare, begin) :
        self.declare = declare
        self.begin = begin

    def __repr__(self):
        return str(vars(self))

    def compile(self, enviroment):

        if self.declare is not None:
            for declaration in self.declare:
                print(declaration)
                declaration.compile(enviroment)

        if self.begin is not None:
            for instr in self.begin:
                print(instr)
                instr.compile(enviroment)
    
    def process(self):
        pass

class Call(Instruction):
    def __init__(self, id_func, params) :
        self.id_func = id_func
        self.params = params

    def __repr__(self):
        return str(vars(self))

    def compile(self, enviroment):
        pass
    
    def process(self):
        pass