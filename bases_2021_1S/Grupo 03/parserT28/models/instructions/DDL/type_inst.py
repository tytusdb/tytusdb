from parserT28.models.instructions.shared import Instruction
from parserT28.models.type import Type
from parserT28.controllers.symbol_table import SymbolTable
from parserT28.controllers.three_address_code import ThreeAddressCode


class CreateType(Instruction):
    '''
        CREATE TYPE recibe un array con todas los parametros
    '''

    def __init__(self,  name, values, tac):
        self._name = name
        self._values = values
        self._tac = tac

    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        typeNew = Type(self._name.alias)
        for valor in self._values:
            typeNew._values.append(valor.alias)

        SymbolTable().add(typeNew._name, str(typeNew._values), 'TYPE', 'DB', None, '0', '0')
        print(typeNew)
        # CREANDO C3D
        temp = ThreeAddressCode().newTemp()
        database_id = SymbolTable().useDatabase
        if database_id is not None:
            ThreeAddressCode().addCode(
                f"{temp} = \"USE {database_id}; {self._tac}\"")
        else:
            ThreeAddressCode().addCode(f"{temp} = \"{self._tac}\"")
        # LLAMANDO A FUNCION PARA ANALIZAR ESTA COCHINADA
        temp1 = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp1} = parse({temp})")

    def compile(self, instrucction):
        temp = ThreeAddressCode().newTemp()
        database_id = SymbolTable().useDatabase
        if database_id is not None:
            ThreeAddressCode().addCode(
                f"{temp} = \"USE {database_id}; {self._tac}\"")
        else:
            ThreeAddressCode().addCode(f"{temp} = \"{self._tac}\"")

    def optimizate(self, instrucction):
        temp = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp} = '{self._tac};'")
