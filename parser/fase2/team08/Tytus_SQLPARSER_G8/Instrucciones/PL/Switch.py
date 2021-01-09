from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.TablaSimbolos.Arbol import Arbol
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones.Relacional import Relacional
from Instrucciones.PL.Return import Return

class Switch(Instruccion):
    def __init__(self, expresion1, lista_case, instrucciones_else, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.expresion1 = expresion1
        self.lista_case = lista_case
        self.instrucciones_else = instrucciones_else

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        retorno = None
        for caso in self.lista_case:
            if len(caso.expresion2) == 1:
                condicion = Relacional(self.expresion1, caso.expresion2[0], "=", "", self.linea, self.columna)
                resultado = condicion.analizar(tabla, arbol)
                if isinstance(resultado, Excepcion):
                    return resultado
            else:
                for expre in caso.expresion2:
                    condicion = Relacional(self.expresion1, expre, "=", "", self.linea, self.columna)
                    resultado = condicion.analizar(tabla, arbol)
                    if isinstance(resultado, Excepcion):
                        return resultado
        
        for caso in self.lista_case:
            r = caso.analizar(tabla, arbol)
            if isinstance(r, Excepcion):
                return None
            if isinstance(r, Return):
                retorno = r
        return retorno
         
    def traducir(self, tabla:Tabla, arbol:Arbol):
        super().traducir(tabla,arbol)
        arbol.addc3d("# Inicia Case")
        etiquetasSalida = []
        for caso in self.lista_case:
            if len(caso.expresion2) == 1:
                relacional = Relacional(self.expresion1, caso.expresion2[0], "=", "", self.linea, self.columna)
                condicion = relacional.traducir(tabla, arbol)
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
                
                # Se traducen todas las funciones dentro del case
                caso.traducir(tabla, arbol)

                arbol.addc3d(f"goto .{etiquetaFin}")
                condicion.imprimirEtiquetDestino(arbol, condicion.etiquetaFalse)
                etiquetasSalida.append(f"label .{etiquetaFin}") 
            else:
                for expre in caso.expresion2:
                    relacional = Relacional(self.expresion1, expre, "=", "", self.linea, self.columna)
                    condicion = relacional.traducir(tabla, arbol)
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
                    
                    # Se traducen todas las funciones dentro del case
                    caso.traducir(tabla, arbol)

                    arbol.addc3d(f"goto .{etiquetaFin}")
                    condicion.imprimirEtiquetDestino(arbol, condicion.etiquetaFalse)
                    etiquetasSalida.append(f"label .{etiquetaFin}") 
               
        if len(self.instrucciones_else) != 0:
            # Se traducen todas las instrucciones dentro del else
            for i in self.instrucciones_else:
                i.traducir(tabla, arbol)
        
        # Se agregan las etiquetas de salida de los elsif
        for etiqueta in etiquetasSalida:
            arbol.addc3d(etiqueta)
                










