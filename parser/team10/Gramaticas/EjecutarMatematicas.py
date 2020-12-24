from instruccion import *
from funcionesTS import *
from conexionDB import *
from expresiones import *
from VerificarDatos import *
from funcionesNativas import *
import numpy as np
import EjecutarOperacion  as ejec
import hashlib 


class MateFunction():
    def __init__( self ,conectar,ts):
        self.conectar = conectar
        self.ts = ts 
        self.aritexc =  ejec.ExecOperacion(self.conectar,self.ts)
    def procesar_funcion(self,funcion):
        if isinstance(funcion,aritmetica2):return self.ejecutar_funop(funcion.operacion)
    
    def ejecutar_funop(self,operacion):
        if isinstance(operacion, funcionextra): return self.ejecutar_mat1(operacion.funcion)
        elif isinstance(operacion,funcionextra2): return self.ejecutar_trigo(operacion.funcion)
        elif isinstance(operacion,funcionextra3): return self.ejecutar_binary(operacion.funcion)
    def ejecutar_mat1(self, funcion):
        if isinstance(funcion, mathfunctions):
            if funcion.funcion == 'abs':
                try:
                    return abs(self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    print('error al convertir valores ')
                    return 0
            if funcion.funcion == 'cbrt':
                try:
                    return self.aritexc.ejecutar_operacion(funcion.op1)**(1./3.)
                except:
                    print('error al convertir valores ')
                    return 0
            if funcion.funcion =='ceil':
                try:
                    return np.ceil( self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    print('error al convertir valores ')
                    return 0
            if funcion.funcion =='celing':
                try:
                    return np.ceil( self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    print('error al convertir valores ')
                    return 0
            if funcion.funcion =='degrees':
                try:
                    return np.degrees( self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    print('error al convertir valores ')
                    return 0
            if funcion.funcion =='exp':
                try:
                    return np.exp( self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    print('error al convertir valores ')
                    return 0
            if funcion.funcion =='factorial':
                try:
                    return np.factorial( self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    errorsem.append('error al convertir valores ')
                    return 0
            if funcion.funcion =='floor':
                try:
                    return np.floor( self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    errorsem.append('error al convertir valores ')
                    return 0
            if funcion.funcion =='ln':
                try:
                    return np.ln( self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    errorsem.append('error al convertir valores ')
                    return 0
            if funcion.funcion =='log':
                try:
                    return np.log10( self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    errorsem.append('error al convertir valores ')
                    return 0
            if funcion.funcion =='radians':
                try:
                    return np.radians( self.aritexc.ejecutar_operacion(funcion.op1))
                except:
                    errorsem.append('error al convertir valores ')
                    return 0
            if funcion.funcion =='sign':
                try:
                    valor = self.aritexc.ejecutar_operacion(funcion.op1)
                    return  -1 if (valor<0) else 1
                except:
                    errorsem.append('error al convertir valores ')
                    return 0
    def ejecutar_trigo(self, funcion):
        if funcion.funcion =='acos':
            try:
                
                return np.acos( self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en acos ')
                return 0
        elif funcion.funcion =='acosd':
            try:
                return np.acosd( self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en acosd ')
                return 0
        elif funcion.funcion =='asin':
            try:
                return np.asin( self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en asin ')
                return 0
        elif funcion.funcion =='asind':
            try:
                return np.asind( self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en asind ')
                return 0
        elif funcion.funcion =='atan':
            try:
                 return np.atan( self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores ')
                return 0
        elif funcion.funcion =='atand':
            try:
                return np.atand(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores atand ')
                return 0
        elif funcion.funcion =='atan2':
            try:
                return np.atan2(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en atan2 ')
                return 0
        elif funcion.funcion =='cos':
            try:
                return np.cos(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en cos ')
                return 0
        elif funcion.funcion =='cosd':
            try:
               return np.cosd(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores cosd cosd')
                return 0
        elif funcion.funcion =='cot':
            try:
                return np.cot(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores cot')
                return 0
        elif funcion.funcion =='cotd':
            try:
                return np.cotd(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en cotd ')
                return 0
        elif funcion.funcion =='sin':
            try:
                 return np.sin(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en sin ')
                return 0
        elif funcion.funcion =='sind':
            try:
                return np.sind(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en sind ')
                return 0
        elif funcion.funcion =='tan':
            try:
                 return np.tan(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en tan ')
                return 0
        elif funcion.funcion =='tand':
            try:
                return np.tand(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en tand')
                return 0
        elif funcion.funcion =='sinh':
            try:
                return np.sinh(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en sinh')
                return 0
        elif funcion.funcion =='cosh':
            try:
                 return np.cosh(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en cosh ')
                return 0
        elif funcion.funcion =='tanh':
            try:
                return np.tanh(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en tanh ')
                return 0
        elif funcion.funcion =='asinh':
            try:
                return np.asinh(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en asinh')
                return 0
        elif funcion.funcion =='acosh':
            try:
                return np.acosh(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en acosh ')
                return 0
        elif funcion.funcion =='atanh':
            try:
                return np.atanh(self.aritexc.ejecutar_operacion(funcion.op1))
            except:
                errorsem.append('error al convertir valores en atanh ')
                return 0

    def ejecutar_binary(self, funcion):
        #validar si instancia es binarystring2 hacer esto
        if isinstance(funcion, binarystring2):
            valores =''
            if isinstance(funcion.operacion,cadenaCaracter):
                try:
                    valores = self.aritexc.ejecutar_operacion(funcion.operacion).replace('\'','')
                except:
                   errorsem.append('error conversion cadena ')
            else:
                try:
                    valores = self.aritexc.ejecutar_operacion(funcion.operacion).replace('\"','')
                except:
                   errorsem.append('error conversion cadena ')

            if funcion.funcion =='trim':
           
                    return valores.lstrip()
               
            elif funcion.funcion =='md5':
               
                    valores = hashlib.md5(valores.encode('utf-8'))
                    return valores.hexdigest()
               
            if funcion.funcion =='sha256':
        
                    valores = hashlib.sha256(valores.encode('utf-8'))
                    return valores.hexdigest()
               
            if funcion.funcion =='length':
                
                    return len(valores)
        # elif isinstance(funcion,binarystring3):
