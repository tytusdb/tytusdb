from parse.ast_node import ASTNode
from jsonMode import showDatabases as showDB


class ShowDatabases(ASTNode):
    def __init__(self, name, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name

    def execute(self, table, tree):
        super().execute(table, tree)
        result_name = self.name.execute()
        return showDB()  # add filter using name_like_regex... this has to be stored on TS or comes from function?


class Union(ASTNode):
    def __init__(self, records_a, records_b, is_all, line, column):
        ASTNode.__init__(self, line, column)
        self.records_a = records_a
        self.records_b = records_b
        self.is_all = is_all

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.is_all:
            return self.records_a + self.records_b
        else:
            in_first = set(self.records_a)
            in_second = set(self.records_b)
            in_second_but_not_in_first = in_second - in_first
            return self.records_a + list(in_second_but_not_in_first)


class Intersect(ASTNode):
    def __init__(self, records_a, records_b, is_all, line, column):
        ASTNode.__init__(self, line, column)
        self.records_a = records_a
        self.records_b = records_b
        self.is_all = is_all

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.is_all:  # TODO I have no idea of what the result of a intersect all is
            return list(set(self.records_a).intersection(self.records_b))
        else:
            return list(set(self.records_a).intersection(self.records_b))


class Except(ASTNode):
    def __init__(self, records_a, records_b, is_all, line, column):
        ASTNode.__init__(self, line, column)
        self.records_a = records_a
        self.records_b = records_b
        self.is_all = is_all

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.is_all:  # TODO I may have an idea of what the result
            return list(set(self.records_a).intersection(self.records_b))
        else:
            return self.records_a - self.records_b