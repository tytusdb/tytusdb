from graphviz import Digraph

class TreeGen():
    grafo = ""
    def getDot(self,node ):
        grafo += "digraph G{";
        grafo += "nodo0[label=\"";
        grafo += "root"
        grafo += "\"];\n";
        contador = 1
        RunTree("nodo0", node)
        grafo += "}"
        return grafo

    def RunTree(self, father , node):
        for elem in node:
            childsName = "node"+self.contador
            grafo+= '[label=\"'+"tipo"+"\"];\n"
            grafo+=father
            grafo+=childsName
            grafo+=";\n"