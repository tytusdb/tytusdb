from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
 

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
       
        if self.tipo.tipo == Tipo_Dato.BOOLEAN:
            if self.valor:
                retorno.temporalAnterior = "1"
            else:
                retorno.temporalAnterior = "0"
            return retorno
        retorno.temporalAnterior = str(self.valor)
        return retorno

'''        
p = Primitivo(1,Tipo(Tipo_Dato.INTEGER),1,2)
print(p.tipo.toString())
res = p.ejecutar(None,None)
print(res)
'''