from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo3D import Simbolo3d
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class Primitivo(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.valor = valor
       

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return self.valor

    def traducir(self,tabla,arbol,cadenaTraducida):
        super().ejecutar(tabla,arbol)
        temporal = arbol.generaTemporal()
        codigo = "\t" + temporal + " = " + str(self.valor) + "\n"
        nuevo = Simbolo3d(self.tipo,temporal,codigo,None,None)
        return nuevo


'''        
p = Primitivo(1,Tipo(Tipo_Dato.INTEGER),1,2)
print(p.tipo.toString())
res = p.ejecutar(None,None)
print(res)
'''