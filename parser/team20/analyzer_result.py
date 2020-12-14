class analyzer_result:

    def __init__(self, AST_Tree, Dot_Graphviz_AST_Tree, Error_Table, Printed_Error_Table):
        self.AST_Tree = AST_Tree
        self.Dot_Graphviz_AST_Tree = Dot_Graphviz_AST_Tree
        self.Error_Table = Error_Table
        self.Printed_Error_Table = Printed_Error_Table