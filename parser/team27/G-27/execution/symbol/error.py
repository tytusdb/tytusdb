class T_error():
    def __init__(self, tipo, token, descripcion, row, column):
        self.tipo = tipo
        self.token = token
        self.description = descripcion
        self.row = row
        self.column = column

    def toString(self):
        valor = self.token
        if not isinstance(self.token, str):
            valor = str(valor)
        return "Tipo: " + self.tipo + " Token: " + valor  + " Descripcion: " + self.description + " Linea: " + self.row + " Columna: " + self.column

    def getTipo(self):
        return self.tipo

    def getLinea(self):
        return self.row

    def getDescripcion(self):
        return self.description