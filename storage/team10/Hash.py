from Node import Node

class TablaHash:
    def __init__(self, size, name, nCols):
        self.id = 0
        self.Size = size-1
        self.name = name
        self.nCols = nCols
        self.genericId = 0
        self.pk = None
        self.diccionario = {}
        self.values = [None]*self.Size

    def getName(self):
        return self.name

    def getSize(self):
        return self.Size

    def setSize(self, n):
        self.Size = n

    def getNodo(self):
        return self.values

    #dato sera de tipo nodo 
    def setNodo(self, nodo):
        self.values = nodo

    def alterAddPK(self, indices):
        self.pk = indices
    
    def toASCII(self, cadena):
        result = ""
        for char in cadena:
            result += str(ord(char))
        return int(result)


    def funcionHash(self, dato, flag = False):
        if isinstance(dato, list):
            lenDato = 0
            res = ""
            if flag:
                for key in self.pk:
                    res = str(dato[key]) + "," + res
            else:
                for key in dato:
                    res = str(key) + "," + res
            lenDato = self.toASCII(res)
        else:
            if str(dato).isalnum():
                lenDato = self.toASCII(str(dato))
            else:
                lenDato = int(dato)
        return (int(lenDato % self.Size),lenDato)

    def sizeTabla(self):
        contadorAux = 0
        for i in self.values:
            if i is not None:
                contadorAux +=1
        return contadorAux   

   
    def insertIntoArray(self, dato, posicion_hash, key):
        bandera = self.verificarDato(key, posicion_hash)
        if self.values[posicion_hash] is not None:
            if bandera:
                nuevo_dato = self.values[posicion_hash]
                nuevo_dato.insert(dato, key)
                return 0
        else:
            nuevo_dato = Node()
            nuevo_dato.pk = self.pk
            nuevo_dato.insert(dato,key)
            self.values[posicion_hash] = nuevo_dato
            return 0

    def insert(self, table, dato):
        self.rehashing()
        if isinstance(dato, list):
            if len(dato) == self.nCols:
                if self.pk:
                    posicion_hash = self.funcionHash(dato, True)
                    self.insertIntoArray(dato, posicion_hash[0], posicion_hash[1]) #aqui manda las dos llaves
                else:
                    posicion_hash = int(self.genericId % self.Size)
                    self.insertIntoArray(dato, posicion_hash , [self.genericId] )
                    self.genericId += 1
            else:
                return 2
        else:
            return 1

    def eliminarDato(self, dato):
        posicion_hash = self.funcionHash(dato)
        nodo_hash = self.values[posicion_hash]
        if nodo_hash is not None:
            if nodo_hash.eliminar(dato):
                print("dato eliminado")
            elif nodo_hash.eliminar(dato) == 0: 
                print("dato eliminado")
                self.values[posicion_hash] = None
            else:
                print("dato no eliminado")
        else:
            print("el dato no existe")

    def truncate(self):
        try:
            self.values.clear()
            return 1
        except:
            return 0

    def editar(self, columna, modificacion, key):
        posicion_hash = self.funcionHash(key)
        nodo = self.values[posicion_hash]
        if nodo:
            respuesta = nodo.modificar(columna,modificacion,posicion_hash)
            if respuesta == 0:
                print("dato modificado exitosamente")
            elif respuesta == 4:
                print("llave no existente")
            else:
                print("error de indice")
        else:
            print("Error de llave")

    def ElementosEn_tbl(self):
        auxiliar = 0 
        for nodo in self.values:
            if nodo is not None:
                auxiliar +=1
        return auxiliar

     def rehashing(self):
        actualSize = self.ElementosEn_tbl()
        factorAgregado = int(self.Size * 0.75)
        if actualSize >= factorAgregado:
            #estoy_en_rehashing = True
            self.setSize( int(self.Size*3.75))
            arrayAuxiliar = self.values[:]
            self.values.clear()
            self.values = [None]*self.Size
            lista = [tupla for nodo in arrayAuxiliar if nodo is not None for tupla in nodo.array]
            for j in lista:
                self.insert(self.name, j[1])
            arrayAuxiliar.clear()
            return "El rehashing fue realizado con exito"

    def verificarDato(self, dato, position):
        aux_bol = False
        if self.values[position] is not None:
            if not self.values[position].buscarDato_binary(dato):
                aux_bol = True
        return aux_bol

    def eliminarDato(self, dato):
        posicion_hash = self.funcionHash(dato)
        nodo_hash = self.values[posicion_hash[0]]
        if nodo_hash.eliminar(posicion_hash[1]):
            return "dato eliminado"
        elif nodo_hash.eliminar(posicion_hash[1]) == 0: 
            return "dato eliminado"
            self.values[posicion_hash] = None
        else:
            return "dato no eliminado"

    def printTbl(self):
        if self.values:
            for i in self.values:
                if i :
                    print(str(i.pk) + " | " + str(i.array)) 
        else:
            print("vacio")

    def buscar(self, dato):
        posicion_hash = self.funcionHash(dato)
        nodo = self.values[posicion_hash[0]]
        if nodo is not None:
            return nodo.busquedaB(posicion_hash[1])
        else:
            return None

    def printlistTbl(self):
        listTbl=[]
        if self.values:
            for i in self.values:
                if i :
                    new = str(i.pk) + " | " + str(i.array).replace('[','')
                    new2 = new.replace(']','')
                    listTbl.append(new2)            
        else:
            print("vacio")        
        return listTbl

    def imp1(self,columnNumber,lower,upper):
        listCol=[]
        for nodo in self.values:
            if nodo is not None:
                val = nodo.imp_column(columnNumber,lower,upper)
                if val != None:
                    listCol.append(val)   
        return listCol   
    
    # agrega la nueva columna y asigna el valor
    def alterAddColumn(self, dato):
        self.nCols += 1
        for i in self.values:
                if i :
                    i.alterAddColumn(dato)
                   
  
    def getNumeroColumnas(self):
        return self.nCols
