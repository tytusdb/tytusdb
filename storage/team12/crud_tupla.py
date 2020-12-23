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

    def Buscar2(self, Clave, Actual):
        if Actual != None:
            Aux = Actual.Valores
            if Clave < Aux[0][0]:
                return self.Buscar2(Clave, Actual.Hijos[0])
            elif Clave == Aux[0][0]:
                return Aux[0]
            elif Aux[1][0] != -1 and Clave > Aux[1][0]:
                return self.Buscar2(Clave, Actual.Hijos[2])
            elif Aux[1][0] != -1 and Clave == Aux[1][0]:
                return Aux[1]
            else:
                return self.Buscar2(Clave, Actual.Hijos[1])
        else:
            return None

    def Buscar(self, Clave):
        if self.Raiz == None:
            return None
        else:
            return self.Buscar2(Clave, self.Raiz)

    def BuscarN2(self, Clave, Actual):
        if Actual != None:
            Aux = Actual.Valores
            if Clave < Aux[0][0]:
                return self.BuscarN2(Clave, Actual.Hijos[0])
            elif Clave == Aux[0][0]:
                return [Actual, 0]
            elif Aux[1][0] != -1 and Clave > Aux[1][0]:
                return self.BuscarN2(Clave, Actual.Hijos[2])
            elif Aux[1][0] != -1 and Clave == Aux[1][0]:
                return [Actual, 1]
            else:
                return self.BuscarN2(Clave, Actual.Hijos[1])
        else:
            return None

    def BuscarN(self, Clave):
        if self.Raiz == None:
            return None
        else:
            return self.BuscarN2(Clave, self.Raiz)

    def Ajustar(self, Actual):
        if Actual == None:
            self.Raiz = self.Raiz.Hijos[0]
        else:
            if Actual.Hijos[0].Valores[0][0] == -1:
                if Actual.Hijos[1].Valores[1][0] != -1:
                    Actual.Hijos[0].Valores[0] = Actual.Valores[0]
                    Actual.Valores[0] = Actual.Hijos[1].Valores[0]
                    Actual.Hijos[1].Valores[0] = Actual.Hijos[1].Valores[1]
                    Actual.Hijos[1].Valores[1] = [-1, ""]
                    Actual.Hijos[0].Hijos[1] = Actual.Hijos[1].Hijos[0]
                    if Actual.Hijos[0].Hijos[1] != None:
                        Actual.Hijos[0].Hijos[1].Anterior = Actual.Hijos[0]
                    Actual.Hijos[1].Hijos[0] = Actual.Hijos[1].Hijos[1]
                    Actual.Hijos[1].Hijos[1] = Actual.Hijos[1].Hijos[2]
                    Actual.Hijos[1].Hijos[2] = None
                elif Actual.Valores[1][0] != -1:
                    Actual.Hijos[0].Valores[0] = Actual.Valores[0]
                    Actual.Hijos[0].Valores[1] = Actual.Hijos[1].Valores[0]
                    Actual.Hijos[0].Hijos[1] = Actual.Hijos[1].Hijos[0]
                    if Actual.Hijos[0].Hijos[1] != None:
                        Actual.Hijos[0].Hijos[1].Anterior = Actual.Hijos[0]
                    Actual.Hijos[0].Hijos[2] = Actual.Hijos[1].Hijos[1]
                    if Actual.Hijos[0].Hijos[2] != None:
                        Actual.Hijos[0].Hijos[2].Anterior = Actual.Hijos[0]
                    Actual.Valores[0] = Actual.Valores[1]
                    Actual.Valores[1] = [-1, ""]
                    Actual.Hijos[1] = Actual.Hijos[2]
                    Actual.Hijos[2] = None
                else:
                    Actual.Hijos[0].Valores[0] = Actual.Valores[0]
                    Actual.Hijos[0].Valores[1] = Actual.Hijos[1].Valores[0]
                    Actual.Hijos[0].Hijos[1] = Actual.Hijos[1].Hijos[0]
                    if Actual.Hijos[0].Hijos[1] != None: 
                        Actual.Hijos[0].Hijos[1].Anterior = Actual.Hijos[0]
                    Actual.Hijos[0].Hijos[2] = Actual.Hijos[1].Hijos[1]
                    if Actual.Hijos[0].Hijos[2] != None: 
                        Actual.Hijos[0].Hijos[2].Anterior = Actual.Hijos[0]
                    Actual.Valores[0] = [-1, ""]
                    Actual.Hijos[1] = None
                    self.Ajustar(Actual.Anterior)
            elif Actual.Hijos[1].Valores[0][0] == -1:
                if Actual.Hijos[0].Valores[1][0] != -1:
                    Actual.Hijos[1].Valores[0] = Actual.Valores[0]
                    Actual.Valores[0] = Actual.Hijos[0].Valores[1]
                    Actual.Hijos[1].Hijos[1] = Actual.Hijos[1].Hijos[0]
                    Actual.Hijos[1].Hijos[0] = Actual.Hijos[0].Hijos[2]
                    if Actual.Hijos[1].Hijos[0] != None: 
                        Actual.Hijos[1].Hijos[0].Anterior = Actual.Hijos[1]
                    Actual.Hijos[0].Hijos[2] = None
                    Actual.Hijos[0].Valores[1] = [-1, ""]
                elif Actual.Valores[1][0] != -1:
                    if Actual.Hijos[2].Valores[1][0] != -1:
                        Actual.Hijos[1].Valores[0] = Actual.Valores[1]
                        Actual.Valores[1] = Actual.Hijos[2].Valores[0]
                        Actual.Hijos[2].Valores[0] = Actual.Hijos[2].Valores[1]
                        Actual.Hijos[2].Valores[1] = [-1, ""]
                        Actual.Hijos[1].Hijos[1] = Actual.Hijos[2].Hijos[0]
                        if Actual.Hijos[1].Hijos[1] != None: 
                            Actual.Hijos[1].Hijos[1].Anterior = Actual.Hijos[1]
                        Actual.Hijos[2].Hijos[0] = Actual.Hijos[2].Hijos[1]
                        Actual.Hijos[2].Hijos[1] = Actual.Hijos[2].Hijos[2]
                        Actual.Hijos[2].Hijos[2] = None
                    else:
                        Actual.Hijos[1].Valores[0] = Actual.Valores[1]
                        Actual.Hijos[1].Valores[1] = Actual.Hijos[2].Valores[0]
                        Actual.Hijos[1].Hijos[1] = Actual.Hijos[2].Hijos[0]
                        if Actual.Hijos[1].Hijos[1] != None: 
                            Actual.Hijos[1].Hijos[1].Anterior = Actual.Hijos[1]
                        Actual.Hijos[1].Hijos[2] = Actual.Hijos[2].Hijos[1]
                        if Actual.Hijos[1].Hijos[2] != None: 
                            Actual.Hijos[1].Hijos[2].Anterior = Actual.Hijos[1]
                        Actual.Valores[1] = [-1, ""]
                        Actual.Hijos[2] = None
                else:
                    Actual.Hijos[0].Valores[1] = Actual.Valores[0]
                    Actual.Valores[0] = [-1, ""]
                    Actual.Hijos[0].Hijos[2] = Actual.Hijos[1].Hijos[0]
                    if Actual.Hijos[0].Hijos[2] != None: 
                        Actual.Hijos[0].Hijos[2].Anterior = Actual.Hijos[0]
                    Actual.Hijos[1] = None
                    self.Ajustar(Actual.Anterior)
            else:
                if Actual.Hijos[1].Valores[1][0] != -1:
                    Actual.Hijos[2].Valores[0] = Actual.Valores[0]
                    Actual.Valores[0] = Actual.Hijos[1].Valores[1]
                    Actual.Hijos[1].Valores[1] = [-1, ""]
                    Actual.Hijos[2].Hijos[1] = Actual.Hijos[2].Hijos[0]
                    Actual.Hijos[2].Hijos[0] = Actual.Hijos[1].Hijos[2]
                    if Actual.Hijos[2].Hijos[0] != None: 
                        Actual.Hijos[2].Hijos[0].Anterior = Actual.Hijos[2]
                    Actual.Hijos[1].Hijos[2] = None
                else:
                    Actual.Hijos[1].Valores[1] = Actual.Valores[1]
                    Actual.Valores[1] = [-1, ""]
                    Actual.Hijos[1].Hijos[2] = Actual.Hijos[2].Hijos[1]
                    if Actual.Hijos[1].Hijos[2] != None: 
                        Actual.Hijos[1].Hijos[2].Anterior = Actual.Hijos[1]
                    Actual.Hijos[2] = None 

    def MayorDeLosMenores(self, Actual):
        if Actual.Hijos[0] == None:
            if Actual.Valores[1][0] != -1:
                return Actual.Valores[1]
            else:
                return Actual.Valores[0]
        else:
            if Actual.Valores[1][0] != -1:
                return self.MayorDeLosMenores(Actual.Hijos[2])
            else:
                return self.MayorDeLosMenores(Actual.Hijos[1])
        return None

    def Eliminar2(self, Eliminado):
        if Eliminado[0].Hijos[0] == None:
            if Eliminado[1] == 0:
                Eliminado[0].Valores[0] = Eliminado[0].Valores[1]
            Eliminado[0].Valores[1] = [-1, ""]
            if Eliminado[0].Valores[0][0] == -1:
                self.Ajustar(Eliminado[0].Anterior)
        else:
            Cambio = None
            if Eliminado[1] == 0:
                Cambio = self.MayorDeLosMenores(Eliminado[0].Hijos[0])
                Eliminado[0].Valores[Eliminado[1]] = Cambio
                self.Eliminar2(self.BuscarN2(Cambio[0], Eliminado[0].Hijos[0]))
            else:
                Cambio = self.MayorDeLosMenores(Eliminado[0].Hijos[1])
                Eliminado[0].Valores[Eliminado[1]] = Cambio
                self.Eliminar2(self.BuscarN2(Cambio[0], Eliminado[0].Hijos[1]))

    def Eliminar(self, Clave):
        Eliminar = self.BuscarN(Clave)
        if Eliminar != None:
            self.Eliminar2(Eliminar)
            self.Mostrar()
        else:
            print("Valor No Encontrado")

Prueba = Arbol()
Prueba.Insertar([5, "Hola"])
Prueba.Insertar([10, "Hola2"])
Prueba.Insertar([15, "Hola3"])
Prueba.Insertar([20, "Hola4"])
Prueba.Insertar([21, "Hola5"])
Prueba.Insertar([22, "Hola6"])
Prueba.Insertar([23, "Hola7"])
Prueba.Insertar([24, "Hola8"])
Prueba.Insertar([25, "Hola9"])
Prueba.Insertar([26, "Hola10"])
Prueba.Insertar([27, "Hola11"])
Prueba.Insertar([4, "Hola12"])
Prueba.Insertar([3, "Hola13"])
Prueba.Insertar([2, "Hola14"])
Prueba.Insertar([1, "Hola15"])
Prueba.Eliminar(26)
Prueba.Eliminar(23)
Prueba.Eliminar(27)
Prueba.Eliminar(20)