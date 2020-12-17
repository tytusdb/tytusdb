import sys

sys.path.insert(0, '..')
from ast_node import ASTNode


class Select(ASTNode):
    def __init__(self, is_distinct, col_names, tables, where, group_by, having, order_by, limit, offset, line, column):
        ASTNode.__init__(self, line, column)
        self.is_distinct = is_distinct  # true = distinct, false = not distinct, None = not specified
        self.col_names = col_names      # could be identifier or identifier.identifier
        self.tables = tables            # could be a string list and/or a list of node, not sure
        self.where = where              # could be a boolean and/or a node, not sure
        self.group_by = group_by        # is a list of col_names, like previous one
        self.having = having            # having is a logical expression, could be a node?
        self.order_by = order_by        # column name, could be identifier or identifier.identifier
        self.limit = limit              # integer
        self.offset = offset            # integer

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Names(ASTNode):
    def __init__(self, is_asterisk, exp, alias, line, column):
        ASTNode.__init__(self, line, column)
        self.is_asterisk = is_asterisk
        self.exp = exp
        self.alias = alias

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class TableReference(ASTNode):
    def __init__(self, table, natural_join, join_type, table_to_join, subquery, line, column):
        ASTNode.__init__(self, line, column)
        self.table = table                      # Unique field to be mandatory, others are None if no joins
        self.natural_join = natural_join        # Probably will be easier to add naturals to enum, dev must decide
        self.join_type = join_type              # join type reference, NOT string (maybe)
        self.table_to_join = table_to_join
        self.subquery = subquery                # Result of subquery or node, dev must decide

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Table(ASTNode):
    def __init__(self, name, alias, subquery, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name
        self.alias = alias
        self.subquery = subquery

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Where(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


#  Probably not needed but added anyways
class Join(ASTNode):
    def __init__(self, name, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


# Probably needs to have a way to create a list from comma separated string
class GroupBy(ASTNode):
    def __init__(self, names, line, column):
        ASTNode.__init__(self, line, column)
        self.name = names

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Having(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class TimeOps(ASTNode):
    def __init__(self, extract_opt, time_string, aux_string, line, column):
        ASTNode.__init__(self, line, column)
        self.extract_opt = extract_opt      # extract opt from Enum, if None then is date_part and needs aux_string
        self.time_string = time_string      # string used to parse date
        self.aux_string  = aux_string       # needed only if is date_part, ex. HOUR... would this be an enum?

    def execute(self, table, tree):
        super().execute(table, tree)
        return True
