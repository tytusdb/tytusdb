from Instrucciones.Identificador import Identificador
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import *
from Instrucciones.TablaSimbolos.Simbolo3D import Simbolo3d

class Substring(Instruccion):
    def __init__(self, valor, inicio, fin, tipo, strGram, linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.valor = valor
        self.inicio = inicio
        self.fin = fin

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        if self.valor.tipo.tipo== Tipo_Dato.CHAR or self.valor.tipo.tipo== Tipo_Dato.VARCHAR or self.valor.tipo.tipo== Tipo_Dato.VARYING or self.valor.tipo.tipo== Tipo_Dato.CHARACTER or self.valor.tipo.tipo== Tipo_Dato.TEXT:
            self.tipo= Tipo("",Tipo_Dato.TEXT)
            return str(resultado)[int(self.inicio):int(self.fin)] 

        error = Excepcion('42883',"Semántico",f"No existe la función SUBSTRING({self.valor.tipo.toString()})",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append("HINT: Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos.")
        arbol.consola.append(error.toString())
        return error

    def traducir(self, tabla, arbol, cadenaTraducida):
        resultado = self.ejecutar(tabla, arbol)
        if isinstance(resultado,Excepcion):
            return resultado        
        codigo = ""
        temporal = arbol.generaTemporal()
        codigo += "\t" + temporal + " = " + str(resultado) + "\n"
        nuevo = Simbolo3d(self.tipo, temporal, codigo, None, None)
        return nuevo
'''
instruccion = Substring("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)
'''