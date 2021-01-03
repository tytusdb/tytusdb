from models.instructions.shared import Instruction
from models.Other.ambito import Ambito
from controllers.three_address_code import ThreeAddressCode

class Parametro(Instruction):
    def __init__(self, id, data_type, line, column) :
        self.id = id
        self.data_type = data_type
        self.line = line
        self.column = column

    def compile(self):
        pass
    def process(self):
        pass
    def __repr__(self):
        return str(vars(self))

class Funcion(Instruction):

    def __init__(self, id, params, body, val_return, line, column) :
        self.id = id
        self.params = params
        self.body = body
        self.val_return = val_return
        self.line = line
        self.column = column
    
    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        pass
    
    def compile(self, environment):
        newAmbito = Ambito(environment)
        pos = 0
        for var in self.params:
            pos = ThreeAddressCode().stackCounter
            newAmbito.addVar(var.id, var.data_type, None, pos, var.line, var.column)
        lbl_exit = ThreeAddressCode().newLabel()
        self.body.compile(newAmbito)
        
        ThreeAddressCode().addCode(f"label .{lbl_exit}") #Agregando etiqueta
        ThreeAddressCode().addCode(f"print(\"GraciasDios, SALI\")")

