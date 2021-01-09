from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Excepcion import Excepcion
from Instrucciones.PL.Return import Return

class Proc(Instruccion):
    def __init__(self, id, replace, parametros, instrucciones, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna,strGram)
        self.id = id
        self.replace = replace
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.activa = True

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def llenarTS(self, tabla, arbol):
        existe = tabla.getSimboloFuncion(self.id)
        if existe != None:
            if self.replace != None:
                # Espacio para el return
                arbol.contador += 1

                # Espacio para los parámetros
                arbol.contador += len(self.parametros)

                existe.rol = "Metodo"
                existe.funcion = self
                existe.tamanio = arbol.contador 
                arbol.contador = 0
                #print("se limpió? ------------>",arbol.contador, existe.tamanio)
                return 
            else:
                error = Excepcion("42723", "Semantico", f"La función {self.id} ya existe.", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        
        if self.tipo.tipo != Tipo_Dato.VOID:
            # Espacio para el return
            arbol.contador += 1

        # Espacio para los parámetros
        arbol.contador += len(self.parametros)

        f = Simbolo(self.id, self.tipo, "", self.linea, self.columna)
        f.rol = "Metodo"
        f.funcion = self
        f.tamanio = arbol.contador
        tabla.agregarSimbolo(f) 
        arbol.contador = 0     

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        tablaLocal = Tabla(None)

        for i in self.parametros:
            i.analizar(tablaLocal, arbol)

        tablaLocal.anterior = tabla
        
        esFuncion = False
        if self.tipo.tipo != Tipo_Dato.VOID:
            esFuncion = True
        
        hayReturn = False
        for i in self.instrucciones:
            resultado = i.analizar(tablaLocal, arbol)
            if isinstance(i, Return):
                if isinstance(resultado, Excepcion):
                    return resultado
                hayReturn = True

        if esFuncion and not hayReturn:
            error = Excepcion("42723", "Semantico", f"La función {self.id} requiere un valor de retorno", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        
        if not esFuncion and hayReturn:
            error = Excepcion("42723", "Semantico", f"El método {self.id} no requiere un valor de retorno", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error  
        #print("finaliza funcion")    
        
        
    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        tablaLocal = Tabla(None)
        arbol.addc3d('\r@with_goto  # Decorador necesario.')
        arbol.addc3d(f"\rdef {self.id}():")
        arbol.addc3d("global P")
        arbol.addc3d("global Pila")
    
        if self.tipo.tipo != Tipo_Dato.VOID:
            variable = Simbolo("return", self.tipo, None, self.linea, self.columna)
            variable.rol = "Variable Local"
            variable.posicion = tablaLocal.stack
            variable.tamanio = 1
            tabla.agregarSimbolo(variable)
            tablaLocal.stack += 1
        
        for i in self.parametros:
            i.traducir(tablaLocal, arbol)
        tablaLocal.anterior = tabla

        for i in self.instrucciones:
            i.traducir(tablaLocal, arbol)
        
        # Se llena el reporte de la tabla de símbolo
        for i in tablaLocal.variables:
            i.ambito = self.id
            tabla.agregarReporteSimbolo(i)

        arbol.addc3d(f"\n\treturn\n")

        return
        