from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Relaciones(Instruccion):
    def __init__(self, lista, opcion, query, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.query = query
        self.lista = lista
        self.opcion = opcion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("entro a relaciones")