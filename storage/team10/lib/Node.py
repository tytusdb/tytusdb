class Node:
    
    def __init__(self):
        self.array = []
        self.key = -1
        self.pk = None
        self.isGeneric = False

    def insert(self, dato, key):
        self.array.append((key,dato)) #ahora recibe el parametro key 
        lista = self.array[:]
        lista_ordenada= self.quick_sorted(lista)
        self.array = lista_ordenada[:]

    def buscarDato_binary(self, dato):
        inicio = 0
        final = len(self.array) -1 
        while inicio <= final:
            mid = inicio + (final - inicio) //2
            arreglo = self.array[mid]
            # if int(arreglo[0]) == int(dato):
            if int(arreglo[0]) == int(dato):
                return True
            elif int(dato) < int(arreglo[0]):
                final = mid -1 
            else:
                inicio = mid +1
        return False

    def busquedaB(self, dato):
        inicio = 0
        final = len(self.array) -1 
        while inicio <= final:
            mid = inicio + (final - inicio) //2
            arreglo = self.array[mid]
            # if int(arreglo[0]) == int(dato):
            if int(arreglo[0]) == int(dato):
                return arreglo[1]
            elif int(dato) < int(arreglo[0]):
                final = mid -1 
            else:
                inicio = mid +1
        return []

    def quick_sorted(self, sequencia):
        lista = sequencia
        if(len(lista)) <= 1:
            return lista
        else:
            pivote = lista.pop()
        elementos_mayores = []
        elementos_menores = []
        elemento_medio= []
        elemento_medio.append(pivote)
        for elemento in lista:
            if int(elemento[0]) > int(pivote[0]):
                elementos_mayores.append(elemento)
            else:
                elementos_menores.append(elemento)
        return self.quick_sorted(elementos_menores) + elemento_medio + self.quick_sorted(elementos_mayores)

    def eliminar(self, dato):
        if self.Eliminar_porbusqueda(dato):
            lista = self.array[:]
            lista_ordenada= self.quick_sorted(lista)
            self.array.clear()
            self.array = lista_ordenada[:]
            if len(self.array) == 0:
                return 0
            else:
                return True
        else:
            return False

    def modificar(self, columna, modificacion, key):
        try:
            inicio = 0
            final = len(self.array) -1 
            while inicio <= final:
                mid = inicio + (final - inicio) //2
                arreglo = self.array[mid]
                # if int(arreglo[0]) == int(key):
                if int(arreglo[0]) == int(key):
                    self.array[mid][1][columna] = modificacion
                    return 0
                elif int(key) < int(arreglo[0]):
                    final = mid -1 
                else:
                    inicio = mid +1
            return 4
        except :
            return 1

    def Eliminar_porbusqueda(self, dato):
        inicio = 0
        final = len(self.array) -1 
        while inicio <= final:
            mid = inicio + (final - inicio) //2
            arreglo = self.array[mid]
            # if int(arreglo[0]) == int(dato):
            if int(arreglo[0]) == int(dato):
                self.array.pop(mid)
                return True
            elif int(dato) < int(arreglo[0]):
                final = mid -1 
            else:
                inicio = mid +1
        return None

    def obtenerLower(self,columna,valor,lower): ##Cristian 17/12/2020
        let=""
        contador = 0
        x= len(lower)-1
        for i in valor[columna]:
            if contador > x:
                if lower.upper() == let.upper():
                    return True
                else:
                    return False
            else:
                contador+=1
                let+=i

    def obtenerUpper(self,columna,valor,upper):
        let=""
        contador = 0
        x= len(upper)-1
        valor1 = valor[columna]
        for i in valor1[::-1]:
            if contador > x:
                if upper.upper() == let[::-1].upper():
                    return True
                else:
                    return False
            else:
                contador+=1
                let+=i    

    def Numbervalidation(self,columnNumber,valor,lower,upper):       
        if int(valor[columnNumber]) <= upper and int(valor[columnNumber]) >= lower :
                return valor
        else:
            return None

    def NumbervalidationFloat(self,columnNumber,valor,lower,upper):       
        if float(valor[columnNumber]) <= upper and float(valor[columnNumber]) >= lower :
                return valor
        else:
            return None        

    def imp_column(self,subnodo,columnNumber,lower,upper): 
        if isinstance(lower, int) == True:       ##para enteros
            return self.Numbervalidation(columnNumber,subnodo,lower,upper)  
        elif isinstance(lower, float) == True:       ##para float
            return self.NumbervalidationFloat(columnNumber,subnodo,lower,upper)  
        else:                                       ##para string
            if self.obtenerLower(columnNumber,subnodo,lower) == True and self.obtenerUpper(columnNumber,subnodo,upper) == True: ##
                return subnodo
            else:
                return None

    def imp_column2(self,columnNumber,lower,upper): 
        if isinstance(lower, int) == True:
            for i in self.array:     
                return self.Numbervalidation(columnNumber,i[1],lower,upper)      
        elif isinstance(lower, float) == True:       ##para float
            for i in self.array:     
                return self.NumbervalidationFloat(columnNumber,i[1],lower,upper)          
        else:
            for i in self.array:
                if self.obtenerLower(columnNumber,i[1],lower) == True and self.obtenerUpper(columnNumber,i[1],upper) == True:
                    return i[1]
                else:
                    return None

    #agrega una columna y registra un dato
    def alterAddColumn(self, dato):
        try:
            for i in self.array:
                i[1].append(dato)
            # print("ya jalo")
        except Exception as e:
            print("########")
            print("en el nodo")
            print(e)
            print("########")
