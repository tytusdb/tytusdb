class ReporteTS_forFunction():

    def __init__(self, alias, nombre, tipo, estado, fila, columna):
        self.alias = alias
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado
        self.fila = fila
        self.columna = columna

    def isActive(self):
        if str(self.estado) == 'ACTIVO':
            return True
        return False