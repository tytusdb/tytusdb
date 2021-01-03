from models.instructions.shared import ObjectReference
from models.instructions.Expression.expression import Expression
from models.Other.ambito import Ambito, Variable
from controllers.three_address_code import ThreeAddressCode

class DeclaracionID(Expression):
    
    def __init__(self, id, data_type, value, line, column) :
        self.id = id
        self.data_type = data_type
        self.line = line
        self.column = column
        self.value = value

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        val = self.value[0].compile()
        pos = ThreeAddressCode().stackCounter
        environment.addVar(self.id, self.data_type, val, pos, self.line, self.column)
        temp = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp} = {val.value}")
        ThreeAddressCode().addStack(temp)
        # ThreeAddressCode().addCode(f"print(Stack)")
        print("ANDO POR AQUI")

class AsignacionID(Expression):
    
    def __init__(self, id, value, line, column) :
        self.id = id
        self.line = line
        self.column = column
        self.value = value

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment: Ambito):
        var_search = environment.getVar(self.id)
        if var_search == None:
            print("VARIABLE NO DECLARADA " + self.id)
            return

        if isinstance(self.value, ObjectReference): #Buscar variable
            val = self.value.compile(environment)
            val = environment.getVar(val)
            if val is None: 
                print("VARIABLE NO DECLARADA")
                return

            position = val.position
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = Stack[{position}]")
            ThreeAddressCode().addCode(f"Stack[{var_search.position}] = {temporal}  #ASIGNACION")

        else:
            val = self.value.compile()
            ThreeAddressCode().addCode(f"Stack[{var_search.position}] = {val.value}  #ASIGNACION")



