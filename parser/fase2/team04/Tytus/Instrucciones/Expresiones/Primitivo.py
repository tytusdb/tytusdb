from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato

class Primitivo(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
       

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return self.valor
    
    def getCodigo(self, tabla, arbol):
        valor = f"\"{self.valor}\"" if self.tipo.tipo == Tipo_Dato.TEXT or self.tipo.tipo == Tipo_Dato.CHAR else self.valor
        return { 'codigo' : '', 'dir' : f"{valor}" }
    
    def toString(self):
        return f"{self.valor}"
    
'''        
p = Primitivo(1,Tipo(Tipo_Dato.INTEGER),1,2)
print(p.tipo.toString())
res = p.ejecutar(None,None)
print(res)
'''