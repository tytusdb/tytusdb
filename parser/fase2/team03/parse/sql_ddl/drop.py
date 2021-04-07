from parse.ast_node import ASTNode
from jsonMode import dropDatabase, dropTable
from parse.symbol_table import SymbolTable, DatabaseSymbol, TableSymbol, FieldSymbol, TypeSymbol, generate_tmp
from parse.errors import Error, ErrorType
from TAC.tac_enum import *
from TAC.quadruple import *


class DropDatabase(ASTNode):
    def __init__(self, name, if_exists, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name  # db name
        self.if_exists = if_exists  # boolean if exists
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)

        result = 0
        if self.if_exists:
            dropDatabase(result_name)
            table.drop_data_base(result_name)
            return "Database " + str(result_name) + " has been dropped"
        else:
            result = dropDatabase(result_name)
            if result == 0:  # successful operation
                table.drop_data_base(result_name)
                return "Database " + str(result_name) + " has been dropped."
            elif result == 1:  # operation error
                raise Error(self.line, self.column, ErrorType.RUNTIME, '58000: system_error')
            elif result == 2:  # database does not exist.
                raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: database_does_not_exists')

    def generate(self, table, tree):
        super().generate(table, tree)
        result_name = self.name.generate(table, tree)
        quad = Quadruple(None, 'exec_sql', f'DROP DATABASE{" IF EXISTS" if self.if_exists else ""} {result_name};',
                         generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad


class DropTable(ASTNode):
    def __init__(self, name, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name  # table name
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)
        result = dropTable(table.get_current_db().name, result_name)
        if result == 0:  # successful operation
            table.drop_table(result_name)
            return "Table " + str(result_name) + " has been dropped."
        elif result == 1:  # operation error
            raise Error(self.line, self.column, ErrorType.RUNTIME, '58000: system_error')
        elif result == 2:  # database does not exist.
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: database_does_not_exists')
        elif result == 3:  # table does not exist
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P01: table_does_not_exists')

    def generate(self, table, tree):
        super().generate(table, tree)
        result_name = self.name.generate(table, tree)
        quad = Quadruple(None,'exec_sql', f'DROP TABLE {result_name};', generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad
