class Entorno:
    def __init__(self, anterior = None):
        self.anterior = anterior
        self.ts = {}
    
    def agregarSimbolo(self,key,valor,tipo):
        if key in self.ts: #error de existir
            return 0
        else:
            self.ts[key] = Simbolo(valor,tipo)
            return 1

    def modificarSimbolo(self,key,valor,tipo):
        if not(key in self.ts): #Error de no existir
            return 0 
        else:
            if self.ts[key].tipo != tipo: #Error si no son del mismo tipo
                return 0
            else:
                self.ts[key] = Simbolo(valor, tipo)
                return 1

    def buscarSimbolo(self,key):
        if not(key in self.ts):
            if self.anterior != None:
                return self.anterior.buscarSimbolo(key)
            else:
                return None
        else:
            return self.ts[key]

class Simbolo:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo