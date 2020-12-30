class Base:
    #Constructor de la clase Base
    def __init__(self, nombre):
        self.nombre = nombre
        
        
        
        
class InterpretBase():
    def __init__(self, entrada):
        self.bases=[]
        base=entrada.split("%")
        posf=len(entrada.split("%"))-1
        for i in range(0,posf):
            self.bases.append(base[i])
            bd=Base(base[i])
            
           
          