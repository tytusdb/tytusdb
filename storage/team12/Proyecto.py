class NodoArbol:
    
    def __init__(self, ValorI = -1, AnteriorI = None):
        self.Valores = []
        self.Hijos = []
        self.Anterior = None
        if ValorI==-1 and AnteriorI == None:
            for i in range(4):
                if i!=3:
                    self.Valores.append(-1)
                self.Hijos.append(None)
            self.Anterior = None
        elif ValorI!=-1 and AnteriorI == None:
            for i in range(4):
                if i!=3:
                    self.Valores.append(-1)
                self.Hijos.append(None)
            self.Valores[0] = ValorI
            self.Anterior = None
        elif ValorI!=-1 and AnteriorI != None:
            for i in range(4):
                if i!=3:
                    self.Valores.append(-1)
                self.Hijos.append(None)
            self.Valores[0] = ValorI
            self.Anterior = AnteriorI

class Arbol:

    Raiz = None

    def __init__(self):
        self.Raiz = None
    
    def Mostrar2(self, Actual):
        print("[",end="")
        for i in range(3):
            if Actual.Hijos[i] != None:
                self.Mostrar2(Actual.Hijos[i])
            if Actual.Valores[i] != -1:
                if i!=0:
                    print(",",end="")
                print(Actual.Valores[i],end="")
        if Actual.Hijos[3] != None:
            self.Mostrar2(Actual.Hijos[2])
        print("]",end="")

    def Mostrar(self):
        self.Mostrar2(self.Raiz)
        print("\n")

    def InsertarArriba(self, Actual):
        Anterior = Actual.Anterior
        if Anterior == None:
            Anterior = NodoArbol(Actual.Valores[1])
            Hijo0 = NodoArbol(Actual.Valores[0], Anterior)
            Hijo0.Hijos[0] = Actual.Hijos[0]
            Hijo0.Hijos[1] = Actual.Hijos[1]
            if Hijo0.Hijos[0] != None:
                Hijo0.Hijos[0].Anterior = Hijo0
            if Hijo0.Hijos[1] != None:
                Hijo0.Hijos[1].Anterior = Hijo0
            Hijo1 = NodoArbol(Actual.Valores[2], Anterior)
            Hijo1.Hijos[0] = Actual.Hijos[2]
            Hijo1.Hijos[1] = Actual.Hijos[3]
            if Hijo1.Hijos[0] != None:
                Hijo1.Hijos[0].Anterior = Hijo1
            if Hijo1.Hijos[1] != None:
                Hijo1.Hijos[1].Anterior = Hijo1
            Anterior.Hijos[0] = Hijo0
            Anterior.Hijos[1] = Hijo1
            self.Raiz = Anterior
        else:
            Auxiliar = Anterior.Hijos
            Aux = Anterior.Valores
            i = 0
            while Auxiliar[i] != Actual:
                i=i+1
            j = 3
            while (j>i):
                if j!=3:
                    Aux[j] = Aux[j-1]
                Auxiliar[j] = Auxiliar[j-1]
                j = j - 1
                
            Aux[i] = Actual.Valores[1]
            Hijo0 = NodoArbol(Actual.Valores[0], Anterior)
            Hijo0.Hijos[0] = Actual.Hijos[0]
            Hijo0.Hijos[1] = Actual.Hijos[1]
            if Hijo0.Hijos[0] != None:
                Hijo0.Hijos[0].Anterior = Hijo0
            if Hijo0.Hijos[1] != None:
                Hijo0.Hijos[1].Anterior = Hijo0
            Hijo1 = NodoArbol(Actual.Valores[2], Anterior)
            Hijo1.Hijos[0] = Actual.Hijos[2]
            Hijo1.Hijos[1] = Actual.Hijos[3]
            if Hijo1.Hijos[0] != None:
                Hijo1.Hijos[0].Anterior = Hijo1
            if Hijo1.Hijos[1] != None:
                Hijo1.Hijos[1].Anterior = Hijo1
            Anterior.Hijos[i] = Hijo0
            Anterior.Hijos[i+1] = Hijo1
            if(Aux[2] != -1):
                self.InsertarArriba(Anterior)

    def InsertarEnNodo(self, Actual, Nuevo):
        Aux = Actual.Valores
        if Aux[0] == -1:
            Aux[0] = Nuevo
        elif Aux[1] == -1:
            if Nuevo < Aux[0]:
                Aux[1] = Aux[0]
                Aux[0] = Nuevo
            else:
                Aux[1] = Nuevo
        else:
            if Nuevo < Aux[0]:
                Aux[2] = Aux[1]
                Aux[1] = Aux[0]
                Aux[0] = Nuevo
            elif Nuevo < Aux[1]:
                Aux[2] = Aux[1]
                Aux[1] = Nuevo
            else:
                Aux[2] = Nuevo
            self.InsertarArriba(Actual)

    def BuscarInsercion(self, Actual, Nuevo):
        Auxiliar = Actual.Hijos
        if Auxiliar[0] == None:
            self.InsertarEnNodo(Actual, Nuevo)
        else:
            Aux = Actual.Valores
            if Nuevo < Aux[0]:
                self.BuscarInsercion(Auxiliar[0], Nuevo)
            elif Aux[1] != -1 and Aux[1] < Nuevo:
                self.BuscarInsercion(Auxiliar[2], Nuevo)
            else:
                self.BuscarInsercion(Auxiliar[1], Nuevo)

    def Insertar(self, Nuevo):
        if self.Raiz == None :
            self.Raiz = NodoArbol(Nuevo)
        else:
            self.BuscarInsercion(self.Raiz, Nuevo)
        self.Mostrar()

Prueba = Arbol()
Prueba.Insertar(5)
Prueba.Insertar(10)
Prueba.Insertar(15)
Prueba.Insertar(20)
Prueba.Insertar(21)
Prueba.Insertar(22)
Prueba.Insertar(23)
Prueba.Insertar(24)
Prueba.Insertar(25)
Prueba.Insertar(26)
Prueba.Insertar(27)
Prueba.Insertar(4)
Prueba.Insertar(3)
Prueba.Insertar(2)
Prueba.Insertar(1)