class Foreign:
    def __init__(self,nombreConstraint:str,columnas:list,nombreTablaReferencia:str, columnasOtraTabla:list):
        self.nombreConstraint = nombreConstraint
        self.columnas = columnas
        self.nombreTabla = nombreTablaReferencia
        self.columnasrefer = columnasOtraTabla

