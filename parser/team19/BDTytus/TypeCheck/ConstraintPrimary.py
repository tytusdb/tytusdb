class Primary:
    def __init__(self, nombreConstraint:str,columnas:list):
        self.nombreConstraint = nombreConstraint
        self.columnas = columnas

    def esPrimary(self, nombre:str) -> bool:
        existe = False
        for columna in self.columnas:
            if columna == nombre:
                existe = True
                break
        return existe