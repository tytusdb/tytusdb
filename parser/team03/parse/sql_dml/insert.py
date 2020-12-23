from parse.ast_node import ASTNode
from jsonMode import insert
from parse.symbol_table import SymbolTable, SymbolType
from parse.errors import Error, ErrorType


class InsertInto(ASTNode):
    def __init__(self, table_name, column_list, insert_list, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.column_list = column_list  # Optional. Columns to insert. Already a list of Strings?
        self.insert_list = insert_list  # Could be a list coming from <EXP_LST> or list from <STM_SELECT>
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        # Table symbol so we can run checks and validations
        table_symbol = table.get(self.table_name, SymbolType.TABLE)
        all_fields_declared = table.get_fields_from_table(self.table_name)
        # Sorting list, so we know order to insert is correct
        all_fields_declared.sort(key=lambda x: x.field_index)
        # Mapping values to insert, to actual structure on data structure
        to_insert = []
        for field_symbol in all_fields_declared:
            # looking in column list if declared field appears or None
            match = next((col for col in self.column_list if col.val == field_symbol.name), None)
            # Run validations only if result is not None
            value_related_to_match = self.column_list.index(match)
            if match is not None:
                # TODO ADD HERE TYPE VALIDATIONS PER FIELD, JUST ONE ADDED BY NOW TO GIVE EXAMPLE
                if field_symbol.field_type.upper() == 'INTEGER' and type(self.insert_list[value_related_to_match].val) != int:
                    raise Error(0, 0, ErrorType.SEMANTIC, f'Field {field_symbol.name} must be an integer type')
            to_insert.append(self.insert_list[value_related_to_match].val)
        # TODO ADD HERE CHECK VALIDATION
        result = insert(table.get_current_db().name, self.table_name, to_insert)
        if result == 1:
            raise Error(0, 0, ErrorType.RUNTIME, '5800: system_error')
        elif result == 2:
            raise Error(0, 0, ErrorType.RUNTIME, '42P04: database_does_not_exists')
        elif result == 3:
            raise Error(0, 0, ErrorType.RUNTIME, '42P07: table_does_not_exists')
        elif result == 4:
            raise Error(0, 0, ErrorType.RUNTIME, '42P10: duplicated_primary_key')
        else:
            return True


# This class probably is not going to be needed, depends on how the contents are gonna be handled
class InsertItem(ASTNode):
    def __init__(self, column_list, values_list, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.column_list = column_list
        self.values_list = values_list
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return True
