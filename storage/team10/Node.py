class Node:
    
    def __init__(self):
        self.array = []
        
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
    """def buscarDato_binary(self,lista, dato):
        if len(lista) == 0:
            return False
        else:
            medio = len(lista)//2
            arreglo = lista[medio]
            if int(arreglo[0]) == int(dato[0]):
                return True
            else:
                if int(dato[0]) < int(arreglo[0]):
                    return self.buscarDato_binary(lista[:medio], dato)
                else: 
                    return self.buscarDato_binary(lista[medio+1:],dato)"""

    """def buscarDato_binary(self, dato):
        mid = 0 
        start = 0
        end = len(self.array)
        step = 0
        if(end != 0 ):
            while(start <=end):
                step = step +1 
                mid = (start + end) //2
                arreglo = self.array[mid]
                if int(arreglo[0]) == int(dato[0]):
                    return True
                if int(dato[0]) < int(arreglo[0]):
                    end = mid -1
                else:
                    start = mid +1
        return False"""

    def busquedaB(self, dato):
        mid = 0 
        start = 0
        end = len(self.array)
        step = 0
        while(start <=end):
            step = step +1 
            mid = (start + end) //2
            arreglo = self.array[mid]
            if int(arreglo[0]) == dato:
                return arreglo
            if int(dato) < int(arreglo[0]):
                end = mid -1
            else:
                start = mid +1
        return "no se encontro el dato"
    #ordenamiento 
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
        if not self.buscarDato(dato):
            self.array.remove(dato)
            self.quick_sorted(self.array)
            if len(self.array) == 0:
                return 0
            else:
                return True
        else:
            return False
    def printArray(self):
        print(self.array)
