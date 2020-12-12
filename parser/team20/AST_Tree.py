class AST_Tree_Node:

    def __init__(self, type, data, row, column, environment, children):
        self.type = type
        self.data = data
        self.row = row
        self.column = column
        self.environment = environment
        if children == None:
            children = []
        self.children = children


class AST_Tree:

    def __init__(self, root_node):
        self.root_node = root_node

    def preorder(self):
        self.preorder_aux(self.root_node)

    def preorder_aux(self, node):
        if node != None:
            print(node.data)
            i = 0
            while i < len(node.children):
                self.preorder_aux(node.children[i])
                i += 1