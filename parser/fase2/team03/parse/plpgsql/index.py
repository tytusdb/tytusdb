from parse.ast_node import ASTNode
from parse.symbol_table import *
from TAC.tac_enum import *
from TAC.quadruple import *
from parse.errors import *


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
        # validate fields
        all_fields_declared = table.get_fields_from_table(self.table)
        fields = []
        for field in self.fields:
            field_text = ''
            field_order = None
            if type(field) == str:
                field_text = field
            elif type(field.field_name) == str:
                field_text = field.field_name
                field_order = f'{field.order_by}{" NULLS" if field.is_nulls else ""}{field.border if field.border is not None else ""}'
            else:
                field_text = field.field_name.generate(table, tree)
                field_order = field.order_by
            match = next((col for col in all_fields_declared if field_text == col.name), None)
            if match is None:
                raise Error(self.line, self.column, ErrorType.SEMANTIC, f'{field_text} does not exists in table declaration')
            fields.append([field_text, field_order])
        obj = IndexSymbol(self.name, self.table, table.get_current_db(), self.is_unique, self.using_hash, fields, self.where)
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
        return f'Index {self.idx_name} dropped successfully'

    def generate(self, table, tree):
        super().generate(table, tree)
        return Quadruple(None, f'DROP INDEX{" CONCURRENTLY" if self.is_concurrent else ""}{" IF EXISTS" if self.if_exists else ""} '
                               f'{self.idx_name};', None, generate_tmp(), OpTAC.CALL)


class AlterIndex(ASTNode):
    def __init__(self, if_exists, idx_name, old_field, new_field, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.if_exists = if_exists is not None
        self.idx_name = idx_name
        self.old_field = old_field
        self.new_field = new_field
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        # if not self.if_exists:
        try:
            idx_symbol = table.get(self.idx_name, SymbolType.INDEX)  # To raise exception if not exists
            all_fields_declared = table.get_fields_from_table(idx_symbol.table_name)
            # validate old field exists
            match = next((col for col in all_fields_declared if col.name == self.old_field), None)
            if match is None:
                raise Error(self.line, self.column, ErrorType.SEMANTIC, f'Old Field does not exists in table declaration')
            # validate new field exists
            match = next((col for col in all_fields_declared if col.name == self.new_field), None)
            if match is None:
                raise Error(self.line, self.column, ErrorType.SEMANTIC,
                            f'New Field does not exists in table declaration')

            for field in idx_symbol.applied_to:
                if field[0] == self.old_field:
                    field[0] = self.new_field
                    break
        except Error:
            return f'Index {self.idx_name} changed successfully :)'

        return f'Index {self.idx_name} changed successfully'

    def generate(self, table, tree):
        super().generate(table, tree)
        return Quadruple(None, f'ALTER INDEX{" IF EXISTS" if self.if_exists else ""} {self.idx_name} ALTER COLUMN '
                               f'{self.old_field} {self.new_field};', None, generate_tmp(), OpTAC.CALL)