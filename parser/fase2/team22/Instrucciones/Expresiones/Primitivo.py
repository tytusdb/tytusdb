from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Primitivo(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
        self.tipo = tipo

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return self.valor

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        if self.tipo.tipo.name == 'TEXT':
            return '\\"' + self.valor + '\\"'
        elif self.tipo.tipo.name == 'CHAR':
            return "'" + self.valor + "'"
        return self.valor
'''        
p = Primitivo(1,Tipo(Tipo_Dato.INTEGER),1,2)
print(p.tipo.toString())
res = p.ejecutar(None,None)
print(res)
'''