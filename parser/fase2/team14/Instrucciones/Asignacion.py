
from Instrucciones.Instruccion import Instruccion
from Tipo import Tipo
from Expresion.variablesestaticas import variables
from tkinter import *
from reportes import *
from Instrucciones.Select import Select
from Expresion.Terminal import Terminal

class Asignacion(Instruccion):
    def __init__(self, nombre,valor):
        self.nombre=nombre
        self.valor=valor

    def ejecutar(self, ent):
        'ejecutar asignacion'
        sim=ent.buscarSimbolo(self.nombre)
        if sim==None:
            reporteerrores.append(Lerrores("Error Semantico",
                                           'Error,no existe la variable '+self.nombre,
                                           0, 0))
            variables.consola.insert(INSERT, 'Error,no existe la variable '+self.nombre+'\n')
            return

        util=Tipo(None,None,-1,-1)
        if isinstance(self.valor,Select):
            val=self.valor.ejecutar(ent,0)
            val=val[1][0]
            self.valor=Terminal(sim.tipo,val[0])
        if isinstance(self.valor,Terminal):
            sim.valor=self.valor.getval(ent).valor
            ent.editarSimbolo(self.nombre, sim)

        else:
            self.valor=self.valor.getval(ent)
            sim.valor=self.valor.getval(ent).valor
            ent.editarSimbolo(self.nombre, sim)



    def traducir(self,entorno):
        'traduzco asignacion'
        expval=self.valor.traducir(entorno)
        cad = expval.codigo3d
        cad += self.nombre + '=' + str(expval.temp) + '\n'
        self.codigo3d=cad

        sql=self.nombre
        if self.valor != None:
            sql += ' = ' + self.valor.stringsql
        sql += ';'
        self.stringsql=sql
        return self
