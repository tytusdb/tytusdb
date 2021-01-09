from Expresion.Id import Identificador
from Instrucciones.Instruccion import Instruccion
from Instrucciones.AtrColumna import AtributosColumna
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.Logica import Logica
from Expresion.Aritmetica import Aritmetica
from Expresion.Unaria import  Unaria
from Expresion.FuncionesNativas import FuncionesNativas
from Expresion.Terminal import Terminal
from Expresion.Relacional import Relacional
from Expresion.variablesestaticas import variables
from tkinter import *
from enum import Enum
from reportes import *

class Delete(Instruccion):
    encabezado=[]
    def __init__(self,tabla,where):
        self.tabla = tabla
        self.where = where

    def ejecutar(self,ent:Entorno):
        self.encabezado.clear()
        resultfiltro=[]
        resultfiltro.clear()
        llavesprim=[]
        llavesprim.clear()
        dbActual = ent.getDataBase()
        result=[]
        result.clear()

        if dbActual != None:
            tabla:Simbolo = ent.buscarSimbolo(self.tabla + "_" + dbActual)
            if tabla!= None:
                'obtengo tabla'
                real = tabla.nombre.replace('_' + ent.getDataBase(), '')
                result = DBMS.extractTable(ent.getDataBase(), real)
                columnas=tabla.valor
                'lleno encabezado'
                for col in columnas:
                    self.encabezado.append(col.nombre)


                for i in range(0, len(result)):
                    resexp = self.resolver(self.where, ent, result, tabla, i)
                    try:
                        if not resexp.valor:
                            resultfiltro.append(result[i])
                            'envio datos para delete'
                            llavePrim = []
                            for column in tabla.valor:
                                prim: Simbolo = ent.buscarSimbolo(column.atributos.get('primary'))
                                if prim!=None:
                                    llavePrim = prim.valor
                                    break

                    except:
                        reporteerrores.append(Lerrores("Error Semantico",'Error el resultado del where no es booleano',0, 0))
                        variables.consola.insert(INSERT, 'Error el resultado del where no es booleano \n')

                llavesprim = llavePrim
                self.resultdelete(resultfiltro,self.tabla,ent.getDataBase(),llavesprim)
            else:
                variables.consola.insert(INSERT,"La tabla '" + self.tabla + "' que desea eliminar no existe\n")
                reporteerrores.append(Lerrores("Error Semántico","La tabla '" + self.tabla + "' que desea eliminar no existe","",""))

    def resultdelete(self, result, nomresult, DB,llaves):
        if not len(result) > 0:
            return ("En la instrucción Delete no hay registros que cumplan la expresión")
        else:
            if not len(llaves)>0:
                columnas = len(self.encabezado)
                DBMS.dropTable(DB, nomresult)
                DBMS.createTable(DB, nomresult, columnas)
                for x in range(0, len(result)):
                    DBMS.insert(DB, nomresult, result[x])
                self.encabezado.clear()
                variables.consola.insert(INSERT, "La instrucción DELETE se realizó exitosamente \n")
                return "La instrucción DELETE se realizó exitosamente"
            else:
                columnas = len(self.encabezado)
                DBMS.dropTable(DB, nomresult)
                DBMS.createTable(DB, nomresult, columnas)
                DBMS.alterAddPK(DB, nomresult, llaves)
                for x in range(0, len(result)):
                    DBMS.insert(DB, nomresult, result[x])
                self.encabezado.clear()
                variables.consola.insert(INSERT, "La instrucción DELETE se realizó exitosamente \n")
                return "La instrucción DELETE se realizó exitosamente"



    def resolver(self, expresion, entorno, result, tabla, fila):
        # para expresion binaria
        if not isinstance(expresion, Terminal) and not isinstance(expresion, Unaria) and not isinstance(expresion,FuncionesNativas) and not isinstance(expresion,Identificador):
            'resuelvo logicas,aritmeticas y relacionales'
            exp1 = expresion.exp1
            exp2 = expresion.exp2
            res1 = self.resolver(exp1, entorno, result, tabla, fila)
            res2 = self.resolver(exp2, entorno, result, tabla, fila)

            op = None
            if isinstance(expresion, Logica):
                op = Logica(res1, res2, expresion.operador)
            if isinstance(expresion, Relacional):
                op = Relacional(res1, res2, expresion.operador)
            if isinstance(expresion, Aritmetica):
                op = Aritmetica(res1, res2, expresion.operador)

            return op.getval(entorno)
        elif isinstance(expresion, Unaria):  # para expresion unaria
            exp = expresion.exp1
            res = self.resolver(exp, entorno, result, tabla, fila)
            op = Unaria(res, expresion.operador)
            return op.getval(entorno)

        else:
            'aqui resuelvo los terminales y funciones'
            if isinstance(expresion, Identificador):
                ''
                term = expresion.getval(entorno)
                if term != None:
                    return term
                else:
                    for i in range(0, len(self.encabezado)):
                        nombrediv = self.encabezado[i].split('.')
                        nombrecol = nombrediv[0]
                        if expresion.nombre == nombrecol:
                            dato = result[fila][i]
                            tipo = None
                            if len(nombrediv) > 1:
                                tipo = self.gettipo(entorno, tabla, nombrediv[0], nombrediv[1])
                            else:
                                tipo = self.gettipo(entorno, tabla, nombrediv[0])
                            term = Terminal(tipo, dato)
                            return term
            elif isinstance(expresion, Terminal):
                if expresion.tipo.tipo == 'acceso':
                    return self.getacceso(entorno, expresion, result, fila, tabla)
                else:
                    return expresion


            elif isinstance(expresion,FuncionesNativas):
                '''if expresion.identificador.lower()=='count':
                    t=Tipo('integer',None,-1,-1)
                    self.agregacion=1
                    return Terminal(t,len(result))'''
                tempexp=[]
                for exp in expresion.expresiones:
                    tempexp.append(exp)

                for j in range(0, len(expresion.expresiones)):
                    if isinstance(expresion.expresiones[j],Identificador):
                        val = expresion.expresiones[j].nombre
                        for i in range(0, len(self.encabezado)):
                            nombrediv = self.encabezado[i].split('.')
                            nombrecol = nombrediv[0]
                            if val == nombrecol:
                                tipo=None
                                if len(nombrediv)>1:
                                    tipo = self.gettipo(entorno, tabla, val,nombrediv[1])
                                else:
                                    tipo = self.gettipo(entorno, tabla, val)
                                dato = result[fila][i]
                                tempexp[j]=Terminal(tipo,dato)
                    func=FuncionesNativas(expresion.identificador, tempexp)
                return func.getval(entorno)

    def gettipo(self, entorno, tabla, col):
        tipo = None
        real = tabla.nombre.replace('_' + entorno.getDataBase(), '')
        columnas = tabla.valor
        i = 0
        for columna in columnas:
            nombre = columna.nombre
            if col == nombre:
                    tipo = columna.tipo
            i = i + 1
        return tipo

    def getacceso(self,entorno,expresion,result,fila,tablas):
        for i in range(0, len(self.encabezado)):
            nombrediv = self.encabezado[i].split('.')

            nombrecol = nombrediv[0]
            nombretabla = nombrediv[1]
            nombrecol = nombretabla + '.' + nombrecol
            if expresion.getval(entorno).valor == nombrecol:
                dato = result[fila][i]
                tipo = None
                if len(nombrediv) > 1:
                    tipo = self.gettipo(entorno, tablas, nombrediv[0], nombrediv[1])
                else:
                    tipo = self.gettipo(entorno, tablas, nombrediv[0])
                term = Terminal(tipo, dato)
                return term

            for x in range(0,len(self.aliast)):
                nombreacc = self.aliast[x] + '.' + nombrediv[0]
                if expresion.getval(entorno).valor == nombreacc and nombrediv[1]== tablas[x].nombre.replace('_' + entorno.getDataBase(), ''):
                    dato = result[fila][i]
                    tipo = None
                    if len(nombrediv) > 1:
                        tipo = self.gettipo(entorno, tablas, nombrediv[0], nombrediv[1])
                    else:
                        tipo = self.gettipo(entorno, tablas, nombrediv[0])
                    term = Terminal(tipo, dato)
                    return term

        return None

    def traducir(self, entorno):
        if(self.tabla!=None or self.tabla!=""):
            self.codigo3d = 'ci.ejecutarsql(\"delete from '+self.tabla

            if self.where != None:
                self.codigo3d += ' Where '
                self.codigo3d += self.where.traducir(entorno).stringsql

            self.codigo3d += ' ;\")\n'
            return self

class Campo():
    def __init__(self,columna,exp):
        self.columna = columna
        self.exp = exp
