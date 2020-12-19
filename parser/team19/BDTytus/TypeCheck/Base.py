import ListaTablas as ListaTablas
import Tabla as Tabla

class Base:
    def __init__(self,nombreBase: str):
        #Punteros
        self.nombreBase = nombreBase
        self.owner = None
        self.listaTablas = ListaTablas.ListaTablas()
        self.siguiente = None
        self.anterior = None
    
    