from Instrucciones.Identificador import Identificador
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import *
from Instrucciones.Expresiones.Aritmetica import Aritmetica

class SetByte(Instruccion):
    def __init__(self, valor, tipo, indice, caracter, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.tipo = tipo
        self.indice = indice
        self.caracter = caracter
        self.linea= linea
        self.columna= columna

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado        
        if self.indice <len(resultado):
            if self.valor.tipo.tipo== Tipo_Dato.CHAR or self.valor.tipo.tipo== Tipo_Dato.VARCHAR or self.valor.tipo.tipo== Tipo_Dato.VARYING or self.valor.tipo.tipo== Tipo_Dato.CHARACTER or self.valor.tipo.tipo== Tipo_Dato.TEXT:
                cadena =""
                cont=0
                for letra in str(self.valor.valor):
                    if(cont==int(self.indice)):
                        cadena+= chr(self.caracter)
                        cont +=1
                        continue                    
                    cadena += letra
                    cont +=1
                resultado= cadena
                self.tipo = Tipo(Tipo_Dato.TEXT)
                return resultado
        else:
            error = Excepcion('2202E',"Semántico",f"El índice {self.indice} esta fuera de rango [0..{len(self.valor.valor)}]",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error

        error = Excepcion('42883',"Semántico",f"No existe la función SET_BYTE({self.valor.tipo.toString()})",self.linea,self.columna)
        arbol.excepciones.append(error)
        arbol.consola.append("HINT: Ninguna función coincide en el nombre y tipos de argumentos. Puede ser necesario agregar conversión explícita de tipos.")
        arbol.consola.append(error.toString())
        return error
    
    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        valor=""
        indice=""
        caracter = ""
        if isinstance(self.valor, Primitivo):
            valor = self.valor.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.valor, Aritmetica):
            valor = self.valor.concatenar(tabla,arbol)
        elif isinstance(self.valor, str) or isinstance(self.valor, int):
            valor = self.valor
        else:
            valor=self.valor.traducir(tabla,arbol)
        
        if isinstance(self.indice, Primitivo):
            indice = self.indice.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.indice, Aritmetica):
            indice = self.indice.concatenar(tabla,arbol)
        elif isinstance(self.indice, str) or isinstance(self.indice, int):
            indice = self.indice
        else:
            indice= self.indice.traducir(tabla,arbol)

        if isinstance(self.caracter, Primitivo):
            caracter = self.caracter.traducir(tabla,arbol).temporalAnterior
        elif isinstance(self.caracter, Aritmetica):
            caracter = self.caracter.concatenar(tabla,arbol)
        elif isinstance(self.caracter, str) or isinstance(self.caracter, int):
            caracter = self.caracter
        else:
            caracter= self.caracter.traducir(tabla,arbol)

        return f"SET_BYTE({valor},{indice},{caracter})"
    