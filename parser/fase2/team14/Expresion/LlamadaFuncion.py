from Expresion.Expresion import Expresion
from Instrucciones.Declaracion import Declaracion
from tkinter import *
from reportes import *
from Expresion.variablesestaticas import variables
from Tipo import Tipo
from Entorno.Entorno import Entorno
import Instrucciones

class LLamadaFuncion(Expresion):
    def __init__(self,nombre,parametros):
        self.nombre=nombre
        self.parametros=parametros
        sql=self.nombre +'('
        if self.parametros!=None:
            for i in range(0,len(self.parametros)):
                if i>1:
                    sql+=','
                sql+=self.parametros[i].stringsql

        sql+=')'
        self.stringsql=sql


    def getval(self, ent:Entorno,err=1):
        'ejecucion llamada funcinon'
        sim=ent.buscarSimbolo('_f'+self.nombre)
        if sim != None:
            tipo=sim.tipo
            defparams=sim.valor[0]
            instrucciones=sim.valor[1]
            newent=Entorno(ent)
            if self.parametros!=None and defparams!=None:
                if len(defparams)==len(self.parametros):
                    for i in range(0,len(defparams)):
                        param=defparams[i]
                        dec=Declaracion(param.nombre,False,param.tipo,self.parametros[i])
                        dec.ejecutar(newent)
                    for inst in instrucciones:
                        v=  inst.ejecutar(newent)
                        if v!=None:
                            util=Tipo('',None,-1,-1)
                            if util.comparetipo(v.tipo,tipo):
                                return v
                            else:
                                reporteerrores.append(Lerrores("Error Semantico", "Error el tipo devuelto no coincide con el de la funcion",  0, 0))
                                variables.consola.insert(INSERT, "Error el tipo devuelto no coincide con el de la funcion\n")

                else:
                    reporteerrores.append(Lerrores("Error Semantico","Error Los parametros no coinciden con la definicion de la funcion",0, 0))
                    variables.consola.insert(INSERT,"Error Los parametros no coinciden con la definicion de la funcion\n")
                    return
            else:
                for inst in instrucciones:
                    v = inst.ejecutar(newent)
                    if v != None:
                        util = Tipo('', None, -1, -1)
                        if util.comparetipo(v.tipo, tipo):
                            return v
                        else:
                            reporteerrores.append(
                                Lerrores("Error Semantico", "Error el tipo devuelto no coincide con el de la funcion",
                                         0, 0))
                            variables.consola.insert(INSERT, "Error el tipo devuelto no coincide con el de la funcion\n")
        else:
            if err==1:
                reporteerrores.append(
                    Lerrores("Error Semantico", "Error la funcion '"+self.nombre+"' no existe",
                             0, 0))
                variables.consola.insert(INSERT, "Error la funcion '"+self.nombre+"' no existe\n")



    def traducir(self,ent):
        lenp = 0
        cad = ''
        if self.parametros != None:
            lenp = len(self.parametros)

        for i in range(0, lenp):
                ''
                #cad += 'stack.append(' + str(self.params[i].traducir(ent).temp) + ')\n'#
        nl = ent.newlabel()
        #cad += 'stack.append(\'' + nl + '\')\n'
        #variables.stack.append('\'' + nl + '\'')
        #cad += 'goto .Lp_' + self.nombre + '\n'
        cad += 'label ' + nl + '\n'
        self.codigo3d = cad

        #quemado
        strsql=self.nombre+'('
        if self.parametros!=None:
            for i in range(0,len(self.parametros)):
                if i>1:
                    strsql+=','
                strsql+=self.parametros[i].traducir(ent).stringsql
        strsql+=') '
        self.stringsql=strsql

        return self

