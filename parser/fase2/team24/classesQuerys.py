#
import hashlib
from datetime import date
from os.path import split

from variables import NombreDB
import storage as s
from enum import Enum

import mathtrig as mt
import prettytable as pt
import reportError as errores
from reportError import CError
from sql import *


from variables import cont
from variables import tabla
from variables import NombreDB

import tablaDGA as TS


#
class exp_type(Enum):
    numeric = 1
    text  = 2
    boolean = 3
    identifier = 4

#

class query():
    ' Clase abstracta query'

class select_func(query):
    def __init__(self,lista):
        self.lista = lista

    def traducir(self):
        ''''''
        return ''

    def ejecutar(self):
        global tabla
        global NombreDB
        if self.lista == None: 
            e = errores.CError(0,0,"Error funcion",'Semantico') 
            errores.insert_error(e)
            return e
        else: 
            if not isinstance(self.lista,list):
                e = errores.CError(0,0,"Error funcion",'Semantico') 
                errores.insert_error(e)
                return e
            else:
                tables = {}

                results = []
                for col in self.lista:
                    res = col.ejecutar(tables)
                    if isinstance(res,errores.CError):
                        e = errores.CError(0,0,"Error funcion",'Semantico') 
                        errores.insert_error(e)
                        print()
                        return e
                    results.append(res)

                ptable = pt.PrettyTable()
                enc = []
                con = 0
                for col in self.lista:
                    if col.alias == None:
                        enc.append(str(con)+' Funcion')
                    else: 
                        enc.append(col.alias)
                    con += 1
                ptable.field_names = enc
                ptable.add_row(results)
                #print(ptable)
                print(ptable.get_string())
                return ptable

class select(query):

    def __init__(self, distinct=False, select_list=[], table_expression=[], condition=[], group=False, having=[], orderby=[], limit=0, offset=0):
        self.distinct = distinct
        self.select_list = select_list
        self.table_expression = table_expression
        self.condition = condition
        self.group = group
        self.having = having
        self.orderby = orderby
        self.limit = limit
        self.offset = offset
        if having is not None and condition is not None:
            self.condition.append(having)
        
    def traducir(self):
        global Listaselects
        Nuevoselect = select(self.distinct,self.select_list,self.table_expression,self.condition,
        self.group,self.having,
        self.orderby,
        self.limit,
        self.offset)

        insertarS(Nuevoselect)
        serialaizer()
        traduccion = '\t'
        traduccion += 'sql.execute(\'SELECT * FROM temp\')\n'
        
        return traduccion

    def ejecutar(self):
        global tabla
        global NombreDB
        gro = self.group
        #Obtener la lista de tablas
        tables = {}
        for tabla in self.table_expression:
            tables[tabla.id]  = tabla.alias
        
        results = []
        for col in self.select_list:
            res = col.ejecutar(tables)
            if isinstance(res,errores.CError):
                e = errores.CError(0,0,"Error obteniendo informacion de alguna columna.",'Semantico') 
                errores.insert_error(e)
                return e
            
            results.append(res)
        
        
        conditions = []
        if self.condition is not None:
            conditions = ejecutar_conditions(tables,self.condition)
            if isinstance(conditions,errores.CError):
                e = errores.CError(0,0,"Error realizando las condiciones.",'Semantico')
                errores.insert_error(e)
                return e
        grouped = []
        
        if self.group :
            
            grouped = ejecutar_groupBy(results,self.select_list)
            if isinstance(grouped,errores.CError):
                e = errores.CError(0,0,"Error agrupando los elementos.",'Semantico')
                errores.insert_error(e)
                return e

        #Mostrar resultados
        for column in results:

            if isinstance(column,dict) and isinstance(column['valores'],list) and isinstance(conditions,dict):
                column['valores'] = filtrar(column['valores'],conditions['posiciones'])
            elif isinstance(column,dict) and isinstance(conditions,list) and conditions:
                column['valores'] = filtrar(column['valores'],conditions)
        
            
        consulta = []
        fila = []
        for col in self.select_list:
            fila.append([col.alias])
    
        contador = 0
        nombres = []
        for column in results:
            actual = fila[contador]
            if None in actual:
                if not isinstance(results[contador]['columna'][0],dict): 
                    r = results[contador]['columna']
                    fila[contador] = r
                else:
                    r = results[contador]['columna'][0]['nombre']
                    fila[contador] = [r]
            contador += 1
        
        enc = []
        contador = 1
        for arreglo in fila:
            for valor in arreglo:
                enc.append(str(contador)+'. '+valor)
                nombres.append(str(contador)+'. '+valor)
                contador = contador+1        

        consulta.append(enc)
        if gro:
            colss=[]
            contador = 0
            for fila in grouped:
                colss.append([])
            for fila in grouped:
                for i in range(len(grouped[0])):
                    colss[i].append(fila[i])
            consulta.extend(colss)    
        else:
            #añadiendo las columnas
            conta = 0
            for res in results:
                vals = res['valores']
                if isinstance(vals,int) or isinstance(vals,float):
                    consulta.append([vals])
                elif isinstance(vals[0],list):
                    for v in vals:
                        consulta.append(v)
                else:
                    consulta.append(vals)

        #buscamos el arreglo mas largo   
        max = 0
        for i in range(1,len(consulta)) :
            actual = len(consulta[i])
            if actual>max: max = actual
        
        for col in consulta:
            for i in range(max):
                if len(col)<=i:
                    col.append('-')
        
        
                      
        #Distinct
        if self.distinct:
            cabeceras = consulta[0]
            rest = []
            for i in range(1,len(consulta)):
                rest.append(tuple(consulta[i]))
            #remove duplicates
            rest = list(set(rest))
            result = [cabeceras]
            for val in rest:
                converted = list(val)
                result.append(converted)
            consulta = result
            

        salida = []
        if self.limit != 0:
            #self.limit = self.limit + 1
            contador = 0
            for fila in consulta:
                salida.append(fila)
                if contador == self.limit:
                    break
                
                contador = contador + 1
            consulta = salida

        salida = []
        if self.offset != 0:
            #self.offset = self.offset + 1
            contador = 0
            for fila in consulta:
                
                if contador != self.offset:
                    salida.append(fila)
                
                contador = contador + 1
            consulta = salida

        #
        #Order by
        sortby =''
        if self.orderby is not None:
            for nombre in nombres:
                if self.orderby[1]  in nombre :
                    sortby = nombre
        #

        
        ptable = pt.PrettyTable()
        for i in range(1,len(consulta)):
            ptable.add_column(consulta[0][i-1],consulta[i])
        if sortby != '':
            ptable.sortby = sortby
            if self.orderby[2].lower() =='desc':
                ptable.reversesort = True

        print(ptable.get_string())
        return ptable


class exp_query():
    'Abstract Class'


class exp_id(exp_query):
    'Esta expresion devuelve'
    'el arreglo de la base de datos'

    def __init__(self, val, table):
        self.val = val
        self.table = table
        self.alias = None
        

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Falta definir el tipo de la columna
        #Verificar si sabemos la tabla
        if self.table is None:
            #No sabemos la tabla
            if self.val == '*':
                #Verificamos que solo sea una tabla la importada
                if len(tables)>1:
                    e = errores.CError(0,0,"La tabla buscada no está en el from",'Semantico')
                    errores.insert_error(e)
                    return e
                t = list(tables)[0]
                registros = s.extractTable(NombreDB,t)
                #Buscamos los encabezados
                encabezados = ts.getColumns(NombreDB,t)
                if registros ==[] and encabezados == []:
                    e = errores.CError(0,0,"La tabla especificada no existe",'Semantico')
                    errores.insert_error(e)
                    return e
                #Devolvemos todas las columnas
                cols = []
                #llenamos vacio
                cont = len(registros[0])
                for i in range(0,cont):
                    cols.append([])
                #metemos en los registros
                for reg in registros:
                    for i in range(0,cont):
                        cols[i].append(reg[i])
                dict = {
                "valores":cols,
                "columna":encabezados
                }
                return dict

            #Verificamos si es *

            #Tenemos que tener la tabla
            c=0
            while True:
                tupla = ts.getTabla(self.val,c)
                if tupla is None:
                    e = errores.CError(0,0,"La tabla especificada no existe",'Semantico')
                    errores.insert_error(e)
                    return e
                if tupla[0] not in tables and tupla[0] not in tables.values():
                    c+=1
                    tupla = ts.getTabla(self.val,c)
                else:
                    break



            #Este devuelve la base de datos y la
            # tabla
            if tupla is None :
                e = errores.CError(0,0,"La tabla buscada no está en el from",'Semantico')
                errores.insert_error(e)
                return e
            #Ahora obtenemos los registros de la columna
            registros = s.extractTable(tupla[1],tupla[0])

            #Obtener el indice de la columna

            indice = ts.getIndice(tupla[1],tupla[0],self.val)

            # Obtener la columna de los registros

            columna = []
            for reg in registros:
                columna.append(reg[indice])
            dict = {
                "valores":columna,
                "columna":[{"nombre":self.val,"indice":indice,"tabla":tupla[0]}]
            }
            return dict
        else:
            #Verificamos que exista
            if self.table not in tables and self.table not in tables.values():
                e = errores.CError(0,0,"La tabla buscada no está en el from",'Semantico')
                errores.insert_error(e)
                return e
            # Existe, ahora obtenemos el nombre de la tabla

            if self.table not in tables.values():
                # si no fuera un alias
                #significa que el nombre es la tabla
                registros = s.extractTable(NombreDB,self.table)
                if self.val == '*':
                    encabezados = ts.getColumns(NombreDB,self.table)
                    cols = []
                    #llenamos vacio
                    cont = len(registros[0])
                    for i in range(0,cont):
                        cols.append([])
                    #metemos en los registros
                    for reg in registros:
                        for i in range(0,cont):
                            cols[i].append(reg[i])
                    dict = {
                            "valores":cols,
                            "columna":encabezados
                    }
                    return dict

                indice = ts.getIndice(NombreDB,self.table,self.val)
                if registros ==[] and indice == -1:
                    e = errores.CError(0,0,"La tabla especificada no existe",'Semantico')
                    errores.insert_error(e)
                    return e
                col = []
                for reg in registros:
                    col.append(reg[indice])

                dic = {
                    "valores" : col,
                    "columna" : [{"nombre":self.val,"indice":indice,"tabla":self.table}]
                }

                return dic

            else:
                #Obtenemos el nombre basado en el alias
                table = getKeyFromValue(self.table,tables)
                if isinstance(table,CError):
                    return table
                #Obtenemos la tabla
                registros = s.extractTable(NombreDB,table)

                if self.val == '*':
                    encabezados = ts.getColumns(NombreDB,table)
                    if registros ==[] and encabezados == []:
                        e = errores.CError(0,0,"La tabla especificada no existe",'Semantico')
                        errores.insert_error(e)
                        return e
                    cols = []
                    #llenamos vacio
                    cont = len(registros[0])
                    for i in range(0,cont):
                        cols.append([])
                    #metemos en los registros
                    for reg in registros:
                        for i in range(0,cont):
                            cols[i].append(reg[i])
                    dict = {
                        "valores":cols,
                        "columna":encabezados
                    }
                    return dict
                #Obtenemos el indice de esa tabla
                indice = ts.getIndice(NombreDB,table,self.val)
                if indice == -1:
                    e = errores.CError(0,0,"La tabla especificada no existe",'Semantico')
                    errores.insert_error(e)
                    return e
                #Obtenemos la columan que queremos
                col = []
                for reg in registros:
                    col.append(reg[indice])

                dic = {
                    "valores" : col,
                    "columna" : [{"nombre":self.val,"indice":indice,"tabla":table}]
                }
                return dic

class exp_bool(exp_query):
    'Esta expresion devuelve un'
    'boolean'

    def __init__(self, val):
        self.val = val

    def ejecutar(self,tables):
        return self.val


class exp_text(exp_query):
    'Devuelve el texto'

    def __init__(self, val):
        self.val = val
    def ejecutar(self,tables):
        return self.val

class exp_num(exp_query):
    'Devuelve un número'

    def __init__(self, val):
        self.val = val
    def ejecutar(self,tables):
        return self.val



class exp_suma(exp_query):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    #Vamos a asumir el tipo
    # suponemos que es numérico :v

    def ejecutar(self,tablas):
        global tabla
        global NombreDB
        exp1 = self.exp1.ejecutar(tablas)
        exp2 = self.exp2.ejecutar(tablas)
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        me = float(menor[i])
                        ma = float(mayor[i])
                        result.append(me+ma)
                    except ValueError:
                        e = errores.CError(0,0,"Imposible convertir a numeric en la suma.",'Semantico')
                        errores.insert_error(e)
                        return e
                menor = exp1 if len(val1) < len(val2) else exp2
                newdict = {
                    'valores':result,
                    'columna': menor['columna']
                }

                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:
                    try:

                        result.append(float(col)+float(val))
                    except ValueError:
                        e = errores.CError(0,0,"Imposible convertir a numeric en la suma.",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:

                return float(exp1) + float(exp2)
            except ValueError:
                e = errores.CError(0,0,"Imposible convertir a numeric en la suma.",'Semantico')
                errores.insert_error(e)
                return e



class exp_resta(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        me = float(menor[i])
                        ma = float(mayor[i])
                        result.append(me-ma)
                    except ValueError:
                        e = errores.CError(0,0,"Imposible convertir a numeric en la resta.",'Semantico')
                        errores.insert_error(e)
                        return e

                newdict = {
                    'valores':result,
                    'columna': exp1['columna'].append(exp2['columna'][0])
                }
                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:

                    try:

                        result.append(float(col)-float(val))
                    except ValueError:
                        e = errores.CError(0,0,"Imposible convertir a numeric en la suma.",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:

                return float(exp1) - float(exp2)
            except ValueError:
                e = errores.CError(0,0,"Imposible convertir a numeric en la resta.",'Semantico')
                errores.insert_error(e)
                return e



class exp_multiplicacion(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        me = float(menor[i])
                        ma = float(mayor[i])
                        result.append(me*ma)
                    except ValueError:
                        e = errores.CError(0,0,"Imposible convertir a numeric en la multiplicacion.",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': exp1['columna'].append(exp2['columna'][0])
                }
                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:
                    try:

                        result.append(float(col)*float(val))
                    except ValueError:
                        e = errores.CError(0,0,"Imposible convertir a numeric en la suma.",'Semantico')
                        errores.insert_error(e)
                        return e

                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:

                return float(exp1) *float(exp2)
            except ValueError:
                e = errores.CError(0,0,"Imposible convertir a numeric en la multiplicacion.",'Semantico')
                errores.insert_error(e)
                return e


class exp_division(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        me = float(menor[i])
                        ma = float(mayor[i])
                        result.append(me/ma)
                    except ValueError:
                        e = errores.CError(0,0,"Imposible convertir a numeric en la division.",'Semantico')
                        errores.insert_error(e)
                        return e

                newdict = {
                    'valores':result,
                    'columna': exp1['columna'].append(exp2['columna'][0])
                }
                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:
                    try:

                        result.append(float(col)/float(val))
                    except ValueError:
                        e = errores.CError(0,0,"Imposible convertir a numeric en la suma.",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:

                return float(exp1) - float(exp2)
            except ValueError:
                e = errores.CError(0,0,"Imposible convertir a numeric en la division.",'Semantico')
                errores.insert_error(e)
                return e


class select_column():
    'Abstract Class'


#class column_id(select_column):
#    def __init__(self, id, table, alias):
#        self.id = id
#        self. table = table
#        self.alias = alias




class column_mathtrig(select_column):
    'Abstract Class'


class math_abs(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
        self.type = exp_type.numeric

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = int(reg)
                    result.append(abs(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e

            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return num
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e




class math_cbrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(mt.cbrt(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return mt.cbrt(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_ceil(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(num)
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return mt.ceil(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_degrees(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(mt.degrees(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return mt.degrees(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_div(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        num1 = float(menor[i])
                        num2 = float(mayor[i])
                        result.append(mt.div(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': exp1['columna'].append(exp2['columna'][0])
                }
                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:
                    try:
                        num1 = float(col)
                        num2 = float(val)
                        result.append(mt.div(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:
                num1 = float(exp1)
                num2 = float(exp2)
                return mt.div(num1 , num2)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_exp(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = int(reg)
                    result.append(mt.exp(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = int(exp)
                return mt.exp(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e

class math_factorial(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = int(reg)
                    result.append(mt.factorial(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = int(exp)
                return mt.factorial(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_floor(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(mt.floor(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return mt.floor(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico','Semantico')
                errores.insert_error(e)
                return e


class math_gcd(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        num1 = int(menor[i])
                        num2 = int(mayor[i])
                        result.append(mt.gcd(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': exp1['columna'].append(exp2['columna'][0])
                }
                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:
                    try:
                        num1 = int(col)
                        num2 = int(val)
                        result.append(mt.gcd(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:
                num1 = int(exp1)
                num2 = int(exp2)
                return mt.gcd(num1,num2)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e

class math_lcm(column_mathtrig):
    def __init__(self,exp1,exp2,alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        num1 = int(menor[i])
                        num2 = int(mayor[i])
                        result.append(mt.lcm(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': exp1['columna'].append(exp2['columna'][0])
                }
                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:
                    try:
                        num1 = int(col)
                        num2 = int(val)
                        result.append(mt.lcm(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:
                num1 = int(exp1)
                num2 = int(exp2)
                return mt.lcm(num1,num2)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e



class math_ln(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(mt.ln(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return mt.ln(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_log(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        global tabla
        global NombreDB
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        num1 = int(menor[i])
                        num2 = int(mayor[i])
                        result.append(mt.log(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': exp1['columna'].append(exp2['columna'][0])
                }
                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:
                    num1 = int(col)
                    num2 = int(val)
                    result.append(mt.log(num1,num2))
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:
                num1 = int(exp1)
                num2 = int(exp2)
                return mt.log(num1,num2)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_log10(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(mt.log10(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            num = float(exp)
            return mt.log10(num)

class math_min_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = int(reg)
                    result.append(mt.min_scale(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = int(exp)
                return mt.min_scale(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e

class math_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.scale(str(reg)))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.scale(str(exp))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e

class math_mod(column_mathtrig):
    def __init__(self, exp1,exp2, alias):
        self.exp1 = exp1
        self.exp2  = exp2
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        num1 = float(menor[i])
                        num2 = float(mayor[i])
                        result.append(mt.mod(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': exp1['columna'].append(exp2['columna'][0])
                }
                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:
                    try:
                        num1 = float(col)
                        num2 = float(val)
                        result.append(mt.mod(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:
                num1 = float(exp1)
                num2 = float(exp2)
                return mt.mod(num1,num2)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_pi(column_mathtrig):
    def __init__(self, alias):
        self.val = mt.pi()
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        try:
            return self.val
        except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_power(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        # si al menos una es diccionario
        if isinstance(exp1,dict) or isinstance(exp2,dict):
            #Si ambas son diccionario
            if isinstance(exp1,dict) and isinstance(exp2,dict):
                val1 = exp1['valores']
                val2 = exp2['valores']
                #vemos cual es el menor
                menor = val1 if len(val1) < len(val2) else val2
                mayor = val1 if len(val1) > len(val2) else val2
                result = []
                #iteramos sobre el menor
                for i in range(len(menor)):
                    try:
                        num1 = int(menor[i])
                        num2 = int(mayor[i])
                        result.append(mt.power(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': exp1['columna'].append(exp2['columna'][0])
                }
                return newdict
            else:
                #Solo una de ellas es diccionario
                dic = exp1 if isinstance(exp1,dict) else exp2
                val = exp1 if not isinstance(exp1,dict) else exp2
                valores = dic['valores']
                result = []
                for col in valores:
                    try:
                        num1 = int(col)
                        num2 = int(val)
                        result.append(mt.power(num1,num2))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica",'Semantico')
                        errores.insert_error(e)
                        return e
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:
                num1 = int(exp1)
                num2 = int(exp2)
                return mt.power(num1,num2)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_radians(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(mt.radians(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return mt.radians(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_round(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(round(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return round(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_sign(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(mt.sign(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return mt.sign(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_sqrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(mt.sqrt(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return mt.sqrt(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e

class math_trim_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = int(reg)
                    result.append(mt.trim_scale(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario

            try:
                num = int(exp)
                return mt.trim_scale(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e

class math_widthBucket(column_mathtrig):
    def __init__(self, exp1, exp2, exp3, exp4, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4
        self.alias = alias

    def ejecutar(self,tables):
        #xd
        try:
            return mt.width_bucket(9,8,7,6)
        except ValueError:
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e


class math_trunc(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    num = float(reg)
                    result.append(mt.trunc(num))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica",'Semantico')
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                num = float(exp)
                return mt.trunc(num)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e


class math_random(column_mathtrig):
    def __init__(self, alias):
        self.alias = alias

    def ejecutar(self,tables):

        return mt.random()

class math_setseed(column_mathtrig):
    def __init__(self,exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        global tabla
        global NombreDB
        try:
            mt.setseed(self.exp.ejecutar(tables))
        except ValueError:
                e = CError(0,0,"Error en funcion matematica",'Semantico')
                errores.insert_error(e)
                return e



class trig_acos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.acos(temp)
                subs.append(trim)

            val['valores'] = subs

            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.acos(float(temp))

            return trim





class trig_acosd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.acosd(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.acosd(float(temp))

            return trim



class trig_asin(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.asin(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.asin(float(temp))

            return trim





class trig_asind(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.asind(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.asind(float(temp))

            return trim






class trig_atan(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.atan(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.atan(float(temp))

            return trim




class trig_atand(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.atand(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.atand(float(temp))

            return trim




class trig_atan2(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
        if isinstance(val1,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico','Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val2,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico','Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val1,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val1['valores']:
                try:
                    temp1 = float(st)
                    temp2 = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.atan2(temp1,temp2)
                subs.append(trim)

            val1['valores'] = subs
            return val1


        #Es solo un valor en especifico
        else:
            try:
                temp1 = float(self.exp1)
                temp2 = float(self.exp2)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.atan2(temp1,temp2)

            return trim







class trig_atan2d(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
        if isinstance(val1,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val2,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val1,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val1['valores']:
                try:
                    temp1 = float(st)
                    temp2 = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.atan2d(temp1,temp2)
                subs.append(trim)

            val1['valores'] = subs
            return val1


        #Es solo un valor en especifico
        else:
            try:
                temp1 = float(self.exp1)
                temp2 = float(self.exp2)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.atan2d(temp1,temp2)

            return trim





class trig_cos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.cos(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.cos(float(temp))

            return trim

class trig_cosd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.cosd(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.cosd(float(temp))

            return trim






class trig_cot(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.cot(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.cot(float(temp))

            return trim



class trig_cotd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.cotd(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.cotd(float(temp))

            return trim




class trig_sin(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.sin(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.sin(float(temp))

            return trim


class trig_sind(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.sind(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.sind(float(temp))

            return trim


class trig_tan(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.tan(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.tan(float(temp))

            return trim



class trig_tand(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias


    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion tri",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.tand(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.tand(float(temp))

            return trim


class trig_sinh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.sinh(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.sinh(float(temp))

            return trim




class trig_cosh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.cosh(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val, int)):
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e
            trim = mt.cosh(float(val))

            return trim




class trig_tanh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.tanh(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.tanh(float(temp))

            return trim




class trig_asinh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.asinh(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.asinh(float(temp))

            return trim


class trig_acosh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.acosh(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.acosh(float(temp))

            return trim

class trig_atanh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                    errores.insert_error(e)
                    return e

                trim =  mt.atanh(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.atanh(float(temp))

            return trim


class column_function(select_column):
    'clase Abstracta'

class fun_sum(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion sum",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

            #recorro valores y saco el substring
            total = 0
            for st in val['valores']:
                total = total + int(st)


            val['valores'] = total
            return val


        #Es solo un valor en especifico
        else:
            e = CError(0,0,"Error en funcion sum",'Semantico')
            errores.insert_error(e)
            return e

class fun_avg(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion avg",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            total = 0
            for st in val['valores']:
                total = total + float(st)

            prom = total / len(val['valores'])
            val['valores'] = prom
            return val


        #Es solo un valor en especifico
        else:
            e = CError(0,0,"Error en funcion avg",'Semantico')
            errores.insert_error(e)
            return e

class fun_max(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion max",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring
                if len(val['valores']) == 0:
                    e = CError(0,0,"Error en funcion max",'Semantico')
                    errores.insert_error(e)
                    return e

                minimo = val['valores'][0]
                for st in val['valores']:
                    temp =  st
                    if minimo < temp:
                        minimo =  temp

                posiciones = []
                contador = 0
                for st in val['valores']:

                    if st == min :
                        posiciones.append(contador)
                    contador = contador + 1

                val['posiciones'] = posiciones
                return val
            else:
                e = CError(0,0,"Error en funcion max",'Semantico')
                errores.insert_error(e)
                return e



        #Es solo un valor en especifico
        else:
            e = CError(0,0,"Error en funcion max",'Semantico')
            errores.insert_error(e)
            return e


class fun_min(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion min",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring
                if len(val['valores']) == 0:
                    e = CError(0,0,"Error en funcion min",'Semantico')
                    errores.insert_error(e)
                    return e

                minimo = val['valores'][0]
                for st in val['valores']:
                    temp =  st
                    if minimo > temp:
                        minimo =  temp

                posiciones = []
                contador = 0
                for st in val['valores']:

                    if st == min :
                        posiciones.append(contador)
                    contador = contador + 1

                val['posiciones'] = posiciones
                return val
            else:
                e = CError(0,0,"Error en funcion min",'Semantico')
                errores.insert_error(e)
                return e


        #Es solo un valor en especifico
        else:
            e = CError(0,0,"Error en funcion min",'Semantico')
            errores.insert_error(e)
            return e





class fun_count(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en parametros de count",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor


            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring

            temp = len(val['valores'])
            val['valores']= temp
            return val



        #Es solo un valor en especifico
        else:
            if val == '*':
                    if len(tables) != 1:
                        e = CError(0,0,"Error en funcion count",'Semantico')
                        errores.insert_error(e)
                        return e
                    else:
                        a = tables[0]['values']
                        t = ts.getTabla(a)
                        r = s.extractTable(t.db,t.table)
                        return len(r)
            else:

                e = CError(0,0,"Error en funcion count",'Semantico')
                errores.insert_error(e)
                return e


class fun_length(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en parametros de lenght",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                temp =  str(st )
                trim =  len(temp)
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val['valores'] )
            trim = len(temp)

            return trim



class fun_trim(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en parametros de trim",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                temp =  str(st )
                trim =  temp.strip()
                subs.append(trim)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val['valores'] )
            trim =  temp.strip()

            return trim





class fun_md5(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en parametros md5",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                temp =  str(st )
                crypt = hashlib.md5()
                crypt.update(temp.encode('utf-8'))
                r = crypt.hexdigest()
                subs.append(r)

            val['valores'] = subs
            return val
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val['valores'] )
            crypt = hashlib.md5()
            crypt.update(temp.encode('utf-8'))
            r = crypt.hexdigest()
            newdict = {
                        'valores' : r,
                        'columna': []
                    }
            return newdict



class fun_sha256(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en parametros sha2556",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

                #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                temp =  str(st )
                crypt = hashlib.sha256()
                crypt.update(temp.encode('utf-8'))
                r = crypt.hexdigest()
                subs.append(r)

            val['valores'] = subs
            return val





        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val['valores'] )
            crypt = hashlib.sha256()
            crypt.update(temp.encode('utf-8'))
            r = crypt.hexdigest()

            return r




class fun_convert(column_function):
    def __init__ (self,exp,tipo,alias):
        self.exp = exp
        self.type = tipo
        self.alias = alias

    def ejecutar(self,tables):
        return self.exp

class fun_substr(column_function):
    def __init__ (self,exp,min,max,alias):
        self.exp = exp
        self.min = min
        self.max = max
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en parametros substring",'Semantico')
            errores.insert_error(e)
            return e
        if isinstance(val,dict):
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring

               #recorro valores y saco el substring
            subs = []
            for st in val['valores']:
                temp =  str(st )
                sub = temp[self.min:self.max]
                subs.append(sub)

            val['valores'] = subs
            return val


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val)
            sub = temp[self.min:self.max]

            return sub


class fun_greatest(column_function):
    def __init__ (self,lexps,alias):
        self.lexps = lexps
        self.alias = alias

    def ejecutar(self,tables):

        try:
            if len(self.lexps) == 0 :
                e = CError(0,0,"Funcion greatest necesita una lista",'Semantico')
                errores.insert_error(e)
                return e

            val = self.lexps[0].ejecutar(tables)
            if isinstance(val,CError):
                e = CError(0,0,"Error en parametros diferente",'Semantico')
                errores.insert_error(e)
                return e
            #if val['valores'] == None or len(val['valores']) == 0: return None
            #Viene solo un id, es columna
            if len(self.lexps) == 1 and isinstance(val,dict):
                maximo = val['valores'][0]
                for valor in val['valores']:

                    if  maximo < valor :
                        maximo = valor
                #retornar min
                val['valores'] = maximo
                return val
            #Es una lista de valores puede venir como dict o no
            else:

                maximo = val

                for dato in self.lexps:
                    temp = dato.ejecutar(tables)

                    if maximo < temp:
                        maximo = temp


                return maximo
        except:
            #Error
            e = CError(0,0,"Error en parametros de funcion greatest",'Semantico')
            errores.insert_error(e)
            return e

class fun_least(column_function):
    def __init__ (self,lexps,alias):
        self.lexps = lexps
        self.alias = alias

    def ejecutar(self,tables):
        if len(self.lexps) == 0 :
            e = CError(0,0,"Funcion least necesita una lista",'Semantico')
            errores.insert_error(e)
            return e
        try:

            val = self.lexps[0].ejecutar(tables)

            if isinstance(val,CError):
                e = CError(0,0,"Error en parametros de menor o igual",'Semantico')
                errores.insert_error(e)
                return e
            if val == None:
                e = CError(0,0,"Error en parametros de menor o igual",'Semantico')
                errores.insert_error(e)
                return e

            #if isinstance(lexps[0],exp_id) :


            #Viene solo un id, es columna
            if len(self.lexps) == 1 and isinstance(val,dict):
                minimo = val['valores'][0]
                for valor in val['valores']:

                    if  minimo < valor :
                        minimo = valor
                #retornar min
                val['valores'] = minimo
                return val
            #Es una lista de valores puede venir como dict o no
            else:


                minimo = val

                for dato in self.lexps:

                    #obtengo el valor de diferente manera
                    temp = dato.ejecutar(tables)

                    if minimo > temp:
                        minimo = temp


                return minimo
        except:
            #Error
            e = CError(0,0,"Error en funcion least",'Semantico')
            errores.insert_error(e)
            return e





class dato(column_function):
    def __init__ (self,val,alias):
        self.val = val
        self.alias = alias


class fun_now(column_function):
    def __init__ (self,alias):
        self.alias = alias

    def ejecutar(self,tables):
        # dd/mm/YY
        today = date.today()
        d1 = today.strftime("%Y-%m-%d %H:%M:%S")
        return d1

class exp_igual(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5

        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
        if isinstance(val1,CError) or  isinstance(val2,CError):
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                try:
                    val = float(val)
                except ValueError:
                    val2 = str(val2)
                if val == val2:
                    posiciones.append(contador)
                contador = contador +1
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :

            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
                        try:
                            val = float(val)
                            val2 = float(val2)
                        except ValueError:
                            val = str(val)
                            val2 = str(val2)
                        if val == val2['valores'][contador]:
                            posiciones.append(contador)
                        contador = contador +1
                    columna1 = val1['columna']
                    if len(val2['columna'] != 0):
                        columna1.append(val2['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna1
                    }
                    return newdict
            else:
                if len(val2['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
                        try:
                            val1['valores'][contador] = float(val1['valores'][contador])
                            val = float(val)
                        except ValueError:
                            val1['valores'][contador] = str(val1['valores'][contador])
                            val = str(val)
                        if  val1['valores'][contador] == val:
                            posiciones.append(contador)
                        contador = contador +1
                    columna2 = val2['columna']
                    if len(val1['columna'] != 0):
                        columna2.append(val1['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna2
                    }
                    return newdict
        #Error
        else:
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e



class exp_mayor(exp_query):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5

        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
        if isinstance(val1,CError) or  isinstance(val2,CError):
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                try:
                    val = float(val)
                except ValueError:
                    val2 = str(val2)
                if val > val2:
                    posiciones.append(contador)
                contador = contador +1
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :

            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
                        try:
                            val = float(val)
                            val2 = float(val2)
                        except ValueError:
                            val = str(val)
                            val2 = str(val2)
                        if val > val2['valores'][contador]:
                            posiciones.append(contador)
                        contador = contador +1
                    columna1 = val1['columna']
                    if len(val2['columna'] != 0):
                        columna1.append(val2['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna1
                    }
                    return newdict
            else:
                if len(val2['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
                        try:
                            val1['valores'][contador] = float(val1['valores'][contador])
                            val = float(val)
                        except ValueError:
                            val1['valores'][contador] = str(val1['valores'][contador])
                            val = str(val)
                        if  val1['valores'][contador] > val:
                            posiciones.append(contador)
                        contador = contador +1
                    columna2 = val2['columna']
                    if len(val1['columna'] != 0):
                        columna2.append(val1['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna2
                    }
                    return newdict
        #Error
        else:
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e




class exp_menor(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5

        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
        if isinstance(val1,CError) or  isinstance(val2,CError):
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                try:
                    val = float(val)
                except ValueError:
                    val2 = str(val2)
                if val < val2:
                    posiciones.append(contador)
                contador = contador +1
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :

            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
                        try:
                            val = float(val)
                            val2 = float(val2)
                        except ValueError:
                            val = str(val)
                            val2 = str(val2)
                        if val < val2['valores'][contador]:
                            posiciones.append(contador)
                        contador = contador +1
                    columna1 = val1['columna']
                    if len(val2['columna'] != 0):
                        columna1.append(val2['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna1
                    }
                    return newdict
            else:
                if len(val2['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
                        try:
                            val1['valores'][contador] = float(val1['valores'][contador])
                            val = float(val)
                        except ValueError:
                            val1['valores'][contador] = str(val1['valores'][contador])
                            val = str(val)
                        if  val1['valores'][contador] < val:
                            posiciones.append(contador)
                        contador = contador +1
                    columna2 = val2['columna']
                    if len(val1['columna'] != 0):
                        columna2.append(val1['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna2
                    }
                    return newdict
        #Error
        else:
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e




class exp_mayor_igual(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5

        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
        if isinstance(val1,CError) or  isinstance(val2,CError):
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                try:
                    val = float(val)
                except ValueError:
                    val2 = str(val2)
                if val >= val2:
                    posiciones.append(contador)
                contador = contador +1
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :

            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
                        try:
                            val = float(val)
                            val2 = float(val2)
                        except ValueError:
                            val = str(val)
                            val2 = str(val2)
                        if val >= val2['valores'][contador]:
                            posiciones.append(contador)
                        contador = contador +1
                    columna1 = val1['columna']
                    if len(val2['columna'] != 0):
                        columna1.append(val2['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna1
                    }
                    return newdict
            else:
                if len(val2['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
                        try:
                            val1['valores'][contador] = float(val1['valores'][contador])
                            val = float(val)
                        except ValueError:
                            val1['valores'][contador] = str(val1['valores'][contador])
                            val = str(val)
                        if  val1['valores'][contador] >= val:
                            posiciones.append(contador)
                        contador = contador +1
                    columna2 = val2['columna']
                    if len(val1['columna'] != 0):
                        columna2.append(val1['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna2
                    }
                    return newdict
        #Error
        else:
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e




class exp_menor_igual(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5

        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
        if isinstance(val1,CError) or  isinstance(val2,CError):
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                try:
                    val = float(val)
                except ValueError:
                    val2 = str(val2)
                if val <= val2:
                    posiciones.append(contador)
                contador = contador +1
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :

            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
                        try:
                            val = float(val)
                            val2 = float(val2)
                        except ValueError:
                            val = str(val)
                            val2 = str(val2)
                        if val <= val2['valores'][contador]:
                            posiciones.append(contador)
                        contador = contador +1
                    columna1 = val1['columna']
                    if len(val2['columna'] != 0):
                        columna1.append(val2['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna1
                    }
                    return newdict
            else:
                if len(val2['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
                        try:
                            val1['valores'][contador] = float(val1['valores'][contador])
                            val = float(val)
                        except ValueError:
                            val1['valores'][contador] = str(val1['valores'][contador])
                            val = str(val)
                        if  val1['valores'][contador] <= val:
                            posiciones.append(contador)
                        contador = contador +1
                    columna2 = val2['columna']
                    if len(val1['columna'] != 0):
                        columna2.append(val1['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna2
                    }
                    return newdict
        #Error
        else:
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e



class exp_diferente(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5

        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
        if isinstance(val1,CError) or  isinstance(val2,CError):
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                try:
                    val = float(val)
                except ValueError:
                    val2 = str(val2)
                if val != val2:
                    posiciones.append(contador)
                contador = contador +1
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :

            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
                        try:
                            val = float(val)
                            val2 = float(val2)
                        except ValueError:
                            val = str(val)
                            val2 = str(val2)
                        if val != val2['valores'][contador]:
                            posiciones.append(contador)
                        contador = contador +1
                    columna1 = val1['columna']
                    if len(val2['columna'] != 0):
                        columna1.append(val2['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna1
                    }
                    return newdict
            else:
                if len(val2['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor",'Semantico')
                    errores.insert_error(e)
                    return e
                else:
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
                        try:
                            val1['valores'][contador] = float(val1['valores'][contador])
                            val = float(val)
                        except ValueError:
                            val1['valores'][contador] = str(val1['valores'][contador])
                            val = str(val)
                        if  val1['valores'][contador] != val:
                            posiciones.append(contador)
                        contador = contador +1
                    columna2 = val2['columna']
                    if len(val1['columna'] != 0):
                        columna2.append(val1['columna'][0])
                    newdict = {
                        'posiciones' : posiciones,
                        'columna': columna2
                    }
                    return newdict
        #Error
        else:
            e = CError(0,0,"Error en parametros de mayor",'Semantico')
            errores.insert_error(e)
            return e


class exp_in(exp_query):
    def __init__(self, exp, query):
        self.exp = exp
        self.query = query

class exp_not_in(exp_query):
    def __init__(self, exp, query):
        self.exp = exp
        self.query = query

class exp_between(exp_query):
    def _init_(self, exp1, exp2,exp3):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
        val3 = self.exp3.ejecutar(tables)
        if isinstance(val1,CError) or  isinstance(val2,CError) or isinstance(val3,CError):
            e = CError(0,0,"Error en parametros between",'Semantico')
            errores.insert_error(e)
            return e



        #id op val
        if isinstance(self.exp1,exp_id) and not isinstance(self.exp2,exp_id) and not isinstance(self.exp3,exp_id):
            if isinstance(val2,dict):
                exp2 = val2['valores']
            else:
                exp2 = val2

            if isinstance(val3,dict):
                exp3 = val3['valores']
            else:
                exp3 = val3

            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val < exp3 and val > exp2:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #error
        else: 
            e = CError(0,0,"Error en parametros between",'Semantico')
            errores.insert_error(e)
            return e

    

class casewhen(exp_query):
    def __init__(self, case,exp,lcases,els,alias):
        self.case = case
        self.exp = exp 
        self.lcases = lcases
        self.els = els
        self.alias = alias

class case(exp_query):
    def __init__(self, exp_cas, exp ):
        self.exp_cas = exp_cas
        self.exp = exp

class exp_exists(exp_query):
    def __init__(self,query,alias,yesno) -> None:
        self.query = query
        self.alias = alias
        self.yesno = yesno

class table_expression():
    'Abstract Class'

class texp_id(table_expression):
    def __init__(self,id,alias):
        self.id = id
        self.alias = alias





class texp_query(table_expression)        :
    def __init__(self,query,alias):
        self.query = query
        self.alias = alias

#############
# Funciones que usaré 
#############

def getKeyFromValue(value,d):
    for table, alias in d.items():
        if alias == value:
            return table

    e = errores.CError(0,0,"Imposible obtener la tabla.",'Semantico')
    errores.insert_error(e)
    return e

def getInstance(col):
    if isinstance(col,fun_count):
        return 'count'
    elif isinstance(col,fun_sum):
        return 'sum'
    elif isinstance(col,fun_avg):
        return 'avg'
    elif isinstance(col,fun_min):
        return 'min'
    else:
        return 'max'


def ejecutar_groupBy(valores,select_list):
    #Tenemos que encontrar cual es la funcion de agrupacion
    #En específico que columna es.
    contador = 0
    instance = ''
    for col in select_list:
        if isinstance(col,fun_count) or isinstance(col,fun_sum) or isinstance(col,fun_avg) or isinstance(col,fun_min) or isinstance(col,fun_max):
            instance = getInstance(col)
            break
        else:
            contador = contador +1
    
    #Una vez tenemos el indice obtenemos el valor devuelto por esa funcion
    agg = valores[contador]
    #obtenemos cual es el resultado
    res = agg['valores']
    #obtenemos las columnas por las que tenemos que agrupar
    newlist = []
    newcont = 0
    #Esto nos devuelve todo menos la columna de agregacion
    for val in valores:
        if newcont != contador:
            newlist.append(val)
        newcont = newcont +1

    dictionary = {}
    values = []
    index = 0
    firstpass = True
    for val in newlist:
        if isinstance(val,dict):
            val_vals = val['valores']
            index = 0
            for key in val_vals:
                if firstpass :
                    values.append(key)
                else:
                    values[index] = values[index] + '~' + key
                    index += 1
            firstpass = False

    #Obtenemos una lista basada en campos con las columnas iguales

    #Obtenemos el dato agrupado como columna sin agrupar
    #name_column = agg['columna'][0]['nombre']
    name_table = agg['columna'][0]['tabla']
    index_col = agg['columna'][0]['indice']

    t = s.extractTable(NombreDB,name_table)
    data = []
    for reg in t:
        data.append(reg[index_col])



    #Ahora generamos un diccionario con valores para cada serie de datos
    if instance == 'sum':
        contdata = 0
        for val in values:
            if val not in dictionary:
                if contdata >= len(data):
                    dictionary[val] = '-'
                    continue
                dictionary[val] = data[contdata]
            else:
                if contdata >= len(data):
                    dictionary[val] = '-'
                    continue
                dictionary[val] += data[contdata] 
            contdata+=1
    elif instance == 'count':
        for val in values:
            if val not in dictionary:
                dictionary[val] = 1
            else:
                dictionary[val] += 1
    elif instance=='avg':
        contdata = 0
        for val in values:
            if val not in dictionary:
                if contdata >= len(data):
                    dictionary[val] = '-'
                    continue
                dictionary[val] = data[contdata]
            else:
                if contdata >= len(data):
                    dictionary[val] = '-'
                    continue
                dictionary[val] += data[contdata]
            contdata+=1
        #We make a new dictionary 
        #but with number of repeated rows
        new_dict = {}
        for val in values:
            if val not in new_dict:
                new_dict[val] = 1
            else:
                new_dict[val] += 1
        for val in dictionary:
            dictionary[val] /= new_dict[val]
    elif instance=='max':
        contdata = 0
        for val in values:
            if val not in dictionary:
                if contdata >= len(data):
                    dictionary[val] = '-'
                    continue
                dictionary[val] = data[contdata]
            else:
                if contdata >= len(data):
                    dictionary[val] = '-'
                    continue
                if dictionary[val] < data[contdata] :
                    dictionary[val] = data[contdata]
            contdata+=1
    else:
        contdata = 0
        for val in values:
            if val not in dictionary:
                if contdata >= len(data):
                    dictionary[val] = '-'
                    continue
                dictionary[val] = data[contdata]
            else:
                if contdata >= len(data):
                    dictionary[val] = '-'
                    continue
                if dictionary[val] > data[contdata] :
                    dictionary[val] = data[contdata]
            contdata+=1
    
    # Con el diccionario generado devolvemos
    # una lista para ser tratada en la
    # presentacion de la informacion

    results = []
    for llave in dictionary:
        fila = llave.split('~')
        fila.append(dictionary[llave])
        results.append(fila)

    #Buscamos la lista mas larga
    max = 0
    for res in results:
        if len(res)>max:
            max = len(res)
    #Llenamos los vacios con menos
    for res in results:
        if len(res) < max :
            for i in range(len(res),max):
                res.append('-')
    
    
    return results







    


############
#Condiciones
############

def cond_OR(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 

def cond_AND(lst1, lst2): 
    final_list = list(set(lst1) & set(lst2)) 
    return final_list 

class condition(exp_query):
    def __init__(self,exp ,tipo):
        self.exp = exp
        self.tipo = tipo


    

def ejecutar_conditions(tables,lcond):
    condition = lcond
    if len(condition) == 0:
        e = errores.CError(0,0,"Error en la ejecucion de condiciones.",'Semantico')
        errores.insert_error(e)
        return e
    elif len(condition) == 1:
        return condition[0].exp.ejecutar(tables)
    else:
        #Obtengo las primeras posiciones y dependiendo 
        valor = condition[0].exp.ejecutar(tables)
        res =  valor['posiciones']
        if len(condition) > 1 :
            for i in range(1, len(condition)):
                if condition[i].tipo.upper() == 'AND':
                    
                    res = cond_AND(res, condition[i].exp.ejecutar(tables)['posiciones'])
                else:
                    res = cond_OR(res, condition[i].exp.ejecutar(tables)['posiciones'])
        return res

def filtrar(lista,posiciones):
    delete = []
    for a in range(0,len(lista)):
        if a not in posiciones:
            
            delete.append(a)
    
    
    for index in sorted(delete, reverse=True):
        
        del lista[index]
    
    return lista