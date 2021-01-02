from parse.ast_node import ASTNode


class Case(ASTNode):
    def __init__(self, cases, else_exp, line, column):
        ASTNode.__init__(self, line, column)
        self.cases = cases
        self.else_exp = else_exp

    def execute(self, table, tree):
        super().execute(table, tree)
        # iterate all cases result maybe and returns result or else_exp if no one was returned
        return True

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''


class CaseInner(ASTNode):
    def __init__(self, condition, result, line, column):
        ASTNode.__init__(self, line, column)
        self.condition = condition
        self.result= result

    def execute(self, table, tree):
        super().execute(table, tree)
        if self.condition:
            return self.result
        else:
            return None

    def generate(self, table, tree):
        super().generate(table, tree)
        return ''
