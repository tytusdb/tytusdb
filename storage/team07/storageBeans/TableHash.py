def toASCII2(cadena):
    cadena = str(cadena)
    resultado = 0
    for i in cadena:
        i = str(i)
        resultado += ord(i)
    return resultado


class DataBase(object):

    def __init__(self, name):
        from storage.team07.storageBeans.BHash2 import BHash
        self.name = name
        self.numero = toASCII2(name)
        self.BHash = BHash()


class Hash:
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
            self.h[i] = DataBase(-1)
            i += 1
        # print(len(self.h))

    def insert(self, k):
        cadena = k
        k = self.toASCII(k)
        i = int(self.division(k))
        while (self.h[int(i)].name != -1):
            i = self.linear(i)
        self.h[int(i)] = DataBase(cadena)
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

    def search(self, database):
        k = self.toASCII(database)
        i = int(self.division(k))
        try:
            paso = i
            while (self.h[int(i)].name != database):
                i = self.linear(i)
                if (paso == i):
                    break
            if (self.h[int(i)].name == database):
                return True
            else:
                return False
        except:
            return False

    def delete(self, database):
        k = self.toASCII(database)
        i = int(self.division(k))
        paso = i
        while (self.h[int(i)].name != database):
            i = self.linear(i)
            if (paso == i):
                break
        self.h[int(i)] = DataBase(-1)  # asumiendo que antes se buscara si existe o no la base de datos
        self.n -= 1
        # self.print()
        # self.rehashingInverso()

    # def rehashingInverso(self):
    #     if ((self.n * 100 / self.m) < self.min):
    #         # copia del arreglo existente
    #         temp = self.h  # temp posee la copia del arreglo
    #         self.print()
    #         # rehashing
    #         mprev = self.m  # copia del  tamaño del vector que quedara atras
    #         ant = (mprev * self.min) / 100
    #         self.m = (ant * 100) / self.max  # nuevo tamaño del vector
    #         self.init()
    #         for i in range(int(mprev)):
    #             if (temp[int(i)].name != -1):
    #                 self.insert(temp[int(i)].name)
    #             i += 1
    #     else:
    #         self.print()

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

    def updateName(self, newName, OldName):
        if (self.search(OldName)):  # si la base de datos existe
            k = self.toASCII(OldName)
            i = int(self.division(k))
            paso = i
            while (self.h[int(i)].name != OldName):
                i = self.linear(i)
                if (paso == i):
                    break
            self.h[int(i)].name = newName  # asumiendo que antes se buscara si existe o no la base de datos
            # self.print()
            return True
        else:  # significa que la base de datos no existe
            return False

    def getData(self):
        lista = []
        for i in range(len(self.h)):
            if self.h[i].name != -1:
                lista.append(self.h[i].name)
        return lista

    def getData2(self):
        lista = []
        for i in range(len(self.h)):
            lista.append(self.h[i])
        return lista

    def getDataBase(self, OldName):
        if (self.search(OldName)):  # si la base de datos existe
            k = self.toASCII(OldName)
            i = int(self.division(k))
            paso = i
            while (self.h[int(i)].name != OldName):
                i = self.linear(i)
                if (paso == i):
                    break
            return self.h[int(i)]  # asumiendo que antes se buscara si existe o no la base de datos
        else:  # significa que la base de datos no existe
            return False
