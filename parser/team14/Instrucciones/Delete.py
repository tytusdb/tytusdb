from Instrucciones.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from storageManager import jsonMode as DBMS
from Expresion.Terminal import Terminal
from Expresion.Unaria import Unaria
from Expresion.Relacional import  Relacional
from Expresion.Logica import Logica
from Expresion.Expresion import Expresion
from Expresion.variablesestaticas import variables
from tkinter import *
import copy
from Instrucciones.Select import Select

class Delete(Instruccion):
    'This is an abstract class'
    nombreres=''
    ntabla = ""
    encabezados = []
    def __init__(self,nametable=None,exps=None):
        self.nametable = nametable
        self.exps = exps


    def ejecutar(self,ent:Entorno):
        tablas = []
        result = []
        self.encabezados = []
        if self.nametable != None:
            tipo = self.nametable.tipo
            if tipo.tipo == 'identificador':
                nombre = self.nametable.getval(ent)
                self.ntabla = nombre
                tabla = ent.buscarSimbolo(nombre + "_" + ent.getDataBase())
                if tabla != None:
                    tablas.append(tabla)
                else:
                    return "ERROR >> En la instrucción Delete, la tabla: "+self.ntabla+" NO EXISTE"

        if len(tablas) > 1:
            return "ERROR >> En la instrucción Delete, solo puede ingresar el nombre de una tabla"
        else:
            'llenar resultado desde backend'
            real = tablas[0].nombre.replace('_' + ent.getDataBase(), '')
            result = DBMS.extractTable(ent.getDataBase(), real)

            # filtros
            if self.exps != None:
                result = self.wheredelete(ent, tablas)
            else:
                return "ERROR >> En la instrucción Delete la expresión es incorrecta"

            return self.resultdelete(result,self.ntabla,ent.getDataBase())

    def resultdelete(self,result,nomresult,DB):
            if not len(result)>0:
                return ("En la instrucción Delete no hay registros que cumplan la expresión")
            else:
                columnas = len(self.encabezados)
                print(DBMS.dropTable(DB, nomresult))
                print(DBMS.createTable(DB, nomresult, columnas))
                for x in range(0,len(result)):
                    DBMS.insert(DB,nomresult,result[x])
                self.encabezados.clear()
                return "La instrucción DELETE se realizó exitosamente"


    def wheredelete(self,entorno,tablas):
        filtrado=[]
        exp1:Expresion
        exp2:Expresion
        colres=[]
        tipo=''
        isid=False
        posid=-1
        if isinstance(self.exps, Relacional) or isinstance(self.exps,Logica):
            encontrado=0
            nocol=-1
            nomtabla=''
            'realizar operacion'
            exp1=self.exps.exp1
            exp2=self.exps.exp2
            op=self.exps.operador

            if (op==">"):
                op="<"
            elif (op=="<"):
                op=">"
            elif (op=="!="):
                op="="
            elif (op=="="):
                op="!="
            elif (op==">="):
                op="<="
            elif (op=="<="):
                op=">="
            else:
                print("")

            val=''
            if (exp1.tipo.tipo=='identificador'):
                val = exp1.getval(entorno)
                posid = 1
            else:
                return ("ERROR >> En la instrucción Delete hay problema con la expresión, debe ingresar un identificador antes del operador")

            for tabla in tablas:
                columnas=tabla.valor
                i=0
                for columna in columnas:
                    nombre = columna.nombre
                    self.encabezados.append(nombre)
                    if val == nombre:
                        encontrado+=1
                        tipo=columna.tipo
                        nocol=i
                        nomtabla=tabla.nombre
                        nomtabla=nomtabla.replace('_'+entorno.getDataBase(),'')
                        continue
                    i=i+1
            if encontrado==1 and nocol>-1:
                datos=DBMS.extractTable(entorno.getDataBase(),nomtabla)
                if datos!= None:
                    self.nombreres = nomtabla
                    for i in range(0,len(datos)):
                        dato=datos[i][nocol]

                        expi = Terminal(tipo, dato)
                        expd = exp2

                        if op in ('>','<','>=','<=','='):
                            nuevaop = Relacional(expi,expd,op);
                            if nuevaop.getval(entorno):
                                'Agrego la fila al resultado'
                                filtrado.append(datos[i])
                        elif op in ('or','and','not'):
                            nuevaop = Logica(expi,expd,op);
                            if nuevaop.getval(entorno):
                                'Agrego la fila al resultado'
                                filtrado.append(datos[i])
                        else:
                            return ('ERROR >> En la instrucción Delete, el resultado del where no es booleano')
                    return filtrado
            else:
                return ("ERROR >> En la instrucción Delete, el nombre de las columnas es ambiguo")
        else:
            return ("ERROR >> En la instrucción Delete, no ingreso una expresión relacional")