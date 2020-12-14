#clase de la tabla
class TablaDeSimbolos():
    

    def __init__(self, simbolos={}):
        self.simbolos = simbolos

    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            return None
        return self.simbolos[id]

    def actualizar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtRepTS(self):
        return self.simbolos

    def clearTS(self):
        self.simbolos.clear()

        
#simbolos dentro de la tabla
class Simbolo():

    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        self.valor = None
        self.ambito="Global"
    
    def updateValor(self,valor):
        self.valor=valor

    def updateTipo(self,tipo):
        self.tipo=tipo

    def updateTipoVal(self,valor,tipo):
        self.valor = valor
        self.tipo = tipo
