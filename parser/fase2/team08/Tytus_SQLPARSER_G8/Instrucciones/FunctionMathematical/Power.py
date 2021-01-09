import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones.Aritmetica import Aritmetica
from Instrucciones.Expresiones.Primitivo import Primitivo

class Power(Instruccion):
    def __init__(self, opIzq, opDer, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.NUMERIC),linea,columna,strGram)
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
        if (self.opIzq.tipo.tipo == Tipo_Dato.INTEGER or self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC) and (self.opDer.tipo.tipo == Tipo_Dato.INTEGER or self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.opDer.tipo.tipo == Tipo_Dato.NUMERIC):
            if resultadoDer < 0 or resultadoIzq < 0:
                error = Excepcion('42883',"Semántico","La función POWER únicamente acepta valores númericos positivos",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            if isinstance(resultadoIzq, int) and isinstance(resultadoDer, int):
                self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                return int(math.pow(resultadoIzq, resultadoDer))
            else:
                self.tipo = Tipo(Tipo_Dato.NUMERIC)
                return math.pow(resultadoIzq, resultadoDer) 
        else:
            error = Excepcion('42883',"Semántico","No existe la función power("+self.opIzq.tipo.toString()+", "+self.opDer.tipo.toString()+")",self.linea,self.columna)
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

        return f"POWER({resultadoIzq},{resultadoDer})"