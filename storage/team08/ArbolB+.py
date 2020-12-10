
class Nodo:

    #constructor
    def __init__(self, orden):
        self.orden = orden
        self.cuenta = 0
        self.siguiente = None
        self.claves = []
        self.hijos = []
        self.padre = None

    def nuevoNodo(self, claves, hijos, padre):
        self.claves = claves
        self.hijos = hijos
        self.padre = padre
        self.cuenta = len(claves)
    
    def addHijo(self, hijo):
        self.hijos.append(hijo)
        self.hijos = sorted(self.hijos ,key=lambda x: x.claves)

    def nodoLLeno(self):
        return self.cuenta >= self.orden

    def esHoja(self):
        return len(self.hijos)==0

    def nodoSemiVacio(self):
        return self.cuenta <= self.orden/2
    
    def addClave(self, clave):
        self.claves.append(clave)
        self.cuenta += 1
        self.claves.sort()

    def buscar(self, clave):
        if len(self.hijos)==0:
            return self
        return self.__buscar(0 , clave)

    def __buscar(self, valor, clave):
        if valor == len(self.claves):
            return self.hijos[valor].buscar(clave)

        if clave >= self.claves[valor]:
            return self.__buscar(valor+1,clave)

        return self.hijos[valor].buscar(clave)

    def buscarHijo(self, clave):
        return self.__buscarHijo(0, clave)
    
    def __buscarHijo(self, valor,clave):
        if valor == len(self.claves):
            return len(self.hijos)-1

        if clave > self.claves[valor]:
            return self.__buscarHijo(valor+1,clave)

        return valor

class Arbol:

    def __init__(self, orden):
        self.orden = orden
        self.raiz = None
        self.gr = None

#*************** INSERTAR **********************************************************
    def insertar(self, clave):
        self.raiz = self.__insertar(self.raiz, clave)

    def __insertar(self, raiz, clave):
        if self.raiz == None:
            raiz = Nodo(self.orden)
            raiz.nuevoNodo([clave], [], None)
            return raiz
        else:
            n = raiz.buscarHijo(clave)
            if raiz.esHoja():
                raiz.addClave(clave)
            else:
                raiz = raiz.hijos[n]
            if raiz.nodoLLeno():
                raiz = self.__split(raiz,n)
        return raiz

    def __split(self, raiz, n):
        if raiz.esHoja():
            return self.__splitHoja(raiz, n)
        return raiz

    def __splitHoja(self, raiz, n):
        #Se crea nuevo nodo y se separan las claves
        m = int(self.orden/2)
        nodo = Nodo(self.orden)
        nodo.siguiente = raiz.siguiente
        raiz.siguiente = nodo
        nodo.claves = raiz.claves[m:]
        raiz.claves = raiz.claves[0:m]
        
        if raiz.padre == None:
            #Si el nodo padre es nulo se crea nuevo padre
            padre = Nodo(self.orden)

        else:
            pass
        return raiz

    def buscar(self, clave):
        return self.raiz.buscar(clave)

