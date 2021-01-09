
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
            if not isinstance(self.params[i],Select) :
                param=str(self.params[i].traducir(ent).temp)
                if  not self.isnumber(param):
                    cad+='stack.append(\"'+param+'\")\n'
        nl = ent.newlabel()
        cad += 'stack.append(\'' + nl + '\')\n'
        variables.stack.append('\''+nl+'\'')
        cad+='goto .Lp_'+self.nombre+'\n'
        cad+='label '+nl+'\n'
        self.codigo3d=cad
        return self

    def isnumber(self,char):
        if type(char)  in (int, float, complex):
            return True
        else:
            return False
