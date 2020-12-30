class graficas:
    contador: 0
    grafo: ""

    def getDOT(self, raiz):
        self.grafo = ""
        self.contador = 0
        self.grafo = "digraph G{"
        self.grafo += "nodo0[label=\"" + raiz.nombre + "\"];\n"
        self.contador = 1
        self.recorrerAST("nodo0", raiz)
        self.grafo += "}"
        return self.grafo

    def recorrerAST(self, padre, hijos):
        if hijos != None:
            if hijos.hijos != None:
                a = hijos.hijos.len()
                for  x in hijos.hijos:
                    nombreHijo = "nodo" + self.contador
                    self.grafo += nombreHijo + "[label=\"" + x.nombre + "\"];\n"
                    self.grafo += padre + "->" + nombreHijo + ";\n"
                    self.contador = self.contador+1
                    self.recorrerAST(nombreHijo, x)