from jsonMode import createDatabase, createTable, dropDatabase, alterAddPK
from parse.ast_node import ASTNode
from parse.symbol_table import SymbolTable, TableSymbol, FieldSymbol, TypeSymbol, generate_tmp
from parse.errors import Error, ErrorType
from TAC.tac_enum import *
from TAC.quadruple import *


class CreateEnum(ASTNode):
    def __init__(self, name, value_list, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name.upper()  # type name
        self.value_list = value_list  # list of possible values
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_values = []
        for val in self.value_list:
            result_values.append(val.execute(table, tree))
        symbol = TypeSymbol(self.name, result_values)
        table.add(symbol)
        print(f'[AST] ENUM {self.name} created.')
        return f'[AST] ENUM {self.name} created.'

    def generate(self, table, tree):
        super().generate(table, tree)
        all_val = ''
        for val in self.value_list:
            all_val = f'{all_val}\'{val.generate(table, tree)}\','
        quad = Quadruple(None, 'exec_sql', f'CREATE TYPE {self.name} AS ENUM({all_val[:-1]});', generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad

class CreateDatabase(ASTNode):
    def __init__(self, name, owner, mode, replace, exists, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name  # database name
        self.owner = owner  # optional owner
        self.mode = mode  # mode integer
        self.replace = replace  # boolean type
        self.exists = exists
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        # result_name = self.name.execute(table, tree)
        # result_owner = self.owner.execute(table, tree) if self.owner else None  # Owner seems to be stored only to ST
        # result_mode = self.owner.mode(table, tree) if self.mode else 6  # Change to 1 when default mode from EDD available
        result_name = self.name.execute(table, tree)
        result_owner = self.owner
        result_mode = self.mode.execute(table, tree) if self.mode is not None else 1
        result = 0
        if self.replace:
            dropDatabase(result_name)

        # if result_mode == 6:  # add more ifs when modes from EDD available
        result = createDatabase(result_name)

        if result == 1:
            # log error on operation
            raise Error(self.line, self.column, ErrorType.RUNTIME, '5800: system_error')
        elif result == 2 and self.exists is False:
            # log error because db already exists
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: duplicate_database')
        else:
            # return table.add(DatabaseSymbol(result_name, result_owner, result_mode)) #chaged by loadDatabases
            table.LoadDataBases()
            return ['Database \'' + result_name + '\' was created successfully!']

    def generate(self, table, tree):
        super().generate(table, tree)
        result_mode = self.mode.generate(table, tree) if self.mode is not None else 1
        result_name = self.name.generate(table, tree)
        quad = Quadruple(None, 'exec_sql',
                         f'CREATE DATABASE{" IF NOT EXISTS" if self.exists else ""} {result_name} MODE = {result_mode};',
                         generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad


class CreateTable(ASTNode):  # TODO: Check grammar, complex instructions are not added yet
    def __init__(self, name, inherits_from, fields, check_exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name  # table name
        self.inherits_from = inherits_from  # optional inheritance
        self.fields = fields  # list of fields
        self.check_exp = check_exp  # Expression to evaluate on insert/update, no need to execute on creation
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name
        result_inherits_from = self.inherits_from.val if self.inherits_from else None
        result_fields = self.fields
        if result_inherits_from:
            # get inheritance table, if doesn't exists throws semantic error, else append result
            result_fields += table.get_fields_from_table(result_inherits_from)

        result = createTable(table.get_current_db().name, result_name, len(result_fields))

        if result == 1:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '5800: system_error')
        elif result == 2:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P04: database_does_not_exists')
        elif result == 3:
            raise Error(self.line, self.column, ErrorType.RUNTIME, '42P07: duplicate_table')
        else:
            # add primary keys, jsonMode needs the number of the column to set it to primarykey
            keys = list(
                map(
                    lambda x: result_fields.index(x),
                    filter(lambda key: key.is_pk is True, result_fields)
                )
            )
            if len(keys) > 0:
                result = alterAddPK(table.get_current_db().name, result_name, keys)

            table.add(TableSymbol(table.get_current_db().id, result_name, self.check_exp))

        field_index = 0
        for field in result_fields:
            nuevo = FieldSymbol(table.get_current_db().name, result_name, field_index, field.name, field.field_type,
                                field.length, field.allows_null, field.is_pk, None, None)
            field_index += 1
            table.add(nuevo)

        return "Table: " + str(result_name) + " created."

    def generate(self, table, tree):
        super().generate(table, tree)
        result_fields = self.fields
        result_inherits_from = self.inherits_from.val if self.inherits_from else None
        field_str = ''
        for field in result_fields:
            field_str = f'{field_str}{field.name} {field.field_type}' \
                        f'{" IS NOT NULL" if field.allows_null is False else ""}' \
                        f'{" PRIMARY KEY" if field.is_pk is True else ""},'
        quad = Quadruple(None, 'exec_sql', f'CREATE TABLE {self.name} ({field_str[:-1]})'
                               f'{f" INHERITS ({result_inherits_from})" if result_inherits_from is not None else ""};',
                          generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad


class TableField(ASTNode):  # returns an item, grammar has to add it to a list and synthesize value to table
    def __init__(self, name, field_type, length, allows_null, is_pk, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name  # field name
        self.field_type = field_type  # type of field
        self.length = length
        self.allows_null = False if allows_null and allows_null.val is False else True
        self.is_pk = is_pk  # field is primary key
        self.graph_ref = graph_ref

    def execute(self, table: SymbolTable, tree):
        super().execute(table, tree)
        result_name = self.name.execute(table, tree)
        result_field_type = self.field_type.execute(table, tree)
        result_length = self.length.execute(table, tree)
        return FieldSymbol(
            table.get_current_db().name,
            None,
            0,
            result_name,
            result_field_type,
            result_length,
            self.allows_null,
            self.is_pk,
            None,
            None
        )

    def generate(self, table, tree):
        super().generate(table, tree)
        result_name = self.name.execute(table, tree)
        return f'{result_name}'

# table = SymbolTable([])
# cdb_obj = CreateDatabase('db_test2', None, None, False, 1, 2)
# print(cdb_obj.execute(table, None))
