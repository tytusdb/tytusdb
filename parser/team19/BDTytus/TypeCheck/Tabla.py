import TypeCheck.ListaAtributos as ListaAtributos

class Tabla:
    def __init__(self,nombreTabla:str):
        self.nombreTabla = nombreTabla
        self.listaAtributos = ListaAtributos.ListaAtributos()
        self.primary = None
        self.foreigns = {}
        self.inherits = None
        self.check_general = []
        #Punteros
        self.siguiente = None
        self.anterior = None

    def obtener_lista_numeros_columnas(self, lista_columnas):
        lista_numeros = []
        for columna in lista_columnas:
            i = 1
            temporal = self.listaAtributos.primero
            while temporal is not None:
                if temporal.nombre == columna:
                    lista_numeros.append(i)
                    break
                i += 1
                temporal = temporal.siguiente
        return lista_numeros