class Node:
    
    def __init__(self):
        self.array = []
        post_in_hash = -1

    def insert(self, dato):
        if not self.buscarDato_binary(dato):
            self.array.append(dato)
        else:
            print("dato existente")

    def buscarDato_binary(self, dato):
        ub = len(self.array) -1
        lb = 0 
        while (lb < ub-1):
            med = (ub + lb ) // 2
            if self.array[med] == dato:
                return True
            elif self.array[med] < dato:
                lb = med +1
            elif self.array[med] > dato:
                ub = med -1
    
        return False

    def buscarDato(self, dato):
        ub = len(self.array) -1
        lb = 0 
        while (lb< ub-1):
            med = (ub + lb ) //2
            if self.array[med] == dato:
                return self.array[med]
            elif self.array[med] < dato:
                lb = med +1
            elif self.array[med] > dato:
                ub = med -1
        if(ub == 0):
            return self.array[0]
        return "No se encontro el valor"

    def quick_sorted(self, sequencia):
        if(len(sequencia)) <= 1:
            return sequencia
        else:
            pivote = sequencia.pop()
        elementos_mayores = []
        elementos_menores = []
        for elemento in sequencia:
            if elemento > pivote:
                elementos_mayores.append(elemento)
            else:
                elementos_menores.append(elemento)
        return self.quick_sorted(elementos_menores) + [pivote] + self.quick_sorted(elementos_mayores)

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
