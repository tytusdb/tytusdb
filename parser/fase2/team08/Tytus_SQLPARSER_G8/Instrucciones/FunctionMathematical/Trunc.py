import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones.Aritmetica import Aritmetica
from Instrucciones.Expresiones.Primitivo import Primitivo

class Trunc(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.INTEGER),linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if self.valor.tipo.tipo != Tipo_Dato.SMALLINT and self.valor.tipo.tipo != Tipo_Dato.INTEGER and self.valor.tipo.tipo != Tipo_Dato.BIGINT and self.valor.tipo.tipo != Tipo_Dato.DECIMAL and self.valor.tipo.tipo != Tipo_Dato.NUMERIC and self.valor.tipo.tipo != Tipo_Dato.REAL and self.valor.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION:
            error = Excepcion('42883',"Semántico","No existe la función trunc("+self.valor.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if resultado < 0:
            error = Excepcion('2201F',"Semántico","La función TRUNC únicamente acepta valores númericos positivos",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if isinstance(resultado,int):
            self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
            return math.trunc(resultado)
        else:
            self.tipo = Tipo(Tipo_Dato.NUMERIC)
            return math.trunc(resultado)

    def analizar(self, tabla, arbol):
        super().analizar(tabla, arbol)
        resultado = self.valor.analizar(tabla,arbol)
        if self.valor.tipo.tipo != Tipo_Dato.SMALLINT and self.valor.tipo.tipo != Tipo_Dato.INTEGER and self.valor.tipo.tipo != Tipo_Dato.BIGINT and self.valor.tipo.tipo != Tipo_Dato.DECIMAL and self.valor.tipo.tipo != Tipo_Dato.NUMERIC and self.valor.tipo.tipo != Tipo_Dato.REAL and self.valor.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION:
            error = Excepcion('42883',"Semántico","No existe la función trunc("+self.valor.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if isinstance(resultado,int):
            self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
            return Tipo(Tipo_Dato.NUMERIC)
        else:
            self.tipo = Tipo(Tipo_Dato.NUMERIC)
            return self.tipo

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        retorno = Nodo3D()
        resultado = self.valor.traducir(tabla, arbol)
        temporal1 = tabla.getTemporal()
        temporal2 = tabla.getTemporal()
        arbol.addc3d(f"{temporal1} = {resultado.temporalAnterior}")
        arbol.addc3d(f"{temporal2} = math.trunc({temporal1})")
        retorno.temporalAnterior = temporal2
        return retorno
        
        '''
        if isinstance(self.valor, Primitivo):
            return f"TRUNC({self.valor.traducir(tabla,arbol).temporalAnterior})"
        elif isinstance(self.valor, Aritmetica):
            return f"TRUNC({self.valor.concatenar(tabla,arbol)})"
        return f"TRUNC({self.valor.traducir(tabla,arbol)})"
        '''
        