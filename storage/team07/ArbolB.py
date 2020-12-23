class NodoB:
    def __init__(self,name,  leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []
        self.name = name
        #self.avl = alv()

class ArbolB:
    def __init__(self, t=3):
        self.t = t
        self.arreglo = []

        self.raiz = NodoB("",True)
        self.padre = self.cont = self.con =""

    def insertTable(self, nombre):
        self.ListaTablas(nombre)
        self.insert(nombre)

    def insert(self, k):
        raiz = self.raiz
        raiz.name=k
        if len(raiz.keys) == (2 * self.t) - 1:
            temp = NodoB(k)

            self.raiz = temp
            temp.child.insert(0, raiz)
            self.SepararHijos(temp, 0)
            self.InsertNoLleno(temp, k)
        else:
            self.InsertNoLleno(raiz, k)


    def InsertNoLleno(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.SepararHijos(x, i)
                if k > x.keys[i]:
                    i += 1
            self.InsertNoLleno(x.child[i], k)


    def SepararHijos(self, x, i):
        t = self.t
        y = x.child[i]
        z = NodoB("",y.leaf)

        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t]

    def print_tree(self, x, l=0):
        #print("Level ", l, " ", len(x.keys), end=":")

        for i in range(len(x.keys)):
            self.padre += str(x.keys[i])+" "

        #print(self.padre, end=" ")

        #print()
        l += 1
        if len(x.child) > 0:
            for i in range(len(x.child)):
                for j in range(len(x.child[i].keys)):
                    self.cont += str(x.child[i].keys[j])+" "
                self.con += "\""+self.padre+"\""+ "->"+ "\""+self.cont+"\""+"\n"
                self.cont=""

            for i in x.child:
                self.padre=""
                self.print_tree(i, l)
        print(self.con)


    def imprimir(self, x, l=0):
        ''

    def toASCII(self, cadena):
        cadena = str(cadena)
        resultado = 0
        for i in cadena:
            i = str(i)
            resultado += ord(i)
        return resultado
# Search key
    def SearchTable(self, ValorBusqueda, x=None):
        try:
            if x is None:
                return self.SearchTable(ValorBusqueda, self.raiz)
            else:
                posi = 0
                while posi < len(x.keys) and ValorBusqueda > x.keys[posi]:
                    posi += 1
                if posi < len(x.keys) and ValorBusqueda == x.keys[posi]:
                    return True
                elif x.leaf:
                    return False
                else:
                    return self.SearchTable(ValorBusqueda, x.child[posi])
        except:
            return False
    def SearchTable1(self, ValorNuevo,ValorBusqueda, x=None):
        try:
            if x is None:
                return self.SearchTable1(ValorNuevo,ValorBusqueda, self.raiz)
            else:
                posi = 0
                while posi < len(x.keys) and ValorBusqueda > x.keys[posi]:
                    posi += 1
                if posi < len(x.keys) and ValorBusqueda == x.keys[posi]:
                    x.keys[posi]= ValorNuevo
                    return True
                elif x.leaf:
                    return False
                else:
                    return self.SearchTable1(ValorNuevo,ValorBusqueda, x.child[posi])
        except:
            return False

    def getTable(self, ValorBusqueda, x=None):
        try:
            if x is None:
                return self.getTable(ValorBusqueda, self.raiz)
            else:
                posi = 0
                while posi < len(x.keys) and ValorBusqueda > x.keys[posi]:
                    posi += 1
                if posi < len(x.keys) and ValorBusqueda == x.keys[posi]:

                    return x
                elif x.leaf:
                    return False
                else:
                    return self.getTable(ValorBusqueda, x.child[posi])
        except:
            return False
    def updateNameTable(self, NombreNuevo, NombreViejo):
        existeTabla = self.SearchTable(NombreViejo)
        if(existeTabla):
            ''
        else:
            ''

    def getPosicion(self, valor, x=None):
        try:
            if x is None:
                return self.getPosicion(valor, self.raiz)
            else:
                posi = 0
                while posi < len(x.keys) and valor > x.keys[posi]:
                    posi += 1
                if posi < len(x.keys) and valor == x.keys[posi]:
                    return x.indice
                elif x.leaf:
                    return False
                else:
                    return self.getPosicion(valor, x.child[posi])
        except:
            return False



    def updateNameTable(self, ValorNuevo, ValorAntiguo):
        if(self.searchTable(ValorAntiguo)):
            ''


    def ListaTablas(self,nombre):
        self.arreglo.append(nombre)

    def getDataTables(self):
        return self.arreglo

def main():
    B = ArbolB(3)

    for i in range(21):
        #B.insertTable(i)
        B.insertTable("BDD" + str(i))
    #B.insertTable(10)
    #B.insertTable(20)
    #B.insertTable(21)


    #B.print_tree(B.raiz)
    print()
    print("--------------------------------------")
    #print(B.SearchTable("BaseDeDatos19"))
    #print(B.SearchTable1("Bd19","BDD19"))
    #print(B.SearchTable1("SiSePudoCrack", "BDD16"))

    #print(B.getDataTables())
    print(B.getTable("BDD16").name)



    #B.print_tree(B.raiz)

if __name__ == '__main__':
    main()












