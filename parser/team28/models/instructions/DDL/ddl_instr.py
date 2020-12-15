from models.instructions.shared import Instruction
'''
    Lenguaje de Definición de Datos (DDL) =======================================================================================================================
'''


class Drop(Instruction):
    '''
        DROP recibe el id y si es tabla(0), o database(1)
    '''

    def __init__(self, id, dtype):
        self.id = id
        self.dtype = dtype
