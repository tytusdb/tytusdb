from Instrucciones.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from storageManager import jsonMode as DBMS
from Tipo import Tipo
from Expresion.variablesestaticas import variables
from tkinter import *

class Select(Instruccion):
    'This is an abstract class'

    def __init__(self,distinct=None,exps=None,froms=None,where=None,group=None,having=None,order=None,limit=None,combinging=None):
        self.distinct=distinct
        self.exps=exps
        self.froms=froms
        self.where=where
        self.group=group
        self.having=having
        self.order=order
        self.limit=limit
        self.combinig=combinging


    def ejecutar(self,ent:Entorno):
            'Metodo Abstracto para ejecutar la instruccion'
            if self.distinct is None and self.froms is None and self.where is None and self.group is None and self.having is None and self.order is None and self.combinig is None:
                resultados = [];
                for exp in self.exps:
                    if exp != None:
                        resultados.append(exp.getval(ent))
                return resultados
            elif self.froms != None and self.exps!= None:
                tablas=[]
                for exp in self.froms:
                    if exp != None:
                        tipo =exp.tipo;
                        if tipo.tipo=='identificador':
                            nombre=exp.getval(ent)
                            tabla=ent.buscarSimbolo(nombre)
                            if tabla!=None:
                                tablas.append(tabla)

                #filtros




                #acceder a columnas
                if len(self.exps) == 1:
                    if self.exps[0].getval(ent) == '*':
                        result=[]
                        nametable = []
                        for tabla in tablas:
                            nametable.append(tabla.nombre)
                            result.append(DBMS.extractTable(ent.getDataBase(),tabla.nombre))
                        
                        for a in range(0,len(result)):
                            data = result[a]
                            cols = len(data[0])
                            
                            fields = []
                            for c in range(0,cols):
                                fields.append("Columna "+str(c+1))
                            
                            variables.consola.insert(INSERT,"Ejecutando select * para la tabla: "+nametable[a])
                            variables.consola.insert(INSERT,"\n")
                            variables.x.title="Tabla: "+nametable[a]
                            variables.x.field_names = fields
                            variables.x.add_rows(data)
                            variables.consola.insert(INSERT,variables.x)
                            variables.x.clear()
                            variables.consola.insert(INSERT,"\n")
                    return "Instrucción Select Exitoso"
