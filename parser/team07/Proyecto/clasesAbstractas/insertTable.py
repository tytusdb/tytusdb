from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import retornoInstruccion

class InsertTable(InstruccionAbstracta):

    def __init__(self, nombreTabla, listaColumnas = [], listaExpresiones=[], defaultValues = False):
        self.nombreTabla = nombreTabla
        self.listaColumnas = listaColumnas
        self.listaExpresiones = listaExpresiones
        self.defaultValues = defaultValues


    

    def ejecutar(self, tabalSimbolos, listaErrores):

        #se evalua que haya una base de datos en use
        if tabalSimbolos.useDataBase == None:
            nodoError = errorReportar.ErrorReportar(self.fila, self.columna,"Ejecucion","Ninguna base de datos en uso")
            listaErrores.append(nodoError)
            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
            return nodoRetorno
        else:
            #se evalua que la tabla a la que se va hacer el insert exista y se obtine el nodo de esa tabla
            simTabla = tabalSimbolos.useDataBase.obtenerTabla(self.nombreTabla)

            if simTabla == None:
                nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","42P01 - undefined_table "+self.nombreTabla)
                listaErrores.append(nodoError)
                nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR, None)
                return nodoRetorno
            else:
                pass






        print("Ejecutando InsertTable")             
        
        for tupla in self.listaExpresiones:
            listaExp = tupla.hijos[0]

            for expresion in listaExp.hijos:
                simb = expresion.ejecutar(tabalSimbolos,listaErrores)
                if simb != None:
                    print(simb.valorRetorno)
                else:
                    # guardar el valor como 
                    print("Nada")




        pass   

