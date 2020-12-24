class T_error():
    def __init__(self, tipo, token, descripcion, row, column):
        self.tipo = tipo
        self.token = token
        self.description = descripcion
        self.row = row
        self.column = column

    def toString(self):
        return "Tipo: " + self.tipo + " Token: " + self.token  + " Descripcion: " + self.description + " Linea: " + self.row + " Columna: " + self.column

    def getTipo(self):
        return self.tipo

    def getLinea(self):
        return self.row

    def getDescripcion(self):
        return self.description