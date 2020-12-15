class Error():

    def __init__(self, type, detail, row, column):
        self.type = type
        self.detail = detail
        self.row = row
        self.column = column

    def toString(self):
        return "Error " + self.type + ": " + self.detail + " en Fila " + str(self.row) + " , Columna " + str(self.column)