
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
        strsql=''
        for inst in self.instrucciones:

            obj= inst.traducir(ent)
            cad+=obj.codigo3d
            strsql+=obj.stringsql
        self.codigo3d = cad
        self.stringsql=self.stringsql.replace('LISTACONTENIDO',strsql)
        return self

