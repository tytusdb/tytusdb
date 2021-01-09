
from Instrucciones.Expresiones import Primitivo
from typing import Container
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Identificador import Identificador

class Llamada(Instruccion):
    def __init__(self, id,lista_expresion, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.lista_expresion = lista_expresion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        # ¿Hay errrores en los parámetros?
        listaTiposArgumentos = []
        for i in self.lista_expresion:
            resultado = i.analizar(tabla, arbol)
            if isinstance(resultado, Excepcion):
                return resultado
            listaTiposArgumentos.append(resultado)
        
        f = tabla.getSimboloFuncion(self.id)
        if f == None:
            error = Excepcion("42723", "Semantico", f"No existe la función {self.id}.", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error 
        else:
            if not f.funcion.activa:
                error = Excepcion("42723", "Semantico", f"La función: {self.id} no existe.", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error

        listaTiposFuncion = []
        for i in f.funcion.parametros:
            listaTiposFuncion.append(i.tipo)
        
        if len(listaTiposArgumentos) != len(listaTiposFuncion):
            error = Excepcion("42723", "Semantico", f"La cantidad de argumentos no coincide con la cantidad de parámetros en la función {self.id}.", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error 
        
        hayError = False
        for i in range(0,len(listaTiposFuncion)):
            comprobar = self.comprobarTipo(listaTiposFuncion[i], listaTiposArgumentos[i], None)
            if not comprobar: 
                error = Excepcion("42723", "Semantico", f"Los tipos de argumentos no coincide con los tipos de parámetros en la función {self.id}.", self.linea, self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
        
        if hayError:
            return

        
        if f.tipo.tipo == Tipo_Dato.VOID:
            return None
        return f.tipo

        
    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)
        retorno = Nodo3D()
        funcion = tabla.getSimboloFuncion(self.id)
        arbol.addComen("Simulando el paso de parámetros")
        temporal1 = tabla.getTemporal()
        arbol.addc3d(f"{temporal1} = P + {funcion.tamanio}")
        
        arbol.addComen("Asignación de parámetros")
        if funcion.tipo.tipo == Tipo_Dato.VOID:
            for i in range(0,len(self.lista_expresion)):
                valor = self.lista_expresion[i].traducir(tabla, arbol)
                temporal2 = tabla.getTemporal()
                arbol.addc3d(f"{temporal2} = {temporal1} + {i}")
                arbol.addc3d(f"Pila[{temporal2}] = \"{valor.temporalAnterior}\"")
        else:
            for i in range(0,len(self.lista_expresion)):
                valor = self.lista_expresion[i].traducir(tabla, arbol)
                temporal2 = tabla.getTemporal()
                arbol.addc3d(f"{temporal2} = {temporal1} + {i+1}")
                arbol.addc3d(f"Pila[{temporal2}] = {valor.temporalAnterior}")
        
        temporal3 = tabla.getTemporal()
        temporal4 = tabla.getTemporal()
        arbol.addComen("Cambio de ámbito")
        arbol.addc3d(f"P = P + {funcion.tamanio}")
        arbol.addComen("Llamada a la función")
        arbol.addc3d(f"{self.id}()")
        if funcion.tipo.tipo != Tipo_Dato.VOID:
            arbol.addComen("Posición del return en el ámbito de la función")
            arbol.addc3d(f"{temporal3} = {temporal1} + 0")
            arbol.addc3d(f"{temporal4} = Pila[{temporal3}]")        
        arbol.addc3d(f"P = P - {funcion.tamanio}")
        retorno.temporalAnterior = temporal4
        return retorno
        
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
        
    def concatenar(self, tabla,arbol):
        #ESTO SE AGREGO------------------------
        for expre in self.lista_expresion:
            if isinstance(expre, Primitivo.Primitivo):
                if expre.tipo.tipo==Tipo_Dato.CHAR or expre.tipo.tipo==Tipo_Dato.TEXT:
                    expre.valor = f"\\'{expre.valor}\\'"
        #FIN ESTO SE AGREGO------------------------
        valor = self.traducir(tabla, arbol)
        concatenar = "{"
        concatenar +=f"{valor.temporalAnterior}"
        concatenar +="}"
        return concatenar

    def concatenar2(self, tabla,arbol):
        #print("PASO POR EL CONCATENAR2")
        cadena = f"{self.id}("
        if self.lista_expresion != None:
            for col in self.lista_expresion:
                if isinstance(col, Identificador):
                    cadena += col.concatenar(tabla,arbol)
                else:
                    cadena += col.traducir(tabla,arbol) 
                #col.concatenar(tabla, arbol)
        cadena += ")"
        return cadena

    def parseindex(self, tabla, arbol):
        cadena = f""
        if self.lista_expresion != None:
            for col in self.lista_expresion:
                if isinstance(col, Identificador):
                    cadena += col.concatenar(tabla,arbol)
                else:
                    cadena += col.traducir(tabla,arbol) 
                #col.concatenar(tabla, arbol)
        return cadena