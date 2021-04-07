from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
 
from sql.Instrucciones.TablaSimbolos.Arbol import Arbol
from sql.Instrucciones.TablaSimbolos.Tabla import Tabla
from sql.Instrucciones.Excepcion import Excepcion

class If(Instruccion):
    def __init__(self, condicion, instrucciones, l_if, instrucciones_else, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.condicion = condicion 
        self.instrucciones = instrucciones
        self.l_if = l_if
        self.instrucciones_else = instrucciones_else

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        resultado = self.condicion.analizar(tabla,arbol)
        if not isinstance(resultado, Excepcion):
            self.tipo = resultado
        
        if isinstance(resultado.tipo != Tipo_Dato.BOOLEAN):
            error = Excepcion("22023", "Semantico", "Tipo de datos incorrecto, se esperaba un valor de tipo boolean para la condición.", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        
        
    def traducir(self, tabla:Tabla, arbol:Arbol):
        super().traducir(tabla,arbol)
       
        arbol.addc3d("# Inicia If")
        condicion = self.condicion.traducir(tabla, arbol)

        if condicion.temporalAnterior == "0":
            etiqueta1 = tabla.getEtiqueta()
            arbol.addc3d(f"goto .{etiqueta1}")
            condicion.etiquetaTrue = ""
            condicion.etiquetaFalse = etiqueta1
        elif condicion.temporalAnterior == "1":
            etiqueta1 = tabla.getEtiqueta()
            arbol.addc3d(f"goto .{etiqueta1}")
            condicion.etiquetaTrue = etiqueta1
            condicion.etiquetaFalse = ""

        etiquetaFin = tabla.getEtiqueta()
        condicion.imprimirEtiquetDestino(arbol, condicion.etiquetaTrue)
        
        # Se traducen todas las funciones dentro del if
        for i in self.instrucciones:
            i.traducir(tabla, arbol)

        arbol.addc3d(f"goto .{etiquetaFin}")
        condicion.imprimirEtiquetDestino(arbol, condicion.etiquetaFalse)

        return retorno
