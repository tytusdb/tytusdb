class Entorno:
    def __init__(self,last):
        self.tableofSymbols = {}
        self.last = last


    def add(self, Symbol) :
        self.tableofSymbols[Symbol.id.lower()] = Symbol

    def getLocal(self, id) :
        id = id.lower()
        if not id in self.tableofSymbols :
            return None

        return self.tableofSymbols[id]


    def get(self,id):
        return self.getLocal(id)

    def eliminar(self,id):
        id = id.lower()
        if(self.getLocal(id) != None):
            del self.tableofSymbols[id]

    def existe(self,id):
        id = id.lower()
        return self.getLocal(id)

    def replacesymbol(self,Symbol):
        Symbol.id = Symbol.id.lower()
        if(self.getLocal(Symbol.id) != None):
            self.tableofSymbols[Symbol.id] = Symbol
