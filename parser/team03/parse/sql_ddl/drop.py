from parse.ast_node import ASTNode
from jsonMode import dropDatabase
from parse.symbol_table import SymbolTable, DatabaseSymbol, TableSymbol, FieldSymbol, TypeSymbol
from parse.errors import Error, ErrorType

class DropDatabase(ASTNode):
    def __init__(self, name, if_exists, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name            # db name
        self.if_exists = if_exists  # boolean if exists

    def execute(self, table:SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name

        result = 0
        if self.if_exists:
            dropDatabase(result_name)
            return True
        else:
            result = dropDatabase(result_name)
            if result == 0:     # successful operation
                table.drop_data_base(result_name)
                return True
            elif result == 1:   # operation error
                raise Error(0, 0, ErrorType.RUNTIME, '58000: system_error')
            elif result == 2:    # database does not exist.
                raise Error(0, 0, ErrorType.RUNTIME, '42P04: database_does_not_exists')

class DropTable(ASTNode):
    def __init__(self, name, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name            # table name

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

