from parse.ast_node import ASTNode
from jsonMode import *
from util import *
from parse.plpgsql.function import FuncCall
from TAC.quadruple import Quadruple
from TAC.tac_enum import OpTAC
from parse.symbol_table import generate_tmp
from parse.functions.functions_aggregate import *
class Select(ASTNode):
    def __init__(self, is_distinct, col_names, tables, where, group_by, having, order_by, limit, offset, line, column,
                 graph_ref):
        ASTNode.__init__(self, line, column)
        self.is_distinct = is_distinct  # true = distinct, false = not distinct, None = not specified
        self.col_names = col_names  # could be identifier or identifier.identifier
        self.tables = tables  # could be a string list and/or a list of node, not sure
        self.where = where  # could be a boolean and/or a node, not sure
        self.group_by = group_by  # is a list of col_names, like previous one
        self.having = having  # having is a logical expression, could be a node?
        self.order_by = order_by  # column name, could be identifier or identifier.identifier
        self.limit = limit  # integer
        self.offset = offset  # integer
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)

        header = []
        megaunion = []
        # lets make the cartesiasn from all tables
        if self.tables:

            for t in self.tables:
                columns = []
                data = []
                if t.subquery is not None:
                    r = t.execute(table, tree)
                    if len(r) > 0:
                        columns = r[0]
                        data = r[1]
                else:
                    ####for non subquery
                    # get all columnaes and add into header array
                    columns = table.get_fields_from_table(t.name)
                    columns.sort(key=lambda x: x.field_index)
                    for c in columns:
                        if t.alias is None:
                            header.append(str(c.field_name))
                        else:
                            header.append(str((t.alias) + '.' + str(c.field_name)))

                    data = extractTable(table.get_current_db().name, t.name)
                    #####for non subquery
                if len(megaunion) > 0 and len(data) > 0:
                    megaunion = doBinaryUnion(megaunion, data)
                elif len(megaunion) == 0:
                    megaunion = data
                else:
                    megaunion = megaunion
            # Appying filtering for each row by call the excute function if execute return true we kept the row else remove that
            if self.where:
                megaunion = self.where.execute(megaunion, header)
            # TODO:add agregate functions
            for col in self.col_names:
                s = col
            # TODO:filter columns...
            # TODO:apply group by execution...
            if self.group_by:
                pass
            # TODO:apply having by execution...
            if self.having:
                pass
            if self.is_distinct:
                temp = []
                for item in megaunion:
                    if item not in temp:
                        temp.append(item)
                megaunion = temp

        if not self.col_names[0].is_asterisk:  # return specific columns
            rrow = []  # only one result or row
            lrows = []  # the list of rows
            resutCols = []
            if self.tables:  # there are rows to process
                resutCols = list(map(lambda x: x.alias, self.col_names))
                # for selCol in col_names:
                #    resutCols.append(selCol.alias)#for header
                for row in megaunion:
                    rrow = []
                    for col in self.col_names:                        
                        rrow.append(col.execute(row, header)) #commnet fory to send all registers instad header for agragate functions
                        #rrow.append(col.execute(row, [header,megaunion]))
                    lrows.append(rrow)

                #force gruop by with distinct :s
                if AllAgregateFunc(self.col_names) and len(self.col_names) == 1:
                    return [resutCols, [[len(megaunion)]]]
                    #temp = []
                    #for item in megaunion:
                    #    if item not in temp:
                    #        temp.append(item)
                    #megaunion = temp

                return [resutCols, lrows]

            else:  # there are no rows but could be a select of fuctions
                for selCol in self.col_names:
                    resutCols.append(selCol.alias)  # for header
                    rrow.append(selCol.execute(table, tree))
                return [resutCols, [rrow]]

        return [header, megaunion]

    def generate(self, table, tree):
        super().generate(table, tree)
        col_str = ''
        table_str = ''
        for col in self.col_names:
            col_str = f'{col_str}{col.generate(table, None)},'
        if isinstance(self.tables, list):
            for table in self.tables:
                table_str = f'{table_str}{table.generate(table, tree)},'
        ret = f'SELECT{" DISTINCT" if self.is_distinct else ""} {col_str[:-1]}'
        if table_str:
            ret += f'{f" FROM {table_str[:-1]}" if self.tables is not None else ""}'
        if self.where is not None:
            ret += f'{self.where.generate(table, None)}'
        quad = Quadruple(None, 'exec_sql', f'\'{ret};\'', generate_tmp(), OpTAC.CALL)
        tree.append(quad)
        return quad
       
    def generate_pure(self, table, tree):
        super().generate(table, tree)
        col_str = ''
        table_str = ''
        for col in self.col_names:
            col_str = f'{col_str}{col.generate(table, tree)},'

        for table in self.tables:
            table_str = f'{table_str}{table.generate(table, tree)},'

        return f'SELECT{" DISTINCT" if self.is_distinct else ""} {col_str[:-1]}' \
               f'{f" FROM {table_str[:-1]}" if self.tables is not None else ""} {self.where.generate(table, tree)};'


class Names(ASTNode):
    def __init__(self, is_asterisk, exp, alias, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.is_asterisk = is_asterisk
        self.exp = exp
        self.edited = alias is None
        if alias is None:
            self.alias = 'C_' + str(id(self))
        else:
            self.alias = alias
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.exp:
            return self.exp.execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        if self.is_asterisk:
            return '*'
        else:
            return f'{self.exp.generate(table, tree)}{f" AS {self.alias}" if not self.edited else ""}'

    def isAgregateFunc(self):
        return isinstance(self.exp, Avg) or isinstance(self.exp, Count) or isinstance(self.exp, Greatest) or \
        isinstance(self.exp, Least) or isinstance(self.exp, Max) or isinstance(self.exp, Min) or \
        isinstance(self.exp, Sum) or isinstance(self.exp, Top)

def AllAgregateFunc(lnames:list):
    if isinstance(lnames, list):
        if len(lnames) == 0:
            return false

        allAg = True
        for l in lnames:
            allAg = allAg and l.isAgregateFunc()
        return allAg
    return False

class TableReference(ASTNode):
    def __init__(self, table, natural_join, join_type, table_to_join, subquery, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.table = table  # Unique field to be mandatory, others are None if no joins
        self.natural_join = natural_join  # Probably will be easier to add naturals to enum, dev must decide
        self.join_type = join_type  # join type reference, NOT string (maybe)
        self.table_to_join = table_to_join
        self.subquery = subquery  # Result of subquery or node, dev must decide
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class Table(ASTNode):
    def __init__(self, name, alias, subquery, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name
        self.alias = alias
        self.subquery = subquery
        self.graph_ref = graph_ref
        if self.subquery:
            if self.alias is None:
                self.alias = 'subq' + str(id(self))
            if self.name is None:
                self.name = 'subq' + str(id(self))

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.subquery:
            return self.subquery.execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        if self.subquery:
            return f'({self.subquery.generate(table, tree)})'
        else:
            return f'{self.name}{f" AS {self.alias}" if self.alias is not None and self.alias != self.name else ""}'


class Where(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        result = []
        for row in table:
            # maybe I shouldn't do this... pass this paramas
            keept_this_row = self.exp.execute(row, tree)
            if keept_this_row:
                result.append(row)
        return result

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'WHERE {self.exp.generate(table, tree)}'


#  Probably not needed but added anyways
class Join(ASTNode):
    def __init__(self, name, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = name
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


# Probably needs to have a way to create a list from comma separated string
class GroupBy(ASTNode):
    def __init__(self, names, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.name = names
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class Having(ASTNode):
    def __init__(self, exp, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class TimeOps(ASTNode):
    def __init__(self, extract_opt, time_string, aux_string, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.extract_opt = extract_opt  # extract opt from Enum, if None then is date_part and needs aux_string
        self.time_string = time_string  # string used to parse date
        self.aux_string = aux_string  # needed only if is date_part, ex. HOUR... would this be an enum?
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''
