class nodo_error:
    def __init__(self, linea, columna, valor, descripcion):
        self.line = str(linea)
        self.column = str(columna)
        self.valor = str(valor)
        self.descripcion = str(descripcion)

errores = []