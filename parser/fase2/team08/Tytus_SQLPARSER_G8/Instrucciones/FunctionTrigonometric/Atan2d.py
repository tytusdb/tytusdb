import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones.Aritmetica import Aritmetica
from Instrucciones.Expresiones.Primitivo import Primitivo

class Atan2d(Instruccion):
    def __init__(self, opIzq, opDer, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.DOUBLE_PRECISION),linea,columna,strGram)
        self.opIzq = opIzq
        self.opDer = opDer

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Si existe algún error en el operador izquierdo, retorno el error.
        resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
        if isinstance(resultadoIzq, Excepcion):
            return resultadoIzq
        # Si existe algún error en el operador derecho, retorno el error.
        resultadoDer = self.opDer.ejecutar(tabla, arbol)
        if isinstance(resultadoDer, Excepcion):
            return resultadoDer
        if (self.opIzq.tipo.tipo != Tipo_Dato.SMALLINT and self.opIzq.tipo.tipo != Tipo_Dato.INTEGER and self.opIzq.tipo.tipo != Tipo_Dato.BIGINT and self.opIzq.tipo.tipo != Tipo_Dato.DECIMAL and self.opIzq.tipo.tipo != Tipo_Dato.NUMERIC and self.opIzq.tipo.tipo != Tipo_Dato.REAL and self.opIzq.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION) or (self.opDer.tipo.tipo != Tipo_Dato.SMALLINT and self.opDer.tipo.tipo != Tipo_Dato.INTEGER and self.opDer.tipo.tipo != Tipo_Dato.BIGINT and self.opDer.tipo.tipo != Tipo_Dato.DECIMAL and self.opDer.tipo.tipo != Tipo_Dato.NUMERIC and self.opDer.tipo.tipo != Tipo_Dato.REAL and self.opDer.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION):
            error = Excepcion('42883',"Semántico","No existe la función atan2d("+self.opIzq.tipo.toString()+","+self.opDer.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        try:
            return math.degrees(math.atan2(resultadoIzq,resultadoDer))
        except ValueError as c:
            error = Excepcion('22003',"Semántico","La entrada está fuera de rango",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        
        
    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        resultadoIzq=""
        resultadoDer=""
        if isinstance(self.opIzq, Primitivo):
            resultadoIzq = self.opIzq.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.opIzq, Aritmetica):
            resultadoIzq = self.opIzq.concatenar(tabla,arbol)
        else:
            resultadoIzq=self.opIzq.traducir(tabla,arbol)
        
        if isinstance(self.opDer, Primitivo):
            resultadoDer = self.opDer.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.opDer, Aritmetica):
            resultadoDer = self.opDer.concatenar(tabla,arbol)
        else:
            resultadoDer= self.opDer.traducir(tabla,arbol)

        return f"ATAN2D({resultadoIzq},{resultadoDer})"