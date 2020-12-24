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

class Update(Instruccion):
    encabezado=[]
    def __init__(self,tabla,listaCampos,where):
        self.tabla = tabla
        self.listaCampos = listaCampos
        self.where = where

    def ejecutar(self,ent:Entorno):
        dbActual = ent.getDataBase()
        result=[]

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
                        if resexp.valor:
                            dic={}
                            'busco la columna y le asigno el nuevo valor'
                            for i in range(0, len(self.listaCampos)):
                               nombrecol = self.listaCampos[i].columna
                               expresion = self.listaCampos[i].exp
                               contenido=expresion.getval(ent).valor
                               for nocol in range(0, len(columnas)):
                                   if nombrecol==columnas[nocol].nombre:
                                        dic.update({nocol:contenido})
                            'envio datos par update'
                            llavePrim = []
                            for column in tabla.valor:
                                prim:Simbolo = ent.buscarSimbolo(column.atributos.get('primary'))
                                llavePrim = prim.valor
                                break
                            
                            r = DBMS.update(dbActual,self.tabla,dic,llavePrim)
                            if r == 0:
                                variables.consola.insert(INSERT, 'Se ha actualizado un registro \n')


                    except:
                        reporteerrores.append(Lerrores("Error Semantico",'Error el resultado del where no es booleano',0, 0))
                        variables.consola.insert(INSERT, 'Error el resultado del where no es booleano \n')

            else:
                variables.consola.insert(INSERT,"La tabla '" + self.tabla + "' que desea actualizar no existe\n")
                reporteerrores.append(Lerrores("Error Semántico","La tabla '" + self.tabla + "' que desea actualizar no existe","",""))


    def resolver(self, expresion, entorno, result, tabla, fila):
        # para expresion binaria
        if not isinstance(expresion, Terminal) and not isinstance(expresion, Unaria) and not isinstance(expresion,FuncionesNativas):
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
            if isinstance(expresion, Terminal):
                if expresion.tipo.tipo == 'identificador':
                    for i in range(0, len(self.encabezado)):
                        nombrediv = self.encabezado[i].split('.')
                        nombrecol = nombrediv[0]
                        if expresion.getval(entorno).valor == nombrecol:
                            dato = result[fila][i]
                            tipo = None
                            tipo = self.gettipo(entorno, tabla, nombrediv[0])
                            term = Terminal(tipo, dato)
                            return term
                elif expresion.tipo.tipo == 'acceso':
                    for i in range(0, len(self.encabezado)):
                        nombrediv = self.encabezado[i].split('.')
                        nombrecol = nombrediv[0]
                        nombretabla = nombrediv[1]
                        nombrecol = nombretabla + '.' + nombrecol
                        if expresion.getval(entorno).valor == nombrecol:
                            dato = result[fila][i]
                            tipo = None
                            tipo = self.gettipo(entorno, tabla, nombrediv[0])
                            term = Terminal(tipo, dato)
                            return term.getval(entorno)

                else:
                    return expresion

            elif isinstance(expresion, FuncionesNativas):
                tempexp = []
                for exp in expresion.expresiones:
                    tempexp.append(exp)

                for j in range(0, len(expresion.expresiones)):
                    if expresion.expresiones[j].tipo.tipo == 'identificador':
                        val = expresion.expresiones[j].getval(entorno).valor
                        for i in range(0, len(self.encabezado)):
                            nombrediv = self.encabezado[i].split('.')
                            nombrecol = nombrediv[0]
                            if val == nombrecol:
                                tipo = None
                                tipo = self.gettipo(entorno, tabla, val)
                                dato = result[fila][i]
                                tempexp[j] = Terminal(tipo, dato)
                    func = FuncionesNativas(expresion.identificador, tempexp)
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


class Campo():
    def __init__(self,columna,exp):
        self.columna = columna
        self.exp = exp
