from Instrucciones.Identificador import Identificador
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import *

class GetByte(Instruccion):
    def __init__(self, valor, tipo, indice, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor
        self.indice = indice

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if isinstance(self.valor, Primitivo):
            if self.indice <len(self.valor.valor):
                if self.valor.tipo.tipo== Tipo_Dato.CHAR or self.valor.tipo.tipo== Tipo_Dato.VARCHAR or self.valor.tipo.tipo== Tipo_Dato.VARYING or self.valor.tipo.tipo== Tipo_Dato.CHARACTER or self.valor.tipo.tipo== Tipo_Dato.TEXT:
                    return ord(str(self.valor.valor)[int(self.indice): int(self.indice)+1])
            else:
                error = Excepcion('2202E',"Semántico",f"El índice {self.indice} esta fuera de rango [0..{len(self.valor.valor)}]",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        elif isinstance(self.valor,Identificador):
            print("FALTA PROGRAMAR PARA IDENTIFICADOR GET_BYTE")
        error = Excepcion('42883',"Semántico",f"No existe la función GET_BYTE({self.valor.tipo.toString()})",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append("HINT: Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos.")
        arbol.consola.append(error.toString())
        return error
'''
instruccion = GetByte("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''