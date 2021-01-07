from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import tablaSimbolos,simboloBaseDatos,simboloNuevoTipo
import jsonMode

class createType(InstruccionAbstracta):

    def __init__(self, nombre, listaExpresiones=[]):
        self.nombre = nombre
        self.listaExpresiones = listaExpresiones

    

    def ejecutar(self, tabalSimbolos, listaErrores):
        baseDatos =  tabalSimbolos.obtenerBaseDatos(tabalSimbolos.useDataBase)
        bandera = baseDatos.comprobarNombreTipo(self.nombre)
        if bandera == 1:
            #Tipo ya existe
            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P07")
            listaErrores.append(errorEnviar)
            return
        elif bandera == 0:
            nuevoTipo = simboloNuevoTipo.SimboloNuevoTipo(self.nombre,self.listaExpresiones)
            baseDatos.agregarTipo(nuevoTipo)  
        pass   

