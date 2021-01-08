from parse.ast_node import ASTNode
from parse.symbol_table import *
from TAC.tac_enum import *
from TAC.quadruple import *


class CreateIndex(ASTNode):
    def __init__(self, is_unique, using_hash, name, table, fields, where, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.is_unique = is_unique
        self.using_hash = using_hash
        self.name = name
        self.table = table
        self.fields = fields
        self.where = where
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        # validate that table does exists
        table_obj = table.get(self.table, SymbolType.TABLE)
        fields = []
        for field in self.fields:
            fields.append(field if type(field) == str else field.field_name.generate(table, tree))
        obj = IndexSymbol(self.name, self.table, table.get_current_db(), self.is_unique, fields, self.where)
        table.add(obj)
        return f'Indice {self.name } guardado'

    def generate(self, table, tree):
        super().generate(table, tree)
        fields_str = ''
        for field in self.fields:
            fields_str = f'{fields_str}{field.generate(table, tree)},'
        return Quadruple(None, f'CREATE{" UNIQUE" if self.is_unique else ""} INDEX {self.name} ON {self.table}'
                               f'{" USING HASH" if self.using_hash else ""} ({fields_str[:-1]})'
                               f'{f" {self.where.generate(table, tree)}" if self.where is not None else ""};', None, generate_tmp(), OpTAC.CALL)


class IndexAtributo(ASTNode):
    def __init__(self, exp1, field_name, order_by, is_nulls, border, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.is_exp = exp1 is not None
        self.field_name = field_name
        self.order_by = order_by
        self.is_nulls = is_nulls is not None
        self.border = border
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return 'Stored index attribute'

    def generate(self, table, tree):
        super().generate(table, tree)
        if self.is_exp:
            return self.field_name.generate(table, tree)
        else:
            return f'{self.field_name}{f" {self.order_by}" if self.order_by is not None else ""}' \
                   f'{" NULLS" if self.is_nulls else ""}{f" {self.border}" if self.border else ""}'


class DropIndex(ASTNode):
    def __init__(self, is_concurrent, if_exists, idx_name, drop_mode, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.is_concurrent = is_concurrent is not None
        self.if_exists = if_exists is not None
        self.idx_name = idx_name
        self.drop_mode = drop_mode
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        if not self.if_exists:
            table.get(self.idx_name, SymbolType.INDEX)  # To raise exception if not exists
        table.drop_index(self.idx_name)
        return 'Index dropped successfully'

    def generate(self, table, tree):
        super().generate(table, tree)
        return Quadruple(None, f'DROP INDEX{" CONCURRENTLY" if self.is_concurrent else ""}{" IF EXISTS" if self.if_exists else ""} '
                               f'{self.idx_name};', None, generate_tmp(), OpTAC.CALL)
