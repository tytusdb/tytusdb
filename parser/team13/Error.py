class ErrorS:
    def __init__(self, tipo, descripcion):
        self.tipo  = tipo
        self.descripcion = descripcion

    def __str__(self):
        return "ERROR => tipo: %s, descripcion: %s " % (
        self.tipo, self.descripcion,)
