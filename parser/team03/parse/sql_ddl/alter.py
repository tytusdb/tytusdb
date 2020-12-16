from parse.ast_node import ASTNode
from jsonMode import alterDatabase, alterAddColumn, alterDropColumn


class AlterDatabaseRename(ASTNode):
    def __init__(self, name, new_name, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name  # db current name
        self.new_name = new_name  # db new name

    def execute(self, table, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)
        result_new_name = self.new_name.execute(table, tree)
        result = alterDatabase(result_name, result_new_name)
        if result == 1:
            # log error on operation
            return False
        elif result == 2:
            # log error, old database name does not exists
            return False
        elif result == 3:
            # log error, new database name already exists
            return False
        else:
            return True


class AlterDatabaseOwner(ASTNode):
    def __init__(self, name, owner, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name  # db name
        self.owner = owner  # db new owner

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class AlterTableAddColumn(ASTNode):
    def __init__(self, table_name, field_name, field_type, field_length, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name
        self.field_type = field_type
        self.field_length = field_length

    def execute(self, table, tree):
        super().execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        result_field_name = self.field_name.execute(table, tree)
        result_field_type = self.field_type.execute(table, tree)
        result_field_length = self.field_length.execute(table, tree)
        result = alterAddColumn('db_name_from_st', result_field_name, None)
        if result == 1:
            # log error on operation
            return False
        elif result == 2:
            # log error, old database name does not exists
            return False
        elif result == 3:
            # log error, table does not exists
            return False
        else:
            return True


class AlterTableAddCheck(ASTNode):
    def __init__(self, table_name, validation, line, column):  # what is validation? boolean or any kind of expression?
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.validation = validation

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class AlterTableDropColumn(ASTNode):
    def __init__(self, table_name, field_name, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name

    def execute(self, table, tree):
        super().execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        result_field_name = self.field_name.execute(table, tree)
        result = alterDropColumn('db_name_from_st', result_field_name, 'column_number_from_st')
        if result == 1:
            # log error on operation
            return False
        elif result == 2:
            # log error, old database name does not exists
            return False
        elif result == 3:
            # log error, table does not exists
            return False
        elif result == 4:
            # log error, PK cannot be deleted or table to be empty
            return False
        elif result == 4:
            # log error, column out of index
            return False
        else:
            return True


class AlterTableAddConstraint(ASTNode):
    def __init__(self, table_name, cons_name, field_name, line, column):  # Unique is the only allowed
        ASTNode.__init__(self, line, column)
        self.cons_name = cons_name
        self.table_name = table_name
        self.field_name = field_name

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class AlterTableAddFK(ASTNode):
    def __init__(self, table_name, table_column, table_reference, column_reference, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name  # name of table to alter
        self.table_column = table_column  # name of column to add FK
        self.table_reference = table_reference  # name of table to reference
        self.column_reference = column_reference  # name of column referenced on table to reference

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class AlterTableNotNull(ASTNode):
    def __init__(self, table_name, field_name, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class AlterTableDropConstraint(ASTNode):
    def __init__(self, table_name, cons_name, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name  # table name
        self.cons_name = cons_name  # constraint name

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class AlterTableRenameColumn(ASTNode):
    def __init__(self, table_name, old_name, new_name, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.old_name = old_name
        self.new_name = new_name

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class AlterTableChangeColumnType(ASTNode):
    def __init__(self, table_name, field_name, field_type, field_length, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name
        self.field_type = field_type
        self.field_length = field_length

    def execute(self, table, tree):
        super().execute(table, tree)
        return True
