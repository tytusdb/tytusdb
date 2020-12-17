from parse.ast_node import ASTNode


class InsertInto(ASTNode):
    def __init__(self, table_name, insert_list, line, column):
        ASTNode.__init__(self, line, column)
        self.table_name = table_name
        self.insert_list = insert_list

    def execute(self, table, tree):
        super().execute(table, tree)
        return True


class InsertItem(ASTNode):
    def __init__(self, column_list, values_list, line, column):
        ASTNode.__init__(self, line, column)
        self.column_list = column_list
        self.values_list = values_list

    def execute(self, table, tree):
        super().execute(table, tree)
        return True