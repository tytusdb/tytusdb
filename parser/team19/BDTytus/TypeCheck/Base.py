import TypeCheck.ListaTablas as ListaTablas
class Base:
    def __init__(self,nombreBase: str, owner, mode):
        #Punteros
        self.nombreBase = nombreBase
        self.owner = owner
        self.mode = mode
        self.listaTablas = ListaTablas.ListaTablas()
        self.siguiente = None
        self.anterior = None
    
    