from graphviz import Digraph
from Nodo import Nodo

dot = Digraph(comment='AST')

#dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
#'test-output/round-table.gv.jpg'



class AST:

  
    def __init__(self):
        self.count = 0
        print("constructor")

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
        dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
        'test-output/round-table.gv.jpg'

    

raiz = Nodo("raiz")
update = Nodo("update")
delete = Nodo("delete")

j = 0
while j < 3 :
    select = Nodo("select")
    raiz.addNode(select)
    j += 1
    i = 0
    while i < 5:
        id = Nodo("ID")
        select.addNode(id)
        i += 1


raiz.addNode(update)
raiz.addNode(delete)



ast = AST()
#raiz = Nodo("raiz")
#nod1 = Nodo("nodo1")
#nod2 = Nodo("nodo2")
#nod11 = Nodo("nodo11")
#nod12 = Nodo("nodo12")
#nod121 = Nodo("nodo121")
#raiz.addNode(nod1)
#raiz.addNode(nod2)
#nod1.addNode(nod11)
#nod1.addNode(nod12)
#nod12.addNode(nod121)
#print("lista---------------------------")
#raiz.showList()
#nod1.showList()
#print("--------------------------------")

ast.defineTreeNodes(raiz)
ast.joinTreeNodes(raiz)
ast.drawGraph()