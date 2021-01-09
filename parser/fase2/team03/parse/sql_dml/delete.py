from parse.ast_node import ASTNode
from jsonMode import *
from parse.errors import Error, ErrorType
from util import *
from TAC.tac_enum import *
from TAC.quadruple import *
from parse.symbol_table import *


class Delete(ASTNode):
    def __init__(self, table_name, where, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.where = where
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)

        header = []
        # get all columns and add into header array
        columns = table.get_fields_from_table(self.table_name)
        columns.sort(key=lambda x: x.field_index)
        primary_key = 0
        for c in columns:
            header.append(str(c.field_name))
            if c.is_pk:
                primary_key = c.field_index

        data = extractTable(table.get_current_db().name, self.table_name)
        # Apply filter for each row by call the execute function if execute return true we kept the row else remove that
        if self.where:
            data = self.where.execute(data, header)
        # getting only PKs to delete... Added | as a hack to delete keys
        to_delete = list(map(lambda x: f'{x[primary_key]}|', data))
        result = delete(table.get_current_db().name, self.table_name, to_delete)
        if result == 1:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '5800: system_error')
        elif result == 2:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: database_does_not_exists')
        elif result == 3:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P07: table_does_not_exists')
        elif result == 4:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P10: PK_does_not_exists')
        else:
            return f'A register has been deleted from {self.table_name}'

    def generate(self, table, tree):
        super().generate(table, tree)
        quad = Quadruple(None, 'exec_sql', f'"DELETE FROM {self.table_name} {self.where.generate(table, tree) if self.where is not None else ""};"'
                         , generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad
