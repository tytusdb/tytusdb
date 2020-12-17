
from Expresion.Expresion import Expresion
from Entorno import Entorno
import math
import random as rn
import hashlib
import base64
from reportes import *
class FuncionesNativas(Expresion) :
    '''
        Esta clase representa la Expresión Binaria.
        Esta clase recibe los operandos y el operador
    '''
    def __init__(self, identificador, expresiones) :
        Expresion.__init__(self)
        self.identificador = identificador
        self.expresiones = expresiones
        
    def getval(self,entorno):
        sizeparametro = len(self.expresiones)
        funcion = self.identificador.lower()
        try: 
            if(funcion=="abs" or funcion=="cbrt" or funcion=="ceil" or funcion=="ceiling" or 
            funcion=="degrees" or funcion=="exp" or funcion=="factorial" or funcion=="floor" or
            funcion=="ln" or funcion=="log" or funcion=="radians" or funcion=="sing" or 
            funcion=="trunc" or funcion=="acos" or funcion=="acosd" or funcion=="asin" or 
            funcion=="asind" or funcion=="atan" or funcion=="atand" or funcion=="cos" or
            funcion=="cosd" or funcion=="cot" or funcion=="cotd" or funcion=="sin" or 
            funcion=="sind" or funcion=="tan" or funcion=="tand" or funcion=="sinh" or
            funcion=="cosh" or funcion=="tanh" or funcion=="asinh" or funcion=="acosh" or 
            funcion=="atanh"
            ):
                valexpresion= self.expresiones[0].getval(entorno)
                return self.FunctionWithOneParameter(funcion,sizeparametro,valexpresion)
            elif(funcion=="div" or funcion=="gcd" or funcion=="mod" or funcion=="power" or 
                funcion=="round" or funcion=="atan2" or funcion=="atan2d"
                ):
                val1expresion = self.expresiones[0].getval(entorno)
                val2expresion = self.expresiones[1].getval(entorno)
                return self.FunctionWithTwoParameter(funcion,sizeparametro,val1expresion,val2expresion)
            elif(funcion=="width_bucket"):
                val1expresion = self.expresiones[0].getval(entorno)
                val2expresion = self.expresiones[1].getval(entorno)
                val3expresion = self.expresiones[2].getval(entorno)
                val4expresion = self.expresiones[3].getval(entorno)
                return self.FunctionWithBucket(funcion,sizeparametro,val1expresion,val2expresion,val3expresion,val4expresion)
        except:
             return "Error: La función: "+funcion+" solo recibe valores númericos"
     
        if(funcion=="length" or funcion=="md5" or funcion=="sha256" or funcion=="convert"):
            valexpresion= self.expresiones[0].getval(entorno)
            return self.FunctionWithOneParameter(funcion,sizeparametro,valexpresion)
            
        elif(funcion=="get_byte" or funcion=="set_byte" or funcion=="encode" or funcion=="decode" or funcion=="trim" ):
            val1expresion = self.expresiones[0].getval(entorno)
            val2expresion = self.expresiones[1].getval(entorno)
            return self.FunctionWithTwoParameter(funcion,sizeparametro,val1expresion,val2expresion)

        elif(funcion=="substr" or funcion=="substring" ):
            val1expresion = self.expresiones[0].getval(entorno)
            val2expresion = self.expresiones[1].getval(entorno)
            val3expresion = self.expresiones[2].getval(entorno)
            return self.FunctionWithTreeParameter(funcion,sizeparametro,val1expresion,val2expresion,val3expresion)
        else:
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"no existe",0, 0))
            return "Error: La función: "+funcion+" no existe"
        
    def FunctionWithOneParameter(self,funcion,parametros,exp):
        if(parametros==1):
            if(funcion=="abs"): 
                if(exp<0): 
                    return exp*-1
                else:
                    return exp
            elif(funcion=="cbrt"): 
                return math.pow(exp,3)
            elif (funcion=="ceil"): 
                return math.ceil(exp)
            elif (funcion=="ceiling"): 
                return math.ceil(exp)
            elif (funcion=="degrees"): 
                return math.degrees(exp)
            elif (funcion=="exp"): 
                return math.exp(exp)
            elif (funcion=="factorial"): 
                return math.factorial(exp)
            elif (funcion=="floor"): 
                return math.floor(exp)
            elif (funcion=="ln"): 
                return math.log(exp)
            elif (funcion=="log"): 
                return math.log10(exp)
            elif (funcion=="radians"): 
                return math.radians(exp)
            elif (funcion=="sing"):
                if(exp>0):
                    return 1
                else:
                    return -1
            elif (funcion=="sqrt"): 
                return math.sqrt(exp)
            elif (funcion=="trunc"): 
                return math.trunc(exp)
            elif (funcion=="acos"): 
                return math.acos(exp)
            elif (funcion=="acosd"): 
                return math.degrees(math.acos(exp))
            elif (funcion=="asin"): 
                return math.asin(exp)
            elif (funcion=="asind"): 
                return math.degrees(math.asin(exp))
            elif (funcion=="atan"): 
                return math.atan(exp)
            elif (funcion=="atand"): 
                return math.degrees(math.atan(exp))
            elif (funcion=="cos"): 
                return math.cos(exp)
            elif (funcion=="cosd"): 
                return math.degrees(math.cos(exp))
            elif (funcion=="cot"): 
                return (1/math.tan(exp))
            elif (funcion=="cotd"): 
                return math.degrees(1/math.tan(exp))
            elif (funcion=="sin"): 
                return math.sin(exp)
            elif (funcion=="sind"): 
                return math.degrees(math.sin(exp))
            elif (funcion=="sin"): 
                return math.sin(exp)
            elif (funcion=="sind"): 
                return math.degrees(math.sin(exp))
            elif (funcion=="tan"): 
                return math.tan(exp)
            elif (funcion=="tand"): 
                return math.degrees(math.tan(exp))
            elif (funcion=="sinh"): 
                return math.sinh(exp)
            elif (funcion=="cosh"): 
                return math.cosh(exp)
            elif (funcion=="tanh"): 
                return math.tanh(exp)
            elif (funcion=="asinh"): 
                return math.asinh(exp)
            elif (funcion=="acosh"): 
                return math.acosh(exp)
            elif (funcion=="atanh"): 
                return math.atanh(exp)
            elif (funcion=="length"):
                 leng=len(exp)
                 return leng
            elif (funcion=="md5"):
                m=exp
                result = hashlib.md5(m.encode()) 
                return result.hexdigest()
            elif (funcion=="sha256"):
                m=exp
                result= hashlib.sha256(m.encode()).hexdigest()
                return result
            elif (funcion=="convert"):
                print("convert")
                 
            
                
        else:
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"solo recibe 2 parametros",0, 0))
            return "Error: La funcion: "+funcion+" recibe un parametro"
    
    def FunctionWithTwoParameter(self,funcion,parametros,exp1,exp2):
        if(parametros==2):
            if (funcion=="div"):
                return exp1/exp2
            elif (funcion=="gcd"):
                return math.gcd(exp1,exp2)        
            elif (funcion=="mod"):
                return exp1%exp2
            elif (funcion=="power"):
                return math.pow(exp1,exp2)
            elif (funcion=="round"):
                return round(exp1,exp2)
            elif (funcion=="atan2"):
                return math.atan(exp1/exp2)
            elif (funcion=="atan2d"):
                return math.degrees(math.atan(exp1/exp2))
            elif (funcion=="encode"):
                if(exp2.lower()=="base64"):
                    cascci=exp1.encode('ascii')
                    codificado=base64.b64encode(cascci)
                    return codificado.decode('utf-8')
                elif (exp2.lower()=="hex"): 
                    cascci=exp1.encode('utf-8')
                    codificado=base64.b16encode(cascci)
                    return codificado.decode('utf-8')
                elif (exp2.lower()=="escape"):
                    codificado=exp1.encode('unicode_escape').decode('utf-8')
                    return codificado
            elif (funcion=="decode"):
                if(exp2.lower()=="base64"):
                    codificado=base64.b64decode(exp1)
                    return codificado.decode('utf-8')
                elif (exp2.lower()=="hex"): 
                    codificado=base64.b16decode(exp1)
                    return codificado.decode('utf-8')
                elif (exp2.lower()=="escape"):
                    codificado=exp1.encode('utf-8').decode('unicode_escape')
                    return codificado
        else:
            print("Error semantico en '%s'" % t.value)
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"solo recibe 2 parametros",0, 0))
            return "Error: La funcion: "+funcion+" recibe 2 parametro"
    
    def FunctionWithTreeParameter(self,funcion,parametros,exp1,exp2,exp3):
        if(parametros==3):
            if (funcion=="substring"):
                inicio=exp2-1
                fin=inicio + exp3
                sub=exp1[inicio:fin]
                return sub
            elif (funcion=="substr"):
                inicio=exp2-1
                fin=inicio + exp3
                sub=exp1[inicio:fin]
                return sub       
        else:
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"solo recibe 3 parametros",0, 0))
            return "Error: La funcion: "+funcion+" recibe 3 parametro"
    
    def FunctionWithBucket(self,funcion,parametros,exp1,exp2,exp3,exp4):
        if(parametros==4):
            if(exp1<exp2 or exp1>exp3):
                reporteerrores.append(Lerrores("Error Semantico","Valor"+str(exp1)+"no se encuentra en el rango",0, 0))
                return "Error: El valor: "+str(exp1)+" no esta en el rango de: ("+str(exp2)+","+str(exp3)+")"
            else:
                contador = 1
                for x in range(exp2,exp3):
                    contador = contador+1
                
                columnas = int(contador/exp4)
                inicio = int(exp2)
                final = int(exp2)+(columnas) 
                posbucket = 0       
                for fila in range(0,exp4):
                    for valores in range(inicio,final):
                        if(exp1==valores):
                            posbucket = fila+1
                            return "El valor de: "+str(exp1)+" esta en el bucket: "+str(posbucket)
                    inicio=final
                    final=final+columnas    
        else:
            return "Error: La funcion: "+funcion+" recibe 4 parametro"
            reporteerrores.append(Lerrores("Error Semantico","La funcion"+funcion+"solo recibe 2 parametros",0, 0))
            
