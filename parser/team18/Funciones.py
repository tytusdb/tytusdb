#import 
import math
import random
import base64
import hashlib
import datetime
import AST
from expresiones import *


#Arithmetic Functions

def func_cbrt(exp):
    return exp**(1/3)

def func_sign(exp):
    if(exp >= 0):
        return 1
    else:
        return -1

def func_random():
    return random.uniform(0, 1)

def func_round(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def func_width_bucket(valor,inicio,final,cubos):
    if inicio!=final:
        if inicio==valor:
            return 0
        if final==valor:
            return cubos+1

        intervalo = (final - inicio)/cubos
        result = ((valor-inicio)/intervalo)+1
        if math.floor(result)>cubos :
            return cubos+1
        elif result<0:
            return 0
        else:
            return math.floor(int(result))

#print(func_width_bucket(3, 1, 12, 3))
#print(func_width_bucket(5, 1, 12, 3))
#print(func_width_bucket(9, 1, 12, 3))

#Trigonometric Functions

def func_cot(exp):
    if exp != 0 :
        return (1 / math.tan(exp)) 
    else: 
        return "No definido"

def func_atan2(exp1,exp2):
    print("atand")
    op = exp1/exp2
    return math.atan2(op)

def func_atan2d(exp1,exp2):
    print("atan2d")
    op = exp1/exp2
    return math.atan2(math.degrees(op))

#Binary Strings Functions

def func_length(exp):
    return len(exp)

#Funciones para trim
def func_trim_leading(exp, c): #Caracteres iniciales
    return exp.lstrip(c)

def func_trim_trailing(exp, c): #Caracteres finales
    return exp.rstrip(c)

def func_trim_both(exp, c): #Iniciales y finales
    return exp.strip(c)

#substring y substr
def func_substring(exp,inicio,final):
    return exp[inicio:final]

def func_md5(exp):
    exp = hashlib.md5(exp.encode())
    exp = exp.hexdigest()
    return exp

def func_sha256(exp):
    exp = hashlib.sha256(exp.encode())
    exp = exp.hexdigest()
    return exp 


def func_get_byte(exp, num):
    print(exp)
    byte = bytes(exp, "utf-8")
    if len(byte) > num:
        return byte[num]


#print(func_get_byte('Th\000omas', 4))

def func_set_byte(exp, num, num2):
    byte = bytes(exp, "utf-8")
    array = list()
    i = 0
    for valor in byte:
        array.insert(i + 1, int(str(valor)))
        i += 1
    if (len(array) > num):
        array[num] = num2
    byte = bytes(array)
    return byte


def func_encode(exp, formato):
    if formato == "escape":
        return exp
    elif formato == "base64":
        exp = bytes(exp, "utf-8")
        exp64 = base64.b64encode(exp)
        return exp64
    elif formato == "hex":
        return exp.encode("utf-8").hex()

def func_decode(exp, formato):
    if formato == "escape":
        return exp
    elif formato == "base64":
        result = exp.decode('base64')
        return result
    elif formato == "hex":
        result = exp.decode('utf-8').hex()
        return result
        

#print(encode_string('123\000456', 'escape'))

#Falta implementar todos los convert

def func_convert(exp):
    fecha = datetime.strptime(exp, "%Y-%m-%d %H:%M:%S")
    return fecha




def Between(exp1, exp2,ts):
    if isinstance(exp2, Operacion_Logica_Binaria):
        op1 = AST.resolver_operacion(exp2.op1,ts)
        op2 = AST.resolver_operacion(exp2.op2,ts)
        if (isinstance(op1, str) and isinstance(op2, str)) or (isinstance(op1, (int,float)) and isinstance(op2, (int,float))):
            if exp2.operador == OPERACION_LOGICA.AND:
                if (exp1 >= op1) and (exp1 <= op2):
                    return True
    return False

def In(exp1, exp2, ts):
    lexp = []
    for exp in  exp2:
        op = AST.resolver_operacion(exp,ts)
        lexp.append(op)
    if exp1 in lexp:
        return True
    else:
        return False

def Like(exp1,exp2,ts):
    if isinstance(exp2, (str,Operando_Cadena)):
        op = exp2
        if isinstance(op, Operando_Cadena):
            op = AST.resolver_operacion(op,ts)
        op = op.replace('%','')
        if op in exp1:
            return True
        else:
            return False
    else:
        return False

def Ilike(exp1,exp2,ts):
    if isinstance(exp2, (str,Operando_Cadena)):
        exp1 = exp1.lower() 
        op = exp2
        if isinstance(op, Operando_Cadena):
            op = AST.resolver_operacion(op,ts)
        op = op.replace('%','')
        op = op.lower()
        if op in exp1:
            return True
        else:
            return False
    else:
        return False
        
def Similar(exp1,exp2,ts):
    if isinstance(exp2, (str,Operando_Cadena)):
        op = exp2
        if isinstance(op, Operando_Cadena):
            op = AST.resolver_operacion(op,ts)
        op = op.replace('%','')
        if op == exp1:
            return True
        else:
            return False
    else:
        return False

def Now():
    return datetime.datetime.now()

def Date():
    return datetime.datetime.now().date()

def Time():
    return datetime.datetime.now().time()

def Extract(medida, date_time,ts): # YYYY-MM-DD HH:MM:SS
    datos = AST.resolver_operacion(date_time,ts)
    if len(datos) == 10:
        if medida.lower() == "year": return datos[0:4]
        elif medida.lower() == "month": return datos[5:7]
        elif medida.lower() == "day": return datos[8:10]
    else:
        if medida.lower() == "year": return datos[0:4]
        elif medida.lower() == "month": return datos[5:7]
        elif medida.lower() == "day": return datos[8:10]
        elif medida.lower() == "hour": return datos[11:13]
        elif medida.lower() == "minute": return datos[14:16]
        elif medida.lower() == "second": return datos[17:19]
    return ' '

def Date_Part(medida, date_time,ts): # W years X months Y days Z hours A minutes B seconds
    datos = AST.resolver_operacion(date_time,ts)
    datos = datos.lower()
    datos_med = AST.resolver_operacion(medida,ts)
    datos_med = datos_med.lower()
    if datos is not None:
        splited = datos.split()
        if datos_med in splited:
            index_medida = splited.index(datos_med)
            if index_medida > 0:
                return splited[index_medida-1]
    return ' '

def Greatest(exp,ts):
    lexp = []
    for exp1 in  exp:
        op = AST.resolver_operacion(exp1,ts)
        lexp.append(op)
    return max(lexp)

def Least(exp,ts):
    lexp = []
    for exp1 in  exp:
        op = AST.resolver_operacion(exp1,ts)
        lexp.append(op)
    return min(lexp)

