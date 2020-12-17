import sys

sys.path.insert(0, '..')
from ast_node import ASTNode


class CreateEnum(ASTNode):
    def __init__(self, name, value_list, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name             # type name
        self.value_list = value_list  # list of possible values

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class CreateDatabase(ASTNode):
    def __init__(self, name, owner, mode, replace, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name        # database name
        self.owner = owner      # optional owner
        self.mode = mode        # mode integer
        self.replace = replace  # boolean type

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class CreateTable(ASTNode):  # TODO: Check grammar, complex instructions are not added yet
    def __init__(self, name, inherits_from, fields, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name                    # table name
        self.inherits_from = inherits_from  # optional inheritance
        self.fields = fields                # list of fields

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class TableField(ASTNode):
    def __init__(self, name, field_type, allows_null, is_pk, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name                # field name
        self.field_type = field_type    # type of field
        self.allows_null = allows_null  # if true then NULL or default, if false the means is NOT NULL
        self.is_pk = is_pk              # field is primary key

    def execute(self, table, tree):
        super().execute(table, tree)
        return True