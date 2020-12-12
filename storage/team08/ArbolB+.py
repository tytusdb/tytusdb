
class Nodo:

    #constructor
    def __init__(self, orden):
        self.orden = orden
        self.cuenta = 0
        self.siguiente = None
        self.claves = []
        self.hijos = []
        self.padre = None
        

    def nodoLLeno(self):
        return self.cuenta >= self.orden

    def nodoSemiVacio(self):
        return self.cuenta <= self.orden/2
    
    def addClave(self, clave):
        self.claves.append(clave)
        self.cuenta += 1
        self.claves.sort()

    def buscar(self, clave):
        if len(self.hijos)==0:
            return self
        return self.__buscar(0 ,clave)

    def __buscar(self, valor, clave):
        if valor == len(self.claves):
            return self.hijos[valor].buscar(clave)

        if clave >= self.claves[valor]:
            return self.__buscar(valor+1,clave)

        return self.hijos[valor].buscar(clave)



class Arbol:

    def __init__(self, orden):
        self.orden = orden
        self.raiz = None
        self.gr = None

    def buscar(self, clave):
        return self.raiz.buscar(clave)
  
