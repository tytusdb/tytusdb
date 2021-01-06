
from Instrucciones.Instruccion import Instruccion
from Instrucciones.Declaracion import Declaracion
from Expresion.Terminal import Terminal
from Tipo import Tipo

class Procedure(Instruccion):
    def __init__(self,nombre,params,instrucciones):
        self.nombre=nombre
        self.params=params
        self.instrucciones=instrucciones


    def ejecutar(self, ent):
        ''
    def traducir(self,ent):
        'traduccion proc'
        nl=ent.newlabel()
        cad='goto ' + nl+'\n'
        cad+='label '+ent.newlabel('p_'+self.nombre)+'\n'
        cont=0
        lenparams=0
        if self.params != None:
            lenparams=len(self.params)

        for i in range(0,lenparams):
            val='stack['+str(i)+']'
            term=Terminal(Tipo('staesqck',None,-1,-1),val)
            d=Declaracion(self.params[i].nombre,False,self.params[i].tipo,term)
            c3d=d.traducir(ent).codigo3d
            cad+=c3d
            cont=i

        if self.instrucciones!=None:
            for inst in self.instrucciones:
                if inst !=None:
                    c3d= inst.traducir(ent).codigo3d
                    cad+=c3d
        cad+='stack=[]\n'
        cad+='goto temp\n'
        cad+='label ' +nl+'\n'
        self.codigo3d=cad
        return self

class Parametro():
    def __init__(self,nombre,modo,tipo):
        self.nombre=nombre
        self.modo=modo
        self.tipo=tipo
