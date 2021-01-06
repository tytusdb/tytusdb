class ErrorReportar():

    def __init__(self, fila, columna, tipoError, descripcion):
        self.fila = fila
        self.columna = columna
        self.tipoError = tipoError
        self.descripcion = descripcion
        print(descripcion)
