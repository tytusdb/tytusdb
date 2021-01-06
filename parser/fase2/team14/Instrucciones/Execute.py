
from Instrucciones.Instruccion import Instruccion
from Instrucciones.Select import Select
from Expresion.variablesestaticas import variables

class Execute(Instruccion):
    def __init__(self,nombre,params):
        self.nombre=nombre
        self.params=params

    def ejecutar(self, ent):
        ''
    def traducir(self,ent):
        'traduccion  exec proc'
        lenp=0
        cad=''
        if self.params!=None:
            lenp=len(self.params)

        for i in range(0,lenp):
            if not isinstance(self.params[i],Select):
                cad+='stack.append('+str(self.params[i].traducir(ent).temp)+')\n'


        cad+='goto .Lp_'+self.nombre+'\n'
        nl=ent.newlabel()
        cad+='label '+nl+'\n'
        cad+='stack.append(\''+nl+'\')\n'
        variables.stack.append(nl)
        self.codigo3d=cad
        return self
