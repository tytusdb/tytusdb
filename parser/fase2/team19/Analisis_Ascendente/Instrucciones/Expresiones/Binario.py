import base64

from Analisis_Ascendente.Instrucciones.Expresiones.Math import Math_
from Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import Trigonometrica
from Analisis_Ascendente.Instrucciones.expresion import Primitivo
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class Binario(Instruccion):

    '''#1 LENGTH
       #2 SHA256
       #3 ENCODE
       #4 DECODE
       #5 SUBSTRING | SUBSTR
       #6 TRIM
       #7 GET_BYTE
       #8 SET_BYTE
       #9 CONVERT
       #10 GREATEST
       #11 LEAST '''

    def __init__(self, caso, valor1, valor2, valor3,fila,columna):
        self.caso = caso
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3
        self.fila = fila
        self.columna = columna

    def getC3D(self):
        code = ''
        if self.valor2 is not None:
            code += self.valor2 + '(' + self.valor1.valor
        return code

    def Resolver(bina,ts,Consola,exceptions):
        if isinstance(bina,Binario):
            if bina.valor2== 'LENGTH':
                return len(str(bina.valor1.valor))
            elif bina.valor2 == 'ENCODE':
                message_bytes = bina.valor1.valor.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')
                resultado = base64_message
                return resultado
            elif bina.valor2 == 'DECODE':
                message_bytes = bina.valor1.valor.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')
                resultado = base64_message
                return resultado
            elif bina.valor1 == 'GET_BYTE':
                return ord(str(bina.valor2)[int(bina.valor3): int(bina.valor3) + 1])
            elif bina.caso == 8:#set_byte
                resultado = None
                cadena =""
                cont=0
                for letra in str(bina.valor1):
                    if(cont==int(bina.valor2)):
                        cadena+= chr(bina.valor3)
                        cont +=1
                        continue
                    cadena += letra
                    cont +=1
                resultado= cadena
                return resultado
            elif bina.caso == 5:#substring
                return str(bina.valor1)[int(bina.valor2):int(bina.valor3)]



        elif isinstance(bina, Trigonometrica.Trigonometrica):
            return Trigonometrica.Trigonometrica.Resolver(bina, ts, Consola, exceptions)
        elif isinstance(bina, Math_):
            return Math_.Resolver(bina, ts, Consola, exceptions)
        elif isinstance(bina, Primitivo):
            return bina.valor1
        elif isinstance(bina, Binario):
            return Binario.Resolver(bina, ts, Consola, exceptions)

