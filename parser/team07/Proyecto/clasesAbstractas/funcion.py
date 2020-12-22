import math
import random
from tabla_Simbolos import simbolo
from tabla_Simbolos import simboloColumna
from .instruccionAbstracta import InstruccionAbstracta


class funcion(InstruccionAbstracta):

    def __init__(self):
        pass

    def funcionTimeExtract(self, VarTime, TipoTiempo, CadenaTiempo):
        self.VarTime = VarTime
        self.TipoTiempo = TipoTiempo
        self.CadenaTiempo = CadenaTiempo

    def funcionTimeDatePart(self, CadenaPart, TipoTiempo, CadenaTiempo):
        self.CadenaPart = CadenaTiempo
        self.TipoTiempo = TipoTiempo
        self.CadenaTiempo = CadenaTiempo

    def funcionTiempoPredefinido(self, TipoLlamada):
        self.TipoLlamada = TipoLlamada

    def funcionMateUnitaria(self, TipoFuncion, Parametro):
        self.TipoFuncion = TipoFuncion
        self.Parametro = Parametro

    def funcionMateBinaria(self, TipoFuncion, Param1, Param2):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2

    def funcionMateWidthBucket(self, TipoFuncion, Param1, Param2, Param3, Param4):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2
        self.Param3 = Param3
        self.Param4 = Param4

    def funcionTrigonometricaUnitaria(self, TipoFuncion, Parametro):
        self.TipoFuncion = TipoFuncion
        self.Parametro = Parametro

    def funcionTrigonometricaBinaria(self, TipoFuncion, Param1, Param2):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2

    def funcionBinariaStrUnitaria(self, TipoFuncion, Parametro):
        self.TipoFuncion = TipoFuncion
        self.Parametro = Parametro
    
    def funcionTrigonometricaBinaria(self, TipoFuncion, Param1, Param2):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2

    def funcionTrigonometricaTriple(self, TipoFuncion, Param1, Param2, Param3):
        self.TipoFuncion = TipoFuncion
        self.Param1 = Param1
        self.Param2 = Param2
        self.Param3 = Param3

    def funcionExprecion(self, TipoFuncion, ListaFunciones):
        self.TipoFuncion = TipoFuncion
        self.ListaFunciones = ListaFunciones

    def funcionAgregacion(self, TipoFuncion, Parametro):
        self.TipoFuncion = TipoFuncion
        self.parametro = Parametro

    def ejecutar(self, tabalSimbolos, listaErrores):
#----------------------------------------------------------FUNCIONES MATEMATICAS----------------------------------------------------------

        if str.lower(self.TipoFuncion.valor) == "abs":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = abs(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "cbrt":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = Res.valorRetorno ** (1/3)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "ceil":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.ceil(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "ceiling":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.ceil(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "degrees":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.degrees(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "div":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            Res2 = self.Param2.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = Res.valorRetorno / Res2.valorRetorno
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "exp":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.exp(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "factorial":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.factorial(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "floor":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.floor(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "gcd":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            Res2 = self.Param2.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.gcd(Res.valorRetorno, Res2.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "ln":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.log(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "log":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.log10(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "mod":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            Res2 = self.Param2.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = Res.valorRetorno % Res2.valorRetorno
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "pi":
            simboloRetornar = simbolo.Simbolo()
            simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.double_precision, float(math.pi))
            return simboloRetornar

        elif str.lower(self.TipoFuncion.valor) == "power":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            Res2 = self.Param2.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = Res.valorRetorno ** Res2.valorRetorno
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "radians":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.radians(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "round":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            Res2 = self.Param2.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = round(Res.valorRetorno, Res2.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "sign":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                if Res.valorRetorno > 0:
                    simboloRetornar = simbolo.Simbolo()
                    simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.double_precision, int(1))
                    return simboloRetornar
                else:
                    simboloRetornar = simbolo.Simbolo()
                    simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.double_precision, int(-1))
                    return simboloRetornar
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "sqrt":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.sqrt(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "width_bucket": #Pendiente
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.double_precision, int(1))
                return simboloRetornar
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "trunc":
            Res = self.Param1.ejecutar(tabalSimbolos, listaErrores)
            if Res.tipoDatoRetorno == simboloColumna.TiposDatos.bigInit or Res.tipoDatoRetorno == simboloColumna.TiposDatos.integer or Res.tipoDatoRetorno == simboloColumna.TiposDatos.double_precision or Res.tipoDatoRetorno == simboloColumna.TiposDatos.decimal:
                Res.valorRetorno = math.trunc(Res.valorRetorno)
                return Res
            else:
                print("El parametro no es un numero")

        elif str.lower(self.TipoFuncion.valor) == "random":
            simboloRetornar = simbolo.Simbolo()
            simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.double_precision, random.random())
            return simboloRetornar


#---------------------------------------------------FUNCIONES TRIGONOMETRICAS----------------------------------------------------------


        