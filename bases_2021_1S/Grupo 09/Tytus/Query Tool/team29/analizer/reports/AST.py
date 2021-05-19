from graphviz import Digraph
from team29.analizer.reports.Nodo import Nodo
from team29.analizer import variables

dot = Digraph(comment="AST")


class AST:
    def __init__(self):
        self.count = 0

    def makeAst(self, root):
        self.defineTreeNodes(root)
        self.joinTreeNodes(root)
        self.drawGraph()

    def defineTreeNodes(self, root):
        root.setId(str(self.count))
        dot.node(str(self.count), root.getVal())
        self.count += 1
        for node in root.getLista():
            self.defineTreeNodes(node)

    def joinTreeNodes(self, root):
        for node in root.getLista():
            dot.edge(root.getId(), node.getId())
            self.joinTreeNodes(node)

    def drawGraph(self):
        global dot
        dot.render("test-output/round-table.gv", view=False)
        dot = Digraph(comment="AST")
        with open("test-output/round-table.gv", 'r') as archivo:
            texto = archivo.read()
            variables.graph = texto
        archivo.close()