from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D

class Primitivo(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
       

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return self.valor

    def analizar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return self.tipo

    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        retorno = Nodo3D()
        if self.tipo.tipo == Tipo_Dato.BOOLEAN:
            if self.valor:
                retorno.temporalAnterior = "1"
            else:
                retorno.temporalAnterior = "0"
            return retorno
        self.valor = str(self.valor).replace("\"","\\\"")
        if self.tipo.tipo == Tipo_Dato.CHAR:
            retorno.temporalAnterior = f"\'{self.valor}\'"
            return retorno
        elif self.tipo.tipo == Tipo_Dato.TEXT:
            retorno.temporalAnterior = f"\'{self.valor}\'"
            return retorno
        retorno.temporalAnterior = str(self.valor)
        return retorno

'''        
p = Primitivo(1,Tipo(Tipo_Dato.INTEGER),1,2)
print(p.tipo.toString())
res = p.ejecutar(None,None)
print(res)
'''