from Entorno.Simbolo import Simbolo

class Entorno:
    def __init__(self, anterior = None):
        self.anterior = anterior
        self.database = "" 
        self.tablaSimbolo = {}

    def nuevoSimbolo(self, symbol):
        x = self.tablaSimbolo.get(symbol.nombre)

        if x == None:
            self.tablaSimbolo[symbol.nombre] = symbol
        else:
            print("el simbolo", symbol.nombre,"no se puede agregar porque ya existe")

    def editarSimbolo(self, identificador, nuevo):
        x = self.tablaSimbolo.get(identificador)

        if x != None:
            self.tablaSimbolo[identificador] = nuevo
        else:
            print("el simbolo", identificador, "no se puede modificar porque no existe")
    
    def eliminarSimbolo(self, identificador):
        x = self.tablaSimbolo.get(identificador)

        if x != None:
            del self.tablaSimbolo[identificador]
        else:
            print("el simbolo", identificador, "no se puede eliminar porque no existe")
    
    def buscarSimbolo(self, identificador):
        ent = self

        while ent != None:
            x = ent.tablaSimbolo.get(identificador)
            if x != None:
                return x
            ent = ent.anterior
        
        return None

    def mostrarSimbolos(self):
        ent = self

        while ent != None:
            for x in ent.tablaSimbolo.values():
                print(x.toString())
                
            ent = ent.anterior

    def getDataBase(self):
        ent = self

        while ent != None:
            x = ent.database
            if x != "":
                return x
            ent = ent.anterior
        
        return None