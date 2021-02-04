from typing import List


class ReportIndice():


    def __init__(self, alias, nombre, tipo,columnas:List[str], consideracion, fila, columna):
        self.alias = alias
        self.nombre = nombre
        self.tipo = tipo
        self.columnas:List[str] = columnas
        self.consideracion = consideracion
        self.fila = fila
        self.columna = columna
