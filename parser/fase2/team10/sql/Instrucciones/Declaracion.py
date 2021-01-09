from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.Excepcion import Excepcion
from sql.lexico import columas
from tkinter.constants import FALSE
from sql.Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from sql.Instrucciones.TablaSimbolos.Instruccion import *
from sql.Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from sql.Instrucciones.TablaSimbolos.Simbolo import Simbolo
from sql.Instrucciones.Expresiones.Primitivo import Primitivo
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from sql.storageManager.jsonMode import *
class Declaracion(Instruccion):
    def __init__(self, nombre, tipo, expresion):
        Instruccion.__init__(self,tipo,0,0,"strGram")
        self.nombre=nombre
        self.tipo=tipo
        self.expresion = expresion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        prim = None
        strGram = ""
        if self.tipo.tipo == Tipo_Dato.SMALLINT:
            prim = Primitivo(0, Tipo(Tipo_Dato.SMALLINT), strGram,0,0)
        elif self.tipo.tipo == Tipo_Dato.INTEGER:
            prim = Primitivo(0, Tipo(Tipo_Dato.INTEGER), strGram,0,0)
        elif self.tipo.tipo == Tipo_Dato.BIGINT:
            prim = Primitivo(0, Tipo(Tipo_Dato.BIGINT), strGram, 0,0)
        elif self.tipo.tipo == Tipo_Dato.DECIMAL:
            prim = Primitivo(0, Tipo(Tipo_Dato.DECIMAL),strGram, 0,0)
        elif self.tipo.tipo == Tipo_Dato.NUMERIC:
            prim = Primitivo(0, Tipo(Tipo_Dato.NUMERIC), strGram,0,0)
        elif self.tipo.tipo == Tipo_Dato.REAL:
            prim = Primitivo(0, Tipo(Tipo_Dato.REAL), strGram,0,0)
        elif self.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
            prim = Primitivo(0, Tipo(Tipo_Dato.DOUBLE_PRECISION),strGram, 0,0)
        elif self.tipo.tipo == Tipo_Dato.MONEY:
            prim = Primitivo(0, Tipo(Tipo_Dato.MONEY),strGram, 0,0)
        elif self.tipo.tipo == Tipo_Dato.DATE:
            prim = Primitivo('1900-01-01', Tipo(Tipo_Dato.DATE),strGram, 0,0)
        elif self.tipo.tipo == Tipo_Dato.TIMESTAMP:
            prim = Primitivo('1900-01-01', Tipo(Tipo_Dato.TIMESTAMP),strGram, 0,0)
        elif self.tipo.tipo == Tipo_Dato.TIME:
            prim = Primitivo('1900-01-01', Tipo(Tipo_Dato.DATE),strGram, 0,0)
        elif self.tipo.tipo == Tipo_Dato.BOOLEAN:
            prim = Primitivo(True, Tipo(Tipo_Dato.BOOLEAN),strGram, 0,0)

        variable = Simbolo(self.nombre,self.tipo,prim.valor,0,0)
        resultadoInsertar = tabla.setVariable(variable)
        if resultadoInsertar != None:
            error = Excepcion("100","Semantico","La columna "+self.nombre+" yo existe",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if self.expresion != None:
            resultado = self.expresion.ejecutar(tabla, arbol)
            if isinstance(resultado, Excepcion):
                return resultado
        return True


