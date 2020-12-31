class error():

    def __init__(self, _tipo, _descripcion, _linea):
        self.tipo = _tipo
        self.description = _descripcion
        self.linea = _linea


    def toString(self):
        return "Tipo: " + self.tipo + "Descripcion: " + self.description + "Linea: " + self.linea

    def getTipo(self):
        return self.tipo

    def getLinea(self):
        return self.linea

    def getDescripcion(self):
        return self.description