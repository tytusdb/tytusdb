from instruccion import *
from funcionesTS import *
from conexionDB import *
from expresiones import *
from funcionesNativas import *
from datetime import datetime
from RevisionTipos import *
from VerificarDatos import *

class ExecOperacion():
    def __init__( self ,conectar,ts):
        self.conectar = conectar
        self.ts = ts 


    def ejecutar_operacion(self,operacion):
        if isinstance(operacion, aritmetica): return self.ejecutar_aritmetica(operacion)
        elif isinstance(operacion, logica): return self.ejecutar_logica(operacion)
        elif isinstance(operacion, relacional): return self.ejecutar_relacional(operacion)
        else:
           # errorsem.append('lo sentimos pero no es una operacion')
            return self.obtener_valor(operacion)
            
    def ejecutar_aritmetica(self,operacion):
        if operacion.operacion == arit.MAS :return self.obtener_valor(operacion.op1) + self.obtener_valor(operacion.op2)
        if operacion.operacion == arit.RES : return self.obtener_valor(operacion.op1) - self.obtener_valor(operacion.op2)
        if operacion.operacion == arit.POR : return self.obtener_valor(operacion.op1) * self.obtener_valor(operacion.op2)
        if operacion.operacion == arit.DIV : return self.obtener_valor(operacion.op1) / self.obtener_valor(operacion.op2)
     
        
        print('ejecuion de operacion aritmetica')
   
    def obtener_valor(self,expression):
        if isinstance(expression,aritmetica):
            return self.ejecutar_aritmetica(expression)
        elif isinstance(expression, numero):
            return int(expression.numero)
        elif isinstance(expression,numDecimal):
            return float(expression.numDec)
        elif isinstance(expression, numeroM):
            return -1*int(expression.numero)
        elif isinstance(expression,numDecimalM):
            return -1* float(expression.numDec)
        elif isinstance(expression,cadenaCaracter):
            return expression.cadC
        elif isinstance(expression,cadena):
            return expression.cad
        return None
    def ejecutar_logica(self,operacion):
        
        op1 =self.obtener_valor( operacion.op1)
        izq = False
        der = False
        if op1 ==1:
            izq =True
        elif op1 == 0:
            izq =False
        else:
            print('no se puede procesar la operacion logica izquierda')
            return 0

        #Operacion NOT
        if operacion.op2 == valido.invalido:
            return 1 if(izq==False) else 0
        else:
            op2 = self.obtener_valor(operacion.op2)
            if op2 ==1 :
                der =True
            elif op2 ==0:
                der = False
            else:
                errorsem.append('no se puede realizar la operacion logica derecha')
                return 0
            if operacion.operacion == logic.AND:
                return 1 if(izq or der) else 0
            elif operacion.operacion == logic.OR:
                return 1 if(izq or der ) else 0

    def ejecutar_relacional(self,operacion):
        try:
            op1 = self.obtener_valor(operacion.op1)
            op2 = self.obtener_valor(operacion.op2)

            if operacion.operacion == relac.II : return 1 if(op1==op2) else 0
            elif operacion.operacion == relac.NI : return 1 if(op1!=op2) else 0
            elif operacion.operacion == relac.MENI : return 1 if(op1<=op2) else 0
            elif operacion.operacion == relac.MAYI : return 1 if(op1>=op2) else 0
            elif operacion.operacion == relac.MAYOR : return 1 if(op1>op2) else 0
            elif operacion.operacion == relac.MENOR : return 1 if(op1<op2) else 0
        
        except:
            errorsem.append('no se puede realizar la operacion')