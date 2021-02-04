from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from sql.Instrucciones.Excepcion import Excepcion
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


        '''
        try:
            if self.tipo.tipo == Tipo_Dato.SMALLINT:
                val = int(resultado)
                if(val > -32768 or val < 32767):
                    return val
            elif self.tipo == Tipo_Dato.INTEGER:
                val = int(resultado)
                if(val > -2147483648 or val < 2147483647):
                    return val
            elif self.tipo == Tipo_Dato.BIGINT:
                val = int(resultado)
                if(val > -2147483648 or val < 2147483647):
                    return val
            elif self.tipo == Tipo_Dato.DECIMAL:
                val = Decimal(resultado)
                self.tipo = Tipo(Tipo_Dato.NUMERIC)
                return val
            elif self.tipo == Tipo_Dato.NUMERIC:
                val = Decimal(resultado)
                return val
            elif self.tipo == Tipo_Dato.REAL:
                val = Decimal(resultado)
                return round(val,7)
            elif self.tipo == Tipo_Dato.DOUBLE_PRECISION:
                val = Decimal(resultado)
                return round(val,15)
            elif self.tipo == Tipo_Dato.MONEY:
                val = Decimal(resultado)
                return val
            elif self.tipo == Tipo_Dato.DATE:
                #dt = parse(resultado)
                #return dt.date()
            elif self.tipo == Tipo_Dato.TIMESTAMP:
                #val = datetime.strptime(resultado, '%d/%m/%y %H:%M:%S')
                #return val
            elif self.tipo == Tipo_Dato.BOOLEAN:
                val = bool(resultado)
                return val
        except ValueError as c:
            error = Excepcion('22P02',"Semántico","La sintaxis de entrada no es válida para tipo "+self.tipo.toString()+": <<"+resultado+">>",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        '''    
        