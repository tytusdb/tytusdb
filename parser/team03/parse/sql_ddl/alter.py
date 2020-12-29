from parse.ast_node import ASTNode
from jsonMode import alterDatabase, alterAddColumn, alterDropColumn
from parse.errors import Error, ErrorType
from parse.symbol_table import SymbolTable, FieldSymbol, SymbolType


class AlterDatabaseRename(ASTNode):
    def __init__(self, name, new_name, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name  # db current name
        self.new_name = new_name  # db new name

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)
        result_new_name = self.new_name.execute(table, tree)
        result = alterDatabase(result_name, result_new_name)
        if result == 1:
            raise Error(0, 0, ErrorType.RUNTIME, '5800: system_error')
            return False
        elif result == 2:
            raise Error(0, 0, ErrorType.RUNTIME, '42P04: old_database_does_not_exists')
            return False
        elif result == 3:
            raise Error(0, 0, ErrorType.RUNTIME, '42P04: new_database_already_exists')
            return False
        else:
            old_symbol = table.get(result_name, SymbolType.DATABASE)
            old_symbol.name = result_new_name
            table.update(old_symbol)
            return "You renamed table " + str(self.name) + " to "+ str(self.new_name)


class AlterDatabaseOwner(ASTNode):
    def __init__(self, name, owner, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name  # db name
        self.owner = owner  # db new owner

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)
        result_owner = self.owner.execute(table, tree)
        old_symbol = table.get(result_name, SymbolType.DATABASE)
        old_symbol.owner = result_owner
        table.update(old_symbol)
        return True


class AlterTableAddColumn(ASTNode):
    def __init__(self, table_name, field_name, field_type, field_length, allows_null, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name
        self.field_type = field_type
        self.field_length = field_length
        self.allows_null = allows_null

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        result_field_name = self.field_name.execute(table, tree)
        result_field_type = self.field_type.execute(table, tree)
        result_field_length = self.field_length.execute(table, tree)
        result = alterAddColumn(table.get_current_db().name, result_field_name, None)
        if result == 1:
            raise Error(0, 0, ErrorType.RUNTIME, '5800: system_error')
            return False
        elif result == 2:
            raise Error(0, 0, ErrorType.RUNTIME, '42P04: database_does_not_exists')
            return False
        elif result == 3:
            raise Error(0, 0, ErrorType.RUNTIME, '42P04: table_does_not_exists')
            return False
        else:
            total_fields = len(table.get_fields_from_table(result_table_name))
            column_symbol = FieldSymbol(
                table.get_current_db().name,
                result_table_name,
                total_fields + 1,
                result_field_name,
                result_field_type,
                result_field_length,
                self.allows_null,
                False,
                None,
                None
            )
            table.add(column_symbol)
            return True


class AlterTableAddCheck(ASTNode):
    def __init__(self, table_name, validation, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.validation = validation  # Expression to evaluate on insert/update, no need to execute on creation

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        old_symbol = table.get(result_table_name, SymbolType.TABLE)
        old_symbol.check_exp = self.validation  # Change for append if needed to handle multiple ones
        table.update(old_symbol)
        return True


class AlterTableDropColumn(ASTNode):
    def __init__(self, table_name, field_name, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        result_field_name = self.field_name.execute(table, tree)
        # Obtaining all fields because are gonna be needed to get correct field and update indexes later
        all_fields_symbol = table.get_fields_from_table(result_table_name)
        column_symbol = next((sym for sym in all_fields_symbol if sym.field_name == result_field_name), None)
        result = alterDropColumn(table.get_current_db(), result_field_name, column_symbol.field_index)
        if result == 1:
            raise Error(0, 0, ErrorType.RUNTIME, '5800: system_error')
            return False
        elif result == 2:
            # log error, old database name does not exists
            raise Error(0, 0, ErrorType.RUNTIME, '42P04: database_does_not_exists')
            return False
        elif result == 3:
            # log error, table does not exists
            raise Error(0, 0, ErrorType.RUNTIME, '42P04: table_does_not_exists')
            return False
        elif result == 4:
            # log error, PK cannot be deleted or table to be empty
            raise Error(0, 0, ErrorType.RUNTIME, '2300: integrity_constraint_violation')
            return False
        elif result == 4:
            # log error, column out of index
            raise Error(0, 0, ErrorType.RUNTIME, '2300: column_out_of_index')
            return False
        else:
            for field in all_fields_symbol:
                # Update indexes for higher fields
                if field.field_index > column_symbol:
                    field.field_index -= 1
                    table.update(field)
            # TODO just realized it's needed to check for FKs in other tables
            # finally delete symbol of column removed
            table.delete(column_symbol.id)
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

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        result_table_column = self.table_column.execute(table, tree)
        result_table_reference = self.table_reference.execute(table, tree)
        result_column_reference = self.column_reference.execute(table, tree)
        # Obtaining all fields because are gonna be needed to get correct field
        all_fields_symbol = table.get_fields_from_table(result_table_name)
        column_symbol = next((sym for sym in all_fields_symbol if sym.field_name == result_table_column), None)
        # Obtaining table and column itself, since we need to store id
        table_reference = table.get(result_table_reference, SymbolType.TABLE)
        column_reference = table.get(result_column_reference, SymbolType.FIELD)
        column_symbol.fk_table = table_reference.id
        column_symbol.fk_field = column_reference.id
        table.update(column_symbol)

        return True


class AlterTableNotNull(ASTNode):
    def __init__(self, table_name, field_name, allows_null, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name
        self.allows_null = allows_null  # Boolean. If True then is NULL, if False then is NOT NULL

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_field_name = self.field_name.execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        # Obtaining all fields because are gonna be needed to get correct field
        all_fields_symbol = table.get_fields_from_table(result_table_name)
        column_symbol = next((sym for sym in all_fields_symbol if sym.field_name == result_field_name), None)
        column_symbol.allows_null = self.allows_null
        table.update(column_symbol)
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

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_field_name = self.old_name.execute(table, tree)
        result_new_name = self.new_name.execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        # Obtaining all fields because are gonna be needed to get correct field
        all_fields_symbol = table.get_fields_from_table(result_table_name)
        column_symbol = next((sym for sym in all_fields_symbol if sym.field_name == result_field_name), None)
        column_symbol.field_name = result_new_name
        table.update(column_symbol)
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
        result_table_name = self.table_name.execute(table, tree)
        result_field_name = self.field_name.execute(table, tree)
        result_field_type = self.field_type.execute(table, tree)
        result_field_length = self.field_length.execute(table, tree)
        # Obtaining all fields because are gonna be needed to get correct field
        all_fields_symbol = table.get_fields_from_table(result_table_name)
        column_symbol = next((sym for sym in all_fields_symbol if sym.field_name == result_field_name), None)
        column_symbol.field_type = result_field_type
        column_symbol.length = result_field_length
        table.update(column_symbol)
        return True
