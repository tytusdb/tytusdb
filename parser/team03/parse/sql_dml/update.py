from parse.ast_node import ASTNode


class Update(ASTNode):
    def __init__(self, table_name, update_list, where, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.update_list = update_list
        self.where = where

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class UpdateItem(ASTNode):
    def __init__(self, column_name, exp, line, column):
        ASTNode.__init__(self, line, column)
        self.column_name = column_name
        self.exp = exp

    def execute(self, table, tree):
        super().execute(table, tree)
        return True
