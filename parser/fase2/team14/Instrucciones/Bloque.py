
from Instrucciones.Instruccion import Instruccion

class Bloque(Instruccion):
    def __init__(self,instrucciones):
        self.instrucciones=instrucciones


    def ejecutar(self, ent):
            'ejecucion del bloque'
            for inst in self.instrucciones:
                val= inst.ejecutar(ent)
                if val!=None:
                    return val

    def traducir(self,ent):
        'tradyccuion del bloque'
        cad=''
        for inst in self.instrucciones:
            cad+= inst.traducir(ent).codigo3d

        self.codigo3d = cad
        return self
