from Node import Node

class TablaHash:
    def __init__(self, size, db, name, nCols):
        self.Size = size-1
        self.values = list()
        self.db = db
        self.name = name
        self.nCols = nCols

        for i in range (0, size):
            self.values.append(None)

    def getSize(self):
        return self.Size

    def setSize(self, n):
        self.Size = n

    def getNodo(self):
        return self.values

    #dato sera de tipo nodo 
    def setNodo(self, nodo):
        self.values = nodo

    def funcionHash(self, dato):
        if isinstance(dato, list):
            lenDato = int(dato[0])
        else:
            lenDato = int(dato)

        return int(lenDato % self.Size)

    def sizeTabla(self):
        contadorAux = 0
        for i in self.values:
            if i is not None:
                contadorAux +=1
        return contadorAux

    def insertarDato(self, dato):

        if len(dato) <= self.nCols:
            posicion_hash = self.funcionHash(dato)
            posicion_hash =int( posicion_hash)
            bandera = self.verificarDato(dato)
            if self.values[posicion_hash] is not None:
                if bandera:
                    nuevo_dato = self.values[posicion_hash]
                    nuevo_dato.insert(dato)
            else:
                nuevo_dato = Node()
                nuevo_dato.post_in_hash = posicion_hash
                # tupla = (dato, tupla)
                nuevo_dato.insert(dato)
                self.values[posicion_hash] = nuevo_dato
                # print("dato agregado con exito")

    def verificarDato(self, dato):
        aux_bol = False
        posicion_hash = self.funcionHash(dato)
        posicion_hash = int(posicion_hash)
        if self.values[posicion_hash] is not None:
            if self.values[posicion_hash].buscarDato(dato):
                aux_bol = True
                return aux_bol
        return aux_bol

    def eliminarDato(self, dato):
        posicion_hash = self.funcionHash(dato)
        nodo_hash = self.values[posicion_hash]
        if nodo_hash.eliminar(dato):
            print("dato eliminado")
        elif nodo_hash.eliminar(dato) == 0: 
            print("dato eliminado")
            self.values[posicion_hash] = -1
        else:
            print("dato no eliminado")

    def printTbl(self):
        contador = 0
        for i in range(0,self.Size+1):
            if self.values[i] != None:
                print(str(self.values[i].post_in_hash) + " | " + str(self.values[i].array))
            contador +=1

    def buscar(self, dato):
        posicion_hash = self.funcionHash(dato)
        nodo = self.values[posicion_hash]
        return nodo.buscarDato(dato)
