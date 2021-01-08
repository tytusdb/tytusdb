from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.TablaSimbolos.Arbol import Arbol
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Excepcion import Excepcion
from Instrucciones.PL.Return import Return

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
        retorno = None
        resultado = self.condicion.analizar(tabla,arbol)
        if not isinstance(resultado, Excepcion):
            self.tipo = resultado
        tablaLocal = Tabla(tabla)
        # If
        if len(self.l_if) == 0 and len(self.instrucciones_else) == 0:
            for i in self.instrucciones:
                r = i.analizar(tablaLocal, arbol)
                if isinstance(r, Excepcion):
                    return None
                if isinstance(r, Return):
                    retorno = r
        # If - Else            
        elif len(self.l_if) == 0 and len(self.instrucciones_else) != 0:
            for i in self.instrucciones:
                r = i.analizar(tablaLocal, arbol)
                if isinstance(r, Excepcion):
                    return None
                if isinstance(r, Return):
                    retorno = r

            for i in self.instrucciones_else:
                r = i.analizar(tablaLocal, arbol)
                if isinstance(r, Excepcion):
                    return None
                if isinstance(r, Return):
                    retorno = r
        # If ... Elsif
        elif len(self.l_if) > 0 and len(self.instrucciones_else) == 0:
            for i in self.instrucciones:
                r = i.analizar(tablaLocal, arbol)
                if isinstance(r, Excepcion):
                    return None
                if isinstance(r, Return):
                    retorno = r

            for elseif in self.l_if:
                r = elseif.analizar(tablaLocal, arbol)
                if isinstance(r, Excepcion):
                    return None
                if isinstance(r, Return):
                    retorno = r
                
        # If ... Elsif ... Else
        elif len(self.l_if) > 0 and len(self.instrucciones_else) > 0:
            for i in self.instrucciones:
                r = i.analizar(tablaLocal, arbol)
                if isinstance(r, Excepcion):
                    return None
                if isinstance(r, Return):
                    retorno = r

            for elseif in self.l_if:
                r = elseif.analizar(tablaLocal, arbol)
                if isinstance(r, Excepcion):
                    return None
                if isinstance(r, Return):
                    retorno = r

            for i in self.instrucciones_else:
                r = i.analizar(tablaLocal, arbol)
                if isinstance(r, Excepcion):
                    return None
                if isinstance(r, Return):
                    retorno = r
        
        if resultado.tipo != Tipo_Dato.BOOLEAN:
            error = Excepcion("22023", "Semantico", "Tipo de datos incorrecto, se esperaba un valor de tipo boolean para la condición.", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error

        return retorno
        
    def traducir(self, tabla:Tabla, arbol:Arbol):
        super().traducir(tabla,arbol)
        retorno = Nodo3D()
        arbol.addc3d("# Inicia If")
        condicion = self.condicion.traducir(tabla, arbol)
        # If
        if len(self.l_if) == 0 and len(self.instrucciones_else) == 0:
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
            arbol.addc3d(f"label .{etiquetaFin}")
        # If - Else            
        elif len(self.l_if) == 0 and len(self.instrucciones_else) != 0:
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
            
            # Se traducen todas las instrucciones dentro del if
            for i in self.instrucciones:
                i.traducir(tabla, arbol)
            arbol.addc3d(f"goto .{etiquetaFin}")
            condicion.imprimirEtiquetDestino(arbol, condicion.etiquetaFalse)

            # Else
            # Se traducen todas las instrucciones dentro del else
            for i in self.instrucciones_else:
                i.traducir(tabla, arbol)

            arbol.addc3d(f"label .{etiquetaFin}")
        # If ... Elsif
        elif len(self.l_if) > 0 and len(self.instrucciones_else) == 0:
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
            
            # Se traducen todas las instrucciones dentro del if
            for i in self.instrucciones:
                i.traducir(tabla, arbol)
            arbol.addc3d(f"goto .{etiquetaFin}")
            condicion.imprimirEtiquetDestino(arbol, condicion.etiquetaFalse)

            # Elsif
            # Se traducen todas las instrucciones dentro del elsif
            etiquetasSalida = []
            for elseif in self.l_if:
                resultado = elseif.traducir(tabla, arbol)
                etiquetasSalida.append(resultado.temporalAnterior)    
            
            arbol.addc3d(f"label .{etiquetaFin}")
            # Se agregan las etiquetas de salida de los elsif
            for etiqueta in etiquetasSalida:
                arbol.addc3d(etiqueta)
        
        # If ... Elsif ... Else
        elif len(self.l_if) > 0 and len(self.instrucciones_else) > 0:
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
            
            # Se traducen todas las instrucciones dentro del if
            for i in self.instrucciones:
                i.traducir(tabla, arbol)
            arbol.addc3d(f"goto .{etiquetaFin}")
            condicion.imprimirEtiquetDestino(arbol, condicion.etiquetaFalse)
            
            # Elsif
            # Se traducen todas las instrucciones dentro del elsif
            etiquetasSalida = []
            for elseif in self.l_if:
                resultado = elseif.traducir(tabla, arbol)
                etiquetasSalida.append(resultado.temporalAnterior)               

            # Else
            # Se traducen todas las instrucciones dentro del else
            for i in self.instrucciones_else:
                i.traducir(tabla, arbol)

            arbol.addc3d(f"label .{etiquetaFin}")
            # Se agregan las etiquetas de salida de los elsif
            for etiqueta in etiquetasSalida:
                arbol.addc3d(etiqueta)


        return retorno
