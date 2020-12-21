#
import hashlib
from datetime import date
from main import ts
import storage as s
from enum import Enum
from main import default_db
import mathtrig as mt
import main
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
        self.condition.append(having)

    def ejecutar(self):
        gro = False
        #Obtener la lista de tablas
        tables = {}
        for tabla in self.table_expression:
            tables[tabla.id]  = tabla.alias
        
        results = []
        for col in self.select_list:
            
            
            
            res = col.ejecutar(tables)
            
            results.append(res)
        #return results

        conditions = ejecutar_conditions(tables,self.condition)
        
        for column in results:

            if isinstance(column,dict) and isinstance(column['valores'],list):
                
                column['valores'] = filtrar(column['valores'],conditions)
        
        #return results
            
        consulta = []
        fila = []
        for col in self.select_list:
            fila.append(col.alias)
        
        contador = 0
        for column in results:
            
            if fila[contador] == None:
                if isinstance(column,dict):
                    fila[contador]=column['columna'][0]['nombre']
                else:
                    fila[contador]="Funcion"
                
                
            
            contador = contador +1 

        consulta.append(fila)
        if gro:
            pass
        else:
            cantidad = 0
            for column in results:
                if isinstance(column,dict):
                    cantidad = len(column['valores'])
                    break
            
            for i in range(0,cantidad):
                fila = []
                
                for column in results:
                    if isinstance(column,dict):
                        if isinstance(column['valores'],list):
                            
                            fila.append(column['valores'][i])
                        else:
                            fila.append(column['valores'])
                    else:

                        fila.append(column)
                
                consulta.append(fila)
            
            print(consulta)
        return consulta

        
        
            



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
                #Error semántico
                return None
            # Existe, ahora obtenemos el nombre de la tabla
             
            if self.table not in tables.values():
                # si no fuera un alias 
                #significa que el nombre es la tabla
                registros = s.extractTable(default_db,self.table)
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
                        result.append(me-ma)
                    except ValueError: 
                        return None
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
                return None


    


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
                        return None
                    
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
                return None
            


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
                        return None
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
                return None


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
                        return None
                    
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
                return None


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
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(abs(reg))
                except ValueError:
                    return None
                
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return abs(exp)
            except ValueError:
                return None
        
        


class math_cbrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try: 
                    result.append(mt.cbrt(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.cbrt(exp)
            except ValueError:
                return None


class math_ceil(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.ceil(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.ceil(exp)
            except ValueError:
                return None


class math_degrees(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.degrees(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.degrees(exp)
            except ValueError:
                return None


class math_div(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
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
                        result.append(mt.div(menor[i],mayor[i]))
                    except ValueError:
                        return None
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
                        return None
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
                return None
        

class math_exp(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.exp(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.exp(exp)
            except ValueError:
                return None

class math_factorial(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.factorial(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.factorial(exp)
            except ValueError:
                return None


class math_floor(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.floor(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.floor(exp)
            except ValueError:
                return None


class math_gcd(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
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
                        result.append(mt.gcd(menor[i],mayor[i]))
                    except ValueError:
                        return None
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
                        return None
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
                return None

class math_lcm(column_mathtrig):
    def __init__(self,exp1,exp2,alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias 

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
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
                        result.append(mt.lcm(menor[i],mayor[i]))
                    except ValueError:
                        return None
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
                        return None
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
                return None



class math_ln(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.ln(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.ln(float(exp))
            except ValueError:
                return None


class math_log(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
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
                        result.append(mt.log(menor[i],mayor[i]))
                    except ValueError:
                        return None
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
                return None


class math_log10(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.log10(reg))
                except ValueError:
                    return None
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
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.min_scale(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.min_scale(float(exp))
            except ValueError:
                return None

class math_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.scale(str(reg)))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.scale(str(exp))
            except ValueError:
                return None

class math_mod(column_mathtrig):
    def __init__(self, exp1,exp2, alias):
        self.exp1 = exp1
        self.exp2  = exp2
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
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
                        result.append(mt.mod(menor[i],mayor[i]))
                    except ValueError:
                        return None
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
                        return None
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
                return None


class math_pi(column_mathtrig):
    def __init__(self, alias):
        self.val = mt.pi()
        self.alias = alias

    def ejecutar(self,tables):
        try:
            return self.val
        except ValueError:
                return None


class math_power(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias
    
    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
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
                        result.append(mt.power(menor[i],mayor[i]))
                    except ValueError:
                        return None
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
                        return None 
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
                return None


class math_radians(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.radians(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.radians(exp)
            except ValueError:
                return None


class math_round(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(round(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return round(exp)
            except ValueError:
                return None


class math_sign(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.sign(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.sign(exp)
            except ValueError:
                return None


class math_sqrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.sqrt(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.sqrt(exp)
            except ValueError:
                return None

class math_trim_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.trim_scale(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario

            try:
                return mt.trim_scale(exp)
            except ValueError:
                return None

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
            return None


class math_trunc(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar(tables)
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                try:
                    result.append(mt.trunc(reg))
                except ValueError:
                    return None
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            try:
                return mt.trunc(exp)
            except ValueError:
                return None


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
                return None


class trig_acos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.acos(float(temp))
            
            return trim
 




class trig_acosd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.acosd(float(temp))
            
            return trim
 


class trig_asin(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.asin(float(temp))
            
            return trim
 




class trig_asind(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.asind(float(temp))
            
            return trim
 





class trig_atan(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.atan(float(temp))
            
            return trim
 



class trig_atand(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.atand(float(temp))
            
            return trim
 



class trig_atan2(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.atan2(float(temp))
            
            return trim
 


    

    

class trig_atan2d(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp = exp1
        self.exp2 = exp2
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.atan2d(float(temp))
            
            return trim
 




class trig_cos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.cos(float(temp))
            
            return trim
 





class trig_cosd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.cosd(float(temp))
            
            return trim
 





class trig_cot(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.cot(float(temp))
            
            return trim
 


class trig_cotd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.cotd(float(temp))
            
            return trim
 



class trig_sin(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.sin(float(temp))
            
            return trim
 

class trig_sind(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.sind(float(temp))
            
            return trim
 
 
class trig_tan(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.tan(float(temp))
            
            return trim
 
 

class trig_tand(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias
    

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.tand(float(temp))
            
            return trim
 
 
class trig_sinh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.sinh(float(temp))
            
            return trim
 
    


class trig_cosh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None
                    
                trim =  mt.cosh(temp)
                subs.append(trim)
                
            val['valores'] = subs
            return val
            
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val, int)): return None
            trim = mt.cosh(float(val))
            
            return trim
 



class trig_tanh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.tanh(float(temp))
            
            return trim
 
 


class trig_asinh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.asinh(float(temp))
            
            return trim
 

class trig_acosh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None
                
            trim = mt.acosh(float(temp))
            
            return trim
 
class trig_atanh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            
                #recorro valores y saco el substring 
            subs = []
            for st in val['valores']:
                try:
                    temp = float(st)
                except ValueError:
                    return None

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
                return None

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
            return None

class fun_avg(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
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
            return None
 
class fun_max(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                if len(val['valores']) == 0: return None

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
               
                return None
                
        #Es solo un valor en especifico
        else:
            return None
 

class fun_least(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                if len(val['valores']) == 0: return None

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
               
                return None
                
        #Es solo un valor en especifico
        else:
            return None
 




class fun_count(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
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
                        return None
                    else:
                        a = tables[0]['values']
                        t = ts.getTabla(a)
                        r = s.extractTable(t.db,t.table)
                        return len(r)
            else:
                return None
 

class fun_length(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self,tables):
        val = self.exp.ejecutar(tables)
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
        if len(self.lexps) == 0 : return None
        try:
            val = self.lexps[0].ejecutar(tables)
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
            return None
 
class fun_min(column_function):
    def __init__ (self,lexps,alias):
        self.lexps = lexps
        self.alias = alias
    
    def ejecutar(self,tables):
        if len(self.lexps) == 0 : return None
        try:

            val = self.lexps[0].ejecutar(tables)
            if val == None:
                return None
            
            #if isinstance(lexps[0],exp_id) :

            
            #Viene solo un id, es columna
            if len(self.lexps) == 1 and isinstance(val,dict):                   
                minimo = val['valores'][0]
                for valor in val['valores']:
                        
                    if  minimo > valor :
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
            return None

  
    
    

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
                    return None
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
                    return None
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
            return None

    

class exp_mayor(exp_query):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
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
                    return None
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
                    return None
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
            return None




class exp_menor(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    
    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
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
                    return None
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
                    return None
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
            return None

     


class exp_mayor_igual(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
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
                    return None
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
                    return None
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
            return None




class exp_menor_igual(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
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
                    return None
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
                    return None
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
            return None



class exp_diferente(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self,tables):
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = self.exp1.ejecutar(tables)
        val2 = self.exp2.ejecutar(tables)
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
                    return None
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
                    return None
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
            return None


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
            return None

    

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
        for i in range(1, len(condition)):
            if condition[i].tipo == 'AND':
                
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