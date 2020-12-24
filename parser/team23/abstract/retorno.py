class retorno:
    def __init__(self, valor, tipo, query=False, index_col = None, encabezados = None):
        self.valor = valor
        self.tipo = tipo
        self.query = query
        self.index_col = index_col
        self.encabezados = encabezados