# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


import os


class AVLGraph:

    def __init__(self, tree):
        self.content = ""
        self.tree = tree
        self.title = tree.name

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
        fname = '_tmp_/grafo-avl'
        archivo = open(fname + '.dot', 'w')
        archivo.write('digraph D{\ngraph[bgcolor="#0f1319"]\n')
        archivo.write(
            'node [shape= circle, style= filled, fontname="Century Gothic", color="#006400", fillcolor="#90EE90"]; \n')
        archivo.write('edge[color="#145A32"]')
        archivo.write(
            "label= <<font color=\"white\">\"  AVL de '" + self.title + "' \" </font>> fontname=\"Century Gothic\" \n")

        self.__prepare()

        archivo.write(self.content)
        archivo.write('\n}')
        archivo.close()

        os.system('dot ' + fname + '.dot' + ' -Tpng -o ' + fname + '.png')
        os.remove(fname + '.dot')
