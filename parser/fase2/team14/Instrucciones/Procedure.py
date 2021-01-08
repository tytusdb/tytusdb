from Entorno.Simbolo import Simbolo
from Expresion.variablesestaticas import variables
from Instrucciones.Instruccion import Instruccion
from Instrucciones.Declaracion import Declaracion
from Expresion.Terminal import Terminal
from Tipo import Tipo
from tkinter import *
class Procedure(Instruccion):
    def __init__(self,nombre,params,instrucciones):
        self.nombre=nombre
        self.params=params
        self.instrucciones=instrucciones


    def ejecutar(self, ent):
        'ejecucion de la definicion del procedimiento'
        simbolo = Simbolo(Tipo('Procedure',None,-1,-1), '_P'+self.nombre, [self.params,self.instrucciones], -1)
        s = ent.nuevoSimbolo(simbolo)
        if s!='ok':
            variables.consola.insert(INSERT,'La funcion '+self.nombre+' no se pudo crear porque ya existe\n')


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
            term=Terminal(Tipo('stack',None,-1,-1),val)
            d=Declaracion(self.params[i].nombre,False,self.params[i].tipo,term)
            c3d=d.traducir(ent).codigo3d
            cad+=c3d
            cont=i

        if self.instrucciones!=None:
            for inst in self.instrucciones:
                if inst !=None:
                    c3d= inst.traducir(ent).codigo3d
                    cad+=c3d
        cad+='temp=stack['+str(lenparams)+']\n'
        cad+='stack=[]\n'
        cad+='goto temp\n'
        cad+='label ' +nl+'\n'
        self.codigo3d=cad
        self.ejecutar(ent)
        return self

class DropProcedure(Instruccion):
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self, ent):
        res = ent.eliminarSimbolo('_P' + self.nombre)
        if res == 'ok':
            variables.consola.insert(INSERT, 'Se elimino el Procedimiento ' + self.nombre + '\n')

    def traducir(self, entorno):
        self.ejecutar(entorno)
        cad = 'ci.ejecutarsql(\"DROP procedure ' + self.nombre + ';\")\n'
        self.codigo3d = cad
        return self
