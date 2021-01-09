from Instrucciones.Identificador import Identificador
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import *
from Instrucciones.Expresiones.Aritmetica import Aritmetica

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
    
    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        valor=""
        inicio=""
        fin = ""
        if isinstance(self.valor, Primitivo):
            valor = self.valor.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.valor, Aritmetica):
            valor = self.valor.concatenar(tabla,arbol)
        elif isinstance(self.valor, str) or isinstance(self.valor, int):
            valor = self.valor
        else:
            valor=self.valor.traducir(tabla,arbol)
        
        if isinstance(self.inicio, Primitivo):
            inicio = self.inicio.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.inicio, Aritmetica):
            inicio = self.inicio.concatenar(tabla,arbol)
        elif isinstance(self.inicio, str) or isinstance(self.inicio, int):
            inicio = self.inicio
        else:
            inicio= self.inicio.traducir(tabla,arbol)

        if isinstance(self.fin, Primitivo):
            fin = self.fin.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.fin, Aritmetica):
            fin = self.fin.concatenar(tabla,arbol)
        elif isinstance(self.fin, str) or isinstance(self.fin, int):
            fin = self.fin
        else:
            fin= self.fin.traducir(tabla,arbol)

        return f"SUBSTRING({valor},{inicio},{fin})"
    
'''
instruccion = Substring("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)
'''