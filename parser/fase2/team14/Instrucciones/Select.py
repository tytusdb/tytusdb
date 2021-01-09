from Instrucciones.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from storageManager import jsonMode as DBMS
from Expresion.Terminal import Terminal
from Expresion.Unaria import Unaria
from Expresion.Relacional import Relacional
from Expresion.Logica import Logica
from Tipo import Tipo
from Expresion.variablesestaticas import variables
from Expresion.FuncionesNativas import FuncionesNativas
from Expresion.Aritmetica import Aritmetica
from tkinter import *
from reportes import *
from Expresion.Id import Identificador
from Entorno.Simbolo import Simbolo


class Select(Instruccion):
    'This is an abstract class'
    encabezado = []
    nombreres = ''
    todo = []
    tipos = []
    aliast = []
    agregacion = 0

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

    def ejecutar(self, ent: Entorno, imp=1):

        try:
            tablas = []
            result = []
            self.encabezado = []
            self.aliast = []

            if self.distinct is None and self.froms is None and self.where is None and self.group is None and self.having is None and self.order is None and self.combinig is None:
                resultados = []
                newenc = []
                for i in range(0, len(self.exps)):
                    exp = self.exps[i]
                    if isinstance(self.exps[i], FuncionesNativas):
                        newenc.append(self.exps[i].identificador + str(i))
                    elif isinstance(self.exps[i], Alias):
                        newenc.append(self.exps[i].nombre)
                        exp = self.exps[i].expresion
                    elif isinstance(self.exps[i], Identificador):
                        newenc.append(self.exps[i].nombre)
                    else:
                        newenc.append('Exp' + str(len(newenc)))

                    result.append(exp.getval(ent).valor)

                result = [result]
                self.encabezado = newenc

            elif self.froms != None and self.exps != None:

                for exp in self.froms:
                    if isinstance(exp, Identificador) or isinstance(exp, Terminal):
                        self.aliast.append('')
                        tipo = exp.tipo
                        tablas = self.gettablas(tipo, exp, ent, tablas)

                    elif isinstance(exp, Alias):
                        self.aliast.append(exp.nombre)
                        expre = exp.expresion
                        tipo = expre.tipo
                        tablas = self.gettablas(tipo, expre, ent, tablas)

                if len(tablas) > 1:
                    'Obteniendo encabezados de las tablas'
                    for tabla in tablas:
                        cols = tabla.valor
                        for columna in cols:
                            nombre = columna.nombre
                            self.encabezado.append(nombre + "." + tabla.nombre.replace('_' + ent.getDataBase(), ''))

                    'producto cartesiano'
                    real = tablas[0].nombre.replace('_' + ent.getDataBase(), '')
                    result = DBMS.extractTable(ent.getDataBase(), real)
                    self.nombreres = real
                    for i in range(0, len(tablas) - 1):
                        real2 = tablas[i + 1].nombre.replace('_' + ent.getDataBase(), '')
                        self.nombreres += "_" + real2
                        tabla2 = DBMS.extractTable(ent.getDataBase(), real2)
                        result = self.producto(result, tabla2)

                else:
                    'llenar resultado desde backend'
                    real = tablas[0].nombre.replace('_' + ent.getDataBase(), '')
                    result = DBMS.extractTable(ent.getDataBase(), real)

                'encabezados 1 tabla'
                if (len(self.encabezado) == 0):
                    for tabla in tablas:
                        cols = tabla.valor
                        for columna in cols:
                            nombre = columna.nombre
                            self.encabezado.append(nombre)

                # add  columnas

                newenc = []
                newres = []
                for i in range(0, len(self.exps)):

                    if isinstance(self.exps[i], Terminal) or isinstance(self.exps[i], Identificador):
                        'aqui no agrego las que ya existen'

                    else:
                        exp = self.exps[i]
                        'aqui agrego las expresiones que se agregaran para filtrar'
                        if isinstance(self.exps[i], FuncionesNativas):
                            newenc.append(self.exps[i].identificador)
                        elif isinstance(self.exps[i], Alias):
                            newenc.append(self.exps[i].nombre)
                            exp = self.exps[i].expresion
                        elif isinstance(self.exps[i], Identificador):
                            newenc.append(self.exps[i].nombre)
                        else:
                            newenc.append('Exp' + str(len(newenc)))

                        for fila in range(0, len(result)):
                            res = self.resolver(exp, ent, result, tablas, fila)
                            if fila == 0:
                                self.tipos.append([newenc[len(newenc) - 1], res.tipo])
                            if len(newres) != len(result):
                                newres.append([res.valor])
                            else:
                                newres[fila].append(res.valor)

                for i in range(0, len(result)):
                    if newres != []:
                        result[i] = result[i] + newres[i]

                self.encabezado = (self.encabezado + newenc)

                # filtros
                if self.where != None:
                    result = self.optwhere(ent, result, tablas)

                # DEVUELVO SOLO COLUMNAS PEDIDAS
                newenc = []
                newres = []

                for i in range(0, len(self.exps)):
                    if isinstance(self.exps[i], Identificador):
                        for j in range(0, len(self.encabezado)):
                            nombrediv = self.encabezado[j].split('.')
                            nombrecol = nombrediv[0]
                            if self.exps[i].nombre == nombrecol:
                                newenc.append(self.encabezado[j])
                                for x in range(0, len(result)):
                                    valcol = result[x][j]
                                    if len(newres) != len(result):
                                        newres.append([valcol])
                                    else:
                                        newres[x].append(valcol)
                    elif isinstance(self.exps[i], Terminal):
                        if self.exps[i].tipo.tipo == 'acceso':
                            expresion = self.exps[i]
                            campos = expresion.getval(ent).valor.split('.')
                            if campos[1] == '*':
                                tablares = self.getasterisco(campos[0], tablas, result, ent, newres, newenc)
                                newenc = tablares[0]
                                newres = tablares[1]
                            # busco el campo pedido si no es *
                            for j in range(0, len(self.encabezado)):
                                nombrediv = self.encabezado[j].split('.')
                                nombrecol = nombrediv[0]

                                nombretabla = nombrediv[1]
                                nombrecol = nombretabla + '.' + nombrecol
                                if expresion.getval(ent).valor == nombrecol:
                                    newenc.append(self.encabezado[j])
                                    for x in range(0, len(result)):
                                        dato = result[x][j]
                                        if len(newres) != len(result):
                                            newres.append([dato])
                                        else:
                                            newres[x].append(dato)

                                for k in range(0, len(self.aliast)):
                                    nombreacc = self.aliast[k] + '.' + nombrediv[0]
                                    if expresion.getval(ent).valor == nombreacc and nombrediv[1] == tablas[
                                        k].nombre.replace('_' + ent.getDataBase(), ''):
                                        newenc.append(self.encabezado[j])
                                        for x in range(0, len(result)):
                                            dato = result[x][j]
                                            if len(newres) != len(result):
                                                newres.append([dato])
                                            else:
                                                newres[x].append(dato)
                        elif len(self.exps) == 1 and self.exps[0].valor == '*':
                            newres = result[:]
                            newenc = self.encabezado[:]
                            break

                    else:
                        exp = self.exps[i]
                        if isinstance(self.exps[i], FuncionesNativas):
                            newenc.append(self.exps[i].identificador + str(i))
                        elif isinstance(self.exps[i], Alias):
                            newenc.append(self.exps[i].nombre)
                            exp = self.exps[i].expresion
                        else:
                            newenc.append('Exp' + len(newenc))

                        for fila in range(0, len(result)):
                            res = self.resolver(exp, ent, result, tablas, fila)
                            '''if isinstance(res,str):
                                if len(newres) != len(result):
                                    newres.append([''])
                                else:
                                    newres[fila].append('')
                                continue'''
                            if len(newres) != len(result):
                                newres.append([res.valor])
                            else:

                                newres[fila].append(res.valor)

                result = newres[:]
                self.encabezado = newenc[:]

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

                # distinct
                if self.distinct != None:
                    newres = []
                    'elimino duplicados'
                    for i in range(0, len(result)):
                        encontrado = False
                        fila = result[i]
                        for j in range(0, len(result)):
                            if j != i:
                                if fila == result[j]:
                                    encontrado = True
                        if encontrado == False:
                            newres.append(fila)
                    result = newres

                # imprimir resultado solo si no se llamo de un subquery,union,intersect,except
            if self.agregacion == 1:
                result = [result[0]]
            if imp == 1:
                self.mostarresult(result, self.encabezado, self.nombreres)

            return [self.encabezado, result]

        except  Exception as inst:
            print(inst)
            return

    def traducir(self, entorno):
        self.codigo3d = 'ci.ejecutarsql("select '
        self.stringsql = ' Select '
        if self.distinct != None:
            self.codigo3d += ' distinct '
            self.stringsql += ' distinct '

        if self.exps != None:
            for i in range(0, len(self.exps)):
                if i == 0:

                    exp = self.exps[i]
                    if isinstance(self.exps[i], FuncionesNativas):
                        self.codigo3d += self.exps[i].traducir(entorno).stringsql
                        self.stringsql += self.exps[i].traducir(entorno).stringsql
                    elif isinstance(self.exps[i], Alias):
                        self.codigo3d += self.exps[i].stringsql
                        self.stringsql += self.exps[i].stringsql
                    elif isinstance(self.exps[i], Identificador):
                        self.codigo3d += (self.exps[i].nombre)
                        self.stringsql += self.exps[i].traducir(entorno).stringsql
                    else:
                        self.codigo3d += (self.exps[i].traducir(entorno).stringsql)
                        self.stringsql += self.exps[i].traducir(entorno).stringsql
                else:
                    exp = self.exps[i]
                    if isinstance(self.exps[i], FuncionesNativas):
                        self.codigo3d += ', ' + self.exps[i].traducir(entorno).stringsql
                        self.stringsql += ', ' + self.exps[i].traducir(entorno).stringsql
                    elif isinstance(self.exps[i], Alias):
                        self.codigo3d += ', ' + self.exps[i].stringsql
                        self.stringsql += ', ' + self.exps[i].stringsql
                        exp = self.exps[i].expresion
                    elif isinstance(self.exps[i], Identificador):
                        self.codigo3d += ', ' + self.exps[i].traducir(entorno).nombre
                        self.stringsql += ', ' + self.exps[i].traducir(entorno).stringsql
                    else:
                        self.codigo3d += ', ' + self.exps[i].traducir(entorno).stringsql
                        self.stringsql += ', ' + self.exps[i].traducir(entorno).stringsql

        if self.froms != None:
            self.codigo3d += ' from '
            self.stringsql += ' from '
            i = 0
            for exp in self.froms:
                if i == 0:

                    if isinstance(exp, Identificador) or isinstance(exp, Terminal):
                        self.codigo3d += exp.traducir(entorno).stringsql
                        self.stringsql += exp.traducir(entorno).stringsql
                    elif isinstance(exp, Alias):
                        self.codigo3d += exp.traducir(entorno).stringsql
                        self.stringsql += exp.traducir(entorno).stringsql
                else:
                    if isinstance(exp, Identificador) or isinstance(exp, Terminal):
                        self.codigo3d += ', ' + exp.traducir(entorno).stringsql
                        self.stringsql += ', ' + exp.traducir(entorno).stringsql
                    elif isinstance(exp, Alias):
                        self.codigo3d += ', ' + exp.traducir(entorno).stringsql
                        self.stringsql += ', ' + exp.traducir(entorno).stringsql
                i = i + 1

        if self.where != None:
            self.codigo3d += ' Where '
            self.stringsql += ' Where '
            # v=self.where.getval(ent)
            self.stringsql += self.where.traducir(entorno).stringsql
            self.codigo3d += self.where.traducir(entorno).stringsql

        if self.group != None:
            self.codigo3d += ' Group by '
            self.stringsql += ' Group by '
            i = 0
            for exp in self.group:
                if i == 0:
                    self.codigo3d += exp.traducir(entorno).stringsql
                    self.stringsql += exp.traducir(entorno).stringsql
                else:
                    self.codigo3d += ', ' + exp.traducir(entorno).stringsql
                    self.stringsql += ', ' + exp.traducir(entorno).stringsql
                i = i + 1

        if self.having != None:
            ''
        if self.order != None:
            ''
        if self.limit != None:
            self.codigo3d += ' ' + self.limit.stringsql
            self.stringsql += ' ' + self.limit.stringsql
        if self.combinig != None:
            self.codigo3d += self.combinig.stringsql
            self.stringsql += self.combinig.stringsql

        self.codigo3d += ' ;")\n'
        self.temp=self.codigo3d

        return self

    def getasterisco(self, nombtabla, tablas, result, ent, newres, newenc):
        real = ''
        postabla = -1
        if newres == []:
            for i in range(0, len(self.aliast)):
                if nombtabla == self.aliast[i]:
                    real = tablas[i].nombre.replace('_' + ent.getDataBase(), '')
                if nombtabla == tablas[i].nombre.replace('_' + ent.getDataBase(), ''):
                    real = nombtabla
            if real != '':
                for i in range(0, len(self.encabezado)):
                    splitted = self.encabezado[i].split('.')
                    campo = splitted[0]
                    tabla = ''
                    if len(splitted) > 0:
                        tabla = splitted[1]

                    if tabla == real:
                        newenc.append(self.encabezado[i])
                        for x in range(0, len(result)):
                            dato = result[x][i]
                            if len(newres) != len(result):
                                newres.append([dato])
                            else:
                                newres[x].append(dato)

        else:
            '''            for x in range(0, len(result)):
                dato = result[x][j]
                if len(newres) != len(result):
                    newres.append([dato])
                else:
                    newres[x].append(dato)'''

        return [newenc, newres]

    def gettablas(self, tipo, exp, ent, tablas):
        if isinstance(exp, Identificador):
            nombre = exp.nombre
        elif isinstance(exp, Terminal):
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

        return tablas

    def mostarresult(self, result, enc, nomresult):
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

    def optwhere(self, entorno, result, tablas):
        newres = []
        if result==[]:
            self.encabezado=['']
            result=[[0]]
            return result
        for i in range(0, len(result)):
            resexp = self.resolver(self.where, entorno, result, tablas, i)
            try:
                if resexp.valor:
                    newres.append(result[i])

            except:
                reporteerrores.append(Lerrores("Error Semantico",
                                               'Error el resultado del where no es booleano',
                                               0, 0))
                variables.consola.insert(INSERT, 'Error el resultado del where no es booleano \n')

        return newres

    def resolver(self, expresion, entorno, result, tablas, fila):
        # para expresion binaria
        if not isinstance(expresion, Terminal) and not isinstance(expresion, Unaria) and not isinstance(expresion,FuncionesNativas) and not isinstance(expresion, Identificador):
            'resuelvo logicas,aritmeticas y relacionales'
            exp1 = expresion.exp1
            exp2 = expresion.exp2
            res1 = self.resolver(exp1, entorno, result, tablas, fila)
            res2 = self.resolver(exp2, entorno, result, tablas, fila)

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
            res = self.resolver(exp, entorno, result, tablas, fila)
            op = Unaria(res, expresion.operador)
            return op.getval(entorno)

        else:
            'aqui resuelvo los terminales y funciones'
            if isinstance(expresion, Identificador):
                ''
                sim = expresion.getval(entorno)

                if sim != None:
                    term = Terminal(Tipo(sim.tipo.tipo, None, -1, -1), sim.valor)
                    return term
                else:
                    for i in range(0, len(self.encabezado)):
                        nombrediv = self.encabezado[i].split('.')
                        nombrecol = nombrediv[0]
                        if expresion.nombre == nombrecol:
                            dato = result[fila][i]
                            tipo = None
                            if len(nombrediv) > 1:
                                tipo = self.gettipo(entorno, tablas, nombrediv[0], nombrediv[1])
                            else:
                                tipo = self.gettipo(entorno, tablas, nombrediv[0])
                            term = Terminal(tipo, dato)
                            return term
            elif isinstance(expresion, Terminal):
                if expresion.tipo.tipo == 'acceso':
                    return self.getacceso(entorno, expresion, result, fila, tablas)
                else:
                    return expresion

            elif isinstance(expresion, FuncionesNativas):
                if expresion.identificador.lower() == 'count':
                    t = Tipo('integer', None, -1, -1)
                    self.agregacion = 1
                    return Terminal(t, len(result))
                tempexp = []
                for exp in expresion.expresiones:
                    tempexp.append(exp)

                for j in range(0, len(expresion.expresiones)):
                    if isinstance(expresion.expresiones[j], Identificador):
                        val = expresion.expresiones[j].nombre
                        for i in range(0, len(self.encabezado)):
                            nombrediv = self.encabezado[i].split('.')
                            nombrecol = nombrediv[0]
                            if val == nombrecol:
                                tipo = None
                                if len(nombrediv) > 1:
                                    tipo = self.gettipo(entorno, tablas, val, nombrediv[1])
                                else:
                                    tipo = self.gettipo(entorno, tablas, val)
                                dato = result[fila][i]
                                tempexp[j] = Terminal(tipo, dato)
                    func = FuncionesNativas(expresion.identificador, tempexp)
                return func.getval(entorno)

    def getacceso(self, entorno, expresion, result, fila, tablas):
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

            for x in range(0, len(self.aliast)):
                nombreacc = self.aliast[x] + '.' + nombrediv[0]
                if expresion.getval(entorno).valor == nombreacc and nombrediv[1] == tablas[x].nombre.replace(
                        '_' + entorno.getDataBase(), ''):
                    dato = result[fila][i]
                    tipo = None
                    if len(nombrediv) > 1:
                        tipo = self.gettipo(entorno, tablas, nombrediv[0], nombrediv[1])
                    else:
                        tipo = self.gettipo(entorno, tablas, nombrediv[0])
                    term = Terminal(tipo, dato)
                    return term

        return None

    def gettipo(self, entorno, tablas, col, ntabla=''):
        tipo = None
        for tabla in tablas:
            real = tabla.nombre.replace('_' + entorno.getDataBase(), '')
            columnas = tabla.valor
            i = 0
            for columna in columnas:
                nombre = columna.nombre
                if col == nombre:
                    if (ntabla == real or ntabla == '') and tipo == None:
                        tipo = columna.tipo
                i = i + 1
            for val in self.tipos:
                if val[0] == col:
                    return val[1]

        return tipo

    # def group(self):
    # 'Ejecucucion del group'
    # def having(self):
    # 'Ejecucucion del having'
    # def order(self):
    # 'Ejecucucion del order'
    def m_limit(self, result, limit, off):

        if str(limit).lower == 'all':
            limit = len(result)

        if off < 0 or off > len(result):
            off = 0

        if limit < 0 or limit > len(result):
            limit = len(result)
        datos = []
        for i in range(off, off + limit):
            datos.append(result[i])

        return datos

    def m_combining(self, combi, enc1, res1, enc2, res2):

        if len(enc1) == len(enc2):
            if combi.combi.lower() == 'union':
                if combi.all == 'all':
                    if len(enc1) == len(enc2):
                        return res1 + res2

                else:
                    result = []
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
                    if esta == False:
                        result.append(res1[i])
                return result
        else:
            reporteerrores.append(Lerrores("Error Semantico",
                                           'Error union,intersect, solo se puede hacer con la misma cantidad de columnas',
                                           0, 0))
            variables.consola.insert(INSERT,
                                     'Error union,intersect, solo se puede hacer con la misma cantidad de columnas\n')
        return []


class Limit():
    def __init__(self, limit=-1, off=-1, sqls=''):
        self.limit = limit
        self.off = off
        self.sqls = sqls
        self.stringsql = sqls


class Alias():
    def __init__(self, expresion, nombre, ali):
        self.expresion = expresion
        self.nombre = nombre
        self.ali = ali
        self.stringsql=expresion.traducir(Entorno).stringsql+' '+ali+' '


class Combi():
    def __init__(self, combi, select, all=''):
        self.combi = combi
        self.select = select
        self.all = all

        sel: Instruccion = select
        v = sel.traducir(Entorno).stringsql
        self.stringsql = ' ' + combi + ' ' + all + ' ' + v



