from parse.ast_node import ASTNode
from jsonMode import alterDatabase, alterAddColumn, alterDropColumn
from parse.errors import Error, ErrorType
from parse.symbol_table import SymbolTable, FieldSymbol, SymbolType, generate_tmp
from TAC.tac_enum import *
from TAC.quadruple import *


class AlterDatabaseRename(ASTNode):
    def __init__(self, name, new_name, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name  # db current name
        self.new_name = new_name  # db new name
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result = alterDatabase(self.name, self.new_name)
        if result == 1:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '5800: system_error')
        elif result == 2:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: old_database_does_not_exists')
        elif result == 3:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: new_database_already_exists')
        else:
            old_symbol = table.get(self.name, SymbolType.DATABASE)
            old_symbol.name = self.new_name
            table.update(old_symbol)
            return "You renamed table " + str(self.name) + " to " + str(self.new_name)

    def generate(self, table, tree):
        super().generate(table, tree)
        quad = Quadruple(None, 'exec_sql', f'ALTER DATABASE {self.name} RENAME TO {self.new_name};', generate_tmp(),
                         OpTAC.CALL)
        tree.append(quad)
        return quad


class AlterDatabaseOwner(ASTNode):
    def __init__(self, name, owner, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name  # db name
        self.owner = owner  # db new owner
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        # result_owner = self.owner.execute(table, tree)
        old_symbol = table.get(self.name, SymbolType.DATABASE)
        old_symbol.owner = self.owner.val
        table.update(old_symbol)
        return f'You changed owner of database {self.name}'

    def generate(self, table, tree):
        super().generate(table, tree)
        quad = Quadruple(None, 'exec_sql', f'ALTER DATABASE {self.name} OWNER TO {self.owner.val};', generate_tmp(),
                         OpTAC.CALL)
        tree.append(quad)
        return quad
        


class AlterTableAddColumn(ASTNode):
    def __init__(self, table_name, field_name, field_type, field_length, allows_null, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name
        self.field_type = field_type
        self.field_length = field_length
        self.allows_null = allows_null
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_table_name = self.table_name
        result_field_name = self.field_name
        result_field_type = self.field_type.val
        result_field_length = self.field_length
        result = alterAddColumn(table.get_current_db().name, result_table_name, None)
        if result == 1:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '5800: system_error')
        elif result == 2:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: database_does_not_exists')
        elif result == 3:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: table_does_not_exists')
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
            return f'You added column {self.field_name} to table {self.table_name}'

    def generate(self, table, tree):
        super().generate(table, tree)
        result_field_type = self.field_type.val
        quad = Quadruple(None, 'exec_sql', f'ALTER TABLE {self.table_name} ADD COLUMN {self.field_name} {result_field_type};', 
                         generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad


# TODO Pending to add checks
class AlterTableAddCheck(ASTNode):
    def __init__(self, table_name, validation, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.validation = validation  # Expression to evaluate on insert/update, no need to execute on creation
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        old_symbol = table.get(result_table_name, SymbolType.TABLE)
        old_symbol.check_exp = self.validation  # Change for append if needed to handle multiple ones
        table.update(old_symbol)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class AlterTableDropColumn(ASTNode):
    def __init__(self, table_name, field_name, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_table_name = self.table_name
        result_field_name = self.field_name
        # Obtaining all fields because are gonna be needed to get correct field and update indexes later
        all_fields_symbol = table.get_fields_from_table(result_table_name)
        column_symbol = next((sym for sym in all_fields_symbol if sym.field_name == result_field_name), None)
        result = alterDropColumn(table.get_current_db().name, result_table_name, column_symbol.field_index)
        if result == 1:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '5800: system_error')
        elif result == 2:
            # log error, old database name does not exists
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: database_does_not_exists')
        elif result == 3:
            # log error, table does not exists
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: table_does_not_exists')
        elif result == 4:
            # log error, PK cannot be deleted or table to be empty
            raise Error(self.line, self.column, ErrorType.RUNTIME, '2300: integrity_constraint_violation')
        elif result == 5:
            # log error, column out of index
            raise Error(self.line, self.column, ErrorType.RUNTIME, '2300: column_out_of_index')
        else:
            for field in all_fields_symbol:
                # Update indexes for higher fields
                if field.field_index > column_symbol.field_index:
                    field.field_index -= 1
                    table.update(field)
            # TODO just realized it's needed to check for FKs in other tables
            # finally delete symbol of column removed
            table.delete(column_symbol.id)
            return f'You dropped column {self.field_name} from {self.table_name}'

    def generate(self, table, tree):
        super().generate(table, tree)
        quad = Quadruple(None, 'exec_sql', f'ALTER TABLE {self.table_name} DROP COLUMN {self.field_name};', generate_tmp(),
                         OpTAC.CALL)
        tree.append(quad)
        return quad


# TODO add constraint
class AlterTableAddConstraint(ASTNode):
    def __init__(self, table_name, cons_name, field_name, line, column, graph_ref):  # Unique is the only allowed
        ASTNode.__init__(self, line, column)
        self.cons_name = cons_name
        self.table_name = table_name
        self.field_name = field_name
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


# TODO add fk
class AlterTableAddFK(ASTNode):
    def __init__(self, table_name, table_column, table_reference, column_reference, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name  # name of table to alter
        self.table_column = table_column  # name of column to add FK
        self.table_reference = table_reference  # name of table to reference
        self.column_reference = column_reference  # name of column referenced on table to reference
        self.graph_ref = graph_ref

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

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class AlterTableNotNull(ASTNode):
    def __init__(self, table_name, field_name, allows_null, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name
        self.allows_null = allows_null  # Boolean. If True then is NULL, if False then is NOT NULL
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_field_name = self.field_name
        result_table_name = self.table_name
        # Obtaining all fields because are gonna be needed to get correct field
        all_fields_symbol = table.get_fields_from_table(result_table_name)
        column_symbol = next((sym for sym in all_fields_symbol if sym.field_name == result_field_name), None)
        column_symbol.allows_null = self.allows_null
        table.update(column_symbol)
        return f'Updated column {self.table_name} [No]Nullable'

    def generate(self, table, tree):
        super().generate(table, tree)
        quad = Quadruple(None, 'exec_sql', f'ALTER TABLE {self.table_name} ALTER COLUMN {self.field_name} '
                               f'SET {"NOT NULL" if self.allows_null is False else "NULL"};', generate_tmp(),
                         OpTAC.CALL)
        tree.append(quad)
        return quad


# TODO drop constraint
class AlterTableDropConstraint(ASTNode):
    def __init__(self, table_name, cons_name, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name  # table name
        self.cons_name = cons_name  # constraint name
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class AlterTableRenameColumn(ASTNode):
    def __init__(self, table_name, old_name, new_name, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.old_name = old_name
        self.new_name = new_name
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_field_name = self.old_name
        result_new_name = self.new_name
        result_table_name = self.table_name
        # Obtaining all fields because are gonna be needed to get correct field
        all_fields_symbol = table.get_fields_from_table(result_table_name)
        column_symbol = next((sym for sym in all_fields_symbol if sym.field_name == result_field_name), None)
        column_symbol.field_name = result_new_name
        column_symbol.name = result_new_name
        table.update(column_symbol)
        return f'Column {self.old_name} renamed to {self.new_name}'

    def generate(self, table, tree):
        super().generate(table, tree)
        quad = Quadruple(None, 'exec_sql', f'ALTER TABLE {self.table_name} RENAME COLUMN {self.old_name} TO {self.new_name};',
                         generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad


class AlterTableChangeColumnType(ASTNode):
    def __init__(self, table_name, field_name, field_type, field_length, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.field_name = field_name
        self.field_type = field_type
        self.field_length = field_length
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        result_table_name = self.table_name
        result_field_name = self.field_name
        result_field_type = self.field_type.val
        result_field_length = self.field_length
        # Obtaining all fields because are gonna be needed to get correct field
        all_fields_symbol = table.get_fields_from_table(result_table_name)
        column_symbol = next((sym for sym in all_fields_symbol if sym.field_name == result_field_name), None)
        column_symbol.field_type = result_field_type
        column_symbol.length = result_field_length
        table.update(column_symbol)
        return f'Type of column {self.field_type} changed'

    def generate(self, table, tree):
        super().generate(table, tree)
        quad = Quadruple(None, 'exec_sql', f'ALTER TABLE {self.table_name} ALTER COLUMN {self.field_name} '
                               f'TYPE {self.field_type.generate(table, tree)};', generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad
        