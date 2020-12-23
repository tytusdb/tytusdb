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
from tkinter import *
import copy


class Select(Instruccion):
    'This is an abstract class'
    encabezado = []
    nombreres = ''

    def __init__(self, distinct=None, exps=None, froms=None, where=None, group=None, having=None, combinging=None,
                 order=None, limit=None):
        self.distinct = distinct
        self.exps = exps
        self.froms = froms
        self.where = where
        self.group = group
        self.having = having
        self.order = order
        self.limit = limit
        self.combinig = combinging

    def ejecutar(self, ent: Entorno):
        tablas = []
        result = []
        self.encabezado = []

        'Metodo Abstracto para ejecutar la instruccion'
        if self.distinct is None and self.froms is None and self.where is None and self.group is None and self.having is None and self.order is None and self.combinig is None:
            resultados = [];
            for exp in self.exps:
                if exp != None:

                    res=exp.getval(ent)
                    if isinstance(res,Terminal):
                        res=res.getval(ent)
                    resultados.append(res)

            return resultados
        elif self.froms != None and self.exps != None:

            for exp in self.froms:
                if exp != None:
                    tipo = exp.tipo;
                    if tipo.tipo == 'identificador':
                        nombre = exp.getval(ent)
                        self.nombreres = nombre
                        tabla = ent.buscarSimbolo(nombre + "_" + ent.getDataBase())
                        if tabla != None:
                            tablas.append(tabla)
                        else:
                            return ("ERROR >> En la instrucción Select, la tabla: " + nombre + " NO EXISTE")
                    else:
                        return ("ERROR >> En la instrucción Select, ingreso un nombre de tabla incorrecto")
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
            if (len(self.encabezado)==0):
                for tabla in tablas:
                    cols = tabla.valor
                    for columna in cols:
                        nombre = columna.nombre
                        self.encabezado.append(nombre)

            # filtros
            if self.where != None:
                result = self.execwhere(ent, tablas,result)

            #limitar resultados
            if self.limit!=None:
                a=self.limit
                result=self.m_limit(result,a.limit,a.off)

            # acceder a columnas
            if len(self.exps) == 1:
                if self.exps[0].getval(ent) == '*':
                    self.mostarresult(result,self.encabezado, self.nombreres)
                elif self.exps[0].tipo.tipo == 'identificador':
                    newenc=[]
                    'obtengo  solo columnas pedidas'
                    for i in range(0, len(self.encabezado)):
                        nombrediv = self.encabezado[i].split('.')
                        nombrecol = nombrediv[0]
                        if self.exps[0].getval(ent) == nombrecol:
                           for x in range(0,len(result)):
                                valcol=result[x][i]
                                result[x]=[valcol]
                                if(len(newenc)==0):
                                    newenc.append(self.encabezado[i])

                    self.mostarresult(result, newenc,self.nombreres)
                else:
                    'pendientes subconsultas y funciones'
            else:
                newenc = []
                newres=[]
                for i in range(0,len(self.exps)):
                    if self.exps[i].tipo.tipo == 'identificador':
                        for j in range(0, len(self.encabezado)):
                            nombrediv = self.encabezado[j].split('.')
                            nombrecol = nombrediv[0]
                            if self.exps[i].getval(ent) == nombrecol:
                                newenc.append(self.encabezado[j])
                                for x in range(0, len(result)):
                                    valcol = result[x][j]
                                    if len(newres)!=len(result):
                                        newres.append([valcol])
                                    else:
                                        newres[x].append(valcol)

                self.mostarresult(newres, newenc, self.nombreres)


    def mostarresult(self, result,enc, nomresult):
        if not len(result) > 0:
            return "Instrucción Select realizada, No hay registros que cumplan la condición especificada"
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

    def getcolumna(self, entorno, tablas):
        '''   datos = DBMS.extractTable(entorno.getDataBase(), nomtabla)
        if datos != None:
            for fila in datos:
                colres.append(fila[nocol])
        tam = len(colres) '''

    def where2id(self, entorno, tablas,result):
        filtrado = []
        exp1: Expresion
        exp2: Expresion
        nocol1 = -1
        nocol2 = -1


        'realizar operacion'
        exp1 = self.where.exp1
        exp2 = self.where.exp2
        val1 = exp1.getval(entorno)
        val2 = exp2.getval(entorno)
        op = self.where.operador

        tipo1=self.gettipo(entorno,tablas,val1)
        tipo2=self.gettipo(entorno,tablas,val2)

        for i in range(0,len(self.encabezado)):
            nombrediv=self.encabezado[i].split('.')
            nombrecol=nombrediv[0]
            if val1 == nombrecol:
                nocol1=i
                i=i+1
                continue
            if val2==nombrecol:
                nocol2=i
                i = i + 1
                continue



        if tipo1 != None and tipo2 != None and nocol2!=-1 and nocol1!=-1:
                for i in range(0, len(result)):
                    dato1 = result[i][nocol1]
                    dato2 = result[i][nocol2]
                    expi = Terminal(tipo1, dato1)
                    expd = Terminal(tipo2, dato2)

                    if op in ('>', '<', '>=', '<=', '='):
                        nuevaop = Relacional(expi, expd, op);
                        if nuevaop.getval(entorno):
                            'Agrego la fila al resultado'
                            filtrado.append(result[i])
                    elif op in ('or', 'and', 'not'):
                        nuevaop = Logica(expi, expd, op);
                        if nuevaop.getval(entorno):
                            'Agrego la fila al resultado'
                            filtrado.append(result[i])

                    else:
                        variables.consola.insert('Error el resultado del where no es booleano \n')
                return filtrado

        else:
            variables.consola.insert('Error el nombre de las columnas es ambiguo \n')

    def execwhere(self, entorno, tablas,result):
        filtrado = []
        exp1: Expresion
        exp2: Expresion
        tipo = None
        posid = -1
        if isinstance(self.where, Relacional) or isinstance(self.where, Logica):
            encontrado = 0
            nocol = -1
            'realizar operacion'
            exp1 = self.where.exp1
            exp2 = self.where.exp2
            op = self.where.operador
            val = ''
            expi = None
            expd = None
            func1 = False
            func2 = False
            nombrefunc1=''
            nombrefunc2 = ''

            'tomando datos si vienen identificadores'
            if isinstance(exp1, Terminal) and isinstance(exp2, Terminal):
                if exp1.tipo.tipo == 'identificador' and exp2.tipo.tipo == 'identificador':
                    return self.where2id(entorno, tablas,result)


            if isinstance(exp1, Terminal):
                if (exp1.tipo.tipo == 'identificador'):
                    val = exp1.getval(entorno)
                    posid = 1
                    expd = exp2

            if isinstance(exp2, Terminal):
                if (exp2.tipo.tipo == 'identificador'):
                    val = exp2.getval(entorno)
                    posid = 2
                    expi = exp1


            'si viene una columna como parametro de una funcion'
            if isinstance(exp1,FuncionesNativas) or isinstance(exp2,FuncionesNativas):
                if isinstance(exp1,FuncionesNativas):
                    'resolver funcion'
                    nombrefunc1=exp1.identificador
                    parametros1=exp1.expresiones
                    for param in parametros1:
                        if (param.tipo.tipo == 'identificador'):
                            func1 = True
                            break

                if isinstance(exp2,FuncionesNativas):
                    'resolver funcion'
                    nombrefunc2 = exp2.identificador
                    parametros2 = exp2.expresiones
                    for param in parametros2:
                        if(param.tipo.tipo=='identificador'):
                            func2 = True
                            break

            if val!='':
                for i in range(0, len(self.encabezado)):
                    nombrediv = self.encabezado[i].split('.')
                    nombrecol = nombrediv[0]
                    if val == nombrecol:
                        nocol = i
                        break
                tipo = self.gettipo(entorno, tablas, val)
            elif func1==False and func2==False:
                expi=exp1
                expd=exp2
            elif func1== False and func2 ==True:
                expi=exp1
            elif func2==False and func1==True:
                expd = exp2

            'resolver expresion'
            for x in range(0, len(result)):
                if nocol!=-1:
                    dato = result[x][nocol]
                    if posid == 1:
                        expi = Terminal(tipo, dato)
                    elif posid==2:
                        expd = Terminal(tipo, dato)

                if func1:
                    tempexp=[]
                    for exp in exp1.expresiones:
                        tempexp.append(exp)

                    for j in range(0, len(exp1.expresiones)):
                        if exp1.expresiones[j].tipo.tipo == 'identificador':
                            val = exp1.expresiones[j].getval(entorno)
                            for i in range(0, len(self.encabezado)):
                                nombrediv = self.encabezado[i].split('.')
                                nombrecol = nombrediv[0]
                                if val == nombrecol:
                                    tipo = self.gettipo(entorno, tablas, val)
                                    dato = result[x][i]
                                    tempexp[j]=Terminal(tipo,dato)
                    expi=FuncionesNativas(nombrefunc1,tempexp)

                if func2:
                    tempexp = []
                    for exp in exp2.expresiones:
                        tempexp.append(exp)
                    for j in range(0, len(exp2.expresiones)):
                        if exp2.expresiones[j].tipo.tipo == 'identificador':
                            val = exp2.expresiones[j].getval(entorno)
                            for i in range(0, len(self.encabezado)):
                                nombrediv = self.encabezado[i].split('.')
                                nombrecol = nombrediv[0]
                                if val == nombrecol:
                                    tipo = self.gettipo(entorno, tablas, val)
                                    dato = result[x][i]
                                    tempexp[j] = Terminal(tipo, dato)
                    expd = FuncionesNativas(nombrefunc2, tempexp)



                if op in ('>', '<', '>=', '<=', '='):
                    nuevaop = Relacional(expi, expd, op);
                    if nuevaop.getval(entorno):
                        'Agrego la fila al resultado'
                        filtrado.append(result[x])
                elif op in ('or', 'and', 'not'):
                    nuevaop = Logica(expi, expd, op);
                    if nuevaop.getval(entorno):
                        'Agrego la fila al resultado'
                        filtrado.append(result[x])

                else:
                    variables.consola.insert('Error el resultado del where no es booleano \n')
            return filtrado


        elif isinstance(self.where, Unaria):
            'busco columna y resulvo unaria'


        else:
            'ya veremos dijo el ciego'



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


    def group(self):
        'Ejecucucion del group'
    def having(self):
        'Ejecucucion del having'
    def order(self):
        'Ejecucucion del order'
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




    def combining(self):
        'Ejecucucion de combining'

class Limit():
    def __init__(self,limit=-1,off=-1):
        self.limit=limit
        self.off=off
