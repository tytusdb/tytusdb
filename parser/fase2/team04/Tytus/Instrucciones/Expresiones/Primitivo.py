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
        value_list = []
        
        tipo_result = self.tipo.getCodigo(tabla, arbol)
        
        value_list.append(valor)        
        value_list.append(tipo_result['dir'])
        value_list.append(f"\"\"")
        value_list.append(self.linea)
        value_list.append(self.columna)
        
        native_result = arbol.getExpressionCode(value_list, 'primitivo')
        
        codigo = tipo_result['codigo']
        codigo += native_result['codigo']

        return {'codigo': codigo, 'dir': native_result['dir']}
    
    def toString(self):
        return f"{self.valor}"
    
'''        
p = Primitivo(1,Tipo(Tipo_Dato.INTEGER),1,2)
print(p.tipo.toString())
res = p.ejecutar(None,None)
print(res)
'''