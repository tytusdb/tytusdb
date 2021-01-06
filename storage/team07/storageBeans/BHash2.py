def toASCII2(cadena):
    cadena = str(cadena)
    resultado = 0
    for i in cadena:
        i = str(i)
        resultado += ord(i)
    return resultado


class Tabla(object):
    def __init__(self, name, noColumnas):
        from storage.team07.storageBeans.AVLtree import arbolAVL
        self.name = name
        self.numero = toASCII2(name)
        self.AVLtree = arbolAVL(noColumnas)  # datos de tabla


class BHash:
    def __init__(self):
        self.m = 5  # tamaño del vector de posiciones
        self.min = 20  # porcentaje minimo a ocupar
        self.max = 80  # porcentaje maximo a ocupar
        self.n = 0  # numero de elementos
        self.h = []  # vector de posiciones
        self.init()

    def division(self, k):
        return int(k % self.m)

    def linear(self, k):
        return ((k + 1) % self.m)

    def init(self):
        self.n = 0
        self.h = []
        for i in range(int(self.m)):
            self.h.append(None)
        for i in range(int(self.m)):
            self.h[i] = Tabla(-1, -1)
            i += 1
        # print(len(self.h))

    def insertTable(self, k, noColumnas):
        cadena = k
        k = self.toASCII(k)
        i = int(self.division(k))
        while (self.h[int(i)].name != -1):
            i = self.linear(i)
        self.h[int(i)] = Tabla(cadena, noColumnas)
        self.n += 1
        self.rehashing()

    def rehashing(self):
        if ((self.n * 100 / self.m) >= self.max):
            # copia del arreglo existente
            temp = self.h  # temp posee la copia del arreglo
            # self.print()
            # rehashing
            mprev = self.m  # copia del  tamaño del vector que quedara atras
            self.m = self.n * 100 / self.min  # nuevo tamaño del vector
            self.init()
            for i in range(int(mprev)):
                if (temp[i].name != -1):
                    self.insert(temp[i].name)
                i += 1
        else:
            pass
            # self.print()

    def searchTable(self, table):
        k = self.toASCII(table)
        i = int(self.division(k))
        try:
            paso = i
            while (self.h[int(i)].name != table):
                i = self.linear(i)
                if (paso == i):
                    break
            if (self.h[int(i)].name == table):
                return True
            else:
                return False
        except:
            return False

    def deleteTable(self, table):
        k = self.toASCII(table)
        i = int(self.division(k))
        paso = i
        while (self.h[int(i)].name != table):
            i = self.linear(i)
            if (paso == i):
                break
        self.h[int(i)] = Tabla(-1, -1)  # asumiendo que antes se buscara si existe o no la tabla
        self.n -= 1
        # self.print()
        # self.rehashingInverso()

    def print(self):
        cadena = ""
        cadena += "["
        for i in range(int(self.m)):
            cadena += " " + str(self.h[i].name)
            i += 1
        cadena += " ] " + str((self.n * 100 / self.m)) + "%"
        print(cadena)

    def toASCII(self, cadena):
        cadena = str(cadena)
        resultado = 0
        for i in cadena:
            i = str(i)
            resultado += ord(i)
        return resultado

    def updateNameTable(self, newName, OldName):
        if (self.searchTable(OldName)):  # si la tabla existe
            k = self.toASCII(OldName)
            i = int(self.division(k))
            paso = i
            while (self.h[int(i)].name != OldName):
                i = self.linear(i)
                if (paso == i):
                    break
            self.h[int(i)].name = newName  # asumiendo que antes se buscara si existe o no la tabla
            # self.print()
            return True
        else:  # significa que la tabla no existe
            return False

    def getDataTables(self):
        lista = []
        for i in range(len(self.h)):
            if self.h[i].name != -1:
                lista.append(self.h[i].name)
        return lista

    def getDataTables2(self):
        lista = []
        for i in range(len(self.h)):
            lista.append(self.h[i])  # retorno  el objeto tabla
        return lista

    def getTable(self, OldName):
        if (self.searchTable(OldName)):  # si la tabla existe
            k = self.toASCII(OldName)
            i = int(self.division(k))
            paso = i
            while (self.h[int(i)].name != OldName):
                i = self.linear(i)
                if (paso == i):
                    break
            return self.h[int(i)]  # asumiendo que antes se buscara si existe o no la tabla
        else:  # significa que la tabla no existe
            return False
