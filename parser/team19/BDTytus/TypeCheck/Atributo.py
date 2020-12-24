import TypeCheck.ListaConstraints as ListaConstraints

class Atributo:
    def __init__(self,nombre:str,tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.listaConstraints = ListaConstraints.ListaConstraints()
        #Punteros
        self.siguiente = None
        self.anterior = None
