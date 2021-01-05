from models.instructions.shared import Instruction
from models.type import Type
from controllers.symbol_table import SymbolTable
from controllers.three_address_code import ThreeAddressCode


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

    def compile(self, instrucction):
        temp = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp} = '{self._tac};'")

    def optimizate(self, instrucction):
        temp = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temp} = '{self._tac};'")
