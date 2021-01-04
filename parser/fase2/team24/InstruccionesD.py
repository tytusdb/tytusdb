@@ -1,9 +1,11 @@
import storage as func
import tablaDGA as TS
import reportError as errores
from reports import reportError as errores
import mathtrig as mt
import hashlib
from datetime import date
import Interfaz
import re

#VARIABLES GLOBALES
resultadotxt = ""
@ -22,6 +24,34 @@ def Textoresultado():
    print("\n")
    resultadotxt = ""

def extraerParametros(cadena):
    regex = r'\((.*?)\)'
    matches = re.findall(regex, cadena)

def extraerNombreFunciones(cadena2):
    regex2 = r'(=.*?\()'
    matches2 = re.findall(regex2, cadena2)

def arreglarCadena(clave, cadena):
    cadena = cadena.lower()
    aux = str(clave).lower()
    regex3 = fr'({aux.lower()}.*)'
    matches3 = re.findall(regex3, cadena)
    return matches3[0]

def migrar3D(startWhit: str):
    length = len(Interfaz.STACK_INSTRUCCIONES)
    for i in range(length):
        if startWhit.lower() in str(Interfaz.STACK_INSTRUCCIONES[i]).lower():
            Interfaz.STACK_INSTRUCCIONES[i] = arreglarCadena(startWhit, Interfaz.STACK_INSTRUCCIONES[i])
            if('=' in str(Interfaz.STACK_INSTRUCCIONES[i])):
                print('sql.execute("'+ Interfaz.STACK_INSTRUCCIONES[i] + ';"'+ ',None')
                print()
            else:
                print('sql.execute("'+ Interfaz.STACK_INSTRUCCIONES[i] + ';"'+ ',None')
            Interfaz.STACK_INSTRUCCIONES.pop(i)
            break

class instruccion:
    """INSTRUCCION"""

@ -59,12 +89,15 @@ class createdb(instruccion):
    self.owner = owner
    self.mode = mode

def traducir(self):
    migrar3D('CREATE DATABASE')

def ejecutar(self):
    global resultadotxt
    global cont
    global tabla
    global contambito
    try:
        try:
            resultado = func.createDatabase(self.iden)
            if resultado == 0:
                NuevoSimbolo = TS.Simbolo(cont,self.iden,TS.TIPO.DATABASE,contambito)
@ -74,7 +107,7 @@ class createdb(instruccion):
    resultadotxt += "Se creo la base de datos " + self.iden + "\n"
    return "Se creo la base de datos " + self.iden + "\n"
elif resultado == 2 and not self.replacedb:
e = errores.CError(0,0,"Ya existe la base de datos " + self.iden,'Semantico')
e = errores.CError(0,0,"Ya existe la base de datos " + self.iden,'Semantico')
errores.insert_error(e)
resultadotxt += "Ya existe la base de datos " + self.iden + "\n"
return "Ya existe la base de datos " + self.iden + "\n"
@ -90,7 +123,7 @@ class createdb(instruccion):
    resultadotxt += "Se reemplazo la base de datos: " + self.iden + "\n"
    return "Se reemplazo la base de datos: " + self.iden + "\n"
else:
e = errores.CError(0,0,"Error al crear base de datos: " + self.iden,'Semantico')
e = errores.CError(0,0,"Error al crear base de datos: " + self.iden,'Semantico')
errores.insert_error(e)
resultadotxt += "Error al crear base de datos: " + self.iden + "\n"
return "Error al crear base de datos: " + self.iden + "\n"
@ -102,6 +135,9 @@ class showdb(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

    def traducir(self):
        migrar3D('SHOW DATABASE')

    def ejecutar(self):
        global resultadotxt
        global cont
@ -129,6 +165,9 @@ class alterdb(instruccion):
    def __init__(self,alterdb2):
        self.alterdb2 = alterdb2

    def traducir(self):
        migrar3D('ALTER DATABASE')

    def ejecutar(self):
        global resultadotxt
        global cont
@ -154,8 +193,9 @@ class alterdb(instruccion):
    return "Se actualizo la base de datos " + self.alterdb2.iden + " a " + self.alterdb2.alterdb3.iden + "\n"
except:
"""ERROR SEMANTICO"""


class alterdb2(instruccion):

    def __init__(self,iden, alterdb3):
        self.iden = iden
        self.alterdb3 = alterdb3
@ -176,15 +216,20 @@ class alterdb31(instruccion):

#DROPDB--------------------------------------
class dropdb(instruccion):

    def __init__(self,ifexists, iden):
        self.ifexists = ifexists
        self.iden =iden

    def traducir(self):
        migrar3D('DROP DATABASE')

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        try:
            global NombreDB
        try:
            resultado = func.dropDatabase(self.iden)
            if(resultado == 2):
                e = errores.CError(0,0,"No existe la base de datos " + str(self.iden),'Semantico')
@ -204,7 +249,7 @@ class dropdb(instruccion):
    for element in eliminar:
        tabla.simbolos.pop(element.id)
    tabla.simbolos.pop(BaseDatos.id)
    if self.iden == NombreDB:
        if self.iden == str(NombreDB):
            NombreDB = ""
    resultadotxt += "Se elimino la base de datos " + self.iden + "\n"
    return "Se elimino la base de datos " + self.iden + "\n"
@ -213,9 +258,14 @@ class dropdb(instruccion):

#USEDB----------------------------------------
class usedb(instruccion):


    def __init__(self, iden):
        self.iden =iden

    def traducir(self):
        migrar3D('USE DATABASE')

    def ejecutar(self):
        global resultadotxt
        global NombreDB
@ -226,18 +276,22 @@ class usedb(instruccion):
#MANIPULACION DE TABLAS
#CREATE TABLE---------------------------------------
class createtb(instruccion):

    def __init__(self,iden, coltb, inherits):
        self.iden = iden
        self.coltb = coltb
        self.inherits = inherits

    def traducir(self):
        migrar3D('CREATE TABLE')

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        resultadotxt = ""
        try:
            try:
                resultado = func.createTable(NombreDB, self.iden,0)
                if(resultado == 2):
                    e = errores.CError(0,0,"No existe la base de datos: " + NombreDB,'Semantico')
@ -354,13 +408,16 @@ class droptb(instruccion):
    def __init__(self,iden):
        self.iden = iden

    def traducir(self):
        migrar3D('DROP TABLE')

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        resultadotxt = ""
        try:
            try:
                resultado = func.dropTable(NombreDB, self.iden)
                if(resultado == 2):
                    e = errores.CError(0,0,"No existe la base de datos " + NombreDB,'Semantico')
@ -390,6 +447,8 @@ class altertb(instruccion):
    self.iden = iden
    self.altertb2 = altertb2

def traducir(self):
    migrar3D('ALTER TABLE')
def ejecutar(self):
    global resultadotxt
    global cont
@ -449,7 +508,7 @@ class altertb(instruccion):
    """ERROR SEMANTICO"""
except:
"""ERROR"""
return resultadotxt
return resultadotxt

def OrdenarColumnas(NombreTabla):
    TablaActual = tabla.BuscarNombre(NombreTabla)
@ -457,7 +516,7 @@ def OrdenarColumnas(NombreTabla):
    for simbolo in tabla.simbolos:
        if tabla.simbolos[simbolo].ambito == TablaActual.id and tabla.simbolos[simbolo].tipo == TS.TIPO.COLUMN:
            ListaColumnas.append(tabla.simbolos[simbolo])


    contador = 0
    for columna in ListaColumnas:
        columna.numcol = contador
@ -497,6 +556,9 @@ class insert(instruccion):
    self.iden = iden
    self.valores = valores

def traducir(self):
    migrar3D('INSERT')

def ejecutar(self):
    global resultadotxt
    global cont
@ -574,7 +636,8 @@ class funcionesmath():
    class math_abs2(funcionesmath):
        def __init__(self, exp):
            self.exp = exp


        def traducir(self): '''traduccion''';
        def ejecutar(self):
            #no es diccionario
            try:
@ -589,6 +652,7 @@ class math_cbrt2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -598,11 +662,12 @@ class math_cbrt2(funcionesmath):
    e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
    errores.insert_error(e)
    return e


class math_ceil2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -617,6 +682,7 @@ class math_degrees2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -632,6 +698,7 @@ class math_div2(funcionesmath):
    self.exp1 = exp1
    self.exp2 = exp2

def traducir(self): '''traduccion''';
def ejecutar(self):
    try:
        num1 = float(self.exp1)
@ -641,11 +708,12 @@ class math_div2(funcionesmath):
    e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
    errores.insert_error(e)
    return e


class math_exp2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        try:
            num = int(self.exp)
@ -659,6 +727,7 @@ class math_factorial2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -673,6 +742,7 @@ class math_floor2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -688,6 +758,7 @@ class math_gcd2(funcionesmath):
    self.exp1 = exp1
    self.exp2 = exp2

def traducir(self): '''traduccion''';
def ejecutar(self):
    try:
        num1 = int(self.exp1)
@ -703,6 +774,7 @@ class math_lcm2(funcionesmath):
    self.exp1 = exp1
    self.exp2 = exp2

def traducir(self): '''traduccion''';
def ejecutar(self):
    try:
        num1 = int(self.exp1)
@ -717,6 +789,7 @@ class math_ln2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -732,6 +805,7 @@ class math_log2(funcionesmath):
    self.exp1 = exp1
    self.exp2 = exp2

def traducir(self): '''traduccion''';
def ejecutar(self):
    try:
        num1 = int(self.exp1)
@ -746,6 +820,7 @@ class math_log102(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        num = float(self.exp)
@ -755,6 +830,7 @@ class math_min_scale2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -769,6 +845,7 @@ class math_scale2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -783,6 +860,7 @@ class math_mod2(funcionesmath):
    self.exp1 = exp1
    self.exp2  = exp2

def traducir(self): '''traduccion''';
def ejecutar(self):
    try:
        num1 = float(self.exp1)
@ -797,6 +875,7 @@ class math_pi2(funcionesmath):
    def __init__(self):
        self.val = mt.pi()

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        try:
            return self.val
@ -809,7 +888,8 @@ class math_power2(funcionesmath):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


    def traducir(self): '''traduccion''';
    def ejecutar(self):
        try:
            num1 = int(self.exp1)
@ -824,6 +904,7 @@ class math_radians2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -838,6 +919,7 @@ class math_round2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -852,6 +934,7 @@ class math_sign2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -866,6 +949,7 @@ class math_sqrt2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -880,6 +964,7 @@ class math_trim_scale2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        try:
            num = int(self.exp)
@ -896,6 +981,7 @@ class math_widthBucket2(funcionesmath):
    self.exp3 = exp3
    self.exp4 = exp4

def traducir(self): '''traduccion''';
def ejecutar(self):
    #xd
    try:
@ -909,6 +995,7 @@ class math_trunc2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        #no es diccionario
        try:
@ -923,6 +1010,7 @@ class math_random2(funcionesmath):
    def __init__(self):
        """VACIO"""

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        return mt.random()

@ -930,6 +1018,7 @@ class math_setseed2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):
        try:
            mt.setseed(self.exp)
@ -945,118 +1034,125 @@ class funcionestrig():
    class trig_acos2(funcionestrig):
        def __init__(self, exp):
            self.exp = exp


        def traducir(self): '''traduccion''';
        def ejecutar(self):


            try:
                temp = float(self.exp)
            except ValueError:
                e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
                errores.insert_error(e)
                return e

            trim = mt.acos(float(temp))

            trim = mt.acos(float(temp))
            return trim


class trig_acosd2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp




    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.acosd(float(temp))


        return trim


class trig_asin2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp




    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.asin(float(temp))


        return trim


class trig_asind2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp




    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


            trim = mt.asind(float(temp))


            return trim


class trig_atan2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


            trim = mt.atan(float(temp))


            return trim


class trig_atand2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp




    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


            trim = mt.atand(float(temp))


            return trim


class trig_atan22(funcionestrig):
    def __init__(self, exp1, exp2 ):
        self.exp1 = exp1
        self.exp2 = exp2



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp1 = float(self.exp1)
            temp2 = float(self.exp2)
@ -1064,19 +1160,20 @@ class trig_atan22(funcionestrig):
    e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
    errores.insert_error(e)
    return e


trim = mt.atan2(temp1,temp2)


return trim


class trig_atan2d2(funcionestrig):
    def __init__(self, exp1, exp2 ):
        self.exp1 = exp1
        self.exp2 = exp2




    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp1 = float(self.exp1)
            temp2 = float(self.exp2)
@ -1084,52 +1181,53 @@ class trig_atan2d2(funcionestrig):
    e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
    errores.insert_error(e)
    return e


trim = mt.atan2d(temp1,temp2)


return trim


class trig_cos2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.cos(float(temp))


        return trim


class trig_cosd2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.cosd(float(temp))


        return trim


class trig_cot2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):

        try:
@ -1138,199 +1236,210 @@ class trig_cot2(funcionestrig):
    e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
    errores.insert_error(e)
    return e


trim = mt.cot(float(temp))


return trim

class trig_cotd2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.cotd(float(temp))


        return trim


class trig_sin2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.sin(float(temp))


        return trim


class trig_sind2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.sind(float(temp))


        return trim


class trig_tan2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp




    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.tan(float(temp))


        return trim


class trig_tand2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp





    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.tand(float(temp))


        return trim


class trig_sinh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.sinh(float(temp))


        return trim


class trig_cosh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.cosh(float(self.exp))


        return trim


class trig_tanh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.tanh(float(temp))


        return trim


class trig_asinh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.asinh(float(temp))


        return trim


class trig_acosh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp




    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e


        trim = mt.acosh(float(temp))


        return trim


class trig_atanh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp



    def traducir(self): '''traduccion''';
    def ejecutar(self):


        try:
            temp = float(self.exp)
        except ValueError:
@ -1339,7 +1448,7 @@ class trig_atanh2(funcionestrig):
    return e

trim = mt.atanh(float(temp))


return trim

#FUNCIONES GENERALES
@ -1350,29 +1459,32 @@ class fun_length2(funciongen):
    def __init__ (self,exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):

        #saco el substring y lo devuelvo
        temp =  str(self.exp )
        trim = len(temp)


        return trim


class fun_trim2(funciongen):
    def __init__ (self,exp):
        self.exp = exp
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):


        temp =  str(self.exp)
        trim =  temp.strip()


        return trim


class fun_md52(funciongen):
    def __init__ (self,exp):
        self.exp = exp

    def traducir(self): '''traduccion''';
    def ejecutar(self):

#saco el substring y lo devuelvo
@ -1382,11 +1494,12 @@ class fun_md52(funciongen):
    r = crypt.hexdigest()

    return r


class fun_sha2562(funciongen):
    def __init__ (self,exp):
        self.exp = exp


    def traducir(self): '''traduccion''';
    def ejecutar(self):

#saco el substring y lo devuelvo
@ -1394,61 +1507,64 @@ class fun_sha2562(funciongen):
    crypt = hashlib.sha256()
    crypt.update(temp.encode('utf-8'))
    r = crypt.hexdigest()


    return r


class fun_substr2(funciongen):
    def __init__ (self,exp,min,max):
        self.exp = exp
        self.min = min
        self.max = max


    def traducir(self): '''traduccion''';
    def ejecutar(self):

        #saco el substring y lo devuelvo
        temp =  str(self.exp)
        sub = temp[self.min:self.max]


        return sub


class fun_greatest2(funciongen):
    def __init__ (self,lexps):
        self.lexps = lexps


    def traducir(self): '''traduccion''';
    def ejecutar(self):

        try:

        try:
            maximo = float(self.lexps[0])


            for dato in self.lexps:
                temp = float(dato)


                if maximo < temp:
                    maximo = temp




                return maximo
        except:
            e = errores.CError(0,0,"Funcion least necesita una lista",'Semantico')
            errores.insert_error(e)
            return e


class fun_least2(funciongen):
    def __init__ (self,lexps):
        self.lexps = lexps


    def traducir(self): '''traduccion''';
    def ejecutar(self):

        try:
            try:
                maximo = float(self.lexps[0])


                for dato in self.lexps:
                    temp = float(dato)


                    if maximo > temp:
                        maximo = temp




                    return maximo
            except:
                e = errores.CError(0,0,"Funcion least necesita una lista",'Semantico')
@ -1458,11 +1574,12 @@ class fun_least2(funciongen):
    class dato2(funciongen):
        def __init__ (self,val):
            self.val = val


class fun_now2(funciongen):
    def __init__ (self,exp):
        self.exp = exp


    def traducir(self): '''traduccion''';
    def ejecutar(self):
        # dd/mm/YY
        today = date.today()
@ -1517,14 +1634,17 @@ def definir_tipo(entrada):
    return "date"
else:
return "varchar"""


#UPDATE-----------------------------------------
class update(instruccion):
    def __init__(self,iden, cond, wherecond):
        self.iden = iden
        self.cond = cond
        self.wherecond = wherecond


    def traducir(self):
        migrar3D('UPDATE')

    def ejecutar(self):
        global resultadotxt
        global cont
@ -1624,14 +1744,18 @@ class update(instruccion):
    except:
    """ERROR"""
return resultadotxt


#DELETE-------------------------------------------
class delete(instruccion):
    def __init__(self,iden, wherecond):
        self.iden = iden
        self.wherecond = wherecond

    def traducir(self):
        migrar3D('DELETE')

    def ejecutar(self):

        global resultadotxt
        global cont
        global tabla
@ -1741,4 +1865,4 @@ class delete(instruccion):
    resultadotxt += "Se eliminaron los registros de la tabla\n"
except:
"""ERROR"""
return resultadotxt
return resultadotxt