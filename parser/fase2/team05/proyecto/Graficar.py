from graphviz import Digraph


class Graficar:
    def __init__(self):
        self.dot = Digraph(name="AST")
        self.dot.node_attr['shape'] = 'record'
        self.indice = 0

    def graficar_arbol(self, raiz):
        if raiz is not None:
            self.graficar_nodos(raiz)
            self.indice = 0
            self.relacionar_nodos(raiz)
            self.dot.render('reports/arbolAst', view=True)

    def graficar_nodos(self, raiz):
        if (raiz is None):
            return
        self.dot.node('node' + str(self.indice), raiz.getContenido())
        self.incrementar()
        for hijos in raiz.getHijos():
            self.graficar_nodos(hijos)

    def incrementar(self):
        self.indice = self.indice + 1;

    def set_indice(self, indice):
        self.indice = indice

    def relacionar_nodos(self, raiz):
        if (raiz is None):
            return
        indice_padre = self.indice
        for hijo in raiz.getHijos():
            self.incrementar()
            self.dot.edge('node' + str(indice_padre), 'node' + str(self.indice))
            self.relacionar_nodos(hijo)
