import Instrucciones
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import *
from Instrucciones.Identificador import *
from Instrucciones.Expresiones.Aritmetica import Aritmetica

class Length(Instruccion):
    def __init__(self, valor, tipo, strGram,linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.INTEGER),linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        #print("RESULTADO:",resultado)
        #if isinstance(resultado, Primitivo):
        if self.valor.tipo.tipo== Tipo_Dato.CHAR or self.valor.tipo.tipo== Tipo_Dato.VARCHAR or self.valor.tipo.tipo== Tipo_Dato.VARYING or self.valor.tipo.tipo== Tipo_Dato.CHARACTER or self.valor.tipo.tipo== Tipo_Dato.TEXT:
        #if self.valor.tipo.tipo== Tipo_Dato.CHAR or self.valor.tipo.tipo== Tipo_Dato.CHARACTER:
                self.tipo = Tipo(Tipo_Dato.INTEGER)
                return len(str(resultado)) 
        #elif isinstance(resultado, Identificador):
        #    print("HAY QUE PROGRAMAR LO DE IDENTIFICADOR LENGTH")
        error = Excepcion('42883',"Semántico",f"No existe la función LENGTH({self.valor.tipo.toString()})",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append("HINT: Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos.")
        arbol.consola.append(error.toString())
        return error
        
    def analizar(self, tabla, arbol):
        super().analizar(tabla, arbol)
        return self.tipo

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        if isinstance(self.valor, Primitivo):
            return f"LENGTH({self.valor.traducir(tabla,arbol).temporalAnterior})"
        elif isinstance(self.valor, Aritmetica):
            return f"LENGTH({self.valor.concatenar(tabla,arbol)})"
        elif isinstance(self.valor, str) or isinstance(self.valor, int):
            return f"LENGTH({self.valor})"
        return f"LENGTH({self.valor.traducir(tabla,arbol)})"
    
'''
instruccion = Length("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''