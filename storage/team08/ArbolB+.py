
class Nodo:

    #constructor
    def __init__(self, orden, hoja):
        self.orden = orden
        self.hoja = hoja
        self.cuenta = 0
        self.siguiente = None
        self.claves = []
        self.hijos = []
        self.padre = None
    
    def addHijo(self, hijo):
        self.hijos.append(hijo)
        self.hijos = sorted(self.hijos ,key=lambda x: x.claves)

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
        if valor < len(self.claves):
            if clave >= self.claves[valor]:
                return self.__buscarHijo(valor+1,clave)
            return valor
        return valor

    def acutalizarPadre(self):
        for i in self.hijos:
            i.padre = self

class Arbol:

    def __init__(self, orden):
        self.orden = orden
        self.raiz = None
        self.gr = None

    def buscar(self, clave):
        return self.raiz.buscar(clave)

    #*************** INSERTAR **********************************************************
    def insertar(self, clave):
        self.raiz = self.__insertar(self.raiz, clave)

    def __insertar(self, raiz, clave):
        if self.raiz == None:
            raiz = Nodo(self.orden, True)
            raiz.addClave(clave)
        else:
            if raiz.hoja:
                raiz.addClave(clave)
            else:
                n = raiz.buscarHijo(clave)
                raiz.hijos[n] = self.__insertar(raiz.hijos[n],clave)
            if raiz.nodoLLeno():
                raiz = self.__split(raiz)
        return raiz

    #*************** SPLIT ************************************************************
    
    def __split(self, raiz):
        if raiz.hoja:
            return self.__splitHoja(raiz, int(self.orden/2)) #Es Hoja
        return self.__splitRama(raiz, int(self.orden/2)) #Es Rama

    def __splitHoja(self, raiz, n):
        #Crear Nodo Hoja
        nodo = Nodo(self.orden, True)
        #Separar Claves
        nodo.claves = raiz.claves[n:]
        raiz.claves = raiz.claves[0:n]
        #Actualizar Cuentas
        nodo.cuenta = len(nodo.claves)
        raiz.cuenta = len(raiz.claves)
        #Actualizar Siguientes
        nodo.siguiente = raiz.siguiente
        raiz.siguiente = nodo

        if raiz.padre == None:
            #Crear Padre no es Hoja
            padre = Nodo(self.orden, False)
            #Agregar clave e hijos
            padre.addClave(nodo.claves[0])
            padre.hijos = [raiz, nodo]
            #Actualizar padres de la separacion
            nodo.padre = raiz.padre = padre
            return padre
        else:
            #Agregar clave y nodo nuevo al padre
            raiz.padre.addClave(nodo.claves[0])
            raiz.padre.addHijo(nodo)
            #Actualizar padre
            nodo.padre = raiz.padre
        return raiz
    
    def __splitRama(self, raiz, n):
        #Crear nueva Rama
        nodo = Nodo(self.orden, False)
        #Separar Claves
        nodo.claves = raiz.claves[n:]
        raiz.claves = raiz.claves[0:n]
        #Actualizar Cuentas
        nodo.cuenta = len(nodo.claves)-1
        raiz.cuenta = len(raiz.claves)
        #Repartir hijos y actualizar padres
        nodo.hijos = raiz.hijos[n+1:]
        nodo.acutalizarPadre()
        raiz.hijos = raiz.hijos[0:n+1]

        if raiz.padre == None:
            #Crear Padre no es Hoja
            padre = Nodo(self.orden, False)
            #Agregar clave e hijos
            padre.addClave(nodo.claves.pop(0))
            padre.hijos = [raiz, nodo]
            #Actualizar padres de la separacion
            nodo.padre = raiz.padre = padre
            return padre
        else:
            #Agregar clave y nodo nuevo al padre
            raiz.padre.addClave(nodo.claves.pop(0))
            raiz.padre.addHijo(nodo)
            #Actualizar padre
            nodo.padre = raiz.padre
            
        return raiz

