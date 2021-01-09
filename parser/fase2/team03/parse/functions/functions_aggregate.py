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

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'AVG({self.exp.generate(table, tree)})'


class Count(ASTNode):
    def __init__(self, exp, all_results, line, column, graph_ref):
        ASTNode.__init__(self, line, column)
        self.exp = exp
        self.all_results = all_results
        self.graph_ref = graph_ref
        #self.is_asterisk = False

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.all_results:
            if isinstance(tree, list) and isinstance(tree[1],list):
                return len(tree[1])
            
        return 1

    def generate(self, table, tree):
        super().generate(table, tree)
        if self.all_results: 
            return f'COUNT({self.exp.generate(table, tree)})'
        return f'COUNT({self.exp.generate(table, tree)})'


class Greatest(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class Least(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class Max(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'MAX({self.exp.generate(table, tree)})'


class Min(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'MIN({self.exp.generate(table, tree)})'


class Sum(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'SUM({self.exp.generate(table, tree)})'


class Top(ASTNode):
    def __init__(self, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return f'TOP({self.exp.generate(table, tree)})'


def test():
    avg = Avg('123', 1, 2)
    avg.execute('1', '2')


test()
