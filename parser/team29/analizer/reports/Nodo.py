class Nodo:
    def __init__(self, val):
        self.val_ = val
        self.lista_ = []

    def getId(self):
        return self.id_

    def getVal(self):
        return self.val_

    def setId(self, id):
        self.id_ = id

    def setVal(self, val):
        self.val_ = val

    def getLista(self):
        return self.lista_

    def setLista(self, lista):
        self.lista_ = lista

    def addNode(self, nodo):
        self.getLista().append(nodo)

    def showList(self):
        print(self.val_)
        for n in self.getLista():
            print(n.getVal())
