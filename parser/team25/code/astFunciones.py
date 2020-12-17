from astExpresion import Expresion, ExpresionCadena, ExpresionID, ExpresionNumero, TIPO_DE_DATO
from reporteErrores.errorReport import ErrorReport # EN EL AMBITO MAS EXTERIOR SE INGRESAN A LA LISTA , EN ESTAS SUB CLASES SOLO SE SUBE EL ERROR
import math
import hashlib
import random

class FuncionNumerica(Expresion):
    def __init__(self, funcion, parametro1=None, parametro2=None, linea = 0):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.funcion = funcion
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.funcion + "\" ];"

        # Retorno
        if self.parametro1:
            nodo += "\n" + identificador + " -> " + \
                str(hash(self.parametro1)) + ";"
            nodo += self.parametro1.dibujar()
        if self.parametro2:
            nodo += "\n" + identificador + " -> " + \
                str(hash(self.parametro2)) + ";"
            nodo += self.parametro2.dibujar()

        return nodo
    
    def getTipo(self , valorNumerico):
        if (valorNumerico % 1) == 0:
            return TIPO_DE_DATO.ENTERO
        else:
            return TIPO_DE_DATO.DECIMAL
        
    def metodo_width_bucket(self , lista_numeros):
        if len(lista_numeros) == 4:
            # EXPRESION , MIN_VALLUE , MAX_VALUE , N_BLOQUES
            
            pass    
        else:
            return ErrorReport('sintactico', 'error en width_bucket se esperaba solo 4 parametros' ,self.linea)
        
    
    
    def ejecutar(self, ts = None):            
        if self.parametro2 != None: # 2 PARAMETROS
            nodoSyn1 = self.parametro1.ejecutar(ts)
            if isinstance(nodoSyn1 , ErrorReport):
                return nodoSyn1
            nodoSyn2 = self.parametro2.ejecutar(ts)
            if isinstance(nodoSyn2 , ErrorReport):
                return nodoSyn2

            if isinstance(nodoSyn1 , ExpresionNumero) and isinstance(nodoSyn2 , ExpresionNumero):
                
                if self.funcion == "ATAN2":
                    rads = math.atan2(nodoSyn1.val,nodoSyn2.val)
                    return ExpresionNumero(rads,self.getTipo(rads),self.linea) 
                
                if self.funcion == "ATAN2D":
                    rads = math.atan2(nodoSyn1.val,nodoSyn2.val)
                    grados = (rads * 180/math.pi)
                    return ExpresionNumero(grados,self.getTipo(grados),self.linea)
                
                if self.funcion == "DIV":
                    
                    izq = nodoSyn1.val
                    der = nodoSyn2.val
                    if der == 0:
                        return ErrorReport('semantico', 'error DIVISION entre 0' ,self.linea)
                    valor = izq/der
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion =="GCD":
                    valor = math.gcd(nodoSyn1.val , nodoSyn2.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion =="MOD":
                    try:
                        valor = (nodoSyn1.val % nodoSyn2.val)
                        return ExpresionNumero(valor,self.getTipo(valor),self.linea)                  
                    except:
                        return ErrorReport('semantico', 'error en MODULO' ,self.linea) 
                
                if self.funcion =="POWER":
                    try:
                        valor = (nodoSyn1.val ** nodoSyn2.val)
                        return ExpresionNumero(valor,self.getTipo(valor),self.linea)                  
                    except:
                        return ErrorReport('semantico', 'error en MODULO' ,self.linea)
                
                if self.funcion =="ROUND":
                    valor = round(nodoSyn1.val , nodoSyn2.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion == "TRUNC": 
                    if self.getTipo(nodoSyn2.val) != TIPO_DE_DATO.ENTERO:
                        return ErrorReport('semantico', 'error en Metodo TRUNC el segundo parametro tiene que ser un entero' ,self.linea)
                    cadenaInt = str(nodoSyn1.val)
                    numero_truncado = ''
                    indice = 0
                    decimalesAdjuntados = 0
                    for i in range(len(cadenaInt)):
                        if cadenaInt[i] == '.':
                            numero_truncado += cadenaInt[i]
                            indice = i
                            break
                        else:
                            numero_truncado += cadenaInt[i]
                    indice+=1        
                    while(decimalesAdjuntados < nodoSyn2.val):
                        
                        if  indice < len(cadenaInt):
                            numero_truncado += cadenaInt[indice]
                        else:
                            numero_truncado += '0'
                        
                        indice+=1
                        decimalesAdjuntados+=1
                    valor = float(numero_truncado)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea) 
                    
                        
                    
                    

                    
                    
            
            else:
                return ErrorReport('semantico', 'error de tipo, se esperaba un ENTERO O DECIMAL' ,self.linea)
        elif self.parametro1 != None: # 1 PARAMETRO
            
            nodoSyn1 = self.parametro1.ejecutar(ts)
            if isinstance(nodoSyn1 , ErrorReport):
                return nodoSyn1
            
            if isinstance(nodoSyn1 , ExpresionNumero): # decimales y eneteros
                if self.funcion == "ACOS": # RADIANEES
                    if nodoSyn1.val > 1 or nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ACOS ,el parametro debe estar entre -1 y 1' ,self.linea)   
                    return ExpresionNumero(math.acos(nodoSyn1.val),self.getTipo(nodoSyn1.val),self.linea)
                
                if self.funcion == "ACOSD": # GRADOS 
                    if nodoSyn1.val > 1 or nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ACOSD , el parametro debe estar entre -1 y 1' ,self.linea)   
                    rads = math.acos(nodoSyn1.val)
                    grados = (rads * 180/math.pi)
                    return ExpresionNumero(grados,self.getTipo(grados),self.linea)
                
                if self.funcion == "ASIN":
                    if nodoSyn1.val > 1 or nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ASIN ,el parametro debe estar entre -1 y 1' ,self.linea)   
                    valor = math.asin(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion == "ASIND":
                    if nodoSyn1.val > 1 or nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ASIND ,el parametro debe estar entre -1 y 1' ,self.linea)   
                    rads = math.asin(nodoSyn1.val)
                    grados = (rads * 180/math.pi)
                    return ExpresionNumero(grados,self.getTipo(grados),self.linea)
                
                if self.funcion == "ATAN":
                    try:
                        rads = math.atan(nodoSyn1.val)
                        return ExpresionNumero(rads,self.getTipo(rads),self.linea)
                    except:
                        return ErrorReport('semantico', 'Error en ATAN por el valor del parametro ' ,self.linea)

                if self.funcion == "ATAND":    
                    try:
                        rads = math.atan(nodoSyn1.val)
                        grados = (rads * 180/math.pi)
                        return ExpresionNumero(grados,self.getTipo(grados),self.linea)
                    except:
                        return ErrorReport('semantico', 'Error en ATAND por el valor del parametro ' ,self.linea)

                if self.funcion == "COS":
                    valor = math.cos(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion == "COSD":
                    rads = math.cos(nodoSyn1.val)
                    grados = (rads * 180/math.pi)
                    return ExpresionNumero(grados,self.getTipo(grados),self.linea)
                
                if self.funcion == "COT":
                    tangente=math.tan(nodoSyn1.val)
                    if tangente == 0:
                        return ErrorReport('semantico', 'Error en COT por el valor del parametro ' ,self.linea)
                    cot = 1 / tangente   
                    return ExpresionNumero(cot,self.getTipo(cot),self.linea)
                
                if self.funcion == "COTD":
                    tangente=math.tan(nodoSyn1.val)
                    if tangente == 0:
                        return ErrorReport('semantico', 'Error en COTD por el valor del parametro ' ,self.linea)
                    cot =math.degrees(1 / tangente)    
                    return ExpresionNumero(cot,self.getTipo(cot),self.linea)  

                if self.funcion == "SIN":
                    radianes=math.sin(nodoSyn1.val)
                    return ExpresionNumero(radianes,self.getTipo(radianes),self.linea)  
            
                if self.funcion == "SIND":
                    grados=math.degrees(math.sin(nodoSyn1.val))
                    return ExpresionNumero(grados,self.getTipo(grados),self.linea)
            
                if self.funcion == "TAN":
                    try:
                        radianes=math.tan(nodoSyn1.val)
                        return ExpresionNumero(radianes,self.getTipo(radianes),self.linea) 
                    except:
                        return ErrorReport('semantico', 'Error en TAN por el valor del parametro ' ,self.linea)

                if self.funcion == "TAND":
                    try:
                        grados=math.degrees(math.tan(nodoSyn1.val))
                        return ExpresionNumero(grados,self.getTipo(grados),self.linea) 
                    except:
                        return ErrorReport('semantico', 'Error en TAND por el valor del parametro ' ,self.linea)
                
                if self.funcion == "COSH":
                    try:
                        valor=math.cosh(nodoSyn1.val)
                        return ExpresionNumero(valor,self.getTipo(valor),self.linea) 
                    except:
                        return ErrorReport('semantico', 'Error en COSH por el valor del parametro ' ,self.linea)
                    
                
                if self.funcion == "SINH":
                    try:
                        valor=math.sinh(nodoSyn1.val)
                        return ExpresionNumero(valor,self.getTipo(valor),self.linea) 
                    except:
                        return ErrorReport('semantico', 'Error en SINH por el valor del parametro ' ,self.linea)
                    
                if self.funcion == "TANH":
                    try:
                        valor=math.tanh(nodoSyn1.val)
                        return ExpresionNumero(valor,self.getTipo(valor),self.linea) 
                    except:
                        return ErrorReport('semantico', 'Error en TANH por el valor del parametro ' ,self.linea)
                    
                    
                if self.funcion == "ACOSH":
                    if nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ACOSH, el parametro debe de ser mayor o igual a 1 ' ,self.linea)
                    valor=math.acosh(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion == "ASINH":
                    valor=math.asinh(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion == "ATANH":
                    if nodoSyn1.val > 0.99 or nodoSyn1.val < -0.99:
                        return ErrorReport('semantico', 'Error en ATANH, el parametro debe estar entre 0.99 y -0.99 ' ,self.linea)
                    valor=math.atanh(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                #_________________________________ fin de trigonometricas
                
                if self.funcion == "ABS":
                    valor=math.fabs(nodoSyn1.val)                    
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)

                    
                if self.funcion == "CBRT": #RAIZ CUBICA SOLO PARA ENTREROS
                    if (nodoSyn1.val) < 0 :
                        return ErrorReport('semantico', 'error SQRT solo recibe enteros POSITIVOS :D' ,self.linea)
                    if (nodoSyn1.val % 1) == 0:
                        valor = nodoSyn1.val**(1/3)
                        return ExpresionNumero(valor,self.getTipo(valor),self.linea)  
                    else:
                        return ErrorReport('semantico', 'error CBRT solo recibe enteros, NO decimales' ,self.linea)
                
                if self.funcion =="CEIL" or self.funcion == "CEILING":
                    valor = math.ceil(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion =="DEGREES":
                    valor = math.degrees(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion =="FACTORIAL":
                    valor = math.factorial(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                if self.funcion =="FLOOR":# POR SI VIENE EN UN INSERT  
                    valor = math.floor(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                
                                
                if self.funcion =="LN":
                    try:
                        valor = math.log(nodoSyn1.val)
                        return  ExpresionNumero(valor,self.getTipo(valor),self.linea)
                    except :
                        return ErrorReport('semantico', 'error en el paramtro de LN' ,self.linea)

                
                if self.funcion =="LOG":
                    try:
                        valor = math.log10(nodoSyn1.val)
                        return  ExpresionNumero(valor,self.getTipo(valor),self.linea)    
                    except :
                        return ErrorReport('semantico', 'error en el paramtro de LOG' ,self.linea)
                
                if self.funcion =="EXP":
                    try:
                        valor = math.exp(nodoSyn1.val)
                        return  ExpresionNumero(valor,self.getTipo(valor),self.linea)    
                    except :
                        return ErrorReport('semantico', 'error en el paramtro de EXP' ,self.linea) 
                    
                if self.funcion =="RADIANS":
                    valor = math.radians(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)

                if self.funcion =="ROUND":
                    valor = round(nodoSyn1.val)
                    return ExpresionNumero(valor,self.getTipo(valor),self.linea)
                    
                if self.funcion =="SIGN":
                    if nodoSyn1.val > 0:
                        valor = 1
                        return ExpresionNumero(valor,TIPO_DE_DATO.ENTERO,self.linea)
                    if nodoSyn1.val < 0:
                        valor = -1
                        return ExpresionNumero(valor,TIPO_DE_DATO.ENTERO,self.linea)
                    else:
                        return ErrorReport('semantico', 'error en funcion SING , EL 0 no tiene signo ' ,self.linea)
                if self.funcion == "SQRT":
                    if (nodoSyn1.val) < 0 :
                        return ErrorReport('semantico', 'error SQRT solo recibe enteros POSITIVOS' ,self.linea)
                    if (nodoSyn1.val % 1) == 0:
                        valor = nodoSyn1.val**(1/2)
                        return ExpresionNumero(valor,self.getTipo(valor),self.linea)  
                    else:
                        return ErrorReport('semantico', 'error SQRT solo recibe enteros, NO decimales' ,self.linea)
                if self.funcion =="WIDTH_BUCKET":
                    self.metodo_width_bucket(self.parametro1)
                
                if self.funcion == "TRUNC":
                    valor = math.trunc(nodoSyn1.val)
                    return ExpresionNumero(valor,TIPO_DE_DATO.ENTERO,self.linea)
                 
                
                    
                    

            else:
                return ErrorReport('semantico', 'error de tipo, se esperaba un ENTERO O DECIMAL' ,self.linea)    
                
        
        else:# SIN PARAMETROS
            
            if self.funcion == 'PI':
                return ExpresionNumero(math.pi,TIPO_DE_DATO.DECIMAL,self.linea)
            elif self.funcion == "RANDOM":
                valor = random.choice((1,0))
                return ExpresionNumero(valor,TIPO_DE_DATO.ENTERO,self.linea)
                
                
        
    








class FuncionCadena:
    def __init__(self, funcion, parametro1, parametro2=None, parametro3=None, linea = 0 ):
        self.funcion = funcion
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.parametro3 = parametro3
        self.linea = linea
        
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"" + self.funcion + "\" ];"
        nodo += "\n" + identificador + " -> " + \
            str(hash(self.parametro1)) + ";"
        nodo += "\n" + str(hash(self.parametro1)) + \
            "[label = \"" + self.parametro1 + "\"];"

        if self.parametro2:
            if isinstance(self.parametro2, str):
                nodo += "\n" + identificador + " -> " + \
                    str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + \
                    "[label = \"" + self.parametro2 + "\"];"
            else:
                nodo += "\n" + identificador + " -> " + \
                    str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + \
                    "[label = \"" + str(self.parametro2) + "\"];"

        return nodo
    def ejecutar(self, ts):
        
        if self.parametro2 != None and self.parametro3 != None: # 3 PARAMETROS
            res1 = self.parametro1.ejecutar(ts)
            res2 = self.parametro2.ejecutar(ts)
            res3 = self.parametro3.ejecutar(ts)
            if isinstance(res1 , ErrorReport):
                return res1
            if isinstance(res2 , ErrorReport):
                return res2
            if isinstance(res3 , ErrorReport):
                return res3
            
            if self.funcion == "SUBSTRING" or self.funcion == "SUBSTR":
                if isinstance(res1 , ExpresionID) or isinstance(res1 , ExpresionCadena):
                    if isinstance(res2 , ExpresionNumero) or isinstance(res3 , ExpresionNumero):
                        if res2.tipo == TIPO_DE_DATO.ENTERO and res3.tipo == TIPO_DE_DATO.ENTERO:
                            print("RETORNA: "+ str(res1)[int(res2.val) : int(res3.val)])
                            return ExpresionCadena(str(res1)[int(res2.val) : int(res3.val)], TIPO_DE_DATO.CADENA , self.linea)
                    # si no entra hasta el ultimo if  llega aca 
                    return ErrorReport('semantico', 'error de tipo en el parametro 2 o parametro 3' ,self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo en el parametro 1' ,self.linea)
           
            
        elif self.parametro2 != None:       # 2 PARAMETROS
            print("2 parametros")
            
        elif self.parametro1 != None:       # 1 PARAMETRO
            nodoSimplificado = self.parametro1.ejecutar(ts)
            if isinstance(nodoSimplificado , ErrorReport):
                return nodoSimplificado # SOLO SE SUBE EL ERROR
        
            if self.funcion == "LENGTH":
                if  isinstance(nodoSimplificado , ExpresionCadena) or isinstance(nodoSimplificado , ExpresionID):
                    print("RETORNA: "+ str(len(nodoSimplificado.val)))
                    return ExpresionNumero(len(nodoSimplificado.val), TIPO_DE_DATO.ENTERO , self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
            elif self.funcion == "TRIM":
                if  isinstance(nodoSimplificado , ExpresionCadena) or isinstance(nodoSimplificado , ExpresionID):
                    print("RETORNA: "+ str((nodoSimplificado.val)).strip())
                    return ExpresionCadena(str((nodoSimplificado.val)).strip(), TIPO_DE_DATO.CADENA , self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
            elif self.funcion == "MD5":
                if  isinstance(nodoSimplificado , ExpresionCadena) or isinstance(nodoSimplificado , ExpresionID):
                    return ExpresionCadena(hashlib.md5(nodoSimplificado.val.encode()).hexdigest(), TIPO_DE_DATO.CADENA , self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
            elif self.funcion == "SHA256":
                if  isinstance(nodoSimplificado , ExpresionCadena) or isinstance(nodoSimplificado , ExpresionID):
                    return ExpresionCadena(hashlib.sha256(nodoSimplificado.val.encode()).hexdigest(), TIPO_DE_DATO.CADENA , self.linea)
                    

class FuncionAgregacion:
    def __init__(self, funcion, parametro1, parametro2=None, linea = 0 ):
        self.funcion = funcion
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.linea = linea


    def ejecucion(self, ts):#los que pueden venir en el select 
        pass
        # -SUM es como acumulativa
        