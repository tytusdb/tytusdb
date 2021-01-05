class Column(object):
    def __init__(self, name, tipo, default, lenght):
        self.name = name
        self.tipo = tipo
        self.default = default
        self.lenght = lenght
    
    def setTipo(self, tipo):
        self.tipo = tipo 
    def setName(self, name):
        self.name= name
    def setDefault(self, default):
        self.default = default
    def setLenght(self,lenght):
        self.lenght = lenght