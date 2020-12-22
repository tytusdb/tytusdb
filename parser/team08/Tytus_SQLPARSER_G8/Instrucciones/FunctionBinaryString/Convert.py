from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from decimal import Decimal
from datetime import datetime
#from dateutil.parser import parse

class Convert(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor
        self.tipo = tipo

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append('Función en proceso...')
        '''
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
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
        