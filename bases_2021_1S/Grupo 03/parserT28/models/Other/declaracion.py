from parserT28.models.instructions.shared import ObjectReference
from parserT28.models.instructions.Expression.expression import Expression, PrimitiveData, DATA_TYPE
from parserT28.models.Other.ambito import Ambito, Variable
from parserT28.controllers.three_address_code import ThreeAddressCode
from parserT28.models.instructions.DML.select import Select
from parserT28.controllers.error_controller import ErrorController


class DeclaracionID(Expression):

    def __init__(self, id, data_type, value, line, column):
        self.id = id
        self.data_type = data_type
        self.line = line
        self.column = column
        self.value = value

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment):
        val = None
        if self.value is not None:
            val = self.value.compile(environment)
        if isinstance(val, PrimitiveData):
            if val.data_type == DATA_TYPE.STRING:
                val.value = f"'{val.value}'"
        pos = ThreeAddressCode().stackCounter
        if val is not None:
            environment.addVar(self.id, self.data_type,
                               val.value, pos, self.line, self.column)
            temp = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temp} = {val.value}")
            ThreeAddressCode().addStack(temp)
        else:
            environment.addVar(self.id, self.data_type, None,
                               pos, self.line, self.column)

        # ThreeAddressCode().addCode(f"print(Stack)")
        # print("ANDO POR AQUI")


class AsignacionID(Expression):

    def __init__(self, id, value, line, column):
        self.id = id
        self.line = line
        self.column = column
        self.value = value

    def __repr__(self):
        return str(vars(self))

    def compile(self, environment: Ambito):
        var_search = environment.getVar(self.id)

        if isinstance(self.value, Select):
            val = self.value.compile(environment)
            ThreeAddressCode().addCode(f"Stack[{var_search.position}] = {val}")
            return
        else:
            val = self.value.compile(environment)

        if var_search == None:
            print("VARIABLE NO DECLARADA ")
            print(self.id)
            ErrorController().add(33, 'Execution',
                                  f"VARIABLE {id} NO DECLARADA", self.line, self.column)
            return

        if isinstance(self.value, ObjectReference):  # Buscar variable
            val = self.value.compile(environment)
            if isinstance(val, PrimitiveData):
                ThreeAddressCode().addCode(
                    f"Stack[{var_search.position}] = {val.alias}")
                return

            val = environment.getVar(val)
            if val is None:
                print("VARIABLE NO DECLARADA")
                ErrorController().add(33, 'Execution',
                                      f"VARIABLE {id} NO DECLARADA", self.line, self.column)
                return

            position = val.position
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = Stack[{position}]")
            ThreeAddressCode().addCode(
                f"Stack[{var_search.position}] = {temporal}")
        else:
            if isinstance(val, str):
                ThreeAddressCode().addCode(
                    f"Stack[{var_search.position}] = {val}")
            else:
                ThreeAddressCode().addCode(
                    f"Stack[{var_search.position}] = {val.value}")
