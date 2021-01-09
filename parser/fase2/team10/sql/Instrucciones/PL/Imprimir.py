from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
 
from sql.Instrucciones.Excepcion import Excepcion

class Imprimir(Instruccion):
    def __init__(self, expresion, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.expresion = expresion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        resultado = self.expresion.analizar(tabla,arbol)
        if not isinstance(resultado, Excepcion):
            self.tipo = resultado
        return resultado
        
    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
       
        temp = self.expresion.traducir(tabla,arbol)
        arbol.addc3d("#Inicio print")
        if(self.expresion.tipo.tipo == Tipo_Dato.SMALLINT or self.expresion.tipo.tipo == Tipo_Dato.INTEGER or self.expresion.tipo.tipo == Tipo_Dato.BIGINT or self.expresion.tipo.tipo == Tipo_Dato.DECIMAL or self.expresion.tipo.tipo == Tipo_Dato.NUMERIC or self.expresion.tipo.tipo == Tipo_Dato.REAL or self.expresion.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION or self.expresion.tipo.tipo == Tipo_Dato.MONEY):
            arbol.addc3d(f"print({temp.temporalAnterior})")
        if(self.expresion.tipo.tipo == Tipo_Dato.BOOLEAN):
            temporal1 = tabla.getTemporal()
            if(temp.temporalAnterior == ""):
                etiqueta1 = tabla.getEtiqueta()
                retorno.imprimirEtiquetDestino(arbol, temp.etiquetaTrue)
                arbol.addc3d(f"{temporal1} = 1")
                arbol.addc3d(f"goto .{etiqueta1}")
                retorno.imprimirEtiquetDestino(arbol, temp.etiquetaFalse)
                arbol.addc3d(f"{temporal1} = 0")
                arbol.addc3d(f"goto .{etiqueta1}")
                arbol.addc3d(f"label .{etiqueta1}")
            else:
                arbol.addc3d(f"{temporal1} = {temp.temporalAnterior}")
            
            etiqueta1 = tabla.getEtiqueta()
            etiqueta2 = tabla.getEtiqueta()
            etiqueta3 = tabla.getEtiqueta()
            arbol.addc3d(f"if({temporal1} == 1):\n\t\tgoto .{etiqueta1}")
            arbol.addc3d(f"goto .{etiqueta2}")
            arbol.addc3d(f"#True")
            arbol.addc3d(f"label .{etiqueta1}")
            arbol.addc3d("print(True)")
            arbol.addc3d(f"goto .{etiqueta3}")
            
            arbol.addc3d(f"#False")
            arbol.addc3d(f"label .{etiqueta2}")
            arbol.addc3d("print(False)")
            arbol.addc3d(f"label .{etiqueta3}")
        
        arbol.addc3d("#Fin print")
        return retorno

                

