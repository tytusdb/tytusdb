import sys

sys.path.insert(0, '..')
from ast_node import ASTNode


class Delete(ASTNode):
    def __init__(self, table_name, where, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.where = where

    def execute(self, table, tree):
        super().execute(table, tree)
        return True