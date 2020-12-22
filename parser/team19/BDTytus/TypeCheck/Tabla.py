import TypeCheck.ListaAtributos as ListaAtributos

class Tabla:
    def __init__(self,nombreTabla:str):
        self.nombreTabla = nombreTabla
        self.listaAtributos = ListaAtributos.ListaAtributos()
        self.primary = None
        self.foreigns = {}
        #Punteros
        self.siguiente = None
        self.anterior = None

