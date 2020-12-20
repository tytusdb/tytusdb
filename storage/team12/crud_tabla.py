class NodoArbol:
    
    def __init__(self, ValorI = [-1, ""], AnteriorI = None):
        self.Valores = []
        self.Hijos = []
        self.Anterior = None
        if ValorI[0]==-1 and AnteriorI == None:
            for i in range(4):
                if i!=3:
                    self.Valores.append([-1, ""])
                self.Hijos.append(None)
            self.Anterior = None
        elif ValorI!=-1 and AnteriorI == None:
            for i in range(4):
                if i!=3:
                    self.Valores.append([-1, ""])
                self.Hijos.append(None)
            self.Valores[0] = ValorI
            self.Anterior = None
        elif ValorI!=-1 and AnteriorI != None:
            for i in range(4):
                if i!=3:
                    self.Valores.append([-1, ""])
                self.Hijos.append(None)
            self.Valores[0] = ValorI
            self.Anterior = AnteriorI

class Arbol:

    def __init__(self):
        self.Raiz = None
        self.PK = []
        self.Flag = False
        self.Valores_Temp = []
    
    def Mostrar2(self, Actual):
        print("[",end="")
        for i in range(3):
            if Actual.Hijos[i] != None:
                self.Mostrar2(Actual.Hijos[i])
            if Actual.Valores[i][0] != -1:
                if i!=0:
                    print(",",end="")
                print(Actual.Valores[i][0],end="")
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
            if(Aux[2][0] != -1):
                self.InsertarArriba(Anterior)

    def InsertarEnNodo(self, Actual, Nuevo):
        Aux = Actual.Valores
        if Aux[0][0] == -1:
            Aux[0] = Nuevo
        elif Aux[1][0] == -1:
            if Nuevo[0] < Aux[0][0]:
                Aux[1] = Aux[0]
                Aux[0] = Nuevo
            else:
                Aux[1] = Nuevo
        else:
            if Nuevo[0] < Aux[0][0]:
                Aux[2] = Aux[1]
                Aux[1] = Aux[0]
                Aux[0] = Nuevo
            elif Nuevo[0] < Aux[1][0]:
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
            if Nuevo[0] < Aux[0][0]:
                self.BuscarInsercion(Auxiliar[0], Nuevo)
            elif Aux[1][0] != -1 and Aux[1][0] < Nuevo[0]:
                self.BuscarInsercion(Auxiliar[2], Nuevo)
            else:
                self.BuscarInsercion(Auxiliar[1], Nuevo)

    def Insertar(self, Nuevo):
        if self.Raiz == None :
            self.Raiz = NodoArbol(Nuevo)
        else:
            self.BuscarInsercion(self.Raiz, Nuevo)
        self.Mostrar()

    def Tomar_Datos_BETA(self, Actual):
        Valores = []
        for i in range(3):
            if Actual.Hijos[i] != None:
                self.Tomar_Datos_BETA(Actual.Hijos[i])
            if Actual.Valores[i][0] != -1:
                Valores.append(Actual.Valores[i])
        if Actual.Hijos[3] != None:
            self.Tomar_Datos_BETA(Actual.Hijos[2])
        self.Valores_Temp.append(Valores)

    def Tomar_Datos(self):
        Valores_temp = []

        Valores_temp.append(self.Tomar_Datos_BETA(self.Raiz))
        for n in self.Valores_Temp:
            if n != "None":
                 Valores_temp.append(n[0])

        Valores_temp.pop(0)
        return Valores_temp
    def insertar_(self,datos):
        temp = datos
        Prueba.Insertar(temp)

