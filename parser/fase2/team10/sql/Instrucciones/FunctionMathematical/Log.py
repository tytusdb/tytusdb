import math
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from sql.Instrucciones.Excepcion import Excepcion

class Log(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.NUMERIC),linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if self.valor.tipo.tipo != Tipo_Dato.SMALLINT and self.valor.tipo.tipo != Tipo_Dato.INTEGER and self.valor.tipo.tipo != Tipo_Dato.BIGINT and self.valor.tipo.tipo != Tipo_Dato.DECIMAL and self.valor.tipo.tipo != Tipo_Dato.NUMERIC and self.valor.tipo.tipo != Tipo_Dato.REAL and self.valor.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION:
            error = Excepcion('42883',"Semántico","No existe la función log("+self.valor.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if resultado < 0:
            error = Excepcion('2201F',"Semántico","La función LOG únicamente acepta valores númericos positivos",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if isinstance(resultado,int):
            self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
            return math.log(resultado)
        else:
            self.tipo = Tipo(Tipo_Dato.NUMERIC)
            return math.log(resultado)
