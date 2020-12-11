import os


class TreeGraph:
    def __init__(self, tree):
        self.content = ""
        self.tree = tree
        self.title = 'Arbol AVL'

    def __prepare(self):
        self.__graph(self.tree.root)

    def __graph(self, node):
        if node:
            if node.left:
                self.content = self.content + "\"" + \
                               str(node.index) + "\n" + str(node.height) + "\"" \
                                                                           " -> \"" + str(node.left.index) + "\n" + \
                               str(node.left.height) \
                               + "\" \n"
                self.__graph(node.left)
            if node.right:
                self.content = self.content + "\"" + \
                               str(node.index) + "\n" + str(node.height) + "\"" \
                                                                           " -> \"" + str(node.right.index) + "\n" + \
                               str(node.right.height) \
                               + "\" \n"
                self.__graph(node.right)
            if not node.left or not node.right:
                if node.index == self.tree.root.index:
                    self.content = self.content + "\"" + str(node.index) + "\n" + str(node.height) + "\""
                return

    def export(self):
        archivo = open('treeGraph.dot', 'w')
        archivo.write('digraph D{\n')
        archivo.write("node [shape= circle, style= filled]; \n")
        archivo.write("label= \" Grafico del " + self.title + " \" \n")

        # llenamos el content alv
        self.__prepare()

        # se agrega el content al dot
        archivo.write(self.content)

        # cerramos el archivo . dot y el de python
        archivo.write('\n}')
        archivo.close()

        # exportamos
        os.system('dot treeGraph.dot -Tpng -o treeGraph.png')
        os.system('treeGraph.png')
        print('Generado con exito')
