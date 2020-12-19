import abc

#id estatico para que cada nodo tenga un id unico al graficar
id_arbol = 1

def asign_id_arbol():
    global id_arbol
    temp_id = str(id_arbol)
    id_arbol += 1
    return temp_id

def reset_id_arbol():
    global id_arbol
    id_arbol = 1

class Nodo(metaclass=abc.ABCMeta):

    def __init__(self, fila = 0, columna = 0):
        self.fila = fila
        self.columna = columna
        self.mi_id = asign_id_arbol()

    @abc.abstractmethod
    def ejecutar(self,TS,Errores):
        pass
    @abc.abstractmethod
    def getC3D(self,TS):
        pass
    
    def graficarasc(self,padre,grafica):
        grafica.node(self.mi_id, self.__class__.__name__)
        grafica.edge(padre, self.mi_id)
