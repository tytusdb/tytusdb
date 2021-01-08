from Tipo import Tipo
from Instrucciones.Instruccion import Instruccion

from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.Logica import *
from Expresion.Relacional import *
from Expresion.Expresion import *
from Expresion.Terminal import *
from Expresion.FuncionesNativas import *
from Expresion.variablesestaticas import variables
from tkinter import *
from reportes import *
class Asignacion(Instruccion):
    def __init__(self, nombre,valor):
        self.nombre=nombre
        self.valor=valor

    def ejecutar(self, ent:Entorno):
        'ejecutar asignacion'
        sim=ent.buscarSimbolo(self.nombre)
        if sim==None:
            reporteerrores.append(Lerrores("Error Semantico",
                                           'Error,no existe la variable '+self.nombre,
                                           0, 0))
            variables.consola.insert(INSERT, 'Error,no existe la variable '+self.nombre+'\n')
            return

        util=Tipo(None,None,-1,-1)
        if util.comparetipo(sim.Tipo,self.valor.tipo):
            sim.valor=self.valor.getval()
        else:
            reporteerrores.append(Lerrores("Error Semantico",
                                           'Error,El valor que se desea asignar no coincide con el tipo de la variable '+self.nombre,
                                           0, 0))
            variables.consola.insert(INSERT, 'Error,El valor que se desea asignar no coincide con el tipo sde la variable '+self.nombre+'\n')


    def traducir(self,entorno):
        'traduzco asignacion'
        expval=self.valor.traducir(entorno)
        cad = expval.codigo3d
        cad += self.nombre + '=' + str(expval.temp) + '\n'
        self.codigo3d=cad
        return self
