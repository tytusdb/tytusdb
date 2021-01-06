import base64
import datetime
import hashlib
import time
from datetime import date

import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import Math_
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import Trigonometrica
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import Primitivo, Id
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion, IdId
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones import IdAsId
#from currency_converter import CurrencyConverter

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


    def traducir(bina, ts, consola, exception, tv, regla, antes, optimizado, ID):
        if bina.caso >= 1 and bina.caso <= 5:
            e = Expresion.Expresion.traducir(bina.valor1, ts, consola, exception, tv, regla, antes, optimizado, ID)
            if bina.caso == 1: #'LENGTH'
                temp1 = tv.Temp()
                consola.append(f'\t{temp1} = str({e})\n')
                temp2 = tv.Temp()
                consola.append(f'\t{temp2} = len({temp1})\n')
                return temp2
            elif bina.caso == 3: #'ENCODE'
                message_bytes = tv.Temp()
                consola.append(f'\t{message_bytes} = {e}.encode(\'ascii\')\n')
                #message_bytes = bina.valor1.valor.encode('ascii')
                base64_bytes = tv.Temp()
                consola.append(f'\t{base64_bytes} = base64.b64encode({message_bytes})\n')
                #base64_bytes = base64.b64encode(message_bytes)
                base64_message = tv.Temp()
                consola.append(f'\t{base64_message} = {base64_bytes}.decode(\'ascii\')\n')
                #base64_message = base64_bytes.decode('ascii')
                resultado = tv.Temp()
                consola.append(f'\t{resultado} = {base64_message}')
                #resultado = base64_message
                return resultado
            elif bina.caso == 4: #'DECODE'
                message_bytes = tv.Temp()
                consola.append(f'\t{message_bytes} = {e}.encode(\'ascii\')\n')
                #message_bytes = bina.valor1.valor.encode('ascii')
                base64_bytes = tv.Temp()
                consola.append(f'\t{base64_bytes} = base64.b64encode({message_bytes})\n')
                #base64_bytes = base64.b64encode(message_bytes)
                base64_message = tv.Temp()
                consola.append(f'\t{base64_message} = {base64_bytes}.decode(\'ascii\')\n')
                #base64_message = base64_bytes.decode('ascii')
                resultado = tv.Temp()
                consola.append(f'\t{resultado} = {base64_message}')
                #resultado = base64_message
                return resultado
            elif bina.caso == 2: #'SHA256'
                temp1 = tv.Temp()
                consola.append(f'\t{temp1} = str({e})\n')
                temp2 = tv.Temp()
                consola.append(f'\t{temp2} = {temp1}.encode()\n')
                temp3 = tv.Temp()
                consola.append(f'\t{temp3} = hashlib.sha256({temp2})\n')
                temp4 = tv.Temp()
                consola.append(f'\t{temp4} = {temp3}.hexdigest()\n')
                return temp4
            elif bina.caso == 5: #'SUBSTRING'
                temp1 = tv.Temp()
                consola.append(f'\t{temp1} = str({e})\n')
                inicio = bina.valor2
                if inicio == 1:
                    inicio = 0
                final = bina.valor3
                temp2 = tv.Temp()
                consola.append(f'\t{temp2} = {temp1}[{inicio}:{final}]\n')
                return temp2

        elif bina.caso == 9:
            print("Esto es un convert")
            try:
                print("Tipo: ", bina.valor2.tipo)
                if bina.valor2.tipo == 'INTEGER' or bina.valor2.tipo == 'SMALLINT':
                    e = Expresion.Expresion.traducir(bina.valor1, ts, consola, exception, tv, regla, antes, optimizado, ID)
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = int({e})\n')
                    return temp
                elif bina.valor2.tipo == 'DATE':
                    e = Expresion.Expresion.traducir(bina.valor1, ts, consola, exception, tv, regla, antes, optimizado, ID)
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = time.strftime({e})\n')
                    temp2 = tv.Temp()
                    consola.append(f'\t{temp2} = str({temp})\n')
                    return temp2
                elif bina.valor2.tipo == 'FLOAT':
                    e = Expresion.Expresion.traducir(bina.valor1, ts, consola, exception, tv, regla, antes, optimizado, ID)
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = float({e})\n')
                    return temp
                elif bina.valor2.tipo == 'MONEY':
                    e = Expresion.Expresion.traducir(bina.valor1, ts, consola, exception, tv, regla, antes, optimizado, ID)
                    temp = tv.Temp()
                    consola.append(f'\t{temp} = str({e})\n')
                    temp2 = tv.Temp()
                    consola.append(f'\t{temp2} = "Q " + {temp}\n')
                    return temp2
            except:
                return ''

        elif bina.caso == 7: #'GET_BYTE'
            e = Expresion.Expresion.traducir(bina.valor2, ts, consola, exception, tv, regla, antes, optimizado, ID)
            temp1 = tv.Temp()
            consola.append(f'\t{temp1} = str({e})\n')
            e2 = Expresion.Expresion.traducir(bina.valor3, ts, consola, exception, tv, regla, antes, optimizado, ID)
            temp2 = tv.Temp()
            consola.append(f'\t{temp2} = int({e2})\n')
            temp3 = tv.Temp()
            consola.append(f'\t{temp3} = {temp2} + 1\n')
            temp4 = tv.Temp()
            consola.append(f'\t{temp4} = {temp1}[{temp2}:{temp3}]\n')
            temp5 = tv.Temp()
            consola.append(f'\t{temp5} = ord({temp4})\n')
            return temp5
            #ord(str(bina.valor2)[int(bina.valor3): int(bina.valor3) + 1])
        #falta set byte
        elif bina.caso == 8:
            print('en set byte')
            t = Binario.Resolver(bina, ts, consola, exception)
            temp = tv.Temp()
            consola.append(f'\t{temp} = \'{t}\'\n')
            return temp

    def ObtenerCadenaEntrada(bina,condicion):

        if isinstance(bina,Binario):
            if(bina.valor3==None) and bina.caso<=4:
                tipo = str(bina.valor2)
                Exp= Binario.ObtenerCadenaEntrada(bina.valor1,condicion)

                return ' '+tipo +' ( '+Exp+' ) '
            elif bina.caso == 5:
                tipo = ' SUBSTR (' #PARIZQ E COMA ENTERO COMA ENTERO PARDR
                Exp1= Binario.ObtenerCadenaEntrada(bina.valor1,condicion)
                Exp2= str(bina.valor2)
                Exp3= str(bina.valor3)

                return tipo+Exp1+', '+Exp2+', '+Exp3+' )'
            elif bina.caso == 6:
                tipo = ' TRIM ( '  # TRIM PARIZQ CADENA FROM columna PARDR
                Exp1 = ' \''+bina.valor1+'\' '
                columna = str(Binario.ObtenerCadenaEntrada(bina.valor2,condicion))

                return tipo + Exp1 + ' FROM ' + columna+' )'
            elif bina.caso == 7:  #GET_BYTE PARIZQ CADENA COMA ENTERO PARDR
                tipo = str(bina.valor1) + ' ( '
                cadena = ' \''+str(bina.valor2)+'\' '
                entero = str(bina.valor3)+' ) '

                return tipo +cadena+' , '+entero
            elif bina.caso==8: #SET_BYTE PARIZQ CADENA COMA ENTERO COMA ENTERO PARDR
                tipo = 'SET_BYTE ( '
                cadena= ' \''+str(bina.valor1)+'\' '
                ent1 = str(bina.valor2)
                ent2 = str(bina.valor3)+' ) '

                return tipo + cadena+' , '+ent1+' , '+ent2
            elif bina.caso==9:  #CONVERT PARIZQ CADENA AS tipo PARDR
                tipo = 'CONVERT ( '
                cadena= ' \''+str(bina.valor1)+'\' AS '
                tipo2= str(bina.valor2.tipo)+' ) '

                return tipo+cadena+tipo2
            elif bina.caso==10: #GREATEST PARIZQ listaValores PARDR
                tipo = 'GREATEST ( '
                lista_valores = str(Binario.ObtenerCadenaEntrada(bina.valor1,condicion)) +' ) '

                return tipo + lista_valores
            elif bina.caso == 11:  # LEAST PARIZQ listaValores PARDR
                tipo = 'LEAST ( '
                lista_valores = str(Binario.ObtenerCadenaEntrada(bina.valor1,condicion)) + ' ) '

                return tipo + lista_valores

        elif isinstance(bina, Trigonometrica):
            return Trigonometrica.obtenerCadenaEntrada(bina,condicion)
        elif isinstance(bina, Math_):
            return Math_.obtenerCadenaEntrada(bina,condicion)
        elif isinstance(bina, Primitivo):
            return Primitivo.ObtenerCadenaEntrada(bina)
        elif isinstance(bina,Expresion.Expresion):
            return Expresion.Expresion.ObtenerCadenaEntrada(bina,condicion )
        elif isinstance(bina, Id):
            return str(bina.id)
        elif isinstance(bina, IdId):
            return str(IdId.ObtenerCadenaEntrada(bina))
        elif isinstance(bina, IdAsId.IdAsId):
            return str(IdAsId.IdAsId.ObtenerCadenaEntrada(bina,condicion))
        elif isinstance(bina,list):
            valores = ''
            cont = 0
            for val in bina:
                if isinstance(val, Primitivo):
                    valores += Primitivo.ObtenerCadenaEntrada(val)
                cont += 1
                if cont < len(bina):
                    valores += ', '
                else:
                    valores += ' '
            return valores


