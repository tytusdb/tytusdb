from Expresion.Expresion import Expresion
from datetime import date
from datetime import datetime
from Entorno import Entorno
import random as rn
from Tipo import  Tipo
import math

class Identificador(Expresion) :
    '''
        Esta clase representa un terminal.
    '''
    def __init__(self,tipo,nombre='') :
        Expresion.__init__(self)
        self.tipo=tipo
        self.nombre=nombre
        self.valor=nombre


    def getval(self,entorno:Entorno):
        sim=entorno.buscarSimbolo(self.nombre)
        if sim != None:
            return sim

        return None
    def traducir(self,entorno):
        ''
        self.temp=self.nombre
        self.stringsql = self.nombre
        return self

