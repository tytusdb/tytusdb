
from Instrucciones.Instruccion import Instruccion

from Expresion.Relacional import *



class Raise(Instruccion):
    def __init__(self,level,exp):
        self.level=level
        self.exp=exp

    def ejecutar(self, ent):
        'ejecutar raise'
        if self.level == 'notice':
            variables.consola.insert(INSERT, 'NOTIFICACION: '+str(self.exp.getval(ent).valor))
            variables.consola.insert(INSERT, "\n")

    def traducir(self,entorno):
        'traduzco raise'
        if self.level=='notice':
            exp=self.exp.traducir(entorno)
            cad = exp.codigo3d
            cad += 'print (' + exp.temp + ') \n'
            self.codigo3d = cad
            self.stringsql=' raise notice '+self.exp.traducir(entorno).stringsql+';'
        return self

