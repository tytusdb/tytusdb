import sys

sys.path.insert(0, '..')
from ast_node import ASTNode


class DropDatabase(ASTNode):
    def __init__(self, name, if_exists, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name            # db name
        self.if_exists = if_exists  # boolean if exists

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class DropTable(ASTNode):
    def __init__(self, name, line, column):
        ASTNode.__init__(self, line, column)
        self.name = name            # table name

    def execute(self, table, tree):
        super().execute(table, tree)
        return True
