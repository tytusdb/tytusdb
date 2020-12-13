class Node:
    
    def __init__(self):
        self.array = []
        self.key = 0
        
    #ya no se usa el de buscar porque ya esta implementado en la tabla hash
    def insert(self, dato):
        self.array.append(dato)
        lista = self.array.copy()
        lista_ordenada= self.quick_sorted(lista)
        self.array.clear()
        for i in lista_ordenada:
            self.array.append(i)

    def buscarDato_binary(self, dato):
        ub = len(self.array) 
        lb = 0 
        while (lb <= ub-1):
            med = (ub + lb ) // 2
            arreglo = self.array[med]
            if int(arreglo[0]) == int(dato[0]):
                return True
            elif int(arreglo[0]) < int(dato[0]):
                lb = med +1
            elif int(arreglo[0]) > int(dato[0]):
                ub = med -1
    
        return False

    def busquedaB(self, dato):
        inicio = 0
        final = len(self.array) -1 
        while inicio <= final:
            mid = inicio + (final - inicio) //2
            arreglo = self.array[mid]
            if int(arreglo[0]) == int(dato):
                return arreglo
            elif int(dato) < int(arreglo[0]):
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
        if self.busquedaB_Bol(dato):
            self.array.remove(self.busquedaB(dato))
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
    def printArray(self):
        print(self.array)
