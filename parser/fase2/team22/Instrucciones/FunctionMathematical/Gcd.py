import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

# Esta función unicamente acepta enteros.
class Gcd(Instruccion):
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
        if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
            if resultadoDer < 0 or resultadoIzq < 0:
                error = Excepcion('42883',"Semántico","La función GCD únicamente acepta valores númericos positivos",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
            return math.gcd(resultadoIzq, resultadoDer)
        else:
            error = Excepcion('42883',"Semántico","No existe la función gcd("+self.opIzq.tipo.toString()+", "+self.opDer.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"GCD(" + str(self.opIzq.generar3D(tabla, arbol)) + "," + str(self.opDer.generar3D(tabla, arbol)) + ")\"", "STRING"), ClassOP_ARITMETICO.SUMA))

        return code