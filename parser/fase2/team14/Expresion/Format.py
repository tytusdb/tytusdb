from Expresion.Expresion import Expresion
from datetime import date
from datetime import datetime
from Entorno import Entorno
from Expresion.Id import Identificador
import random as rn
from reportes import *
import re
from Expresion.variablesestaticas import *
import math

class Format(Expresion) :
    '''
        Esta clase representa un terminal.
    '''
    def __init__(self,cadena,exps) :
        Expresion.__init__(self)
        self.cadena=cadena
        self.exps=exps


    def getval(self,entorno:Entorno):
        estado = 0
        token=''
        espacios=''
        pos=0
        newcad=self.cadena
        posexp=0
        for i in range(0,len(self.cadena)):
            c = self.cadena[i]
            if estado==0:
                if c=='%':
                    estado=1
                    continue
            elif estado==1:
                if self.isnumber(c) or c=='-':
                    estado=2
                    if c!='-':
                        token+=c
                else:
                    results=self.sustituir(c,entorno,pos,espacios,newcad,posexp)
                    estado=results[0]
                    newcad=results[1]
            elif estado == 2:
                if self.isnumber(c):
                    token += c
                else:
                    if int(token)>0:
                        pos=0
                    else:
                        pos=-1
                    for x in range(0,c):
                        espacios+=' '
            elif estado == 3:
                'despues implemento los alias  con $'

            return newcad



    def sustituir(self,c,entorno,pos,espacios,newcad,posexp):
        if c == 's':
            param=None
            if posexp<len(self.exps):
                param = self.exps[posexp]
                posexp += 1
            else:
                reporteerrores.append(Lerrores("Error Semantico", "Error, no se proporcionaron parametros suficientes", 0, 0))
                variables.consola.insert(INSERT, "Error no se proporcionaron parametros suficientes")
                return None
            if isinstance(param, Identificador):
                val = param.getval(entorno)
                if val != None:
                    val = val.valor
                    if pos == 0:
                        rep = espacios + val
                    else:
                        rep = val + espacios
                    newcad = re.sub(r'%-?[0-9]*s', rep, newcad, 1)
                else:
                    val=param.nombre
                    if pos == 0:
                        rep = espacios + val
                    else:
                        rep = val + espacios
                    newcad = re.sub(r'%-?[0-9]*s', rep, newcad, 1)
            else:
                val = str(param)
                if pos == 0:
                    rep = espacios + val
                else:
                    rep = val + espacios
                newcad = re.sub(r'%-?[0-9]*s', rep, newcad, 1)
            estado = 0
        elif c == 'I':
            if posexp < len(self.exps):
                param = self.exps[posexp]
                posexp += 1
            else:
                reporteerrores.append(Lerrores("Error Semantico", "Error, no se proporcionaron parametros suficientes", 0, 0))
                variables.consola.insert(INSERT, "Error no se proporcionaron parametros suficientes")
            if isinstance(param, Identificador):
                val = param.nombre
                if pos == 0:
                    rep = espacios + val
                else:
                    rep = val + espacios
                newcad = re.sub(r'%-?[0-9]*I', rep, newcad, 1)
            else:
                val = str(param)
                if pos == 0:
                    rep = espacios + val
                else:
                    rep = val + espacios
                newcad = re.sub(r'%-?[0-9]*I', rep, newcad, 1)
            estado = 0
        elif c == 'L':
            if posexp < len(self.exps):
                param = self.exps[posexp]
                posexp += 1
            else:
                reporteerrores.append(Lerrores("Error Semantico", "Error, no se proporcionaron parametros suficientes", 0, 0))
                variables.consola.insert(INSERT, "Error no se proporcionaron parametros suficientes")
            if isinstance(param, Identificador):
                val = param.nombre
                if pos == 0:
                    rep = espacios + val
                else:
                    rep = val + espacios
                newcad = re.sub(r'%-?[0-9]*L', rep, newcad, 1)
            else:
                val = str(param)
                if pos == 0:
                    rep = espacios + val
                else:
                    rep = val + espacios
                newcad = re.sub(r'%-?[0-9]*L', rep, newcad, 1)
            estado = 0
        elif c == '$':
            estado = 3

        return [estado,newcad]


    def isnumber(self,char):
        if type(char)  in (int, float, complex):
            return True
        else:
            return False