from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones.Aritmetica import Aritmetica
from Instrucciones.Expresiones.Primitivo import Primitivo
from decimal import Decimal
from datetime import date, datetime
import time
#from dateutil.parser import parse

class Convert(Instruccion):
    def __init__(self, valor, tipo, tipo_salida, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.tipo = tipo
        self.tipo_salida = tipo_salida

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        try:
            if self.tipo_salida.tipo == Tipo_Dato.INTEGER:
                int(resultado)
                self.tipo = Tipo(Tipo_Dato.INTEGER)
                return resultado
            elif self.tipo_salida.tipo == Tipo_Dato.SMALLINT:
                int(resultado)
                self.tipo = Tipo(Tipo_Dato.SMALLINT)
                return resultado 
            elif self.tipo_salida.tipo == Tipo_Dato.DECIMAL:
                float(resultado)
                self.tipo = Tipo(Tipo_Dato.DECIMAL)
                return resultado             
            elif self.tipo_salida.tipo == Tipo_Dato.BOOLEAN:
                if bool(resultado):
                    verdadero = ("true","t","1","yes")
                    false = ("false","f","0","not")
                    if resultado in (verdadero + false):
                        self.tipo = Tipo(Tipo_Dato.BOOLEAN)
                        return str(resultado).lower() in verdadero   
                    else:
                        error = Excepcion('22P02',"Semántico",f"La sintaxis de entrada no es válida para tipo {self.valor.tipo.toString()}: << {resultado} >> a Boolean",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error     
            elif self.tipo_salida.tipo == Tipo_Dato.DATE:
                #formats = ("%d-%m-%Y %I:%M %p", "%d/%m/%Y %I:%M %p")
                formats = ("%d-%m-%Y", "%Y-%m-%d","%d-%M-%Y", "%Y-%M-%d","%Y-%b-%d", "%d-%b-%Y")
                for fmt in formats:
                    valid_date=""
                    try:
                        valid_date = time.strptime(resultado, fmt)
                        if isinstance(valid_date, time.struct_time):
                            self.tipo = Tipo(Tipo_Dato.DATE)
                            return time.strftime('%Y-%m-%d',valid_date)
                         
                    except ValueError as e:
                        pass
                error = Excepcion('22007',"Semántico",f"la sintaxis de entrada no es válida para tipo date: << {resultado} >>",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error   
            

        except:
            error = Excepcion('22P02',"Semántico",f"La sintaxis de entrada no es válida para tipo {self.valor.tipo.toString()}: << {resultado} >>",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error

    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        valor=""
        tipo_salida=""
        if isinstance(self.valor, Primitivo):
            valor = self.valor.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.valor, Aritmetica):
            valor = self.valor.concatenar(tabla,arbol)
        elif isinstance(self.valor, str) or isinstance(self.valor, int):
            valor = self.valor
        else:
            valor=self.valor.traducir(tabla,arbol)
        
        if isinstance(self.tipo_salida, Primitivo):
            tipo_salida = self.tipo_salida.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.tipo_salida, Aritmetica):
            tipo_salida = self.tipo_salida.concatenar(tabla,arbol)
        elif isinstance(self.tipo_salida, str) or isinstance(self.tipo_salida, int):
            tipo_salida = self.tipo_salida
        else:
            tipo_salida= self.tipo_salida.traducir(tabla,arbol)

        return f"CONVERT({valor} AS {tipo_salida})"