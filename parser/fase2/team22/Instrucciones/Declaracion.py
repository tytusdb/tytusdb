from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from lexico import columas
from tkinter.constants import FALSE
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.TablaSimbolos.Instruccion import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.Expresiones.Primitivo import Primitivo
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from storageManager.jsonMode import *

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
        

    def generar3D(self, tabla, arbol):  
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        # code.append(c3d.asignacionString(t0, "CREATE INDEX " + self.ID))
        code.append(c3d.asignacionString(t0, "CREATE INDEX test2_mm_idx ON tabla(id);"))
        #CREATE INDEX test2_mm_idx ON tabla(id);

        # code.append(c3d.operacion(t1, Identificador(t0), Valor("\";\"", "STRING"), OP_ARITMETICO.SUMA))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))

        return code