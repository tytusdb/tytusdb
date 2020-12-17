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
    def __init__(self, nombre, tipo, expresion):
        self.nombre=nombre
        self.tipo=tipo
        self.expresion = expresion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        prim = None
        if self.tipo.tipo == Tipo_Dato.INTEGER:
            prim = Primitivo(0, Tipo_Dato.INTEGER, 0,0)
        elif self.tipo.tipo == Tipo_Dato.NUMERIC:
            prim = Primitivo(0.0, Tipo_Dato.NUMERIC, 0,0)
        
        variable = Simbolo(self.nombre,self.tipo,prim,0,0)
        resultadoInsertar = tabla.setVariable(variable)
        if resultadoInsertar != None:
            error = Excepcion("100","Semantico","La columna "+self.nombre+" yo existe",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        resultado = self.expresion.ejecutar(tabla, arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        return True



