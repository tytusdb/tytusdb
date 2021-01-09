class Constraint:
    def __init__(self,nombre,default,isNull:bool,isUnique:bool,check,propiedad:int):
        self.nombreConstraint = nombre
        self.default = default
        self.isNull = isNull
        self.isUnique = isUnique
        self.check = check
        self.propiedad = propiedad      #1: default, 2: isNull, 3: isUnique , 4: check
        #Punteros
        self.siguiente = None
        self.anterior = None
        