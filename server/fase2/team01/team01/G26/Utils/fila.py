class fila():

    def __init__(self, _nombre, _tipo, _size):
        self.nombre = _nombre
        self.tipo = _tipo
        self.size = _size
        self.PK = False
        self.FK = False
        self.unique = False
        self.default = ''
    
    def setPK(self):
        self.PK = True
    
    def setFK(self):
        self.FK = True
    
    def setUnique(self):
        self.unique = True

    def setDefault(self, default):
        self.default = default