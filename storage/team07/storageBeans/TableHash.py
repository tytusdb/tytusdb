class Hash:
    def __init__(self):
        self.m = 5     # cantidad de posiciones iniciales
        self.min = 20   # porcentaje minimo a ocupar
        self.max = 80   # porcentaje maximo a ocupar
        self.n = 0
        self.h = []
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
            self.h[i] = -1
            i += 1

    def insert(self, k):
        i = int(self.division(k))
        while (self.h[int(i)] != -1):
            i = self.linear(i)
        self.h[int(i)] = k
        self.n += 1
        self.rehashing()

    def rehashing(self):
        if ((self.n * 100 / self.m) >= self.max):
            # array copy
            temp = self.h
            self.print()
            # rehashing
            mprev = self.m
            self.m = self.n * 100 / self.min
            self.init()
            for i in range(int(mprev)):
                if (temp[i] != -1):
                    self.insert(temp[i])
                i += 1
        else:
            self.print()

    def print(self):
        cadena = ""
        cadena += "["
        for i in range(int(self.m)):
            cadena += " " + str(self.h[i])
            i += 1
        cadena += " ] " + str((self.n * 100 / self.m)) + "%"
        print(cadena)

t = Hash()
t.insert(5)
t.insert(10)
t.insert(15)
t.insert(20)
t.insert(25)
t.insert(30)
t.insert(35)
t.insert(40)
t.insert(45)
t.insert(50)
t.insert(55)
t.insert(60)
t.insert(65)
t.insert(70)
t.insert(75)
t.insert(80)