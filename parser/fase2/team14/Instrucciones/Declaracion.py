import Instrucciones
from Instrucciones.Instruccion import Instruccion

from Entorno.Simbolo import Simbolo
from Entorno.Entorno import Entorno


class Declaracion(Instruccion):
    def __init__(self, id=None,constant=False,tipo=None,valor=None,nullable=True):

        self.id=id
        self.constant=constant
        self.tipo=tipo
        self.valor=valor
        self.nullable=nullable

    def ejecutar(self, ent:Entorno):
        'ejecutar declaracion'
        if self.valor!=None:
            if isinstance(self.valor,Instrucciones.Select.Select):
                val=self.valor.ejecutar(ent,0)
                val=val=val[1][0]
                simbolo=Simbolo(self.tipo,self.id,val[0],-1)
            else:
                if self.valor.tipo.tipo=='stack':
                    self.valor.valor=self.valor.valor.replace('\'','')
                simbolo = Simbolo(self.tipo, self.id, self.valor.getval(ent).valor, -1)

        else:
            simbolo = Simbolo(self.tipo, self.id, None, -1)
        simbolo.atributos = {'constant': self.constant, 'nullable': self.nullable}
        s=ent.nuevoSimbolo(simbolo)

    def traducir(self,entorno):
        if self.valor==None and self.nullable==True:
            cad=self.id+'=' '\'\'\n'
        elif self.valor!=None:
            exp=self.valor.traducir(entorno)
            cad=exp.codigo3d
            cad+=self.id+'='+str(exp.temp)+'\n'

        self.codigo3d=cad

        sql='DECLARE '
        sql+=self.id
        if self.constant==True:
            sql+=' constant '
        else:
            sql+=' '
        sql+=self.tipo.tipo
        if self.valor !=None:
            sql+=' = '+self.valor.traducir(entorno).stringsql
        if self.nullable==False:
            sql+=' not null'
        sql += ';'
        self.stringsql=sql

        return self





