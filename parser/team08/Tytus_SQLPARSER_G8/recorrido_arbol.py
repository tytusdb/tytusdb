class Recorrido_Arbol():
    def recorrer_arbolito(self,nodo):
        for x in nodo.hijos:
            print(nodo.hijos)
            self.recorrer_arbolito(x)
