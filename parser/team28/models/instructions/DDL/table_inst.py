from models.instructions.shared import Instruction


class CreateTB(Instruction):

    def __init__(self, table_name, column_list):
        self._table_name = table_name
        self._column_list = column_list

    def execute(self):
        pass


class DropTB(Instruction):

    def __init__(self, table_name):
        self._table_name = table_name

    def execute(self):
        pass
