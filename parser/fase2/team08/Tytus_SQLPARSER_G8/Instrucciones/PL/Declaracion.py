from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion

class Declaracion(Instruccion):
    def __init__(self, id, constante, tipo, notnull, default, expresion, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna,strGram)
        self.id = id
        self.constante = constante
        self.notnull = notnull
        self.default = default
        self.expresion = expresion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.expresion.ejecutar(tabla, arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        existe = tabla.getSimboloVariable(self.id)
        if existe != None:
            error = Excepcion("42723", "Semantico", f"La variable {self.id} ya ha sido declarada", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error 
        if self.expresion == None:
            variable = Simbolo(self.id, self.tipo, None, self.linea, self.columna)
            if self.constante:
                variable.rol = "Variable Local"
            else:
                variable.rol = "Constante"
            tabla.agregarSimbolo(variable)
        else:
            resultado = self.expresion.analizar(tabla, arbol)
            if isinstance(resultado, Excepcion):
                return resultado

            comprobar = self.comprobarTipo(self.tipo, resultado, None)
            if not comprobar:
                error = Excepcion("42723", "Semantico", f"Los tipos de datos no coinciden", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error 
            
            variable = Simbolo(self.id, self.tipo, None, self.linea, self.columna)
            if self.constante:
                variable.rol = "Variable Local"
            else:
                variable.rol = "Constante"
            tabla.agregarSimbolo(variable)

        #print("finalizó declare!")

        
    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        retorno = Nodo3D()
        if self.expresion == None:
            s = Simbolo(self.id, self.tipo, None, self.linea, self.columna)
            s.posicion = tabla.stack
            tabla.stack += 1
            s.rol = "Variable Local"
            s.tamanio = 1
            tabla.agregarSimbolo(s)
            return
        else:
            if self.tipo.tipo != Tipo_Dato.BOOLEAN:
                s = Simbolo(self.id, self.tipo, None, self.linea, self.columna)
                s.posicion = tabla.stack
                
                s.rol = "Variable Local"
                s.tamanio = 1
                tabla.agregarSimbolo(s)

                temporal1 = tabla.getTemporal()
                temporal2 = tabla.getTemporal()
                arbol.addComen(f"Declaración local: {self.id}")
                arbol.addc3d(f"{temporal1} = P + {tabla.stack}")
                arbol.addComen(f"Traduce la expresión")
                valor = self.expresion.traducir(tabla, arbol)
                arbol.addComen(f"Asignación")
                arbol.addc3d(f"{temporal2} = {valor.temporalAnterior}")
                arbol.addc3d(f"Pila[{temporal1}] = {temporal2}")
                tabla.stack += 1
                return
            else:
                s = Simbolo(self.id, self.tipo, None, self.linea, self.columna)
                s.posicion = tabla.stack
                
                s.rol = "Variable Local"
                s.tamanio = 1
                tabla.agregarSimbolo(s)

                temporal1 = tabla.getTemporal()
                temporal2 = tabla.getTemporal()
                arbol.addComen(f"Declaración local: {self.id}")
                arbol.addc3d(f"{temporal1} = P + {tabla.stack}")
                arbol.addComen(f"Traduce la expresión")
                valor = self.expresion.traducir(tabla, arbol)
                arbol.addComen(f"Asignación")
                
                if valor.temporalAnterior != "1" and valor.temporalAnterior != "0":
                    retorno.imprimirEtiquetDestino(arbol, valor.etiquetaTrue)
                    arbol.addc3d(f"{temporal2} = 1")
                    etiqueta1 = tabla.getEtiqueta()
                    arbol.addc3d(f"goto .{etiqueta1}")
                    retorno.imprimirEtiquetDestino(arbol, valor.etiquetaFalse)
                    arbol.addc3d(f"{temporal2} = 0")
                    arbol.addc3d(f"label .{etiqueta1}")
                else:
                    arbol.addc3d(f"{temporal2} = {valor.temporalAnterior}")
                arbol.addc3d(f"{temporal2} = {valor.temporalAnterior}")
                arbol.addc3d(f"Pila[{temporal1}] = {temporal2}")
                tabla.stack += 1
                return
            
    def comprobarTipo(self, tipoColumna, tipoValor, val):
        if (tipoColumna.tipo == Tipo_Dato.MONEY) and (tipoValor.tipo == Tipo_Dato.CHAR):
            if ',' in val:
                val = val.replace(',','')
            try:
                val = float(val)
            except:
                return False
            return True
        if (tipoColumna.tipo == Tipo_Dato.CHAR or tipoColumna.tipo == Tipo_Dato.VARCHAR or tipoColumna.tipo == Tipo_Dato.VARYING or tipoColumna.tipo == Tipo_Dato.CHARACTER or tipoColumna.tipo == Tipo_Dato.TEXT) and (tipoValor.tipo == Tipo_Dato.CHAR or tipoValor.tipo == Tipo_Dato.VARCHAR or tipoValor.tipo == Tipo_Dato.VARYING or tipoValor.tipo == Tipo_Dato.CHARACTER or tipoValor.tipo == Tipo_Dato.TEXT):
            if tipoColumna.dimension != None:
                pass
            return True
        elif (tipoColumna.tipo == Tipo_Dato.SMALLINT or tipoColumna.tipo == Tipo_Dato.INTEGER or tipoColumna.tipo == Tipo_Dato.BIGINT or tipoColumna.tipo == Tipo_Dato.DECIMAL or tipoColumna.tipo == Tipo_Dato.NUMERIC or tipoColumna.tipo == Tipo_Dato.REAL or tipoColumna.tipo == Tipo_Dato.DOUBLE_PRECISION or tipoColumna.tipo == Tipo_Dato.MONEY) and (tipoValor.tipo == Tipo_Dato.SMALLINT or tipoValor.tipo == Tipo_Dato.INTEGER or tipoValor.tipo == Tipo_Dato.BIGINT or tipoValor.tipo == Tipo_Dato.DECIMAL or tipoValor.tipo == Tipo_Dato.NUMERIC or tipoValor.tipo == Tipo_Dato.REAL or tipoValor.tipo == Tipo_Dato.DOUBLE_PRECISION or tipoValor.tipo == Tipo_Dato.MONEY):
            if tipoColumna.tipo == Tipo_Dato.SMALLINT:
                pass
            elif tipoColumna.tipo == Tipo_Dato.INTEGER:
                pass
            elif tipoColumna.tipo == Tipo_Dato.BIGINT:
                pass
            return True
        elif (tipoColumna.tipo == Tipo_Dato.DATE or tipoColumna.tipo == Tipo_Dato.TIMESTAMP or tipoColumna.tipo == Tipo_Dato.TIME or tipoColumna.tipo == Tipo_Dato.INTERVAL or tipoColumna.tipo == Tipo_Dato.CHAR ) and (tipoValor.tipo == Tipo_Dato.DATE or tipoValor.tipo == Tipo_Dato.TIMESTAMP or tipoValor.tipo == Tipo_Dato.TIME or tipoValor.tipo == Tipo_Dato.INTERVAL or tipoValor.tipo == Tipo_Dato.CHAR):
            return True
        elif (tipoColumna.tipo == Tipo_Dato.BOOLEAN) and (tipoValor.tipo == Tipo_Dato.BOOLEAN):
            return True
        return False        
        