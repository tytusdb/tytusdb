from astExpresion import Expresion, ExpresionCadena, ExpresionID, ExpresionNumero, TIPO_DE_DATO , TuplaCompleta
from reporteErrores.errorReport import ErrorReport # EN EL AMBITO MAS EXTERIOR SE INGRESAN A LA LISTA , EN ESTAS SUB CLASES SOLO SE SUBE EL ERROR
import math
import hashlib
import random
from datetime import datetime
class FuncionNumerica(Expresion):
    def __init__(self, funcion, parametro1=None, parametro2=None, linea = 0):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.funcion = funcion.upper()
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
        
    def metodo_width_bucket(self , lista_numeros , ts):
        if len(lista_numeros) == 4:
            #EXPRESION , MIN_VALLUE , MAX_VALUE , N_BLOQUES
            valorPrueba = lista_numeros[0].ejecutar(ts)
            if isinstance(valorPrueba , ErrorReport):
                return valorPrueba
            rangoInicial = lista_numeros[1].ejecutar(ts)
            if isinstance(rangoInicial , ErrorReport):
                return rangoInicial
            rangoMax = lista_numeros[2].ejecutar(ts)
            if isinstance(rangoMax , ErrorReport):
                return rangoMax
            nBloques = lista_numeros[3].ejecutar(ts)
            if isinstance(nBloques , ErrorReport):
                return nBloques
            # validacion de tipo numerico , 
            if not isinstance(valorPrueba , ExpresionNumero):
                return ErrorReport('sintactico', 'Error solo se acepta un tipo numero' ,self.linea)
            if not isinstance(rangoInicial, ExpresionNumero):
                return ErrorReport('sintactico', 'Error solo se acepta un tipo numero' ,self.linea)
            if not isinstance(rangoMax, ExpresionNumero):
                return ErrorReport('sintactico', 'Error solo se acepta un tipo numero' ,self.linea)
            if not isinstance(nBloques, ExpresionNumero):
                return ErrorReport('sintactico', 'Error solo se acepta un tipo numero' ,self.linea)
            if not self.getTipo(nBloques.val) == TIPO_DE_DATO.ENTERO:
                return ErrorReport('sintactico', 'Error solo se acepta un ENTERO en el ultimo parametro' ,self.linea)
                
            # dando los meros valores
            valorPrueba = valorPrueba.val
            rangoInicial = rangoInicial.val
            rangoMax = rangoMax.val
            nBloques = nBloques.val            
            if valorPrueba >= rangoMax:
                return ExpresionNumero(1 + nBloques,TIPO_DE_DATO.ENTERO,self.linea)
            elif valorPrueba < rangoInicial:
                return ExpresionNumero( (1-1)*0  , TIPO_DE_DATO.ENTERO,self.linea)
            else:
                diferencia = rangoMax-rangoInicial
                subIntervalos = diferencia/nBloques # _ , _ , _ , _ 
                auxUbicacion = 1
                aux = rangoInicial + subIntervalos
            while(not valorPrueba < aux):                    
                #print(str(aux - subIntervalos) +' , ' + str(aux))
                aux += subIntervalos
                auxUbicacion +=1
            return ExpresionNumero(auxUbicacion, TIPO_DE_DATO.ENTERO,self.linea)
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
            
            if  isinstance(self.parametro1,list):
                if self.funcion =="WIDTH_BUCKET":
                    return self.metodo_width_bucket(self.parametro1,ts)
            
            
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
                    if (nodoSyn1.val % 1) == 0:
                        valor = raizCubica(nodoSyn1.val)
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
                
    def getExpresionToString(self) -> str:          
        if self.parametro2 != None: # 2 PARAMETROS
            nodoSyn1 = self.parametro1.ejecutar(0)
            if isinstance(nodoSyn1 , ErrorReport):
                return nodoSyn1
            nodoSyn2 = self.parametro2.ejecutar(0)
            if isinstance(nodoSyn2 , ErrorReport):
                return nodoSyn2

            if isinstance(nodoSyn1 , ExpresionNumero) and isinstance(nodoSyn2 , ExpresionNumero):
                if self.funcion == "ATAN2":
                    rads = math.atan2(nodoSyn1.val,nodoSyn2.val)
                    return str(rads)
                if self.funcion == "ATAN2D":
                    rads = math.atan2(nodoSyn1.val,nodoSyn2.val)
                    grados = (rads * 180/math.pi)
                    return str(grados)
                
                if self.funcion == "DIV":
                    izq = nodoSyn1.val
                    der = nodoSyn2.val
                    if der == 0:
                        return ErrorReport('semantico', 'error DIVISION entre 0' ,self.linea)
                    valor = izq/der
                    return str(valor)
                
                if self.funcion =="GCD":
                    valor = math.gcd(nodoSyn1.val , nodoSyn2.val)
                    return  str(valor)
                
                if self.funcion =="MOD":
                    try:
                        valor = (nodoSyn1.val % nodoSyn2.val)
                        return  str(valor)               
                    except:
                        return ErrorReport('semantico', 'error en MODULO' ,self.linea) 
                
                if self.funcion =="POWER":
                    try:
                        valor = (nodoSyn1.val ** nodoSyn2.val)
                        return str(valor)               
                    except:
                        return ErrorReport('semantico', 'error en MODULO' ,self.linea)
                
                if self.funcion =="ROUND":
                    valor = round(nodoSyn1.val , nodoSyn2.val)
                    return str(valor)
                
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
                    return str(valor)
            else:
                return ErrorReport('semantico', 'error de tipo, se esperaba un ENTERO O DECIMAL' ,self.linea)
        elif self.parametro1 != None: # 1 PARAMETRO
            
            if  isinstance(self.parametro1,list):
                if self.funcion =="WIDTH_BUCKET":
                    return str(self.metodo_width_bucket(self.parametro1,0))
            
            
            nodoSyn1 = self.parametro1.ejecutar(0)
            if isinstance(nodoSyn1 , ErrorReport):
                return nodoSyn1
            
            if isinstance(nodoSyn1 , ExpresionNumero): # decimales y eneteros

                if self.funcion == "ACOS": # RADIANEES
                    if nodoSyn1.val > 1 or nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ACOS ,el parametro debe estar entre -1 y 1' ,self.linea)   
                    return  str(math.acos(nodoSyn1.val))
                
                if self.funcion == "ACOSD": # GRADOS
                    if nodoSyn1.val > 1 or nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ACOSD , el parametro debe estar entre -1 y 1' ,self.linea)   
                    rads = math.acos(nodoSyn1.val)
                    grados = (rads * 180/math.pi)
                    return str(grados)
                
                if self.funcion == "ASIN":
                    if nodoSyn1.val > 1 or nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ASIN ,el parametro debe estar entre -1 y 1' ,self.linea)   
                    valor = math.asin(nodoSyn1.val)
                    return str(valor)
                
                if self.funcion == "ASIND":
                    if nodoSyn1.val > 1 or nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ASIND ,el parametro debe estar entre -1 y 1' ,self.linea)   
                    rads = math.asin(nodoSyn1.val)
                    grados = (rads * 180/math.pi)
                    return  str(grados)
                
                if self.funcion == "ATAN":
                    try:
                        rads = math.atan(nodoSyn1.val)
                        return str(rads)
                    except:
                        return ErrorReport('semantico', 'Error en ATAN por el valor del parametro ' ,self.linea)

                if self.funcion == "ATAND":    
                    try:
                        rads = math.atan(nodoSyn1.val)
                        grados = (rads * 180/math.pi)
                        return str(grados)
                    except:
                        return ErrorReport('semantico', 'Error en ATAND por el valor del parametro ' ,self.linea)

                if self.funcion == "COS":
                    valor = math.cos(nodoSyn1.val)
                    return  str(valor)
                
                if self.funcion == "COSD":
                    rads = math.cos(nodoSyn1.val)
                    grados = (rads * 180/math.pi)
                    return str(grados)
                
                if self.funcion == "COT":
                    tangente=math.tan(nodoSyn1.val)
                    if tangente == 0:
                        return ErrorReport('semantico', 'Error en COT por el valor del parametro ' ,self.linea)
                    cot = 1 / tangente   
                    return str(cot)
                
                if self.funcion == "COTD":
                    tangente=math.tan(nodoSyn1.val)
                    if tangente == 0:
                        return ErrorReport('semantico', 'Error en COTD por el valor del parametro ' ,self.linea)
                    cot =math.degrees(1 / tangente)    
                    return str(cot)

                if self.funcion == "SIN":
                    radianes=math.sin(nodoSyn1.val)
                    return str(radianes)

            
                if self.funcion == "SIND":
                    grados=math.degrees(math.sin(nodoSyn1.val))
                    return str(grados)
            
                if self.funcion == "TAN":
                    try:
                        radianes=math.tan(nodoSyn1.val)
                        return str(radianes)
                    except:
                        return ErrorReport('semantico', 'Error en TAN por el valor del parametro ' ,self.linea)

                if self.funcion == "TAND":
                    try:
                        grados=math.degrees(math.tan(nodoSyn1.val))
                        return str(grados)
                    except:
                        return ErrorReport('semantico', 'Error en TAND por el valor del parametro ' ,self.linea)
                
                if self.funcion == "COSH":
                    try:
                        valor=math.cosh(nodoSyn1.val)
                        return str(valor) 
                    except:
                        return ErrorReport('semantico', 'Error en COSH por el valor del parametro ' ,self.linea)
                    
                
                if self.funcion == "SINH":
                    try:
                        valor=math.sinh(nodoSyn1.val)
                        return str(valor) 
                    except:
                        return ErrorReport('semantico', 'Error en SINH por el valor del parametro ' ,self.linea)
                    
                if self.funcion == "TANH":
                    try:
                        valor=math.tanh(nodoSyn1.val)
                        return str(valor)  
                    except:
                        return ErrorReport('semantico', 'Error en TANH por el valor del parametro ' ,self.linea)
                    
                    
                if self.funcion == "ACOSH":
                    if nodoSyn1.val < 1:
                        return ErrorReport('semantico', 'Error en ACOSH, el parametro debe de ser mayor o igual a 1 ' ,self.linea)
                    valor=math.acosh(nodoSyn1.val)
                    return str(valor) 
                
                if self.funcion == "ASINH":
                    valor=math.asinh(nodoSyn1.val)
                    return str(valor) 
                
                if self.funcion == "ATANH":
                    if nodoSyn1.val > 0.99 or nodoSyn1.val < -0.99:
                        return ErrorReport('semantico', 'Error en ATANH, el parametro debe estar entre 0.99 y -0.99 ' ,self.linea)
                    valor=math.atanh(nodoSyn1.val)
                    return str(valor) 
                
                #_________________________________ fin de trigonometricas
                
                if self.funcion == "ABS":
                    valor=math.fabs(nodoSyn1.val)                    
                    return str(valor) 

                    
                if self.funcion == "CBRT": #RAIZ CUBICA SOLO PARA ENTREROS
                    if (nodoSyn1.val % 1) == 0:
                        valor = raizCubica(nodoSyn1.val)
                        return str(valor)   
                    else:
                        return ErrorReport('semantico', 'error CBRT solo recibe enteros, NO decimales' ,self.linea)
                
                if self.funcion =="CEIL" or self.funcion == "CEILING":
                    valor = math.ceil(nodoSyn1.val)
                    return  str(valor) 
                
                if self.funcion =="DEGREES":
                    valor = math.degrees(nodoSyn1.val)
                    return str(valor) 
                
                if self.funcion =="FACTORIAL":
                    valor = math.factorial(nodoSyn1.val)
                    return str(valor) 
                
                if self.funcion =="FLOOR":# POR SI VIENE EN UN INSERT  
                    valor = math.floor(nodoSyn1.val)
                    return str(valor) 
                
                                
                if self.funcion =="LN":
                    try:
                        valor = math.log(nodoSyn1.val)
                        return str(valor) 
                    except :
                        return ErrorReport('semantico', 'error en el paramtro de LN' ,self.linea)

                
                if self.funcion =="LOG":
                    try:
                        valor = math.log10(nodoSyn1.val)
                        return str(valor)    
                    except :
                        return ErrorReport('semantico', 'error en el paramtro de LOG' ,self.linea)
                
                if self.funcion =="EXP":
                    try:
                        valor = math.exp(nodoSyn1.val)
                        return str(valor)     
                    except :
                        return ErrorReport('semantico', 'error en el paramtro de EXP' ,self.linea) 
                    
                if self.funcion =="RADIANS":
                    valor = math.radians(nodoSyn1.val)
                    return str(valor) 

                if self.funcion =="ROUND":
                    valor = round(nodoSyn1.val)
                    return str(valor) 
                    
                if self.funcion =="SIGN":
                    if nodoSyn1.val > 0:
                        valor = 1
                        return str(valor) 
                    if nodoSyn1.val < 0:
                        valor = -1
                        return str(valor) 
                    else:
                        return ErrorReport('semantico', 'error en funcion SING , EL 0 no tiene signo ' ,self.linea)
                if self.funcion == "SQRT":
                    if (nodoSyn1.val) < 0 :
                        return ErrorReport('semantico', 'error SQRT solo recibe enteros POSITIVOS' ,self.linea)
                    if (nodoSyn1.val % 1) == 0:
                        valor = nodoSyn1.val**(1/2)
                        return str(valor)   
                    else:
                        return ErrorReport('semantico', 'error SQRT solo recibe enteros, NO decimales' ,self.linea)
                
                if self.funcion == "TRUNC":
                    valor = math.trunc(nodoSyn1.val)
                    return str(valor) 
            else:
                return ErrorReport('semantico', 'error de tipo, se esperaba un ENTERO O DECIMAL' ,self.linea)    
                
        
        else:# SIN PARAMETROS
            
            if self.funcion == 'PI':
                return str(math.pi) 
            elif self.funcion == "RANDOM":
                valor = random.choice((1,0))
                return str(valor)                 
        
    








class FuncionCadena(Expresion):
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
            "[label = \"" + str(self.parametro1) + "\"];"

        if self.parametro2:
            if isinstance(self.parametro2, str):
                nodo += "\n" + identificador + " -> " + \
                    str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + \
                    "[label = \"" + str(self.parametro2) + "\"];"
            else:
                nodo += "\n" + identificador + " -> " + \
                    str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + \
                    "[label = \"" + str(self.parametro2) + "\"];"
        if (self.parametro1,Expresion):
            if (self.parametro1,Expresion):
                nodo += "\n" + self.parametro1.dibujar()
        
        if self.parametro2:
            if (self.parametro2,Expresion):
                nodo += "\n" + self.parametro2.dibujar()

        if self.parametro3:
            if (self.parametro3,Expresion):
                nodo += "\n" + self.parametro3.dibujar()

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
                            
                            return ExpresionCadena(str(res1)[int(res2.val) : int(res3.val)], TIPO_DE_DATO.CADENA , self.linea)
                    # si no entra hasta el ultimo if  llega aca 
                    return ErrorReport('semantico', 'error de tipo en el parametro 2 o parametro 3' ,self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo en el parametro 1' ,self.linea)
           
            
        elif self.parametro2 != None:       # 2 PARAMETROS
            if self.funcion=="CONVERT":
                nodoSimplificado = self.parametro1.ejecutar(ts)
                if isinstance(nodoSimplificado , ErrorReport):
                    return nodoSimplificado # SOLO SE SUBE EL ERROR
                self.parametro2 = self.parametro2.upper()
                
                if isinstance(nodoSimplificado , ExpresionCadena):
                    if self.parametro2 == "DATE":
                        if nodoSimplificado.isFecha:
                            return nodoSimplificado
                        else:
                            try:# ejemplo de lo que espera    año7 mes 7 dia 
                                valor = datetime.strptime( str(nodoSimplificado.val) , '%Y/%m/%d')
                                return ExpresionCadena(str(valor) ,TIPO_DE_DATO.CADENA, self.linea , True)
                            except:
                                try:# ejemplo : dia - mes - anio   7-MAY-2020
                                    valor = datetime.strptime(str(nodoSimplificado.val) , '%u-%b-%Y')
                                    return ExpresionCadena(str(valor) ,TIPO_DE_DATO.CADENA, self.linea , True)
                                except:
                                    print("NO COINCIDE CON NINGUN FORMATO DATE")
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 == "INTEGER":
                        try:
                            valor = nodoSimplificado.val
                            return ExpresionNumero(int(valor) ,TIPO_DE_DATO.DECIMAL, self.linea )
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 == "VARCHAR":
                        try:
                            valor = nodoSimplificado.val
                            return ExpresionCadena(str(valor) ,TIPO_DE_DATO.CADENA, self.linea )
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 =="DECIMAL":
                        try:
                            valor = nodoSimplificado.val
                            return ExpresionNumero(float(valor) ,TIPO_DE_DATO.DECIMAL, self.linea )
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                        
                elif isinstance(nodoSimplificado , ExpresionNumero):
                    if self.parametro2 == "DATE":
                        return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 == "INTEGER":
                        try:
                            valor = nodoSimplificado.val
                            return ExpresionNumero(int(valor) ,TIPO_DE_DATO.DECIMAL, self.linea )
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 == "VARCHAR":
                        try:
                            valor = nodoSimplificado.val
                            return ExpresionCadena(str(valor) ,TIPO_DE_DATO.CADENA, self.linea )
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 =="DECIMAL":
                        try:
                            valor = nodoSimplificado.val
                            return ExpresionNumero(float(valor) ,TIPO_DE_DATO.DECIMAL, self.linea )
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                else:
                    return ErrorReport('semantico', f'error de tipo en la funcion {self.funcion}' ,self.linea)

            else:
                print(':v esas funciones no estan')
            
        elif self.parametro1 != None:       # 1 PARAMETRO
            nodoSimplificado = self.parametro1.ejecutar(ts)
            if isinstance(nodoSimplificado , ErrorReport):
                return nodoSimplificado # SOLO SE SUBE EL ERROR
        
            if self.funcion == "LENGTH":
                if  isinstance(nodoSimplificado , ExpresionCadena) or isinstance(nodoSimplificado , ExpresionID):
                    return ExpresionNumero(len(nodoSimplificado.val), TIPO_DE_DATO.ENTERO , self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
            elif self.funcion == "TRIM":
                if  isinstance(nodoSimplificado , ExpresionCadena) or isinstance(nodoSimplificado , ExpresionID):
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
        
    def getExpresionToString(self) -> str:
        if self.parametro2 != None and self.parametro3 != None: # 3 PARAMETROS
            res1 = self.parametro1.ejecutar(0)
            res2 = self.parametro2.ejecutar(0)
            res3 = self.parametro3.ejecutar(0)
            if isinstance(res1 , ErrorReport):
                return res1
            if isinstance(res2 , ErrorReport):
                return res2
            if isinstance(res3 , ErrorReport):
                return res3
            
            if self.funcion == "SUBSTRING" or self.funcion == "SUBSTR":
                if isinstance(res2 , ExpresionNumero) or isinstance(res3 , ExpresionNumero):
                    if res2.tipo == TIPO_DE_DATO.ENTERO and res3.tipo == TIPO_DE_DATO.ENTERO:
                        return str(res1)[int(res2.val) : int(res3.val)]
                return ErrorReport('semantico', 'error de tipo en el parametro 2 o parametro 3' ,self.linea)
        elif self.parametro2 != None:
            if self.funcion=="CONVERT":
                nodoSimplificado = self.parametro1.ejecutar(0)
                if isinstance(nodoSimplificado , ErrorReport):
                    return nodoSimplificado # SOLO SE SUBE EL ERROR
                self.parametro2 = self.parametro2.upper()
                
                if isinstance(nodoSimplificado , ExpresionCadena):
                    if self.parametro2 == "DATE":
                        if nodoSimplificado.isFecha:
                            return nodoSimplificado
                        else:
                            try:# ejemplo de lo que espera    año7 mes 7 dia 
                                valor = datetime.strptime( str(nodoSimplificado.val) , '%Y/%m/%d')
                                return str(valor)
                            except:
                                try:# ejemplo : dia - mes - anio   7-MAY-2020
                                    valor = datetime.strptime(str(nodoSimplificado.val) , '%u-%b-%Y')
                                    return str(valor)
                                except:
                                    print("NO COINCIDE CON NINGUN FORMATO DATE")
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 == "INTEGER":
                        try:
                            valor = nodoSimplificado.val
                            return str(valor)
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 == "VARCHAR":
                        try:
                            valor = nodoSimplificado.val
                            return str(valor)
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 =="DECIMAL":
                        try:
                            valor = nodoSimplificado.val
                            return str(valor)
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                        
                elif isinstance(nodoSimplificado , ExpresionNumero):
                    if self.parametro2 == "DATE":
                        return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 == "INTEGER":
                        try:
                            valor = nodoSimplificado.val
                            return str(valor)
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 == "VARCHAR":
                        try:
                            valor = nodoSimplificado.val
                            return str(valor)
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                    elif self.parametro2 =="DECIMAL":
                        try:
                            valor = nodoSimplificado.val
                            return str(valor)
                        except:
                            return ErrorReport('semantico', f'error NO ES POSIBLE HACER LA CONVERSION' ,self.linea)
                else:
                    return ErrorReport('semantico', f'error de tipo en la funcion {self.funcion}' ,self.linea)

            else:
                print(':v esas funciones no estan')
            
        elif self.parametro1 != None:       # 1 PARAMETRO
            nodoSimplificado = self.parametro1.ejecutar(0)
            if isinstance(nodoSimplificado , ErrorReport):
                return nodoSimplificado # SOLO SE SUBE EL ERROR
        
            if self.funcion == "LENGTH":
                if  isinstance(nodoSimplificado , ExpresionCadena):
                    return str(len(nodoSimplificado.val))
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
            elif self.funcion == "TRIM":
                if  isinstance(nodoSimplificado , ExpresionCadena):
                    return str((nodoSimplificado.val)).strip()
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
            elif self.funcion == "MD5":
                if  isinstance(nodoSimplificado , ExpresionCadena):
                    return str(hashlib.md5(nodoSimplificado.val.encode()).hexdigest())
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
            elif self.funcion == "SHA256":
                if  isinstance(nodoSimplificado , ExpresionCadena):
                    return str(hashlib.sha256(nodoSimplificado.val.encode()).hexdigest())
            return str('FUNCION DESCONOCIDA')

class FuncionAgregacion(Expresion):
    def __init__(self, funcion, parametro1, parametro2=None, linea = 0 ):
        self.funcion = funcion.upper()
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.linea = linea


    def ejecucion(self, ts):#los que pueden venir en el select 
        pass
        # -SUM es como acumulativa


class BitwaseBinaria(Expresion):
    def __init__(self, exp1, exp2, operador, linea):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador
        self.linea = linea


    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.operador + "\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp1)) + ";"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp2)) + ";\n"

        nodo += self.exp1.dibujar()
        nodo += self.exp2.dibujar()

        return nodo
    def ejecutar(self, ts):
        expizq = self.exp1.ejecutar(ts)
        expder = self.exp2.ejecutar(ts)
        # por si se quiere operar un error con una expresion buena ,  retorna de una el error
        if isinstance(expizq , ErrorReport):
            return expizq
        if isinstance(expder , ErrorReport):
            return expder
        # la UNICA EXPRESION QUE DEBE DE OPERAR ES UN ID-tipo-entero o un tipoentero de la expresion sumerica
        if not (isinstance(expizq , ExpresionNumero)  or isinstance(expizq , ExpresionID)):
            return ErrorReport('semantico', 'Error de tipo con el operando izquierdo' , self.linea )
        
        if not (isinstance(expder , ExpresionNumero)  or isinstance(expizq , ExpresionID)):
            return ErrorReport('semantico', 'Error de tipo con el operando Derecho' , self.linea )

        if self.operador == ">>" :
            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val >> expder.val, TIPO_DE_DATO.ENTERO,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando izquierdo en OPERADOR >>' , self.linea )
            elif expder.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando derecho en OPERADOR >>' , self.linea )

        elif self.operador == "<<":
            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                return ExpresionNumero(expizq.val << expder.val, TIPO_DE_DATO.ENTERO,self.linea) 
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando izquierdo en OPERADOR <<' , self.linea )
            elif expder.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando derecho en OPERADOR <<' , self.linea )
            
        elif self.operador == "#":
            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                try:
                    valor = expizq.val ^ expder.val
                    return ExpresionNumero(valor, TIPO_DE_DATO.ENTERO , self.linea) 
                except:
                    return  ErrorReport('semantico', 'Error de Ejecucion con el OPERADOR | ', self.linea )
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando izquierdo en OPERADOR #' , self.linea )
            elif expder.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando derecho en OPERADOR #' , self.linea )
            else:
                return 0
        elif self.operador == "|":
            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                try:
                    valor = expizq.val | expder.val
                    return ExpresionNumero(valor, TIPO_DE_DATO.ENTERO , self.linea) 
                except:
                    return  ErrorReport('semantico', 'Error de Ejecucion con el OPERADOR | ', self.linea )
                
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando izquierdo en OPERADOR |' , self.linea )
            elif expder.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando derecho en OPERADOR |' , self.linea )
            else:
                return 0
        elif self.operador == "&":

            if expizq.tipo == TIPO_DE_DATO.ENTERO and expder.tipo == TIPO_DE_DATO.ENTERO:
                try:
                    valor = expizq.val & expder.val
                    return ExpresionNumero(valor, TIPO_DE_DATO.ENTERO , self.linea) 
                except:
                    return  ErrorReport('semantico', 'Error de Ejecucion con el OPERADOR | ', self.linea )
            elif expizq.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando izquierdo en OPERADOR #' , self.linea )
            elif expder.tipo == TIPO_DE_DATO.DECIMAL:
                return  ErrorReport('semantico', 'Error de tipo con el operando derecho en OPERADOR #' , self.linea )
        else:
            return  ErrorReport('semantico', 'Error Operador desconocido' , self.linea )
    
    def evaluacionCheck(self ,tipoColumna, idCol, ts = None) -> int: # 0 = booleano , 1 = entero , 2  = decimal , 3 = cadena , 4 = cadenaDate , 5 = id , 6 = Error  
        izq = self.exp1.evaluacionCheck(tipoColumna , idCol , ts)
        der = self.exp2.evaluacionCheck(tipoColumna , idCol , ts)
        print(f'izq {izq} --- der {der}  {self.exp2.ejecutar(0).val}')
        if (izq != 1) or (der != 1):
            return 5
        return 1  # no importa que operacion realice va regresar un numero
    def getExpresionToString(self) -> str:
        izq  = self.exp1.getExpresionToString()
        der  = self.exp2.getExpresionToString()
        if isinstance(izq , ErrorReport):
            return izq
        if isinstance(der , ErrorReport):
            return der
        op = self.operador
        return str(izq + f' { op } '+der)


class FuncionTime(Expresion):# 0 , 1 y 2 
    def __init__(self, funcion, parametro1=None, parametro2=None, linea = 0):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.funcion = funcion.upper()
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"" + self.funcion + "\" ];"
        nodo += "\n" + identificador + " -> " + \
            str(hash(self.parametro1)) + ";"
        nodo += "\n" + str(hash(self.parametro1)) + \
            "[label = \"" + str(self.parametro1) + "\"];"

        if self.parametro2:
            if isinstance(self.parametro2, str):
                nodo += "\n" + identificador + " -> " + \
                    str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + \
                    "[label = \"" + str(self.parametro2) + "\"];"
            else:
                nodo += "\n" + identificador + " -> " + \
                    str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + \
                    "[label = \"" + str(self.parametro2) + "\"];"
        if (self.parametro1,Expresion):
            if (self.parametro1,Expresion):
                nodo += "\n" + self.parametro1.dibujar()
        
        if self.parametro2:
            if (self.parametro2,Expresion):
                nodo += "\n" + self.parametro2.dibujar()

                
    def ejecutar(self, ts):#los que pueden venir en el select 
        if self.parametro1 != None and self.parametro2 != None:        
            if self.funcion == "EXTRACT":
                
                self.parametro2 = str(self.parametro2).strip()
                # AHORA REVISANDO SI TIENE COHERENCIA
                
                try:# EL PARAMETRO 2 ES MI CADENA DATE , PARAMETRO 2 ESPERADO  yyyy-mm-dd hh:mm:dd
                    objetodate = datetime.strptime(self.parametro2, '%Y-%m-%d %H:%M:%S')
                except:
                    return ErrorReport('semantico', 'error Incoherencia con la cadena date' ,self.linea)
                
                if self.parametro1 == "YEAR":
                    anio = str(objetodate.year)
                    return ExpresionNumero(int(anio), TIPO_DE_DATO.ENTERO,self.linea)
                    
                elif self.parametro1 == "MONTH":
                    mes = str(objetodate.month)
                    return ExpresionNumero(int(mes), TIPO_DE_DATO.ENTERO,self.linea)
    
                elif self.parametro1 == "DAY":
                    dia = str(objetodate.day)
                    return ExpresionNumero(int(dia), TIPO_DE_DATO.ENTERO,self.linea)
                        
                elif self.parametro1 == "HOUR":
                    hora = str(objetodate.hour)
                    return ExpresionNumero(int(hora), TIPO_DE_DATO.ENTERO,self.linea)
                
                elif self.parametro1 == "MINUTE":
                    minuto = str(objetodate.minute)
                    return ExpresionNumero(int(minuto), TIPO_DE_DATO.ENTERO,self.linea)
                    
                elif self.parametro1 == "SECOND":
                    seg = str(objetodate.second)
                    return ExpresionNumero(int(seg), TIPO_DE_DATO.ENTERO,self.linea)
            elif self.funcion == "DATE_PART":
                
                self.parametro2 = self.parametro2.lower().strip()
                valores = {}
                lexema = self.parametro2[0]
                x = 1 
                while(x < len(self.parametro2)):
                    lexema += self.parametro2[x]
                    if self.parametro2[x] == "s" and self.parametro2[x-1] != " " :
                        lexema = lexema.strip()
                        key = ''
                        val = ''
                        posIniKey = 0 
                        for i in range( len(lexema)):
                            if lexema[i] == ' ':
                                break
                            else:
                                val += lexema[i]
                                posIniKey = i
                                posIniKey +=1
                        
                        while(posIniKey < len(lexema)):
                            key += lexema[posIniKey]
                            posIniKey+=1
                        lexema = ""
                        key = key.strip()
                        validacion = valores.get(key , 'ok')
                        
                        if validacion == 'ok':
                            valores[key] = val
                        else:
                            return ErrorReport('sintactico', 'ERROR:  la sintaxis de entrada no es válida para tipo interval' ,self.linea)            
                    x+=1
                    
                

                if self.parametro1 == "HOUR" or self.parametro1 == "HOURS":
                    
                    valor = valores.get('hours','NO_ESTA')
                    if valor == 'NO_ESTA':
                        return ErrorReport('semantico', 'solicitud de horas en Interaval y no fue especificado en la cadena' ,self.linea) 
                    else:
                        return ExpresionNumero(int(valor), TIPO_DE_DATO.ENTERO,self.linea)
                    
                elif self.parametro1 == "MINUTE" or self.parametro1 == "MINUTES":
                    
                    valor = valores.get('minutes','NO_ESTA')
                    if valor == 'NO_ESTA':
                        return ErrorReport('semantico', 'solicitud de minutos en Interaval y no fue especificado en la cadena' ,self.linea) 
                    else:
                        return ExpresionNumero(int(valor), TIPO_DE_DATO.ENTERO,self.linea)

                elif self.parametro1 == "SECOND" or self.parametro1 == "SECONDS":
                    
                    valor = valores.get('seconds','NO_ESTA')
                    if valor == 'NO_ESTA':
                        return ErrorReport('semantico', 'solicitud de segundos en Interaval y no fue especificado en la cadena' ,self.linea) 
                    else:                   
                        return ExpresionNumero(int(valor), TIPO_DE_DATO.ENTERO,self.linea)
                else: 
                    return ErrorReport('semantico', 'la cadena debe solicitar hours,minutes or seconds' ,self.linea)
            else:
                print("funcion desconocida")
        elif self.parametro1 != None:
            if self.funcion == 'TIMESTAMP':
                hora_fecha_actual = str(datetime.now())[0:19]
                return ExpresionCadena(hora_fecha_actual,TIPO_DE_DATO.CADENA,self.linea,True)
            else:
                print("funcion desconocida")
        else:
            if self.funcion == "NOW":
                hora_fecha_actual = str(datetime.now())[0:19]
                return ExpresionCadena(hora_fecha_actual,TIPO_DE_DATO.CADENA,self.linea,True)
            elif self.funcion == "CURRENT_DATE":
                fecha_actual = str(datetime.now())[0:10]
                return ExpresionCadena(fecha_actual,TIPO_DE_DATO.CADENA,self.linea,True)
            elif self.funcion == "CURRENT_TIME":
                hora_actual = str(datetime.now())[11:19]
                return ExpresionCadena(hora_actual,TIPO_DE_DATO.CADENA,self.linea,True)
            elif self.funcion == "CURRENT_TIMESTAMP":
                hora_fecha_actual = str(datetime.now())[0:19]
                return ExpresionCadena(hora_fecha_actual,TIPO_DE_DATO.CADENA,self.linea,True)
                                    
    def getExpresionToString(self):#los que pueden venir en el select 
        if self.parametro1 != None and self.parametro2 != None:        
            if self.funcion == "EXTRACT":
                self.parametro2 = str(self.parametro2).strip()
                # AHORA REVISANDO SI TIENE COHERENCIA
                try:# EL PARAMETRO 2 ES MI CADENA DATE , PARAMETRO 2 ESPERADO  yyyy-mm-dd hh:mm:dd
                    objetodate = datetime.strptime(self.parametro2, '%Y-%m-%d %H:%M:%S')
                except:
                    return ErrorReport('semantico', 'error Incoherencia con la cadena date' ,self.linea)
                if self.parametro1 == "YEAR":
                    anio = str(objetodate.year)
                    return str(anio)
                    
                elif self.parametro1 == "MONTH":
                    mes = str(objetodate.month)
                    return str(mes)
    
                elif self.parametro1 == "DAY":
                    dia = str(objetodate.day)
                    return str(dia)
                        
                elif self.parametro1 == "HOUR":
                    hora = str(objetodate.hour)
                    return str(hora)
                
                elif self.parametro1 == "MINUTE":
                    minuto = str(objetodate.minute)
                    return str(minuto)
                    
                elif self.parametro1 == "SECOND":
                    seg = str(objetodate.second)
                    return str(seg)
            elif self.funcion == "DATE_PART":
                
                self.parametro2 = self.parametro2.lower().strip()
                valores = {}
                lexema = self.parametro2[0]
                x = 1 
                while(x < len(self.parametro2)):
                    lexema += self.parametro2[x]
                    if self.parametro2[x] == "s" and self.parametro2[x-1] != " " :
                        lexema = lexema.strip()
                        key = ''
                        val = ''
                        posIniKey = 0 
                        for i in range( len(lexema)):
                            if lexema[i] == ' ':
                                break
                            else:
                                val += lexema[i]
                                posIniKey = i
                                posIniKey +=1
                        
                        while(posIniKey < len(lexema)):
                            key += lexema[posIniKey]
                            posIniKey+=1
                        lexema = ""
                        key = key.strip()
                        validacion = valores.get(key , 'ok')
                        
                        if validacion == 'ok':
                            valores[key] = val
                        else:
                            return ErrorReport('sintactico', 'ERROR:  la sintaxis de entrada no es válida para tipo interval' ,self.linea)            
                    x+=1
                    
                

                if self.parametro1 == "HOUR" or self.parametro1 == "HOURS":
                    
                    valor = valores.get('hours','NO_ESTA')
                    if valor == 'NO_ESTA':
                        return ErrorReport('semantico', 'solicitud de horas en Interaval y no fue especificado en la cadena' ,self.linea) 
                    else:
                        return str(valor)
                    
                elif self.parametro1 == "MINUTE" or self.parametro1 == "MINUTES":
                    
                    valor = valores.get('minutes','NO_ESTA')
                    if valor == 'NO_ESTA':
                        return ErrorReport('semantico', 'solicitud de minutos en Interaval y no fue especificado en la cadena' ,self.linea) 
                    else:
                        return str(valor)

                elif self.parametro1 == "SECOND" or self.parametro1 == "SECONDS":
                    
                    valor = valores.get('seconds','NO_ESTA')
                    if valor == 'NO_ESTA':
                        return ErrorReport('semantico', 'solicitud de segundos en Interaval y no fue especificado en la cadena' ,self.linea) 
                    else:                   
                        return str(valor)
                else: 
                    return ErrorReport('semantico', 'la cadena debe solicitar hours,minutes or seconds' ,self.linea)
            else:
                print("funcion desconocida")
        elif self.parametro1 != None:
            if self.funcion == 'TIMESTAMP':
                hora_fecha_actual = str(datetime.now())[0:19]
                return str(hora_fecha_actual)
            else:
                print("funcion desconocida")
        else:
            if self.funcion == "NOW":
                hora_fecha_actual = str(datetime.now())[0:19]
                return str(hora_fecha_actual)
            elif self.funcion == "CURRENT_DATE":
                fecha_actual = str(datetime.now())[0:10]
                return str(fecha_actual)
            elif self.funcion == "CURRENT_TIME":
                hora_actual = str(datetime.now())[11:19]
                return str(hora_actual)
            elif self.funcion == "CURRENT_TIMESTAMP":
                hora_fecha_actual = str(datetime.now())[0:19]
                return str(hora_fecha_actual)                                
                                    

class BitwaseUnaria(Expresion):
    def __init__(self, operador , exp , linea):
        self.exp = exp
        self.linea = linea
        self.operador = operador
        
    def dibujar(self):
        identificador = str(hash(self))
        nodo = "\n" + identificador + "[ label =\""+self.operador+"\" ];"
        nodo += "\n" + identificador + " -> " + str(hash(self.exp)) + ";\n"
        nodo += self.exp.dibujar()
        return nodo
    
    def ejecutar(self, ts):
        unario = self.exp.ejecutar(ts)
        if isinstance(unario , ErrorReport):
            return unario # si ya viene un error solo lo retorna
        if not (isinstance(unario , ExpresionNumero)):
            return ErrorReport('semantico', f'Error , Tipe Invalido UNARIO {self.operador}' ,self.linea)
    
        
        try:# CASOS DE EJECUCION
            if self.operador == "~":
                if GET_TIPO(unario.val) == TIPO_DE_DATO.ENTERO:
                    return ExpresionNumero(~ unario.val, GET_TIPO(unario.val), self.linea)
                else:
                    return ErrorReport('semantico', 'error operador Unario ~ solo recibe ENTEROS' ,self.linea)
            elif self.operador =="|": # SACA LA RAIZ CUADRADA
                    if (unario.val) < 0:
                        return ErrorReport('semantico', 'error operador Unario | solo recibe numeros POSITIVOS' ,self.linea)
                        valor = unario.val**(1/2)
                        return ExpresionNumero(valor,GET_TIPO(valor),self.linea)
            elif self.operador =="||": # SACA LA RAIZ CUBICA
                        valor = raizCubica(unario.val)
                        return ExpresionNumero(valor,GET_TIPO(valor),self.linea)    
        except:
            return ErrorReport('semantico', f'Error: Tipe Invalido UNARIO {self.operador}' ,self.linea)  

    def evaluacionCheck(self ,tipoColumna, idCol, ts = None) -> int: # 0 = booleano , 1 = entero , 2  = decimal , 3 = cadena , 4 = cadenaDate , 5 = id , 6 = Error  
        value = self.exp.evaluacionCheck(tipoColumna , idCol , ts)
        if value != 1 and value != 2:
            return 5
        return value
    
    def getExpresionToString(self) -> str:
        sint = self.exp.getExpresionToString()
        if isinstance(sint , ErrorReport):
            return sint
        return str(f'{self.operador}' + sint)

# funcion global para ver si es decimal o entero
def GET_TIPO(valorNumerico):
    if (valorNumerico % 1) == 0:
        return TIPO_DE_DATO.ENTERO
    else:
        return TIPO_DE_DATO.DECIMAL
    
def raizCubica(valor):
    if valor < 0 :
        return -(abs(valor))**(1/3)
    elif valor > 0:
        return valor**(1/3)
    else:
        return 0 