import base64
import datetime
import hashlib
import time
from datetime import date

import tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import Math_
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import Trigonometrica
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.expresion import Primitivo, Id
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion, IdId
from currency_converter import CurrencyConverter

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

    def Resolver(bina,ts,Consola,exceptions):

        if isinstance(bina,Binario):
            print("estamos aqui")
            print(bina);
            print(bina.valor1)
            print(bina.valor2)
            if str(bina.valor2).upper() == 'LENGTH':
                return len(str(bina.valor1.valor))
            elif str(bina.valor2).upper() == 'ENCODE':
                message_bytes = bina.valor1.valor.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')
                resultado = base64_message
                return resultado
            elif str(bina.valor2).upper() == 'DECODE':
                message_bytes = bina.valor1.valor.encode('ascii')
                base64_bytes = base64.b64encode(message_bytes)
                base64_message = base64_bytes.decode('ascii')
                resultado = base64_message
                return resultado
            elif str(bina.valor2).upper() == 'SHA256':

                return hashlib.sha256(str(bina.valor1.valor).encode()).hexdigest()
            elif str(bina.valor1).upper() == 'GET_BYTE':
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
                retorno = Expresion.Expresion.Resolver(bina.valor1,ts,Consola,exceptions)
                return str(retorno)[int(bina.valor2):int(bina.valor3)]
            elif bina.caso == 9:
                print("Esto es un convert")
                try:
                    print("Tipo: ",bina.valor2.tipo)
                    if bina.valor2.tipo == 'INTEGER' or bina.valor2.tipo == 'SMALLINT':
                        return int(bina.valor1)
                    elif bina.valor2.tipo == 'DATE':
                        print(bina.valor1)
                        print(time.strftime(bina.valor1))
                        return str(time.strftime(bina.valor1))
                    elif bina.valor2.tipo == 'FLOAT':
                        return float(bina.valor1)
                    elif bina.valor2.tipo == 'MONEY':
                        return str("Q "+str(bina.valor1))






                except:
                    return None


        elif isinstance(bina, Trigonometrica.Trigonometrica):
            return Trigonometrica.Trigonometrica.Resolver(bina, ts, Consola, exceptions)
        elif isinstance(bina, Math_):
            return Math_.Resolver(bina, ts, Consola, exceptions)
        elif isinstance(bina, Primitivo):
            return bina.valor1
        elif isinstance(bina,Expresion.Expresion):
            return Expresion.Expresion.Resolver(bina ,ts,Consola,exceptions)
        elif isinstance(bina, Id):
            return bina.id
        elif isinstance(bina, IdId):
            return [bina.valor1,bina.valor2]

