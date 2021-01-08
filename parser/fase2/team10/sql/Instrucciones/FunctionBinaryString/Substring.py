from sql.Instrucciones.Identificador import Identificador
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from sql.Instrucciones.Expresiones.Primitivo import Primitivo
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Excepcion import *

class Substring(Instruccion):
    def __init__(self, valor, inicio, fin, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.inicio = inicio
        self.fin = fin

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        if self.valor.tipo.tipo== Tipo_Dato.CHAR or self.valor.tipo.tipo== Tipo_Dato.VARCHAR or self.valor.tipo.tipo== Tipo_Dato.VARYING or self.valor.tipo.tipo== Tipo_Dato.CHARACTER or self.valor.tipo.tipo== Tipo_Dato.TEXT:
            self.tipo= Tipo(Tipo_Dato.TEXT)
            return str(resultado)[int(self.inicio):int(self.fin)] 

        error = Excepcion('42883',"Semántico",f"No existe la función SUBSTRING({self.valor.tipo.toString()})",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append("HINT: Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos.")
        arbol.consola.append(error.toString())
        return error
'''
instruccion = Substring("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)
'''