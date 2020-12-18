#
import hashlib
from datetime import date
from main import TS as ts
import storage as s
from enum import Enum
from main import default_db
import mathtrig as mt
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
            if self.table not in tables or self.table not in tables.values():
                #Error semántico
                pass
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
                indice = ts.getIndice(default_db,table,self.val)
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

    def ejecutar(self):
        return self.val


class exp_text(exp_query):
    'Devuelve el texto'

    def __init__(self, val):
        self.val = val
    def ejecutar(self):
        return self.val


class exp_num(exp_query):
    'Devuelve un número'

    def __init__(self, val):
        self.val = val
    def ejecutar(self):
        return self.val



class exp_suma(exp_query):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None
    
    #Vamos a asumir el tipo 
    # suponemos que es numérico :v

    def ejecutar(self):
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(menor[i]+mayor[i])
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
                    result.append(col+val)
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            return float(exp1) + float(exp2)


    


class exp_resta(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    def ejecutar(self):
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(menor[i]-mayor[i])
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
                    result.append(col-val)
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            return float(exp1) - float(exp2)


class exp_multiplicacion(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    def ejecutar(self):
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(menor[i]*mayor[i])
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
                    result.append(col*val)
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            return float(exp1) * float(exp2)


class exp_division(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.type = None

    def ejecutar(self):
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(menor[i]/mayor[i])
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
                    result.append(col/val)
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            return float(exp1) / float(exp2)


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
    
    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(abs(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return abs(exp)
        
        


class math_cbrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.cbrt(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.cbrt(exp)


class math_ceil(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.ceil(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.ceil(exp)


class math_degrees(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.degrees(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.degrees(exp)


class math_div(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(mt.div(menor[i],mayor[i]))
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
                    result.append(mt.div(col,val))
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            return mt.div(float(exp1) , float(exp2))
        

class math_exp(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.exp(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.exp(exp)

class math_factorial(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.factorial(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.factorial(exp)


class math_floor(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.floor(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.floor(exp)


class math_gcd(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(mt.gcd(menor[i],mayor[i]))
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
                    result.append(mt.gcd(col,val))
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            return mt.gcd(float(exp1) , float(exp2))

class math_lcm(column_mathtrig):
    def __init__(self,exp1,exp2,alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias 

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(mt.lcm(menor[i],mayor[i]))
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
                    result.append(mt.lcm(col,val))
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            return mt.lcm(float(exp1) , float(exp2))



class math_ln(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.ln(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.ln(exp)


class math_log(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(mt.log(menor[i],mayor[i]))
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
            return mt.log(float(exp1) , float(exp2))


class math_log10(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.log10(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.log10(exp)

class math_min_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.min_scale(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.min_scale(exp)

class math_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.scale(str(reg)))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.scale(str(exp))

class math_mod(column_mathtrig):
    def __init__(self, exp1,exp2, alias):
        self.exp1 = exp1
        self.exp2  = exp2
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(mt.mod(menor[i],mayor[i]))
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
                    result.append(mt.mod(col,val))
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            return mt.mod(float(exp1) , float(exp2))


class math_pi(column_mathtrig):
    def __init__(self, alias):
        self.val = mt.pi()
        self.alias = alias

    def ejecutar(self):
        return self.val


class math_power(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias
    
    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp1 = self.exp1.ejecutar()
        exp2 = self.exp2.ejecutar()
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
                    result.append(mt.power(menor[i],mayor[i]))
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
                    result.append(mt.power(col,val))
                newdict = {
                    'valores':result,
                    'columna': dic['columna']
                }
                return newdict

        #si ninguna es diccionario
        else:
            return mt.power(float(exp1) , float(exp2))


class math_radians(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.radians(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.radians(exp)


class math_round(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(round(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return round(exp)


class math_sign(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.sign(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.sign(exp)


class math_sqrt(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.sqrt(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.sqrt(exp)

class math_trim_scale(column_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.trim_scale(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.trim_scale(exp)

class math_widthBucket(column_mathtrig):
    def __init__(self, exp1, exp2, exp3, exp4, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4
        self.alias = alias

    def ejecutar(self):
        #xd
        return mt.width_bucket(9,8,7,6)


class math_trunc(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar(self):
        #Verificamos si viene un diccionario o un valor
        exp = self.exp.ejecutar()
        if isinstance(exp,dict):
            #es diccionario
            registros = exp['valores']
            result = []
            for reg in registros:
                result.append(mt.trunc(reg))
            exp['valores']  = result
            return exp

        else:
            #no es diccionario
            return mt.trunc(exp)


class math_random(column_mathtrig):
    def __init__(self, alias):
        self.alias = alias

    def ejecutar(self):
        return mt.random()

class math_setseed(column_mathtrig):
    def __init__(self,exp, alias):
        self.exp = exp
        self.alias = alias 

    def ejecutar(self):
        mt.setseed(self.exp.ejecutar())


class trig_acos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.acos(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.acos(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.acos(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict




class trig_acosd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.acosd(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.acosd(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.acosd(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict


class trig_asin(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.asin(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.asin(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.asin(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict





class trig_asind(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.asind(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.asind(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.asind(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict





class trig_atan(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.atan(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.atan(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.atan(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict



class trig_atand(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias


    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.atand(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.atand(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.atand(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict




class trig_atan2(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.atan2(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.atan2(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.atan2(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict


    

    

class trig_atan2d(column_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp = exp1
        self.exp2 = exp2
        self.alias = alias
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.atan2d(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.atan2d(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.atan2d(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict




class trig_cos(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.cos(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.cos(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.cos(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict





class trig_cosd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.cosd(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.cosd(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.cosd(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict





class trig_cot(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.cot(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.cot(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.cot(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict


class trig_cotd(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.cotd(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.cotd(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.cotd(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict



class trig_sin(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.sin(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.sin(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.sin(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict

class trig_sind(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.sind(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.sind(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.sind(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 
class trig_tan(column_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.tan(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.tan(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.tan(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 

class trig_tand(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias
    

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.tand(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.tand(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.tand(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 
 
class trig_sinh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.sinh(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.sinh(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.sinh(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 
    


class trig_cosh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.cosh(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.cosh(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.cosh(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 


class trig_tanh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.tanh(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.tanh(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.tanh(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 

class trig_asinh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias
    

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.asinh(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.asinh(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.asinh(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 


class trig_acosh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.acosh(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.acosh(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.acosh(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 

class trig_atanh(column_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:

                    if not isinstance(st, int): return None

                    trim =  mt.atanh(st)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                if not (isinstance(val['valores'], int)): return None
                trim =  mt.atanh(val['valores'] )
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            if not (isinstance(val['valores'], int)): return None
            trim = mt.atanh(val['valores'] )
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 

class column_function(select_column):
    'clase Abstracta'

class fun_sum(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                total = 0
                for st in val['valores']:
                    total = total + st
                
                
                val['valores'] = total
                return val
            else:
               
                return None
                
        #Es solo un valor en especifico
        else:
            return None

class fun_avg(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                total = 0
                for st in val['valores']:
                    total = total + st
                
                prom = total / len(val['valores'])
                val['valores'] = prom
                return val
            else:
               
                return None
                
        #Es solo un valor en especifico
        else:
            return None
 
class fun_max(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
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
 

class fun_min(column_function):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
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

    def ejecutar(tablas):
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor


            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                
                temp = len(val['valores'])                
                val['valores'] = temp
                return val
            else:
                if val['valores'] == 'All':
                    if len(tablas) != 1:
                        return None
                    else:
                        t = ts.obtenerTabla(val)
                        r = s.extractTable(t.db,t.table)
                        return len(r)
                else:
                    return None
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val['valores'] )
            trim = len(temp)
            newdict = {
                        'valores' : 15,
                        'columna': []
                    }
            return newdict
 

class fun_length(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:
                    temp =  str(st )
                    trim =  len(temp)
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                temp =  str(val['valores'] )
                trim =  len(temp)
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val['valores'] )
            trim = len(temp)
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 


class fun_trim(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias    

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:
                    temp =  str(st )
                    trim =  temp.strip()
                    subs.append(trim)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                temp =  str(val['valores'] )
                trim =  temp.strip()
                newdict = {
                        'valores' : trim,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val['valores'] )
            trim =  temp.strip()
            newdict = {
                        'valores' : trim,
                        'columna': []
                    }
            return newdict
 


   

class fun_md5(column_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
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
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
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
            else:
                #saco el substring y lo devuelvo
                temp =  str(val['valores'] )
                crypt = hashlib.sha256()
                crypt.update(temp.encode('utf-8'))
                r = crypt.hexdigest()
                newdict = {
                        'valores' : r,
                        'columna': []
                    }
                return newdict
                
                


        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val['valores'] )
            crypt = hashlib.sha256()
            crypt.update(temp.encode('utf-8'))
            r = crypt.hexdigest()
            newdict = {
                        'valores' : r,
                        'columna': []
                    }
            return newdict
 



class fun_convert(column_function):
    def __init__ (self,exp,tipo,alias):
        self.exp = exp
        self.type = tipo
        self.alias = alias
    
    def ejecutar(self):
        return self.exp

class fun_substr(column_function):
    def __init__ (self,exp,min,max,alias):
        self.exp = exp
        self.min = min
        self.max = max
        self.alias = alias
    
    def ejecutar():
        val = exp.ejecutar()
        if isinstance(val,dict):        
            #valores es un arreglo o solo un valor
            #Valores es un arreglo lo recorro y saco substring 
            if isinstance(val['valores'],list):
                #recorro valores y saco el substring 
                subs = []
                for st in val['valores']:
                    temp =  str(st )
                    sub = temp[self.min:self.max]
                    subs.append(sub)
                
                val['valores'] = subs
                return val
            else:
                #saco el substring y lo devuelvo
                temp =  str(val['valores'] )
                sub = temp[self.min:self.max]
                newdict = {
                        'valores' : sub,
                        'columna': []
                    }
                return newdict
                
        #Es solo un valor en especifico
        else:
            #saco el substring y lo devuelvo
            temp =  str(val['valores'] )
            sub = temp[self.min:self.max]
            newdict = {
                        'valores' : sub,
                        'columna': []
                    }
            return newdict
            
 
class fun_greatest(column_function):
    def __init__ (self,lexps,alias):
        self.lexps = lexps
        self.alias = alias
    
    def ejecutar(self):
        if len(lexps) == 0 : return None
        try:
            val = lexps[0].ejecutar()
            if val['valores'] == None or len(val['valores']) == 0: return None
            #Viene solo un id, es columna
            if len(lexps) == 1 and isinstance(val,dict):                    
                maximo = val['valores'][0]
                for valor in val['valores']:
                        
                    if  maximo < valor :
                        maximo = valor
                #retornar min
                val['valores'] = maximo
                return val
            #Es una lista de valores puede venir como dict o no
            else:
                
                if isinstance(val,dict):
                    maximo = val['valores']
                else:
                    maximo = val
                
                for dato in lexps:
                    t = dato.ejecutar()
                    #obtengo el valor de diferente manera
                    if isinstance(t,dict):
                        temp = t['valores']
                    else:
                        temp = t
                    
                    if maximo < temp:
                        maximo = temp
                
                newdict = {
                       'valores' : maximo,
                        'columna': []
                    }   
                return newdict
        except:
            #Error
            return None
 
class fun_least(column_function):
    def __init__ (self,lexps,alias):
        self.lexps = lexps
        self.alias = alias
    
    def ejecutar(self):
        if len(lexps) == 0 : return None
        try:
            val = lexps[0].ejecutar()
            if val['valores'] == None or len(val['valores']) == 0: return None
            #Viene solo un id, es columna
            if len(lexps) == 1 and isinstance(val,dict):                   
                minimo = val['valores'][0]
                for valor in val['valores']:
                        
                    if  minimo > valor :
                        minimo = valor
                #retornar min
                val['valores'] = minimo
                return val
            #Es una lista de valores puede venir como dict o no
            else:
                
                if isinstance(val,dict):
                    minimo = val['valores']
                else:
                    minimo = val
                
                for dato in lexps:
                    t = dato.ejecutar()
                    #obtengo el valor de diferente manera
                    if isinstance(t,dict):
                        temp = t['valores']
                    else:
                        temp = t
                    
                    if minimo > temp:
                        minimo = temp
                
                newdict = {
                       'valores' : minimo,
                        'columna': []
                    }   
                return newdict
        except:
            #Error
            return None

  
    
    

class dato(column_function):
    def __init__ (self,val,alias):
        self.val = val
        self.alias = alias
    

class fun_now(column_function):
    def __init__ (self):
        pass
        
    def ejecutar(self):
        # dd/mm/YY
        today = date.today()
        d1 = today.strftime("%Y-%m-%d %H:%M:%S")
        return d1


class condition(exp_query):
    def __init__(self,exp ,union):
        self.exp = exp
        self.union = union

class exp_igual(exp_query):

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    
    def ejecutar():
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = exp1.ejecutar()
        val2 = exp2.ejecutar()
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val == val2.val:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and not isinstance(val2,dict) :
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

    def ejecutar():
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = exp1.ejecutar()
        val2 = exp2.ejecutar()
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val > val2.val:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and not isinstance(val2,dict) :
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
    
    def ejecutar():
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = exp1.ejecutar()
        val2 = exp2.ejecutar()
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val < val2.val:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and not isinstance(val2,dict) :
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

    def ejecutar():
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = exp1.ejecutar()
        val2 = exp2.ejecutar()
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val >= val2.val:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and not isinstance(val2,dict) :
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

    def ejecutar():
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = exp1.ejecutar()
        val2 = exp2.ejecutar()
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val <= val2.val:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and not isinstance(val2,dict) :
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

    def ejecutar():
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = exp1.ejecutar()
        val2 = exp2.ejecutar()
        #id op val
        if isinstance(val1,dict) and not isinstance(val2,dict) :
            posiciones = []
            contador = 0
            for val in val1['valores']:
                if val != val2.val:
                    posiciones.append(contador)
                contador = contador +1   
            val1['posiciones'] = posiciones
            return val1
        #dic op dic
        elif isinstance(val1,dict) and not isinstance(val2,dict) :
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

    def ejecutar():
        #Vamos a comparar un id con un valor
        # columna > 5
        
        val1 = exp1.ejecutar()
        val2 = exp2.ejecutar()
        val3 = exp2.ejecutar()
        #id op val
        if isinstance(val1,dict):
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
    for table, alias in d:
        if alias == value:
            return table

    return None