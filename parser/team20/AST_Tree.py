from graphviz import Digraph

dot=Digraph()

class AST_Tree_Node:

    def __init__(self, type, data, row, column, environment, children,pos):
        self.type = type
        self.data = data
        self.row = row
        self.column = column
        self.environment = environment
        self.pos=pos
        if children == None:
            children = []
        else:
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

    def preorderG(self):
        self.preorder_auxG(self.root_node)
        dot.node_attr.update(shape='circle'),
        dot.edge_attr.update(color='blue4')
        dot.view()

    def preorder_auxG(self, node):
        if node != None:
            dot.node(str(node.pos),str(node.data))
            print(node.data)
            i = 0
            while i < len(node.children):
                dot.edge(str(node.pos),str(node.children[i].pos))
                self.preorder_auxG(node.children[i])
                i += 1