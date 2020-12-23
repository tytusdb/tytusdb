from jsonMode import createDatabase, createTable, dropDatabase
from parse.ast_node import ASTNode


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
        result_name = self.name.execute(table, tree)
        result_owner = self.owner.execute(table, tree) if self.owner else None  # Owner seems to be stored only to ST
        result_mode = self.owner.mode(table, tree) if self.mode else 6  # Change to 1 when default mode from EDD available
        if self.replace:
            dropDatabase(result_name)
        result = 0
        if result_mode == 6:  # add more ifs when modes from EDD available
            result = createDatabase(result_name)

        if result == 1:
            # log error on operation
            return False
        elif result == 2:
            # log error because db already exists
            return False
        else:
            return True


class CreateTable(ASTNode):  # TODO: Check grammar, complex instructions are not added yet
    def __init__(self, name, inherits_from, fields, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name                    # table name
        self.inherits_from = inherits_from  # optional inheritance
        self.fields = fields                # list of fields

    def execute(self, table, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)
        result_inherits_from = self.inherits_from.execute(table, tree) if self.inherits_from else None
        result_fields = []
        if result_inherits_from:
            # get inheritance table, if doesn't exists throws semantic error, else append result
            result_fields.append([])
        result = createTable('db_from_st', result_name, len(result_fields))
        if result == 1:
            # log error on operation
            return False
        elif result == 2:
            # log error because db does not exists
            return False
        elif result == 3:
            # log error because table already exists
            return False
        else:
            return True
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
