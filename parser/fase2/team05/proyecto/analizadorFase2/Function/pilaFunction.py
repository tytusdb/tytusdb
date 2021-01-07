
class Cola:
    # Representa a una cola, con operaciones de encolar y desencolar.
    #    El primero en ser encolado es también el primero en ser desencolado.
    

    def __init__(self):
        # Crea una cola vacía. 
        # La cola vacía se representa por una lista vacía
        self.items=[]

    def encolar(self, x):
        #""" Agrega el elemento x como último de la cola. """
        self.items.append(x)

    def desencolar(self):
        #""" Elimina el primer elemento de la cola y devuelve su
        #valor. Si la cola está vacía, levanta ValueError. """
        try:
           return self.items.pop(0)
        except:
           raise ValueError("La cola está vacía")

    def es_vacia(self):
        #""" Devuelve True si la lista está vacía, False si no. """
        return self.items == []