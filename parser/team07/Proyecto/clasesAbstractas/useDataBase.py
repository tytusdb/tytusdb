from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import retornoInstruccion

class UseDataBase(InstruccionAbstracta):


    def __init__(self, nombreDB):
        self.nombreBaseDatos = nombreDB


    # *************************************************************************************************
    # *********************************** Metodo de Ejecución *****************************************
    # *************************************************************************************************
    def ejecutar(self, tabalSimbolos, listaErrores):

        #Se evalua que la base de datos exista:
        if tabalSimbolos.setUseDataBase(self.nombreBaseDatos) == 0:
            # Base de datos no existe
            nodoError = errorReportar.ErrorReportar(self.fila, self.columna, "Ejecucion","Base de datos con nombre: "+self.nombreBaseDatos+", no existe")
            listaErrores.append(nodoError)
            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
            return  nodoRetorno
        else:
            #Base de datos encontrada
            tabalSimbolos.guardarMensajeEjecucion("Sentencia Use ejecutada correctamente")
            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.NORMAL, None)
            return nodoRetorno

        


        
