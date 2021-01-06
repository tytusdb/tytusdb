from Entorno.Simbolo import Simbolo
from Instrucciones.Instruccion import Instruccion

class Funcion(Instruccion):
    def __init__(self,nombre,params,instrucciones,tipo=None):
        self.nombre=nombre
        self.params=params
        self.instrucciones=instrucciones
        self.tipo=tipo

    def ejecutar(self, ent):
        'ejecucion de la definicion de la funcion'
        simbolo = Simbolo(self.tipo, '_f'+self.nombre, [self.params,self.instrucciones], -1)
        s = ent.nuevoSimbolo(simbolo)


class Parametro():
    def __init__(self,nombre,modo,tipo):
        self.nombre=nombre
        self.modo=modo
        self.tipo=tipo

