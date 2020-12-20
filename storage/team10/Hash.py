from Node import Node

class TablaHash:
    def __init__(self, size, name, nCols):
        self.id = 0
        self.Size = size-1
        self.name = name
        self.nCols = nCols
        self.genericId = -1
        self.pk = None
        self.values = [None]*self.Size

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

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
        for i in indices:
            if i not in range(0, self.nCols):
                return 5

        if len(indices) <= self.nCols:
            if not self.pk:
                self.pk = indices
                return 0
            else:
                # print("No se puede poner otra PK")
                return 4
        else:
            return 5
    
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
                    res += str(dato[key]) + ","
            else:
                for key in dato:
                    res += str(key) + ","
            lenDato = self.toASCII(res)
        else:
            if str(dato).isalnum():
                lenDato = self.toASCII(str(dato))
            else:
                lenDato = int(dato)
        return (int(lenDato % self.Size),lenDato) #cambie aqui para poder obtener la posicion en el arreglo (posicion hash, posicion en arreglo)

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
                return 4
        else:
            nuevo_dato = Node()
            if self.pk:
                nuevo_dato.pk = self.pk
            else:
                nuevo_dato.pk = self.genericId
                nuevo_dato.isGeneric = True
            nuevo_dato.insert(dato,key)
            nuevo_dato.key = posicion_hash
            self.values[posicion_hash] = nuevo_dato
            return 0

    def insert(self, table, dato):
        self.rehashing()
        if isinstance(dato, list):
            if len(dato) == self.nCols:
                if self.pk:

                    # Recorre las anteriores buscando su llave primaria
                    for node in self.values:
                        if node is not None and node.isGeneric:
                            node.isGeneric = False
                            self.recalculateKey(node)
                            continue

                    posicion_hash = self.funcionHash(dato, True)
                    return self.insertIntoArray(dato, posicion_hash[0], posicion_hash[1]) #aqui manda las dos llaves
                else:
                    posicion_hash = int(self.genericId % self.Size)
                    self.genericId += 1
                    return self.insertIntoArray(dato, posicion_hash, self.genericId)
            else:
                return 5
        else:
            return 1

    def recalculateKey(self, node):
        for dato in node.array:
            posicion_hash = self.funcionHash(dato[1], True)
            index = node.key
            self.values[index] = None
            self.insertIntoArray(dato[1], posicion_hash[0], posicion_hash[1])

    def truncate(self):
        try:
            self.values.clear()
            return 1
        except:
            return 0

    def editar(self, columna, modificacion, key):
        posicion_hash = self.funcionHash(key)
        nodo = self.values[posicion_hash[0]]
        if nodo:
            if columna not in self.pk:
                respuesta = nodo.modificar(columna,modificacion,posicion_hash[1])
            else: 
                return 1
            if respuesta == 0:
                return "dato modificado exitosamente"
            elif respuesta == 4:
                return "llave no existente"
            else:
                return "error de indice"
        else:
            return "Error de llave"

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

    def verificarDato(self, key, position):
        aux_bol = False
        if self.values[position] is not None:
            if not self.values[position].buscarDato_binary(key):
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
                if i and (len(i.array) > 0):
                    print(str(i.key) + " | " + str(i.array) + "\n")
        else:
            return "vacio"

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

    #19/12/2020
    def getNumeroColumnas(self):
        return self.nCols

    def alterDropColumn(self, columnNumber):
        if columnNumber in range(0, self.nCols):
            for i in self.values:
                if i:
                    for j in i.array:
                        j[1].pop(columnNumber)
                pass

        newKeys = []
        for key in self.pk:
            if (columnNumber == (key-1)) and (key is not 0):
                key -= 1
            newKeys.append(key)
        self.pk = None
        self.alterAddPK(newKeys)
        self.nCols -= 1

    def alterDropPK(self):
        self.pk = None
    def genGraph(self, name):
        f = Digraph("structs" , filename = name+".gv" , format = "png",
                    node_attr={'shape' : 'record', } )
        f.attr(rankdir='LR', size='8,5')
        hashTB = ''
        contador = 0 
        for i in self.values:
            if i:
                hashTB += '<f' + str(contador) +'>' + str(i.key)+ '|'
                contador +=1
        hashTB = hashTB[0: len(hashTB)-1]
        f.node('hash', hashTB)

        datos = "{<n>"
        
        for j in self.values:
            count = 0
            if j:
                for i in j.array:
                    for k in i[1]:
                        datos +=    str(k) +"|"
                    datos+="<p>}"
                    with f.subgraph(name=str(j.key)+","+str(count) ) as a:
                        a.node("node" +str(j.key)+str(count),datos)
                        datos="{<n>"
                    count +=1
        n = 0
        for j in self.values:
            m = 0
            if j:
                f.edges([("hash:f"+str(n), "node" +str(j.key)+str(0)+":n")])
                for i in j.array:
                    if m+1 < len(j.array):
                        f.edges([("node" +str(j.key)+str(m)+":p", ("node"+str(j.key)+str(m+1)+":n" ))])
                        m+=1 
                n+=1
        f.view()
