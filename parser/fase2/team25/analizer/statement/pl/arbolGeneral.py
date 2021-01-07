from analizer.reports.Nodo import Nodo


class ArbolGeneral():
    def __init__(self, sentencias):
        self.sentencias = sentencias
    
    def dot(self):
        cabeza = Nodo("RAIZ")
        for sentencia in self.sentencias:
            cabeza.addNode(sentencia.dot())
        return cabeza