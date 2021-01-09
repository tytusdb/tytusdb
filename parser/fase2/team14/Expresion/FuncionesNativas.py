from Expresion.LlamadaFuncion import LLamadaFuncion
from Expresion.Terminal import *

import hashlib
import base64
from reportes import *
from Tipo import Tipo


class FuncionesNativas(Expresion):
    '''
        Esta clase representa la Expresión Binaria.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, identificador, expresiones):
        Expresion.__init__(self)
        self.identificador = identificador
        self.expresiones = expresiones



        # print("en funci==========",self.identificador,self.expresiones[0])

    def getval(self, entorno):
        # print("++++++++++++++++++")
        if self.expresiones != None:
            sizeparametro = len(self.expresiones)
            funcion = self.identificador.lower()
            i = 0
            ''' for param in self.expresiones:
                if str(self.identificador).lower() == 'convert':
                    self.stringsql += self.expresiones[i].stringsql + ' as ' + self.expresiones[i].getTipo(entorno)
                else:
                    if (i == 0):
                        self.stringsql += str(param.getval(entorno).valor)
                    else:
                        self.stringsql += ', ' + str(param.getval(entorno).valor)
                i = i + 1
            self.stringsql += ')' '''

        # print("aqqqqqqqqqqqqq")
        try:
            # print("retornamos el id")
            if (funcion == "abs" or funcion == "cbrt" or funcion == "ceil" or funcion == "ceiling" or
                    funcion == "degrees" or funcion == "exp" or funcion == "factorial" or funcion == "floor" or
                    funcion == "ln" or funcion == "log" or funcion == "radians" or funcion == "sign" or
                    funcion == "trunc" or funcion == "acos" or funcion == "acosd" or funcion == "asin" or
                    funcion == "asind" or funcion == "atan" or funcion == "atand" or funcion == "cos" or
                    funcion == "cosd" or funcion == "cot" or funcion == "cotd" or funcion == "sin" or
                    funcion == "sind" or funcion == "tan" or funcion == "tand" or funcion == "sinh" or
                    funcion == "cosh" or funcion == "tanh" or funcion == "asinh" or funcion == "acosh" or
                    funcion == "atanh" or funcion == 'sqrt'
            ):
                valexpresion = self.expresiones[0].getval(entorno).valor
                return self.FunctionWithOneParameter(funcion, sizeparametro, valexpresion)
            elif (funcion == "div" or funcion == "gcd" or funcion == "mod" or funcion == "power" or
                  funcion == "round" or funcion == "atan2" or funcion == "atan2d"
            ):
                val1expresion = self.expresiones[0].getval(entorno).valor
                val2expresion = self.expresiones[1].getval(entorno).valor
                return self.FunctionWithTwoParameter(funcion, sizeparametro, val1expresion, val2expresion)
            elif (funcion == "width_bucket"):
                val1expresion = self.expresiones[0].getval(entorno).valor
                val2expresion = self.expresiones[1].getval(entorno).valor
                val3expresion = self.expresiones[2].getval(entorno).valor
                val4expresion = self.expresiones[3].getval(entorno).valor
                return self.FunctionWithBucket(funcion, sizeparametro, val1expresion, val2expresion, val3expresion,
                                               val4expresion)
        except:
            return "Error: La función: " + funcion + " solo recibe valores númericos"

        if (
                funcion == "length" or funcion == "md5" or funcion == "sha256" or funcion == "convert" or funcion == "trim"):
            valexpresion = self.expresiones[0].getval(entorno).valor
            t = 0
            for tam in self.expresiones:
                t = t + 1

            if (funcion == "trim" and t == 2):
                val1expresion = self.expresiones[1].getval(entorno).valor
                return self.FunctionWithTwoParameter(funcion, sizeparametro, valexpresion, val1expresion)

            # print(valexpresion,'valooooor')
            r = self.FunctionWithOneParameter(funcion, sizeparametro, valexpresion)
            r.stringsql = self.stringsql
            return r
        elif (
                funcion == "get_byte" or funcion == "set_byte" or funcion == "encode" or funcion == "decode" or funcion == "date_part"):
            val1expresion = self.expresiones[0].getval(entorno).valor
            val2expresion = self.expresiones[1].getval(entorno).valor
            return self.FunctionWithTwoParameter(funcion, sizeparametro, val1expresion, val2expresion)

        elif (funcion == "substr" or funcion == "substring"):
            val1expresion = self.expresiones[0].getval(entorno).valor
            val2expresion = self.expresiones[1].getval(entorno).valor
            val3expresion = self.expresiones[2].getval(entorno).valor
            return self.FunctionWithTreeParameter(funcion, sizeparametro, val1expresion, val2expresion, val3expresion)
        else:
            llam = LLamadaFuncion(self.identificador, self.expresiones)
            return llam.getval(entorno)
            # reporteerrores.append(Lerrores("Error Semantico", "La funcion" + funcion + "no existe", 0, 0))
            # return "Error: La función: " + funcion + " no existe"

    def FunctionWithOneParameter(self, funcion, parametros, exp):
        result = None
        if (parametros == 1):
            if (funcion == "abs"):
                if (exp < 0):
                    return Terminal(Tipo('numeric', exp * -1, self.l(exp * -1), -1), exp * -1)

                else:
                    return Terminal(Tipo('numeric', exp, self.l(exp), -1), exp)

            elif (funcion == "cbrt"):
                return Terminal(Tipo('decimal', math.pow(exp, 3), self.l(math.pow(exp, 3)), -1), math.pow(exp, 3))

            elif (funcion == "ceil"):
                return Terminal(Tipo('numeric', math.ceil(exp), self.l(math.ceil(exp)), -1), math.ceil(exp))

            elif (funcion == "ceiling"):
                return Terminal(Tipo('numeric', math.ceil(exp), self.l(math.ceil(exp)), -1), math.ceil(exp))

            elif (funcion == "degrees"):
                return Terminal(Tipo('decimal', math.degrees(exp), self.l(math.degrees(exp)), -1), math.degrees(exp))

            elif (funcion == "exp"):
                return Terminal(Tipo('numeric', math.exp(exp), self.l(math.exp(exp)), -1), math.exp(exp))

            elif (funcion == "factorial"):

                return Terminal(Tipo('numeric', math.factorial(exp), self.l(math.factorial(exp)), -1),
                                math.factorial(exp))

            elif (funcion == "floor"):

                return Terminal(Tipo('integer', math.floor(exp), self.l(math.floor(exp)), -1), math.floor(exp))

            elif (funcion == "ln"):
                return Terminal(Tipo('decimal', math.log(exp), self.l(math.log(exp)), -1), math.log(exp))


            elif (funcion == "log"):
                return Terminal(Tipo('decimal', math.log10(exp), self.l(math.log10(exp)), -1), math.log10(exp))

            elif (funcion == "radians"):
                return Terminal(Tipo('decimal', math.radians(exp), self.l(math.radians(exp)), -1), math.radians(exp))

            elif (funcion == "sign"):
                if (exp > 0):
                    return Terminal(Tipo('integer', 1, self.l(1), -1), 1)

                else:
                    return Terminal(Tipo('integer', -1, self.l(-1), -1), -1)

            elif (funcion == "sqrt"):
                return Terminal(Tipo('decimal', math.sqrt(exp), self.l(math.sqrt(exp)), -1), math.sqrt(exp))

            elif (funcion == "trunc"):
                return Terminal(Tipo('numeric', math.trunc(exp), self.l(math.trunc(exp)), -1), math.trunc(exp))

            elif (funcion == "acos"):

                return Terminal(Tipo('decimal', math.acos(exp), self.l(math.acos(exp)), -1), math.acos(exp))

            elif (funcion == "acosd"):
                return Terminal(Tipo('decimal', math.degrees(math.acos(exp)), self.l(math.degrees(math.acos(exp))), -1),
                                math.degrees(math.acos(exp)))

            elif (funcion == "asin"):
                return Terminal(Tipo('decimal', math.asin(exp), self.l(math.asin(exp)), -1), math.asin(exp))

            elif (funcion == "asind"):
                return Terminal(Tipo('decimal', math.degrees(math.asin(exp)), self.l(math.degrees(math.asin(exp))), -1),
                                math.degrees(math.asin(exp)))

            elif (funcion == "atan"):
                return Terminal(Tipo('decimal', math.atan(exp), self.l(math.atan(exp)), -1), math.atan(exp))

            elif (funcion == "atand"):
                return Terminal(Tipo('decimal', math.degrees(math.atan(exp)), self.l(math.degrees(math.atan(exp))), -1),
                                math.degrees(math.atan(exp)))

            elif (funcion == "cos"):
                return Terminal(Tipo('decimal', math.cos(exp), self.l(math.cos(exp)), -1), math.cos(exp))

            elif (funcion == "cosd"):
                return Terminal(Tipo('decimal', math.degrees(math.cos(exp)), self.l(math.degrees(math.cos(exp))), -1),
                                math.degrees(math.cos(exp)))

            elif (funcion == "cot"):
                return Terminal(Tipo('decimal', (1 / math.tan(exp)), self.l((1 / math.tan(exp))), -1),
                                (1 / math.tan(exp)))

            elif (funcion == "cotd"):
                return Terminal(
                    Tipo('decimal', math.degrees(1 / math.tan(exp)), self.l(math.degrees(1 / math.tan(exp))), -1),
                    math.degrees(1 / math.tan(exp)))

            elif (funcion == "sin"):

                return Terminal(Tipo('decimal', math.sin(exp), self.l(math.sin(exp)), -1), math.sin(exp))

            elif (funcion == "sind"):

                return Terminal(Tipo('decimal', math.degrees(math.sin(exp)), self.l(math.degrees(math.sin(exp))), -1),
                                math.degrees(math.sin(exp)))

            elif (funcion == "sin"):
                return Terminal(Tipo('decimal', math.sin(exp), self.l(math.sin(exp)), -1), math.sin(exp))

            elif (funcion == "sind"):
                return Terminal(Tipo('decimal', math.degrees(math.sin(exp)), self.l(math.degrees(math.sin(exp))), -1),
                                math.degrees(math.sin(exp)))

            elif (funcion == "tan"):
                return Terminal(Tipo('decimal', math.tan(exp), self.l(math.tan(exp)), -1), math.tan(exp))

            elif (funcion == "tand"):
                return Terminal(Tipo('decimal', math.degrees(math.tan(exp)), self.l(math.degrees(math.tan(exp))), -1),
                                math.degrees(math.tan(exp)))

            elif (funcion == "sinh"):
                return Terminal(Tipo('decimal', math.sinh(exp), self.l(math.sinh(exp)), -1), math.sinh(exp))

            elif (funcion == "cosh"):
                return Terminal(Tipo('decimal', math.cosh(exp), self.l(math.cosh(exp)), -1), math.cosh(exp))

            elif (funcion == "tanh"):
                return Terminal(Tipo('decimal', math.tanh(exp), self.l(math.tanh(exp)), -1), math.tanh(exp))

            elif (funcion == "asinh"):
                return Terminal(Tipo('decimal', math.asinh(exp), self.l(math.asinh(exp)), -1), math.asinh(exp))

            elif (funcion == "acosh"):
                return Terminal(Tipo('decimal', math.acosh(exp), self.l(math.acosh(exp)), -1), math.acosh(exp))

            elif (funcion == "atanh"):

                return Terminal(Tipo('decimal', math.atanh(exp), self.l(math.atanh(exp)), -1), math.atanh(exp))

            elif (funcion == "length"):
                self.leng = len(exp)
                return Terminal(Tipo('smallint', self.leng, self.l(self.leng), -1), self.leng)

            elif (funcion == "md5"):
                m = exp
                result = hashlib.md5(m.encode())
                return Terminal(Tipo('varchar', result.hexdigest(), self.l(result.hexdigest()), -1), result.hexdigest())
            elif (funcion == "sha256"):
                m = exp
                result = hashlib.sha256(m.encode()).hexdigest()
                return Terminal(Tipo('decimal', result, self.l(result), -1), result)

            elif (funcion == "convert"):
                return self.expresiones[0]

            elif (funcion == "trim"):
                trim = exp.strip()
                return Terminal(Tipo('varchar', trim, self.l(trim), -1), trim)




        else:
            reporteerrores.append(
                Lerrores("Error Semantico", "La funcion" + funcion + "solo recibe 2 parametros", 0, 0))
            return "Error: La funcion: " + funcion + " recibe un parametro"

    def FunctionWithTwoParameter(self, funcion, parametros, exp1, exp2):
        if (parametros == 2):
            if (funcion == "div"):

                return Terminal(Tipo('decimal', exp1 / exp2, self.l(exp1 / exp2), -1), exp1 / exp2)

            elif (funcion == "gcd"):
                return Terminal(Tipo('integer', math.gcd(exp1, exp2), self.l(math.gcd(exp1, exp2)), -1),
                                math.gcd(exp1, exp2))


            elif (funcion == "mod"):
                return Terminal(Tipo('integer', exp1 % exp2, self.l(exp1 % exp2), -1), exp1 % exp2)

            elif (funcion == "power"):
                return Terminal(Tipo('decimal', math.pow(exp1, exp2), self.l(math.pow(exp1, exp2)), -1),
                                math.pow(exp1, exp2))

            elif (funcion == "round"):
                return Terminal(Tipo('decimal', round(exp1, exp2), self.l(round(exp1, exp2)), -1), round(exp1, exp2))

            elif (funcion == "atan2"):
                return Terminal(Tipo('decimal', math.atan(exp1 / exp2), self.l(math.atan(exp1 / exp2)), -1),
                                math.atan(exp1 / exp2))

            elif (funcion == "atan2d"):
                return Terminal(
                    Tipo('decimal', math.degrees(math.atan(exp1 / exp2)), self.l(math.atan(exp1 / exp2)), -1),
                    math.degrees(math.atan(exp1 / exp2)))

            elif (funcion == "encode"):
                if (exp2.lower() == "base64"):
                    cascci = exp1.encode('ascii')
                    codificado = base64.b64encode(cascci)
                    return Terminal(Tipo('varchar', codificado.decode('utf-8'), self.l(codificado.decode('utf-8')), -1),
                                    codificado.decode('utf-8'))

                elif (exp2.lower() == "hex"):
                    cascci = exp1.encode('utf-8')
                    codificado = base64.b16encode(cascci)
                    return Terminal(Tipo('varchar', codificado.decode('utf-8'), self.l(codificado.decode('utf-8')), -1),
                                    codificado.decode('utf-8'))

                elif (exp2.lower() == "escape"):
                    codificado = exp1.encode('unicode_escape').decode('utf-8')
                    return Terminal(Tipo('varchar', codificado, self.l(codificado), -1), codificado)

            elif (funcion == "decode"):
                if (exp2.lower() == "base64"):
                    codificado = base64.b64decode(exp1)
                    return Terminal(Tipo('varchar', codificado.decode('utf-8'), self.l(codificado.decode('utf-8')), -1),
                                    codificado.decode('utf-8'))

                elif (exp2.lower() == "hex"):
                    codificado = base64.b16decode(exp1)

                    return Terminal(Tipo('varchar', codificado.decode('utf-8'), self.l(codificado.decode('utf-8')), -1),
                                    codificado.decode('utf-8'))

                elif (exp2.lower() == "escape"):
                    codificado = exp1.encode('utf-8').decode('unicode_escape')

                    return Terminal(Tipo('varchar', codificado, self.l(codificado), -1), codificado)

            elif (funcion == "date_part"):
                datepart = Date_Part(exp1, exp2)
                datepart = datepart.getval()

                return Terminal(Tipo('integer', datepart, self.l(datepart), -1), datepart)

            elif (funcion == "trim"):
                print('exp', exp2)
                trim = exp1.strip(exp2)
                return Terminal(Tipo('varchar', trim, self.l(trim), -1), trim)


        else:

            reporteerrores.append(
                Lerrores("Error Semantico", "La funcion" + funcion + "solo recibe 2 parametros", 0, 0))
            return "Error: La funcion: " + funcion + " recibe 2 parametro"

    def FunctionWithTreeParameter(self, funcion, parametros, exp1, exp2, exp3):
        if (parametros == 3):
            if (funcion == "substring"):
                inicio = exp2 - 1
                fin = inicio + exp3
                sub = exp1[inicio:fin]
                return Terminal(Tipo('decimal', sub, self.l(sub), -1), sub)

            elif (funcion == "substr"):
                inicio = exp2 - 1
                fin = inicio + exp3
                sub = exp1[inicio:fin]
                return Terminal(Tipo('decimal', sub, self.l(sub), -1), sub)
        else:
            reporteerrores.append(
                Lerrores("Error Semantico", "La funcion" + funcion + "solo recibe 3 parametros", 0, 0))
            return "Error: La funcion: " + funcion + " recibe 3 parametro"

    def FunctionWithBucket(self, funcion, parametros, exp1, exp2, exp3, exp4):
        if (parametros == 4):
            if (exp1 < exp2 or exp1 > exp3):
                reporteerrores.append(
                    Lerrores("Error Semantico", "Valor" + str(exp1) + "no se encuentra en el rango", 0, 0))
                return "Error: El valor: " + str(exp1) + " no esta en el rango de: (" + str(exp2) + "," + str(
                    exp3) + ")"
            else:
                contador = 1
                for x in range(exp2, exp3):
                    contador = contador + 1

                columnas = int(contador / exp4)
                inicio = int(exp2)
                final = int(exp2) + (columnas)
                posbucket = 0
                for fila in range(0, exp4):
                    for valores in range(inicio, final):
                        if (exp1 == valores):
                            posbucket = fila + 1
                            msg = "El valor de: " + str(exp1) + " esta en el bucket: " + str(posbucket)
                            tipo = Tipo('varchar', self.l(msg), -1, -1)
                            return Terminal(tipo, msg)
                    inicio = final
                    final = final + columnas
        else:
            reporteerrores.append(
                Lerrores("Error Semantico", "La funcion" + funcion + "solo recibe 2 parametros", 0, 0))
            return "Error: La funcion: " + funcion + " recibe 4 parametro"

    def l(self, valor):
        if type(valor) not in (int, float, complex):
            return len(valor)
        else:
            return len(str(valor))

    def traducir(self, entorno):
        if self.expresiones != None:
            self.stringsql = self.identificador + '('
            i = 0
            for i in range(0, len(self.expresiones), 1):
                if str(self.identificador).lower() == 'convert':
                    self.stringsql += '\'' + self.expresiones[i].traducir(entorno).stringsql + '\' as ' + self.expresiones[i].tipo.tipo
                else:
                    if (i == 0):
                        self.stringsql += self.expresiones[i].traducir(entorno).stringsql
                    else:
                        self.stringsql += ', ' + self.expresiones[i].traducir(entorno).stringsql
                i = i + 1
            self.stringsql += ')'
        try:
            self.temp = self.getval(entorno,0).valor
            return self
        except:
            self.temp=self.stringsql
            return self


class Date_Part(FuncionesNativas):
    'This is an abstract class'

    def __init__(self, field=None, interval=None):
        self.field = field
        self.interval = interval

    def getval(self, entorno=None):
        'spliteo el timestamp'
        splited = self.interval.split(' ')
        cont = 0
        for contenido in splited:
            if contenido == self.field:
                return splited[cont - 1]
            cont = cont + 1
        return None