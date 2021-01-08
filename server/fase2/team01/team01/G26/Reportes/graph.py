import sys
sys.path.append('../team01/G26/Reportes')

from graphviz import Graph

class Grafo():

    def __init__(self, index):
        self.index = index
        self.dot = Graph()
        self.dot.attr(splines='false')
        self.dot.node_attr.update(shape = 'circle')
        self.dot.edge_attr.update(color = 'blue4')

    def newnode(self, label):
        self.index += 1
        self.dot.node(str(self.index), str(label))

    def newchildrenE(self, label):
        self.dot.node(str(self.index)+'_'+str(label), str(label))
        self.dot.edge(str(self.index), str(self.index)+'_'+str(label))
    
    def newchildrenF(self, father, son):
        self.dot.edge(str(father), str(son))

    def showtree(self):
        self.dot.view()