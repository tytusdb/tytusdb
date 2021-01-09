from Entorno.Simbolo import Simbolo
from Instrucciones.Instruccion import Instruccion
from Expresion.variablesestaticas import variables
from tkinter import  *
from Expresion.Terminal import Terminal
from Instrucciones.Declaracion import Declaracion
from Tipo import Tipo
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
        if s!='ok':
            variables.consola.insert(INSERT,'La funcion '+self.nombre+' no se pudo crear porque ya existe\n')


    def traducir(self,ent):
        'traduccion func'
        nl = ent.newlabel()
        cad = 'goto ' + nl + '\n'
        cad += 'label ' + ent.newlabel('f_' + self.nombre) + '\n'
        cont = 0
        lenparams = 0
        if self.params != None:
            lenparams = len(self.params)

        for i in range(0, lenparams):
            val = 'stack[' + str(i) + ']'
            term = Terminal(Tipo('stack', None, -1, -1), val)
            d = Declaracion(self.params[i].nombre, False, self.params[i].tipo, term)
            c3d = d.traducir(ent).codigo3d
            cad += c3d
            cont = i

        if self.instrucciones != None:
            for inst in self.instrucciones:
                if inst != None:
                    c3d = inst.traducir(ent).codigo3d
                    cad += c3d
        cad += 'temp=stack[' + str(lenparams) + ']\n'
        cad += 'stack=[]\n'
        cad += 'goto temp\n'
        cad += 'label ' + nl + '\n'
        self.codigo3d = cad

        # string quemado
        sql= 'ci.ejecutarsql("create function ' + self.nombre + '('
        if self.params != None:
            for i in range(0,len(self.params)):
                if i > 0:
                    sql += ','
                if self.params[i].modo != None:
                    sql += 'inout '

                sql += self.params[i].nombre + ' ' + self.params[i].tipo.tipo

        sql += ') returns ' + self.tipo.tipo+' as $$ '

        if self.instrucciones!=None:
            for ins in self.instrucciones:
                sql+=ins.traducir(ent).stringsql
        sql+=' $$ language plpgsql;\")\n'
        self.codigo3d=sql+self.codigo3d
        return self





class DropFunction(Instruccion):
    def __init__(self,nombre):
        self.nombre=nombre

    def ejecutar(self,ent):
        res= ent.eliminarSimbolo('_f'+self.nombre)
        if res=='ok':
            variables.consola.insert(INSERT,'Se elimino la funcion '+self.nombre +'\n')
    def traducir(self,entorno):
        cad='ci.ejecutarsql(\"DROP function '+self.nombre+';\")\n'
        self.codigo3d=cad
        return self

class Parametro():
    def __init__(self,nombre,modo,tipo):
        self.nombre=nombre
        self.modo=modo
        self.tipo=tipo

