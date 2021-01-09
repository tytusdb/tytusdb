from sql.Instrucciones.Identificador import Identificador
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from sql.Instrucciones.Expresiones.Primitivo import Primitivo
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Excepcion import *

class GetByte(Instruccion):
    def __init__(self, valor, tipo, indice, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.indice = indice

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        if self.indice <len(resultado):
            if self.valor.tipo.tipo== Tipo_Dato.CHAR or self.valor.tipo.tipo== Tipo_Dato.VARCHAR or self.valor.tipo.tipo== Tipo_Dato.VARYING or self.valor.tipo.tipo== Tipo_Dato.CHARACTER or self.valor.tipo.tipo== Tipo_Dato.TEXT:
                self.tipo = Tipo(Tipo_Dato.INTEGER)
                return ord(str(resultado)[int(self.indice): int(self.indice)+1])
        else:
            error = Excepcion('2202E',"Semántico",f"El índice {self.indice} esta fuera de rango [0..{len(self.valor.valor)}]",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        error = Excepcion('42883',"Semántico",f"No existe la función GET_BYTE({self.valor.tipo.toString()})",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append("HINT: Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos.")
        arbol.consola.append(error.toString())
        return error
'''
instruccion = GetByte("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''