#
import hashlib
from datetime import date
from os.path import split
from main import ts
import storage as s
from enum import Enum
from main import default_db
import mathtrig as mt
import main
import prettytable as pt
import reportError as errores
from reportError import CError
#

#
class exp_type(Enum):
    numeric = 1
    text  = 2
    boolean = 3
    identifier = 4

#


class query():
    ' Clase abstracta query'


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

    def ejecutar(self):
        gro = self.group
        #Obtener la lista de tablas
        tables = {}
        for tabla in self.table_expression:
            tables[tabla.id]  = tabla.alias
        
        results = []
        for col in self.select_list:
            
            
            
            res = col.ejecutar(tables)
            if isinstance(res,errores.CError):
                e = errores.CError(0,0,"Error obteniendo informacion de alguna columna.") 
                errores.insert_error(e)
                return e
            
            results.append(res)
        
        
        conditions = []
        if self.condition is not None:
            conditions = ejecutar_conditions(tables,self.condition)
            if isinstance(conditions,errores.CError):
                e = errores.CError(0,0,"Error realizando las condiciones.")
                errores.insert_error(e)
                return e
        grouped = []
        
        if self.group :
            
            grouped = ejecutar_groupBy(results,self.select_list)
            if isinstance(grouped,errores.CError):
                e = errores.CError(0,0,"Error agrupando los elementos.")
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
                if isinstance(vals[0],list):
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
                registros = s.extractTable(default_db,t)
                #Buscamos los encabezados
                encabezados = ts.getColumns(default_db,t)
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
            
            tupla = ts.getTabla(self.val)
            
            #Este devuelve la base de datos y la
            # tabla
            if tupla is None : return #Error semántico
            #Ahora obtenemos los registros de la columna
            registros = s.extractTable(tupla.db,tupla.tabla)

            #Obtener el indice de la columna

            indice = ts.getIndice(tupla.db,tupla.tabla,self.val)

            # Obtener la columna de los registros

            columna = []
            for reg in registros:
                columna.append(reg[indice])
            dict = {
                "valores":columna,
                "columna":[{"nombre":self.val,"indice":indice,"tabla":tupla.table}]
            }
            return dict
        else:
            #Verificamos que exista 
            if self.table not in tables and self.table not in tables.values():
                e = errores.CError(0,0,"La tabla buscada no está en el from")
                errores.insert_error(e)
                return e
            # Existe, ahora obtenemos el nombre de la tabla
             
            if self.table not in tables.values():
                # si no fuera un alias 
                #significa que el nombre es la tabla
                registros = s.extractTable(default_db,self.table)
                if self.val == '*':
                    encabezados = ts.getColumns(default_db,self.table)
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

                indice = ts.getIndice(default_db,self.table,self.val)
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
                #Obtenemos la tabla
                registros = s.extractTable(default_db,table)

                if self.val == '*':
                    encabezados = ts.getColumns(default_db,table)
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
                indice = main.ts.getIndice(default_db,table,self.val)
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
                        e = errores.CError(0,0,"Imposible convertir a numeric en la suma.")
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
                        return None
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
                e = errores.CError(0,0,"Imposible convertir a numeric en la suma.")
                errores.insert_error(e)
                return e


    


class exp_resta(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    def ejecutar(self,tables):
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
                        e = errores.CError(0,0,"Imposible convertir a numeric en la resta.")
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
                        return None
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
                e = errores.CError(0,0,"Imposible convertir a numeric en la resta.")
                errores.insert_error(e)
                return e
            


class exp_multiplicacion(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    def ejecutar(self,tables):
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
                        e = errores.CError(0,0,"Imposible convertir a numeric en la multiplicacion.")
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
                        return None
                    
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
                e = errores.CError(0,0,"Imposible convertir a numeric en la multiplicacion.")
                errores.insert_error(e)
                return e


class exp_division(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    def ejecutar(self,tables):
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
                        e = errores.CError(0,0,"Imposible convertir a numeric en la division.")
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
                        return None
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
                e = errores.CError(0,0,"Imposible convertir a numeric en la division.")
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
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(abs(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
                
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return abs(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e
        
        


class math_cbrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try: 
                    result.append(mt.cbrt(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.cbrt(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_ceil(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.ceil(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.ceil(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_degrees(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.degrees(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.degrees(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_div(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion trigonometrica")
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
                        result.append(mt.div(menor[i],mayor[i]))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.div(col,val))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                return mt.div(float(exp1) , float(exp2))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e
        

class math_exp(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.exp(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.exp(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e

class math_factorial(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.factorial(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.factorial(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_floor(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.floor(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.floor(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_gcd(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.gcd(menor[i],mayor[i]))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.gcd(col,val))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                return mt.gcd(float(exp1) , float(exp2))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e

class math_lcm(column_mathtrig):
    def __init__(self,exp1,exp2,alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias 

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.lcm(menor[i],mayor[i]))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.lcm(col,val))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                return mt.lcm(float(exp1) , float(exp2))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e



class math_ln(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.ln(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.ln(float(exp))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_log(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.log(menor[i],mayor[i]))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                    result.append(mt.log(col,val))
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            try:
                return mt.log(float(exp1) , float(exp2))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_log10(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.log10(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.log10(exp)

class math_min_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.min_scale(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.min_scale(float(exp))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e

class math_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
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
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.scale(str(exp))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e

class math_mod(column_mathtrig):
    def __init__(self, exp1,exp2, alias):
        self.exp1 = exp1
        self.exp2  = exp2
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.mod(menor[i],mayor[i]))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.mod(col,val))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                return mt.mod(float(exp1) , float(exp2))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_pi(column_mathtrig):
    def __init__(self, alias):
        self.val = mt.pi()
        self.alias = alias

    def ejecutar(self,tables):
        try:
            return self.val
        except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_power(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias
    
    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar(tables)
        exp2 = self.exp2.ejecutar(tables)
        if isinstance(exp1,CError) or isinstance(exp2,CError):
            e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.power(menor[i],mayor[i]))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                        result.append(mt.power(col,val))
                    except ValueError:
                        e = CError(0,0,"Error en funcion matematica")
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
                return mt.power(float(exp1) , float(exp2))
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_radians(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.radians(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.radians(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_round(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(round(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return round(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_sign(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.sign(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.sign(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e


class math_sqrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.sqrt(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.sqrt(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e

class math_trim_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.trim_scale(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario

            try:
                return mt.trim_scale(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
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
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e


class math_trunc(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,CError):
            e = CError(0,0,"Error en funcion matematica")
            errores.insert_error(e)
            return e
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.trunc(reg))
                except ValueError:
                    e = CError(0,0,"Error en funcion matematica")
                    errores.insert_error(e)
                    return e
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.trunc(exp)
            except ValueError:
                e = CError(0,0,"Error en funcion matematica")
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
        try:
            mt.setseed(self.exp.ejecutar(tables))
        except ValueError:
                e = CError(0,0,"Error en funcion matematica")
                errores.insert_error(e)
                return e



class trig_acos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
                    errores.insert_error(e)
                    return e

                trim =  mt.atan2(temp)
                subs.append(trim)
                
            val['valores'] = subs
            return val
            
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica")
                errores.insert_error(e)
                return e
                
            trim = mt.atan2(float(temp))
            
            return trim
 


    

    

class trig_atan2d(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp = exp1
        self.exp2 = exp2
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
                    errores.insert_error(e)
                    return e

                trim =  mt.atan2d(temp)
                subs.append(trim)
                
            val['valores'] = subs
            return val
            
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            try:
                temp = float(val)
            except ValueError:
                e = CError(0,0,"Error en funcion trigonometrica")
                errores.insert_error(e)
                return e
                
            trim = mt.atan2d(float(temp))
            
            return trim
 




class trig_cos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion tri")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion trigonometrica")
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
                    e = CError(0,0,"Error en funcion trigonometrica")
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
                e = CError(0,0,"Error en funcion trigonometrica")
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
            e = CError(0,0,"Error en funcion sum")
            errores.insert_error(e)
            return e
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
            #recorro valores y saco el substring 
            total = 0
            for st in val['valores']:
                total = total + st
              
               
            val['valores'] = total
            return val
            
                
        #Es solo un valor en especifico
        else:
            e = CError(0,0,"Error en funcion sum")
            errores.insert_error(e)
            return e

class fun_avg(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion avg")
            errores.insert_error(e)
            return e
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            total = 0
            for st in val['valores']:
                total = total + st
              
            prom = total / len(val['valores'])
            val['valores'] = prom
            return val
           
                
        #Es solo un valor en especifico
        else:
            e = CError(0,0,"Error en funcion avg")
            errores.insert_error(e)
            return e
 
class fun_max(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion max")
            errores.insert_error(e)
            return e
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                if len(val['valores']) == 0:
                    e = CError(0,0,"Error en funcion max")
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
                e = CError(0,0,"Error en funcion max")
                errores.insert_error(e)
                return e
               
                
                
        #Es solo un valor en especifico
        else:
            e = CError(0,0,"Error en funcion max")
            errores.insert_error(e)
            return e
 

class fun_min(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en funcion min")
            errores.insert_error(e)
            return e
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                if len(val['valores']) == 0: 
                    e = CError(0,0,"Error en funcion min")
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
                e = CError(0,0,"Error en funcion min")
                errores.insert_error(e)
                return e
                
                
        #Es solo un valor en especifico
        else:
            e = CError(0,0,"Error en funcion min")
            errores.insert_error(e)
            return e
 




class fun_count(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en parametros de count")
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
                        e = CError(0,0,"Error en funcion count")
                        errores.insert_error(e)
                        return e
                    else:
                        a = tables[0]['values']
                        t = ts.getTabla(a)
                        r = s.extractTable(t.db,t.table)
                        return len(r)
            else:
                
                e = CError(0,0,"Error en funcion count")
                errores.insert_error(e)
                return e
 

class fun_length(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,CError):
            e = CError(0,0,"Error en parametros de lenght")
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
            e = CError(0,0,"Error en parametros de trim")
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
            e = CError(0,0,"Error en parametros md5")
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
            e = CError(0,0,"Error en parametros sha2556")
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
            e = CError(0,0,"Error en parametros substring")
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
                e = CError(0,0,"Funcion greatest necesita una lista")
                errores.insert_error(e)
                return e

            val = self.lexps[0].ejecutar(tables)
            if isinstance(val,CError):
                e = CError(0,0,"Error en parametros diferente")
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
            e = CError(0,0,"Error en parametros de funcion greatest")
            errores.insert_error(e)
            return e
 
class fun_least(column_function):
    def __init__ (self,lexps,alias):
        self.lexps = lexps
        self.alias = alias
    
    def ejecutar(self,tables):
        if len(self.lexps) == 0 : 
            e = CError(0,0,"Funcion least necesita una lista")
            errores.insert_error(e)
            return e
        try:

            val = self.lexps[0].ejecutar(tables)
            
            if isinstance(val,CError):
                e = CError(0,0,"Error en parametros de menor o igual")
                errores.insert_error(e)
                return e
            if val == None:
                e = CError(0,0,"Error en parametros de menor o igual")
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
            e = CError(0,0,"Error en funcion least")
            errores.insert_error(e)
            return e

  
    
    

class dato(column_function):
    def __init__ (self,val,alias):
        self.val = val
        self.alias = alias
    

class fun_now(column_function):
    def __init__ (self,tables):
        pass
        
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
            e = CError(0,0,"Error en parametros de igual")
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val == val2:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and isinstance(val2,dict) :
            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de igual")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
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
                    e = CError(0,0,"Error en parametros de igual")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
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
            e = CError(0,0,"Error en parametros de igual")
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
            e = CError(0,0,"Error en parametros de mayor")
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val > val2:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :
            
            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor")
                    errores.insert_error(e)
                    return e    
                else: 
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
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
                    e = CError(0,0,"Error en parametros de mayor")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
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
            e = CError(0,0,"Error en parametros de mayor")
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
            e = CError(0,0,"Error en parametros de menor")
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val < val2:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :
            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de menor")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
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
                    e = CError(0,0,"Error en parametros de menor")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
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
            e = CError(0,0,"Error en parametros de menor")
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
            e = CError(0,0,"Error en parametros de mayor o igual")
            errores.insert_error(e)
            return e
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val >= val2:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :
            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de mayor o igual")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
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
                    e = CError(0,0,"Error en parametros de mayor o igual")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
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
            e = CError(0,0,"Error en parametros de mayor o igual")
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
            e = CError(0,0,"Error en parametros de menor o igual")
            errores.insert_error(e)
            return e

        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val <= val2:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and isinstance(val2,dict) :
            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros de menor o igual")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
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
                    e = CError(0,0,"Error en parametros de menor o igual")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
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
            e = CError(0,0,"Error en parametros de menor o igual")
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
            e = CError(0,0,"Error en parametros diferente")
            errores.insert_error(e)
            return e

        #id op val
        if isinstance(val1,exp_id) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val != val2:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and  isinstance(val2,dict) :
            if len(val1['valores']) < len(val2['valores']):

                if len(val1['valores']) == 0:
                    e = CError(0,0,"Error en parametros diferente")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val1['valores']:
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
                    e = CError(0,0,"Error en parametros diferente")
                    errores.insert_error(e)
                    return e
                else: 
                    posiciones = []
                    contador = 0
                    for val in val2['valores']:
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
            e = CError(0,0,"Error en parametros diferente")
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
            e = CError(0,0,"Error en parametros between")
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
            e = CError(0,0,"Error en parametros between")
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

    return None

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

    t = s.extractTable(default_db,name_table)
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
        return None
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