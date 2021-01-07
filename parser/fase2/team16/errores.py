class ErrorRep():
    def __init__(self,tipo,descripcion,linea):
        self.tipo=tipo
        self.descripcion=descripcion
        self.linea=linea
    
class TablaError():
    def __init__(self,errores=[]):
        self.errores=errores
    
    def agregar(self,error):
        self.errores.append(error)
    
