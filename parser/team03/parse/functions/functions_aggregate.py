from parse.ast_node import ASTNode


# From here on, classes describing aggregate functions
# TODO: ALL OF THEM ARE PENDING ON EXECUTION, ONLY DEFINITION HAS BEEN SET
class Avg(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Count(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Greatest(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Least(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Max(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Min(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Sum(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class Top(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


def test():
    avg = Avg('123', 1, 2)
    avg.execute('1', '2')


test()
