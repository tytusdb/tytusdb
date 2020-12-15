from models.instructions.shared import Instruction


class CreateCol(Instruction):

    def __init__(self, column_name, type_column, properties):
        self._column_name = column_name
        self._type_column = type_column
        self._properties = properties

    def execute(self):
        pass


class Unique(Instruction):

    def __init__(self, column_list):
        self._column_list = column_list

    def execute(self):
        pass


class Check(Instruction):

    def __init__(self, column_condition):
        self._column_condition = column_condition

    def execute(self):
        pass


class PrimaryKey(Instruction):

    def __init__(self, column_list):
        self._column_list = column_list

    def execute(self):
        pass


class ForeignKey(Instruction):

    def __init__(self, column_list, table_name, table_column_list):
        self._column_list = column_list
        self._table_name = table_name
        self._table_column_list = table_column_list

    def execute(self):
        pass


class Constraint(Instruction):

    def __init__(self, column_name, column_condition):
        self._column_name = column_name
        self._column_condition = column_condition

    def execute(self):
        pass
