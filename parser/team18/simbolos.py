class Simbolo:
    def __init__(self, valor, linea):
        self.valor = valor
        self.linea = linea

class TablaSimbolos:
    def __init__(self):
        self.tabla = []

class TablaMetodos:
    def __init__(self):
        self.metodos = {}
        self.variables = {}
        self.mensajes = []
        self.errores= []

    def añadirMetodo(self,metodo):
        self.metodos[metodo.nombre] = metodo
    
    def añadirVariable(self,name,var,linea):
        self.variables[name] = Simbolo(var,linea)
    
    def borrarVariable(self,var):
        del self.variables[var.nombre]
    

    