from Instrucciones.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from storageManager import jsonMode as DBMS
from Expresion.Terminal import Terminal
from Expresion.Unaria import Unaria
from Expresion.Relacional import Relacional
from Expresion.Logica import Logica
from Expresion.Expresion import Expresion
from Expresion.variablesestaticas import variables
from Expresion.FuncionesNativas import FuncionesNativas
from Expresion.Aritmetica import Aritmetica
from tkinter import *
from reportes import *
import copy


class Select(Instruccion):
    'This is an abstract class'
    encabezado = []
    nombreres = ''

    def __init__(self, distinct=None, exps=None, froms=None, where=None, group=None, having=None, combinging=None,order=None, limit=None):
        self.distinct = distinct
        self.exps = exps
        self.froms = froms
        self.where = where
        self.group = group
        self.having = having
        self.order = order
        self.limit = limit
        self.combinig = combinging

    def ejecutar(self, ent: Entorno,imp=1):
        try:
            tablas = []
            result = []
            self.encabezado = []

            'Metodo Abstracto para ejecutar la instruccion'
            if self.distinct is None and self.froms is None and self.where is None and self.group is None and self.having is None and self.order is None and self.combinig is None:
                resultados = [];
                for exp in self.exps:
                    if exp != None:

                        res = exp.getval(ent)

                        resultados.append(res.valor)
                    variables.consola.insert(INSERT,str(res.valor))
                    variables.consola.insert(INSERT, '\n')
                return resultados
            elif self.froms != None and self.exps != None:

                for exp in self.froms:
                    if exp != None:
                        tipo = exp.tipo;
                        if tipo.tipo == 'identificador':
                            nombre = exp.getval(ent).valor
                            self.nombreres = nombre
                            tabla = ent.buscarSimbolo(nombre + "_" + ent.getDataBase())
                            if tabla != None:
                                tablas.append(tabla)
                            else:
                                reporteerrores.append(Lerrores("Error Semantico",
                                                               "ERROR >> En la instrucción Select, la tabla: " + nombre + " NO EXISTE",
                                                               0, 0))
                                variables.consola.insert(INSERT,
                                                         "ERROR >> En la instrucción Select, la tabla: " + nombre + " NO EXISTE\n")
                        else:
                            reporteerrores.append(Lerrores("Error Semantico",
                                                           "ERROR >> En la instrucción Select, ingreso un nombre de tabla incorrecto",
                                                           0, 0))
                            variables.consola.insert(INSERT,
                                                     "ERROR >> En la instrucción Select, ingreso un nombre de tabla incorrecto\n")
                    else:
                        return ("Algo paso")

                if len(tablas) > 1:
                    'Obteniendo encabezados de las tablas'
                    postab = 1
                    for tabla in tablas:
                        cols = tabla.valor
                        for columna in cols:
                            nombre = columna.nombre
                            self.encabezado.append(nombre + ".T" + str(postab))
                        postab = postab + 1

                    'producto cartesiano'
                    real = tablas[0].nombre.replace('_' + ent.getDataBase(), '')
                    result = DBMS.extractTable(ent.getDataBase(), real)
                    self.nombreres = real + "(T1)"
                    for i in range(0, len(tablas) - 1):
                        real2 = tablas[i + 1].nombre.replace('_' + ent.getDataBase(), '')
                        self.nombreres += '_' + real2 + "(T" + str(i + 2) + ")"
                        tabla2 = DBMS.extractTable(ent.getDataBase(), real2)
                        result = self.producto(result, tabla2)
                else:
                    'llenar resultado desde backend'
                    real = tablas[0].nombre.replace('_' + ent.getDataBase(), '')
                    result = DBMS.extractTable(ent.getDataBase(), real)

                'encabezados'
                if (len(self.encabezado) == 0):
                    for tabla in tablas:
                        cols = tabla.valor
                        for columna in cols:
                            nombre = columna.nombre
                            self.encabezado.append(nombre)

                # filtros
                if self.where != None:
                    result = self.optwhere(ent,result,tablas)
                # combining(union,intersect,except)
                if self.combinig != None:
                    datos2 = self.combinig.select.ejecutar(ent, 0)
                    enc2 = datos2[0]
                    res2 = datos2[1]
                    result = self.m_combining(self.combinig, self.encabezado, result, enc2, res2)
                    aber = result
                # limitar resultados
                if self.limit != None:
                    a = self.limit
                    result = self.m_limit(result, a.limit, a.off)

                # acceder a columnas
                if len(self.exps) == 1:
                    if self.exps[0].getval(ent).valor == '*':
                        if imp == 1:
                            self.mostarresult(result, self.encabezado, self.nombreres)
                    elif self.exps[0].tipo.tipo == 'identificador':
                        newenc = []
                        'obtengo  solo columnas pedidas'
                        for i in range(0, len(self.encabezado)):
                            nombrediv = self.encabezado[i].split('.')
                            nombrecol = nombrediv[0]
                            if self.exps[0].getval(ent).valor == nombrecol:
                                for x in range(0, len(result)):
                                    valcol = result[x][i]
                                    result[x] = [valcol]
                                    if (len(newenc) == 0):
                                        newenc.append(self.encabezado[i])
                        self.encabezado = newenc
                        if imp == 1:
                            self.mostarresult(result, newenc, self.nombreres)
                    else:
                        'pendientes subconsultas y funciones'
                else:
                    newenc = []
                    newres = []
                    for i in range(0, len(self.exps)):
                        if self.exps[i].tipo.tipo == 'identificador':
                            for j in range(0, len(self.encabezado)):
                                nombrediv = self.encabezado[j].split('.')
                                nombrecol = nombrediv[0]
                                if self.exps[i].getval(ent).valor == nombrecol:
                                    newenc.append(self.encabezado[j])
                                    for x in range(0, len(result)):
                                        valcol = result[x][j]
                                        if len(newres) != len(result):
                                            newres.append([valcol])
                                        else:
                                            newres[x].append(valcol)
                    result = newres
                    self.encabezado = newenc
                    if imp == 1:
                        self.mostarresult(newres, newenc, self.nombreres)
                if self.distinct!=None:
                    newres=[]
                    'elimino duplicados'
                    for i in range(0,len(result)):
                        encontrado=False
                        fila=result[i]
                        for j in range(0,len(result)):
                            if j!= i:
                               if fila==result[j]:
                                   encontrado=True
                        if encontrado==False:
                            newres.append(fila)
                    result=newres

            return [self.encabezado, result]

        except  Exception as inst:
            print(inst)
            return


    def mostarresult(self, result,enc, nomresult):
        if not len(result) > 0:
            return "Instrucción Select realizada, No hay registros que cumplan la condición especificada \n"
        else:
            variables.consola.insert(INSERT, "Ejecutando select para la tabla: " + nomresult)
            variables.consola.insert(INSERT, "\n")
            variables.x.title = nomresult
            variables.x.field_names = enc
            variables.x.add_rows(result)
            variables.consola.insert(INSERT, variables.x)
            variables.x.clear()
            variables.consola.insert(INSERT, "\n")

            return ("Instrucción Select realizada con exito")

    def producto(self, tablaacum, tabla2):
        'realizacion producto cartesiano de tablas'
        result = []
        for i in range(0, len(tablaacum)):
            for j in range(0, len(tabla2)):
                result.append(tablaacum[i] + tabla2[j])

        return result

    def optwhere(self,entorno,result,tablas):
        newres=[]
        for i in range(0,len(result)):
            resexp=self.resolver(self.where,entorno,result,tablas,i)
            try:
                if resexp.valor:
                    newres.append(result[i])
            except:
                reporteerrores.append(Lerrores("Error Semantico",
                                               'Error el resultado del where no es booleano',
                                               0, 0))
                variables.consola.insert(INSERT, 'Error el resultado del where no es booleano \n')

        return newres


    def resolver(self,expresion,entorno,result,tablas,fila):
        #para expresion binaria
        if not isinstance(expresion,Terminal) and not isinstance(expresion,Unaria) and not isinstance(expresion,FuncionesNativas):
            'resuelvo logicas,aritmeticas y relacionales'
            exp1=expresion.exp1
            exp2=expresion.exp2
            res1=self.resolver(exp1,entorno,result,tablas,fila)
            res2=self.resolver(exp2,entorno,result,tablas,fila)

            op=None
            if isinstance(expresion,Logica):
                op=Logica(res1, res2, expresion.operador)
            if isinstance(expresion,Relacional):
                op =Relacional(res1, res2, expresion.operador)
            if isinstance(expresion,Aritmetica):
                op =Aritmetica(res1, res2, expresion.operador)

            return op.getval(entorno)
        elif isinstance(expresion,Unaria): #para expresion unaria
            exp=expresion.exp1
            res= self.resolver(exp,entorno,result,tablas,fila)
            op = Unaria(res,expresion.operador)
            return op

        else:
            'aqui resuelvo los terminales y funciones'
            if isinstance(expresion,Terminal):
                if expresion.tipo.tipo=='identificador':
                    for i in range(0, len(self.encabezado)):
                        nombrediv = self.encabezado[i].split('.')
                        nombrecol = nombrediv[0]
                        if expresion.getval(entorno).valor == nombrecol:
                            dato=result[fila][i]
                            tipo=self.gettipo(entorno,tablas,nombrecol)
                            term=Terminal(tipo,dato)
                            return term
                else:
                    return expresion

            elif isinstance(expresion,FuncionesNativas):
                tempexp=[]
                for exp in expresion.expresiones:
                    tempexp.append(exp)

                for j in range(0, len(expresion.expresiones)):
                    if expresion.expresiones[j].tipo.tipo == 'identificador':
                        val = expresion.expresiones[j].getval(entorno).valor
                        for i in range(0, len(self.encabezado)):
                            nombrediv = self.encabezado[i].split('.')
                            nombrecol = nombrediv[0]
                            if val == nombrecol:
                                tipo = self.gettipo(entorno, tablas, val)
                                dato = result[fila][i]
                                tempexp[j]=Terminal(tipo,dato)
                return FuncionesNativas(expresion.identificador,tempexp)


    def gettipo(self,entorno,tablas,col):
        tipo = None
        for tabla in tablas:
            columnas = tabla.valor
            i = 0
            for columna in columnas:
                nombre = columna.nombre
                if col == nombre:
                    if(tipo==None):
                        tipo = columna.tipo
                    else:
                        return None
                i = i + 1
        return tipo


    '''def group(self):
        'Ejecucucion del group'
    def having(self):
        'Ejecucucion del having'
    def order(self):
        'Ejecucucion del order'''

    def m_limit(self,result,limit,off):
        if str(limit).lower=='all':
            limit=len(result)

        if off <0 or off>len(result) :
            off=0

        if limit<0 or limit > len(result):
            limit= len(result)
        datos=[]
        for i in range(off,off+limit):
            datos.append(result[i])

        return datos


    def m_combining(self,combi,enc1,res1,enc2,res2):
        if len(enc1) == len(enc2):
            if combi.combi.lower() == 'union':
                if combi.all == 'all':
                    if len(enc1) == len(enc2):
                        return res1 + res2

                else:
                    result=[]
                    for i in range(0, len(res1)):
                        result.append(res1[i])
                    esta = False
                    for i in range(0, len(res2)):
                        for j in range(0, len(result)):
                            if result[j] == res2[i]:
                                esta = True
                        if not esta:
                            result.append(res2[i])
                    return result


            elif combi.combi.lower() == 'intersect':
                result = []
                for i in range(0, len(res1)):
                    for j in range(0, len(res2)):
                        if res1[i] == res2[j]:
                            result.append(res1[i])
                return result

            elif combi.combi.lower() == 'except':
                result = []

                for i in range(0, len(res1)):
                    esta = False
                    for j in range(0, len(res2)):
                        if res1[i] == res2[j]:
                            esta = True
                    if esta==False:
                        result.append(res1[i])
                return result
        else:
            reporteerrores.append(Lerrores("Error Semantico",'Error union,intersect, solo se puede hacer con la misma cantidad de columnas', 0, 0))
            variables.consola.insert(INSERT,'Error union,intersect, solo se puede hacer con la misma cantidad de columnas\n')
        return []


class Limit():
    def __init__(self,limit=-1,off=-1):
        self.limit=limit
        self.off=off

class Combi():
    def __init__(self,combi,select,all=''):
        self.combi=combi
        self.select=select
        self.all=all
