import tabla_simbolos as TS 
import Errores as E
import math

class expresion_aritmetica():

    def __init__(self,exp1,exp2,op):
        self.exp1 = exp1
        self.exp2 = exp2
        self.op = op

    
    def get_valor(self):
        #ejecutar las expresiones por si tienen otras operaciones
        if expresion2 is None:
            expresion1= self.exp1.get_valor() #unario
        else:
            expresion1= self.exp1.get_valor()
            expresion2= self.exp2.get_valor()

       #operaciones 
        if self.op == '+':
            #comprobar tipos para operar
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 + expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 + exp2_conv
                    except:
                        msj_error = 'No se puede sumar un tipo entero con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 + expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede sumar un tipo entero con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion1 #si llego aqui probablemente expresion1 lleve un tipo error
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 + expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = float(expresion2)
                        return expresion1 + exp2_conv
                    except:
                        msj_error = 'No se puede sumar un tipo decimal con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 + expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede sumar un tipo decimal con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #si llego aqui probablemente expresion2 lleve un tipo error
            elif(isinstance(expresion1,bool)):
                msj_error = 'No se puede sumar un tipo booleano'
                error = E.Errores('ERROR', msj_error)
                return error                
            elif(isinstance(expresion1,str)):            
                if(isinstance(expresion2,str)):
                    msj_error = 'No se puede sumar un tipo cadena'
                    error = E.Errores('ERROR', msj_error)
                    return error  
                elif(isinstance(expresion2,int)):
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv + expresion2
                    except:
                        msj_error = 'No se puede sumar un tipo cadena con entero'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    try:
                        exp1_conv = float(expresion1)
                        return exp1_conv + expresion2
                    except:
                        msj_error = 'No se puede sumar un tipo cadena con decimal'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede sumar un tipo booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error  
                return expresion2  #error
        elif self.op == '-':
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 - expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 - exp2_conv
                    except:
                        msj_error = 'No se puede restar un tipo entero con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 - expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede restar un tipo entero con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error      
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 - expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = float(expresion2)
                        return expresion1 - exp2_conv
                    except:
                        msj_error = 'No se puede restar un tipo decimal con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 - expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede restar un tipo decimal con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 # error
            elif(isinstance(expresion1,bool)):
                msj_error = 'No se puede restar un tipo booleano'
                error = E.Errores('ERROR', msj_error)
                return error                
            elif(isinstance(expresion1,str)):            
                msj_error = 'No se puede restar un tipo cadena'
                error = E.Errores('ERROR', msj_error)
                return error  
            return expresion1
        elif self.op == '*':
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 * expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 * exp2_conv
                    except:
                        msj_error = 'No se puede multiplicar un tipo entero con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 * expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede multiplicar un tipo entero con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error      
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 * expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = float(expresion2)
                        return expresion1 * exp2_conv
                    except:
                        msj_error = 'No se puede multiplicar un tipo decimal con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 * expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede multiplicar un tipo decimal con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,bool)):
                msj_error = 'No se puede multiplicar un tipo booleano'
                error = E.Errores('ERROR', msj_error)
                return error                
            elif(isinstance(expresion1,str)):            
                msj_error = 'No se puede multiplicar un tipo cadena'
                error = E.Errores('ERROR', msj_error)
                return error  
            return expresion1 #error
        elif self.op == '/':
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 / expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 / exp2_conv
                    except:
                        msj_error = 'No se puede dividir un tipo entero con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 / expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede dividir un tipo entero con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error      
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 / expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = float(expresion2)
                        return expresion1 / exp2_conv
                    except:
                        msj_error = 'No se puede dividir un tipo decimal con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 / expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede dividir un tipo decimal con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,bool)):
                msj_error = 'No se puede dividir un tipo booleano'
                error = E.Errores('ERROR', msj_error)
                return error                
            elif(isinstance(expresion1,str)):            
                msj_error = 'No se puede dividir un tipo cadena'
                error = E.Errores('ERROR', msj_error)
                return error  
            return expresion1 #error
        elif self.op == '\^':
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return math.pow(expresion1,expresion2)
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return math.pow(expresion1,exp2_conv)
                    except:
                        msj_error = 'No se puede Elevar un tipo entero con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return math.pow(expresion1,expresion2)
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede Elevar un tipo entero con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error      
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return math.pow(expresion1,expresion2)
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = float(expresion2)
                        return math.pow(expresion1,exp2_conv)
                    except:
                        msj_error = 'No se puede elevar un tipo decimal con cadena'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return math.pow(expresion1,expresion2)
                elif(isinstance(expresion2,bool)):
                    msj_error = 'No se puede elevar un tipo decimal con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,bool)):
                msj_error = 'No se puede elevar un tipo booleano'
                error = E.Errores('ERROR', msj_error)
                return error                
            elif(isinstance(expresion1,str)):            
                msj_error = 'No se puede elevar un tipo cadena'
                error = E.Errores('ERROR', msj_error)
                return error  
            return expresion1 #error
        elif self.op == '--': #unario
            if(isinstance(expresion1,int)):
                return -expresion1 
            elif(isinstance(expresion1,float)):
                return -expresion1 
            else:
                msj_error = 'El operador unario no acepta valores no numericos'
                error = E.Errores('ERROR', msj_error)
                return error  
        return -1111


class expresion_relacional():
    
    def __init__(self,exp1,exp2,op):
        self.exp1 = exp1
        self.exp2 = exp2
        self.op = op

    
    def get_valor(self):
        #ejecutar las expresiones por si tienen otras operaciones
        expresion1= self.exp1.get_valor()
        expresion2= self.exp2.get_valor()

       #operaciones 
        if self.op == '<':
            #comprobar tipos para operar
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 < expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 < exp2_conv
                    except:
                        msj_error = 'El operador < no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 < expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador < no soporta tipos enteros con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 < expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 < exp2_conv
                    except:
                        msj_error = 'El operador < no soporta tipos decimales con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 < expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador < no soporta tipos decimales con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,str)):
                if(isinstance(expresion2,int)):                    
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv < expresion2
                    except:
                        msj_error = 'El operador < no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,str)):
                    msj_error = 'El operador < no soporta tipos cadenas con cadenas'
                    error = E.Errores('ERROR', msj_error)
                    return error
                elif(isinstance(expresion2,float)):
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv < expresion2
                    except:
                        msj_error = 'El operador < no soporta tipos cadenas con decimales'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador < no soporta tipos cadena con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,bool)):
                msj_error = 'El operador < no soporta tipos booleano'
                error = E.Errores('ERROR', msj_error)
                return error   
        elif self.op == '>':
            #comprobar tipos para operar
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 > expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 > exp2_conv
                    except:
                        msj_error = 'El operador > no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 > expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador > no soporta tipos enteros con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 > expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 > exp2_conv
                    except:
                        msj_error = 'El operador > no soporta tipos decimales con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 > expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador > no soporta tipos decimales con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,str)):
                if(isinstance(expresion2,int)):                    
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv > expresion2
                    except:
                        msj_error = 'El operador > no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,str)):
                    msj_error = 'El operador > no soporta tipos cadenas con cadenas'
                    error = E.Errores('ERROR', msj_error)
                    return error
                elif(isinstance(expresion2,float)):
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv > expresion2
                    except:
                        msj_error = 'El operador > no soporta tipos cadenas con decimales'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador > no soporta tipos cadena con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,bool)):
                msj_error = 'El operador > no soporta tipos booleano'
                error = E.Errores('ERROR', msj_error)
                return error
        elif self.op == '<=':
            #comprobar tipos para operar
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 <= expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 <= exp2_conv
                    except:
                        msj_error = 'El operador <= no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 <= expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador <= no soporta tipos enteros con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 <= expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 <= exp2_conv
                    except:
                        msj_error = 'El operador <= no soporta tipos decimales con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 <= expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador <= no soporta tipos decimales con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,str)):
                if(isinstance(expresion2,int)):                    
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv <= expresion2
                    except:
                        msj_error = 'El operador <= no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,str)):
                    msj_error = 'El operador <= no soporta tipos cadenas con cadenas'
                    error = E.Errores('ERROR', msj_error)
                    return error
                elif(isinstance(expresion2,float)):
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv <= expresion2
                    except:
                        msj_error = 'El operador <= no soporta tipos cadenas con decimales'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador <= no soporta tipos cadena con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,bool)):
                msj_error = 'El operador <= no soporta tipos booleano'
                error = E.Errores('ERROR', msj_error)
                return error   
        elif self.op == '>=':
            #comprobar tipos para operar
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 >= expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 >= exp2_conv
                    except:
                        msj_error = 'El operador >= no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 >= expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador >= no soporta tipos enteros con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 >= expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 >= exp2_conv
                    except:
                        msj_error = 'El operador >= no soporta tipos decimales con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 >= expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador >= no soporta tipos decimales con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,str)):
                if(isinstance(expresion2,int)):                    
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv >= expresion2
                    except:
                        msj_error = 'El operador >= no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,str)):
                    msj_error = 'El operador >= no soporta tipos cadenas con cadenas'
                    error = E.Errores('ERROR', msj_error)
                    return error
                elif(isinstance(expresion2,float)):
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv >= expresion2
                    except:
                        msj_error = 'El operador >= no soporta tipos cadenas con decimales'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador >= no soporta tipos cadena con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,bool)):
                msj_error = 'El operador >= no soporta tipos booleano'
                error = E.Errores('ERROR', msj_error)
                return error
            return expresion1
        elif self.op == '=':
            #comprobar tipos para operar
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 == expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 == exp2_conv
                    except:
                        msj_error = 'El operador == no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 == expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador == no soporta tipos enteros con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 == expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 == exp2_conv
                    except:
                        msj_error = 'El operador == no soporta tipos decimales con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 == expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador == no soporta tipos decimales con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,str)):
                if(isinstance(expresion2,int)):                    
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv == expresion2
                    except:
                        msj_error = 'El operador == no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,str)):
                    msj_error = 'El operador == no soporta tipos cadenas con cadenas'
                    error = E.Errores('ERROR', msj_error)
                    return error
                elif(isinstance(expresion2,float)):
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv == expresion2
                    except:
                        msj_error = 'El operador == no soporta tipos cadenas con decimales'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador == no soporta tipos cadena con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,bool)):
                msj_error = 'El operador == no soporta tipos booleano'
                error = E.Errores('ERROR', msj_error)
                return error
            return expresion1
        elif self.op == '<>':
            #comprobar tipos para operar
            if(isinstance(expresion1,int)):
                if(isinstance(expresion2,int)):
                    return expresion1 != expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 != exp2_conv
                    except:
                        msj_error = 'El operador != no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 != expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador != no soporta tipos enteros con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,float)):
                if(isinstance(expresion2,int)):
                    return expresion1 != expresion2
                elif(isinstance(expresion2,str)):
                    try:
                        exp2_conv = int(expresion2)
                        return expresion1 != exp2_conv
                    except:
                        msj_error = 'El operador != no soporta tipos decimales con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,float)):
                    return expresion1 != expresion2
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador != no soporta tipos decimales con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,str)):
                if(isinstance(expresion2,int)):                    
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv != expresion2
                    except:
                        msj_error = 'El operador != no soporta tipos enteros con cadenas'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,str)):
                    msj_error = 'El operador != no soporta tipos cadenas con cadenas'
                    error = E.Errores('ERROR', msj_error)
                    return error
                elif(isinstance(expresion2,float)):
                    try:
                        exp1_conv = int(expresion1)
                        return exp1_conv != expresion2
                    except:
                        msj_error = 'El operador != no soporta tipos cadenas con decimales'
                        error = E.Errores('ERROR', msj_error)
                        return error
                elif(isinstance(expresion2,bool)):
                    msj_error = 'El operador != no soporta tipos cadena con booleano'
                    error = E.Errores('ERROR', msj_error)
                    return error
                return expresion2 #error
            elif(isinstance(expresion1,bool)):
                msj_error = 'El operador != no soporta tipos booleano'
                error = E.Errores('ERROR', msj_error)
                return error
            return expresion1


class expresion_logica():
    
    def __init__(self,exp1,exp2,op):
        self.exp1 = exp1
        self.exp2 = exp2
        self.op = op

    
    def get_valor(self):
        #ejecutar las expresiones por si tienen otras operaciones
        if self.exp2 is None: 
            expresion1= self.exp1.get_valor() #not 
        else:
            expresion1= self.exp1.get_valor()
            expresion2= self.exp2.get_valor()


       #operaciones 
        if self.op == 'AND':
            #comprobar tipos para operar
            if(isinstance(expresion1,bool)):
                if(isinstance(expresion2,bool)):
                    return expresion1 and expresion2
                else:
                    msj_error = 'El operador and no soporta tipos no booleanos.'
                    error = E.Errores('ERROR', msj_error)
                    return error
            else:
                msj_error = 'El operador and no soporta tipos no booleanos.'
                error = E.Errores('ERROR', msj_error)
                return error
        elif self.op == 'OR':
            #comprobar tipos para operar
            if(isinstance(expresion1,bool)):
                if(isinstance(expresion2,bool)):
                    return expresion1 or expresion2
                else:
                    msj_error = 'El operador or no soporta tipos no booleanos.'
                    error = E.Errores('ERROR', msj_error)
                    return error
            else:
                msj_error = 'El operador or no soporta tipos no booleanos.'
                error = E.Errores('ERROR', msj_error)
                return error
        elif self.op == 'NOT':
            #comprobar tipos para operar
            if(isinstance(expresion1,bool)):
                return not expresion1 
            else:
                msj_error = 'El operador not no soporta tipos no booleanos.'
                error = E.Errores('ERROR', msj_error)
                return error

class primitivo():
    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

class datos_id():
    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        #ir a buscar a ts el valor del id
        return self.valor