class NodoB:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class ArbolB:
    def __init__(self, t):
        self.root = NodoB(True)
        self.t = t
        self.padre = self.cont = self.con =""

    def insertTable(self, nombre):
        self.insert(nombre)

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = NodoB()
            self.root = temp
            temp.child.insert(0, root)
            self.SepararHijos(temp, 0)
            self.InsertNoLleno(temp, k)
        else:
            self.InsertNoLleno(root, k)


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
        z = NodoB(y.leaf)
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
    def searchTable(self,table):
        for i in range(table):
            ''

    def imprimir(self, x, l=0):
        ''



def main():
    B = ArbolB(3)

    for i in range(21):
        B.insertTable(i)

    B.print_tree(B.root)


if __name__ == '__main__':
    main()












