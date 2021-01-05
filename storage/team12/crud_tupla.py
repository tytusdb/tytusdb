#NodoContenedor
class NodoArbol:
    #Constructor
    def __init__(self, ValorI = [-1, ""], AnteriorI = None):
        self.Valores = []
        self.Hijos = []
        self.Anterior = None
        #Si solo se creo el Nodo
        if ValorI[0]==-1 and AnteriorI == None:
            for i in range(4):
                if i!=3:
                    self.Valores.append([-1, ""])
                self.Hijos.append(None)
            self.Anterior = None
        #Si el nodo se crea con valor Inicial
        elif ValorI!=-1 and AnteriorI == None:
            for i in range(4):
                if i!=3:
                    self.Valores.append([-1, ""])
                self.Hijos.append(None)
            self.Valores[0] = ValorI
            self.Anterior = None
        #Si el nodo tiene valor inicial y un nodo anterior
        elif ValorI!=-1 and AnteriorI != None:
            for i in range(4):
                if i!=3:
                    self.Valores.append([-1, ""])
                self.Hijos.append(None)
            self.Valores[0] = ValorI
            self.Anterior = AnteriorI

class CRUD_Tuplas:
    def __init__(self):
        #Inicia la raiz vacia
        self.Raiz = None
        self.PK = []
        self.values = []
    
    def dot2(self, Actual, Cadena):
        #Creacion del Nodo
        Dot = "Nodo" + Cadena + " [shape=plaintext\nlabel=<\n<table border='1' cellborder='1'>\n<tr>"
        Last = 0
        for i in range(2):
            if Actual.Valores[i][0] != -1:
                Last = i
                #Toma de datos
                Dot += "<td port='port_" + str(i) + "'></td><td>" + str(Actual.Valores[i][0]) + "</td>"
        Dot += "<td port='port_" + str(Last+1) + "'></td>"
        Dot += "</tr>\n</table>\n>];\n\n"
        for i in range(3):
            if Actual.Hijos[i] != None:
                #Conexion con los hijos
                Dot += "Nodo" + Cadena + ":port_" + str(i) + " -> Nodo" + Cadena + str(i) + ";\n"
                Dot += self.dot2(Actual.Hijos[i], Cadena + str(i))
        return Dot

    def dot(self):
        #Inicio del generador de grafico
        Dot = "digraph G {\n"
        if self.Raiz != None:
            Dot += self.dot2(self.Raiz, "")
        Dot += "\n}"
        file = open("Diagrama-bloques.dot", "w")
        file.write(Dot)
        file.close()
        #check_call(['dot', '-Tpng', 'Diagrama-bloques.dot', '-o', 'Diagrama-bloques.png'])

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
        #Tomamos el valor anterior
        Anterior = Actual.Anterior
        #Si estamos en la raiz, el anterior sera nulo
        if Anterior == None:
            #Se crea el nuevo anterior con el valor mediano del nodo actual
            Anterior = NodoArbol(Actual.Valores[1])
            #El primer Hijo toma el valor pequeño del actual
            Hijo0 = NodoArbol(Actual.Valores[0], Anterior)
            #Los primeros 2 hijos del actual se les asigna al Hijo0
            Hijo0.Hijos[0] = Actual.Hijos[0]
            Hijo0.Hijos[1] = Actual.Hijos[1]
            #Si los Hijos asignados al Hijo0 no son nulos, e establece el anterior Hijo0
            if Hijo0.Hijos[0] != None:
                Hijo0.Hijos[0].Anterior = Hijo0
            if Hijo0.Hijos[1] != None:
                Hijo0.Hijos[1].Anterior = Hijo0
            #Se repite el procedimiento del Hijo0 con el Hijo1
            Hijo1 = NodoArbol(Actual.Valores[2], Anterior)
            #Para el Hijo1 se asignan el 2 y 3 del Actual
            Hijo1.Hijos[0] = Actual.Hijos[2]
            Hijo1.Hijos[1] = Actual.Hijos[3]
            if Hijo1.Hijos[0] != None:
                Hijo1.Hijos[0].Anterior = Hijo1
            if Hijo1.Hijos[1] != None:
                Hijo1.Hijos[1].Anterior = Hijo1
            #El nuevo anterior se le asignan como hijos el Hijo0 y el Hijo1
            Anterior.Hijos[0] = Hijo0
            Anterior.Hijos[1] = Hijo1
            #Se asigna el nodo crado como nueva Raiz
            self.Raiz = Anterior
            #Con esto dividimos el Nodo entero subiendo el valor intermedio y los extremos se toman como nuevos nodos
        else:
            #Tomamos los valores del Anterior
            Auxiliar = Anterior.Hijos
            Aux = Anterior.Valores
            #Se busca en que hijo estamos
            i = 0
            while Auxiliar[i] != Actual:
                i=i+1
            j = 3
            #Los hijos y valores que vayan despues del hijo se corren una posicion
            while (j>i):
                if j!=3:
                    Aux[j] = Aux[j-1]
                Auxiliar[j] = Auxiliar[j-1]
                j = j - 1
            #El valor inmediato 
            Aux[i] = Actual.Valores[1]
            #El primer Hijo toma el valor pequeño del actual
            Hijo0 = NodoArbol(Actual.Valores[0], Anterior)
            #Los primeros 2 hijos del actual se les asigna al Hijo0
            Hijo0.Hijos[0] = Actual.Hijos[0]
            Hijo0.Hijos[1] = Actual.Hijos[1]
            #Si los Hijos asignados al Hijo0 no son nulos, e establece el anterior Hijo0
            if Hijo0.Hijos[0] != None:
                Hijo0.Hijos[0].Anterior = Hijo0
            if Hijo0.Hijos[1] != None:
                Hijo0.Hijos[1].Anterior = Hijo0
            #Se repite el procedimiento del Hijo0 con el Hijo1
            Hijo1 = NodoArbol(Actual.Valores[2], Anterior)
            #Para el Hijo1 se asignan el 2 y 3 del Actual
            Hijo1.Hijos[0] = Actual.Hijos[2]
            Hijo1.Hijos[1] = Actual.Hijos[3]
            if Hijo1.Hijos[0] != None:
                Hijo1.Hijos[0].Anterior = Hijo1
            if Hijo1.Hijos[1] != None:
                Hijo1.Hijos[1].Anterior = Hijo1
            #Al anterior se estableces sus nuevos 2 hijos
            Anterior.Hijos[i] = Hijo0
            Anterior.Hijos[i+1] = Hijo1
            #En caso de que el nodo este lleno, se repite el proceso con el Anterior
            if(Aux[2][0] != -1):
                self.InsertarArriba(Anterior)

    def InsertarEnNodo(self, Actual, Nuevo):
        #Tomamos los valores del nodo
        Aux = Actual.Valores
        #Si esta vacio
        if Aux[0][0] == -1:
            #Se incerta en la posicion 0
            Aux[0] = Nuevo
        #Si hay un valor en el nodo
        elif Aux[1][0] == -1:
            #Se comprueba el orden
            if str(Nuevo[0]) < Aux[0][0]:
                #Si el Nuevo es menos al valor 0 se corre y se inserta al inicio el valor
                Aux[1] = Aux[0]
                Aux[0] = Nuevo
            else:
                #Si el nuevo es mayor  ocupa la posicion 1 
                Aux[1] = Nuevo
        #Si ya hay 2 valores
        else:
            #Se ordena
            if str(Nuevo[0]) < Aux[0][0]:
                Aux[2] = Aux[1]
                Aux[1] = Aux[0]
                Aux[0] = Nuevo
            elif str(Nuevo[0]) < Aux[1][0]:
                Aux[2] = Aux[1]
                Aux[1] = Nuevo
            else:
                Aux[2] = Nuevo
            #Se balancea al ya tener 3 valores en el nodo
            self.InsertarArriba(Actual)

    def BuscarInsercion(self, Actual, Nuevo):
        #Se toman los hijos del nodo actual
        Auxiliar = Actual.Hijos
        #Si no tiene Hijos el nodo
        if Auxiliar[0] == None:
            #Se incerta en el nodo
            self.InsertarEnNodo(Actual, Nuevo)
        #Si no
        else:
            #Se toman los valores del nodo
            Aux = Actual.Valores
            #Si el nuevo es menos al valor menor del actual
            if str(Nuevo[0]) < Aux[0][0]:
                #Se va al hijo izquierdo
                self.BuscarInsercion(Auxiliar[0], Nuevo)
            #Si hay mas de 2 valores en el actual y el nodo es mayor al segundo
            elif Aux[1][0] != -1 and Aux[1][0] < str(Nuevo[0]):
                #Se incerta en el hijo derecho
                self.BuscarInsercion(Auxiliar[2], Nuevo)
            else:
                #Si no en el hijo central
                self.BuscarInsercion(Auxiliar[1], Nuevo)

    def Insertar(self, Nuevo):
        #Si la raiz es nula
        if self.Raiz == None :
            #Se crea la raiz con un nuevo nodo
            arreglo = Nuevo
            auxiliar = ""
            if self.PK == []:
                arreglo = Nuevo
                arreglo.insert(0, Nuevo[0])
                #print(arreglo)
                self.Raiz = NodoArbol(arreglo)
            elif len(self.PK)==1:
                auxiliar =  Nuevo[0]
                arreglo.insert(0,auxiliar)
                #print(arreglo)
                self.Raiz = NodoArbol(arreglo)
            else:
                for n in self.PK:
                    if n == len(self.PK):
                        auxiliar += str(arreglo[n])
                    else:
                        auxiliar += str(arreglo[n]) + "$"
                arreglo.insert(0,auxiliar)
                #print(arreglo)
                self.Raiz = NodoArbol(arreglo)
        else:
            #Si no hay llave primaria aún
            if self.PK == []:
                arreglo = Nuevo
                arreglo.insert(0, Nuevo[0])
                #print(arreglo)
                Existe = self.BuscarN(arreglo[0])
                #print(Existe)
                if Existe == None:
                    # Si no se busca donde insertarlo
                    self.BuscarInsercion(self.Raiz, arreglo)
                else:
                    print("Llave repetida")
            # Si ya hay llave primaria
            elif len(self.PK) == 1:
                arreglo = Nuevo
                arreglo.insert(0, Nuevo[0])
                #print(arreglo)
                self.BuscarInsercion(self.Raiz, arreglo)
            else:
                arreglo = Nuevo
                auxiliar = ""
                for n in self.PK:
                    if n == len(self.PK):
                        auxiliar += str(arreglo[n])
                    else:
                        auxiliar += str(arreglo[n]) + "$"
                arreglo.insert(0, auxiliar)
                #print(arreglo)
                Existe = self.BuscarN(auxiliar)
                #print(Existe)
                if Existe == None:
                    # Si no se busca donde insertarlo
                    self.BuscarInsercion(self.Raiz, arreglo)
                else:
                    return 4
        return 0

    def Buscar2(self, Clave, Actual):
        #Si el nodo actual existe
        if Actual != None:
            Aux = Actual.Valores
            #Si el valor nuevo es menor al valor 0
            if str(Clave) < Aux[0][0]:
                #Se busca en el hijo '
                return self.Buscar2(Clave, Actual.Hijos[0])
            elif str(Clave) == Aux[0][0]:
                #Si es igual al valor 0 se regresa ese valor
                return Aux[0]
            elif Aux[1][0] != -1 and str(Clave) > Aux[1][0]:
                #Si existe el valor 1 y es mayor a ese se busca en el hijo 2
                return self.Buscar2(Clave, Actual.Hijos[2])
            elif Aux[1][0] != -1 and str(Clave) == Aux[1][0]:
                #Si existe el valor 1 y es igual a este se regresa ese
                return Aux[1]
            else:
                #Si no se busca en el hijo 1
                return self.Buscar2(Clave, Actual.Hijos[1])
        else:
            #Si no regresa nulo
            return None

    def Buscar(self, Clave):
        if self.Raiz == None:
            #Si la raiz no existe se regresa none
            return None
        else:
            #Si existe se busca la clave
            return self.Buscar2(Clave, self.Raiz)

    def BuscarN2(self, Clave, Actual):
        #Si el nodo actual existe
        if Actual != None:
            Aux = Actual.Valores
            #Si el valor nuevo es menor al valor 0
            if str(Clave) < str(Aux[0][0]):
                #Se busca en el hijo '
                return self.BuscarN2(Clave, Actual.Hijos[0])
            elif str(Clave) == str(Aux[0][0]):
                #Si es igual al valor 0 se regresa ese valor
                return [Actual, 0]
            elif Aux[1][0] != -1 and str(Clave) > str(Aux[1][0]):
                #Si existe el valor 1 y es mayor a ese se busca en el hijo 2
                return self.BuscarN2(Clave, Actual.Hijos[2])
            elif Aux[1][0] != -1 and str(Clave) == str(Aux[1][0]):
                #Si existe el valor 1 y es igual a este se regresa ese
                return [Actual, 1]
            else:
                #Si no se busca en el hijo 1
                return self.BuscarN2(Clave, Actual.Hijos[1])
        else:
            #Si no regresa nulo
            return None

    def BuscarN(self, Clave):
        if self.Raiz == None:
            #Si la raiz no existe se regresa none
            return None
        else:
            #Si existe se busca la clave
            return self.BuscarN2(Clave, self.Raiz)

    def Ajustar(self, Actual):
        if Actual == None:
            #Si el actual es vacio, significa que la raiz se borro y su hijo ocupa su lugar
            self.Raiz = self.Raiz.Hijos[0]
        else:
            if Actual.Hijos[0].Valores[0][0] == -1:
                #Si el vacio es el hijo 0
                if Actual.Hijos[1].Valores[1][0] != -1:
                    #Si el hijo 1 tiene sus dos valores
                    #El valor 0 del actual se va al valor 0 del hijo 0
                    #El Valor 0 del Hijo 1 se va al valor 0 del actual
                    #El valor 1 del hijo 1 se corre al valor 0 del hijo 1
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
                    #Si no hay 2 valores en el hijo 1 y el actual tiene 2 valores
                    #El valor 0 del actual se va al valor 0 del hijo 0
                    #El valor 1 del hijo 1 se va al valor 1 del hijo 0
                    #El Hijo 1 toma el valor del hijo 2
                    #El hijo 2 se pone como nulo
                    #El valor 0 toma el valor del valor 1
                    #El valor 1 se limpia
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
                    #Si no hay 2 valores en el actual
                    #El valor 0 del hijo 0 toma el valor 0 del actual
                    #El valor 1 del hijo 0 toma el valor 0 del hijo 1
                    #Se pone none en el hijo 1
                    #Se limpia el valor 0 del actual
                    #se repite el metodo con el anterior
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
                #si el hijo vacio es el 1
                #se repite la logica del hijo 0, pero trasladando con el hijo 0 y el hijo 2 de existir
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
                #se usa la logica del hijo 0 solo comparado con el hijo 1
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
        #se comprueba si el actual tiene o no hijos
        if Actual.Hijos[0] == None:
            #Si no tiene hijos, se mira si tiene 1 o 2 valores
            if Actual.Valores[1][0] != -1:
                #Si tiene 2 se manda el segundo
                return Actual.Valores[1]
            else:
                #si tiene 1 se manda ese
                return Actual.Valores[0]
        else:
            #De tener hijos, se comprueba si tiene 2 o 3 hijos
            if Actual.Valores[1][0] != -1:
                #De tener 3 hijos se manda el tercero
                return self.MayorDeLosMenores(Actual.Hijos[2])
            else:
                #si no se manda el segundo
                return self.MayorDeLosMenores(Actual.Hijos[1])
        return None

    def Eliminar2(self, Eliminado):
        #Se comprueba si el nodo es hoja
        if Eliminado[0].Hijos[0] == None:
            #Se elimina el valor correspondiente, de tener uno posterior se corre
            if Eliminado[1] == 0:
                Eliminado[0].Valores[0] = Eliminado[0].Valores[1]
            Eliminado[0].Valores[1] = [-1, ""]
            # si el nodo queda vacio se balancea el arbol
            if Eliminado[0].Valores[0][0] == -1:
                self.Ajustar(Eliminado[0].Anterior)
        else:
            #Si el valor a eliminar tiene hijos, se busca el mayor de los menores y se intercambia, eliminando ese mismo de las ramas de abajo
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
        #Se busca el valor a eliminar
        Eliminar = self.BuscarN(Clave)
        #Se comprueba que exista
        if Eliminar != None:
            #Si existe se procede a eliminar
            self.Eliminar2(Eliminar)
            self.Mostrar()
        else:
            #Si se indica
            return 4
        return 0

    def loadCSV(self, file):
        import csv
        with open(file, 'r') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            for row in reader:
                self.Insertar(row)

    def actualizar(self, register, Clave):
        if self.PK == []:
            Cambio = self.BuscarN(Clave[0])
            if Cambio != None:
                Aux = Cambio[0].Valores[0]
                #print(Aux)
                for key in register:
                    Aux[key] = register[key]
                #print(Aux)
                self.Eliminar2(Cambio)
                self.Insertar(Aux)
            else:
                return 4
        # Si ya hay llave primaria
        else:
            auxiliar = ""
            for i in range(len(self.PK)):
                if i == len(self.PK)-1:
                    auxiliar += str(Clave[i])
                else:
                    auxiliar += str(Clave[i]) + "$"
            Cambio = self.BuscarN(auxiliar)
            if Cambio != None:
                Aux = Cambio[0].Valores[0]
                v2 = ""
                for i in range(len(Aux)):
                    if i == len(Aux)-1:
                        v2+=str(Aux[i])
                    else:
                        v2 += str(Aux[i])+"#"
                v2 = v2.split("#")
                self.Eliminar2(Cambio)
                for key in register:
                    v2[key+1] = register[key]
                v2.pop(0)
                self.Insertar(v2)
            else:
                return 4
        return 0

    def ExtraerFila(self, Clave):
        if self.PK == []:
            Cambio = self.BuscarN(Clave[0])
            if Cambio != None:
                Aux = Cambio[0].Valores[0]
                Aux.pop(0)
                return Aux
            else:
                print("Valor no encontrado")
        else:
            auxiliar = ""
            for i in range(len(self.PK)):
                if i == len(self.PK)-1:
                    auxiliar += str(Clave[i])
                else:
                    auxiliar += str(Clave[i]) + "$"
            Cambio = self.BuscarN(auxiliar)
            if Cambio != None:
                Aux = Cambio[0].Valores[0]
                v2 = ""
                for i in range(len(Aux)):
                    if i == len(Aux)-1:
                        v2+=str(Aux[i])
                    else:
                        v2 += str(Aux[i])+"#"
                v2 = v2.split("#")
                v2.pop(0)
                return v2
            else:
                return []

    def Vaciar(self,):
        #self.Mostrar()
        self.Raiz = None
        return 4

    def DefinirLlaves(self, llaves):
        self.PK = llaves

    def takeDates(self):
        self._takeDates(self.Raiz)
        print("imprimiendo valores")
        vals = self.values
        print(vals)
        print("valores imprimidos")
        self.values = []
        return vals
    values = []
    def _takeDates(self, tmp):
        for i in range(3):
            if tmp.Hijos[i] != None:
                self._takeDates(tmp.Hijos[i])
            if tmp.Valores[i][0] != -1:
                self.values.append(tmp.Valores[i])
                print(tmp.Valores)
        if tmp.Hijos[3] != None:
            self._takeDates(tmp.Hijos[2])

    def insertar_(self, tupla):
        self.Insertar(tupla)