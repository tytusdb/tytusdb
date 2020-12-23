

class nodo :
    def __init__(self,nombreDeLaTabla,numeroDeColumnasDeLaTabla) :
        self.nombre = nombreDeLaTabla
        self.columnas = numeroDeColumnasDeLaTabla
        self.siguiente = None
        self.anterior = None