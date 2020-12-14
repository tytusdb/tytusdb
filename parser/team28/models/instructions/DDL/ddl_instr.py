from models.instructions.shared import Instruction
'''
    Lenguaje de Definición de Datos (DDL) =======================================================================================================================
'''
class CreateDB(Instruction):
    '''
        CREATE DATABASE recibe el id de la base
    '''
    def __init__(self, id) :
        self.id = id

class CreateTable(Instruction):
    '''
        CREATE TABLE recibe el nombre de la tabla y un array con sus columnas
    '''
    def __init__(self, table, arr_columns) :
        self.table = table
        self.arr_columns = arr_columns

class Drop(Instruction):
    '''
        DROP recibe el id y si es tabla(0), o database(1)
    '''
    def __init__(self, id, dtype) :
        self.id = id
        self.dtype = dtype
