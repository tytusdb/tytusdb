from parse.ast_node import ASTNode
from parse.symbol_table import SymbolTable
from jsonMode import delete
from parse.errors import Error, ErrorType

class Delete(ASTNode):
    def __init__(self, table_name, where, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.where = where

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_table_name = self.table_name.execute(table, tree)
        result_where = self.where.execute(table, tree)  # Select is a must, check result from where
        # This array must be filled with pks to delete
        result = delete(table.get_current_db().name, result_table_name, ['1'])
        if result == 1:
            raise Error(0, 0, ErrorType.RUNTIME, '5800: system_error')
        elif result == 2:
            raise Error(0, 0, ErrorType.RUNTIME, '42P04: database_does_not_exists')
        elif result == 3:
            raise Error(0, 0, ErrorType.RUNTIME, '42P07: table_does_not_exists')
        elif result == 4:
            raise Error(0, 0, ErrorType.RUNTIME, '42P10: PK_does_not_exists')
        else:
            return True
