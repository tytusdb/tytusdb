from models.instructions.shared import Instruction
from models.Other.ambito import Ambito
from controllers.three_address_code import ThreeAddressCode
from controllers.procedures import Procedures


class Parametro(Instruction):
    def __init__(self, id, data_type, line, column):
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

    def __init__(self, id, params, body, val_return, isNew, line, column):
        self.id = id
        self.params = params
        self.body = body
        self.val_return = val_return
        self.isNew = isNew
        self.environment = None
        self.line = line
        self.column = column

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        pass

    def compile(self, environment):
        if self.isNew:
            self.environment = environment  # TODO verificar
            if Procedures().saveProcedure(self.id, self, self.line, self.column):
                self.print(environment)
            self.isNew = False
        else:
            name = self.id.compile(environment)
            Procedures().getProcedure(name)

    def print(self, environment):
        ThreeAddressCode().newFunction()

        newAmbito = None
        if self.isNew:
            newAmbito = environment
        else:
            newAmbito = Ambito(environment)

        pos = 0
        for var in self.params:
            pos = ThreeAddressCode().stackCounter
            newAmbito.addVar(var.id, var.data_type, None,
                             pos, var.line, var.column)
            temp = ThreeAddressCode().newTemp()
            # TODO: MANEJAR PARAMETROS
            ThreeAddressCode().addCode(f"{temp} = None")
            ThreeAddressCode().addStack(temp)
        pos = ThreeAddressCode().stackCounter
        lbl_exit = ThreeAddressCode().newLabel()
        self.body.compile(newAmbito)

        ThreeAddressCode().addCode(f"label .{lbl_exit}")  # Agregando etiqueta
        # Imprime primera variable declarada, NO parametro
        ThreeAddressCode().addCode(f"print(Stack[{pos}])")

        ThreeAddressCode().createFunction(self.id, self.params)
