
from Instrucciones.Instruccion import Instruccion

from Entorno.Simbolo import Simbolo


from Expresion.FuncionesNativas import *

class Declaracion(Instruccion):
    def __init__(self, id=None,constant=False,tipo=None,valor=None,nullable=True):

        self.id=id
        self.constant=constant
        self.tipo=tipo
        self.valor=valor
        self.nullable=nullable

    def ejecutar(self, ent:Entorno):
        'ejecutar declaracion'
        simbolo=Simbolo(self.tipo,self.id,self.valor.getval(ent).valor,-1)
        simbolo.atributos = {'constant': self.constant, 'nullable': self.nullable}
        s=ent.nuevoSimbolo(simbolo)

    def traducir(self,entorno):
        if self.valor==None and self.nullable==True:
            cad=self.id+'=' 'None\n'
        elif self.valor!=None:
            exp=self.valor.traducir(entorno)
            cad=exp.codigo3d
            cad+=self.id+'='+str(exp.temp)+'\n'

        self.codigo3d=cad
        return self