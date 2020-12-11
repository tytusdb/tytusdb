class Node:
    
    def __init__(self):
        self.array = []
        post_in_hash = -1

    def insert(self, dato):
        if self.buscarDato(dato):
            self.array.append(dato)
        else:
            print("dato existente")

    def buscarDato(self, dato):
        return False if dato in self.array else True
        
    def eliminar(self, dato):
        if not self.buscarDato(dato):
            self.array.remove(dato)
            if len(self.array) == 0:
                return 0
            else:
                return True
        else:
            return False
    def printArray(self):
        print(self.array)