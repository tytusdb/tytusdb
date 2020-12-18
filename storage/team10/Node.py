class Node:

    def __init__(self):
        self.array = []
        self.key = 0
        self.pk = None

    def insert(self, dato):
        self.array.append(dato)
        lista = self.array.copy()
        lista_ordenada= self.quick_sorted(lista)
        self.array.clear()
        for i in lista_ordenada:
            self.array.append(i)

    def buscarDato_binary(self, dato):
        inicio = 0
        final = len(self.array) -1 
        while inicio <= final:
            mid = inicio + (final - inicio) //2
            arreglo = self.array[mid]
            # if int(arreglo[0]) == int(dato):
            if int(arreglo[self.pk]) == int(dato):
                return True
            elif int(dato) < int(arreglo[self.pk]):
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
            if int(arreglo[self.pk]) == int(dato):
                return arreglo
            elif int(dato) < int(arreglo[self.pk]):
                final = mid -1 
            else:
                inicio = mid +1
        return None

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
                if int(arreglo[self.pk]) == int(key):
                    self.array[mid][columna] = modificacion
                    return 0
                elif int(key) < int(arreglo[self.pk]):
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
            if int(arreglo[self.pk]) == int(dato):
                self.array.pop(mid)
                return True
            elif int(dato) < int(arreglo[self.pk]):
                final = mid -1 
            else:
                inicio = mid +1
        return None

    def imp_column(self,columnNumber,lower,upper): ##trabaja solo en esa tabla, de esa base de datos en esa columna dada. wujuuuuuuuuuuuuuuuuuuuu
        for i in self.array:
            if int(i[columnNumber]) <= upper and int(i[columnNumber]) >= lower :
                #print(i)  
                return i
            else:
                return None
