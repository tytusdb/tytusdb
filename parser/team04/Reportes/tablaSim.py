#clase para implementar la tabla de simbolos
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

#Clase específica para el objeto símbolo y sus atributos
class Simbolo():

    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        self.valor = None
        self.ambito = None #se debera agregar el ámbito en el que se encuentre
    
    def updateValor(self, valor):
        self.valor
    
    def updateTipo(self, tipo):
        self.tipo = tipo
    
    def updateTipoVal(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo