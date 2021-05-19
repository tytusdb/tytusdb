from  Fase1.analizer.reports import Nodo
from  Fase1.storage.storageManager import storage
from  Fase1.analizer.abstract.instruction import Instruction


class showDataBases(Instruction):
    def __init__(self, like, row, column):
        Instruction.__init__(self, row, column)
        if like != None:
            self.like = like[1 : len(like) - 1]
        else:
            self.like = None

    def execute(self, environment):
        lista = []
        if self.like != None:
            shows = storage.showDatabases()
            for l in shows[0]:
                if self.like in l:
                    lista.append(l)
        else:
            lista = storage.showDatabases()
            lista = lista[0]
        if len(lista) == 0:
            return "No hay bases de datos"
        return lista

    def dot(self):
        new = Nodo.Nodo("SHOW_DATABASES")
        if self.like != None:
            l = Nodo.Nodo("LIKE")
            ls = Nodo.Nodo(self.like)
            new.addNode(l)
            l.addNode(ls)

        return new
