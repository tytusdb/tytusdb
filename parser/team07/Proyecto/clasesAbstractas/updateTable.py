
from .instruccionAbstracta import InstruccionAbstracta
from tabla_Simbolos import retornoInstruccion
from Errores import errorReportar
from .updateColumna import UpdateColumna
from tabla_Simbolos import simboloColumna
from .expresion import Expresion
import jsonMode

class UpdateTable(InstruccionAbstracta):

    def __init__(self, nombreTabla, listaUpdates, condicion):
        self.nombreTabla = nombreTabla
        self.condicion = condicion
        self.listaUpdates = listaUpdates


    
    # *************************************************************************************************
    # ************************************ Ejecución **************************************************
    # *************************************************************************************************
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
                # Se evalua que no vengan dos columnas con el mismo nombre
                for nodoColumnaSet in self.listaUpdates:
                    nombreCol = nodoColumnaSet.nombreColumna
                    contador = 0
                    for nodoCol2 in self.listaUpdates:
                        if nombreCol == nodoCol2.nombreColumna:
                            contador = contador + 1
                    
                    if contador > 1:
                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Nombre de columna: "+nombreCol+" aparece con más de una asignacion")
                        listaErrores.append(nodoError)
                        Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                        return Retorno

                # se empiezan a ejecutar todos los sets
                listaSets = {}      #Guardará los simbolos ejecutados con su nombre de columna

                for nodoColumnaSet in self.listaUpdates:
                    if isinstance(nodoColumnaSet, UpdateColumna):
                        # Se setea el nombre de la tabla
                        nodoColumnaSet.nombreTabla = self.nombreTabla
                        simbRecibido = nodoColumnaSet.ejecutar(tabalSimbolos,listaErrores)
                        
                        if simbRecibido != None:
                            #Se guarde el indice de la columna que viene en nombreColumnaDerecho y su valor que viene en valorRetorno
                            listaSets[int(simbRecibido.nombreColumnaDerecho)] = simbRecibido.valorRetorno
                        else:
                            #Hubo error, el error ya fue reportado
                            retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return retorno
                    else:
                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","No se pudo ejecutar la instruccion para setera el valor a la columna")
                        listaErrores.append(nodoError)
                        Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                        return Retorno

                #Se trae la tabla de datos con la informacion
                tablaDatos = jsonMode.extractTable(tabalSimbolos.useDataBase.nombre,self.nombreTabla)
                if tablaDatos == None:
                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","No ahy informacion en la tabla: "+self.nombreTabla)
                    listaErrores.append(nodoError)
                    Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                    return Retorno

                


                #Se manda a ejecutar la condicion
                if self.condicion != None:
                    simboloCondicion = self.condicion.ejecutar(tabalSimbolos,listaErrores)

                    if simboloCondicion != None:
                        if simboloCondicion.tipoDatoRetorno == simboloColumna.TiposDatos.columna:
                            nombreColumnaIzquierda = simboloCondicion.nombreColumnaIzquierdo
                            nombreColumnaDerecha = simboloCondicion.nombreColumnaDerecho
                            listaIndices = []

                            if nombreColumnaIzquierda != None and nombreColumnaDerecha != None:
                                #Se va a traer la información de las dos columnas 
                                columnaIzquierda = simTabla.obtenerSimboloColumna(nombreColumnaIzquierda)
                                columnaDerecha = simTabla.obtenerSimboloColumna(nombreColumnaDerecha)

                                if columnaIzquierda == None:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La columna con nombre: "+nombreColumnaIzquierda+", no existe dentro de la tabla: "+self.nombreTabla)
                                    listaErrores.append(nodoError)
                                    Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return Retorno
                                if columnaDerecha == None:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La columna con nombre: "+nombreColumnaDerecha+", no existe dentro de la tabla: "+self.nombreTabla)
                                    listaErrores.append(nodoError)
                                    Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return Retorno
                                
                                indiceIzquierdo = columnaIzquierda.indice
                                indiceDerecho = columnaDerecha.indice
                                tipoDatoIzquierdo = columnaIzquierda.tipoDato
                                tipoDatoDerecho = columnaDerecha.tipoDato

                                if tipoDatoIzquierdo == simboloColumna.TiposDatos.enum:
                                    tipoDatoIzquierdo = simboloColumna.TiposDatos.varchar
                                if tipoDatoDerecho == simboloColumna.TiposDatos.enum:
                                    tipoDatoDerecho = simboloColumna.TiposDatos.varchar

                                indice = 0
                                for tupla in tablaDatos:
                                    valorIzquierdo = tupla[indiceIzquierdo]
                                    valorDerecho = tupla[indiceDerecho]
                                    expIzquierdo = Expresion()
                                    expIzquierdo.valorPrimitivo(valorIzquierdo,tipoDatoIzquierdo)
                                    expDerecho = Expresion()
                                    expDerecho.valorPrimitivo(valorDerecho,tipoDatoDerecho)
                                    operacion = Expresion()
                                    operacion.operacionBinaria(expIzquierdo,expDerecho,simboloCondicion.tipoOperacion)

                                    simboOperacion = operacion.ejecutar(tabalSimbolos,listaErrores)
                                    if simboOperacion != None:
                                        if simboOperacion.tipoDatoRetorno == simboloColumna.TiposDatos.boolean:
                                            if str(simboOperacion.valorRetorno).lower() == "true":
                                                listaIndices.append[indice]

                                    else:
                                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error al ejecutar la condición del update")
                                        listaErrores.append(nodoError)
                                        Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                        return Retorno  
                                    indice = indice + 1

                            # SOLO Columna Izquierda 
                            elif nombreColumnaIzquierda != None:
                                #Se va a traer la información de las dos columnas 
                                columnaIzquierda = simTabla.obtenerSimboloColumna(nombreColumnaIzquierda)                               

                                if columnaIzquierda == None:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La columna con nombre: "+nombreColumnaIzquierda+", no existe dentro de la tabla: "+self.nombreTabla)
                                    listaErrores.append(nodoError)
                                    Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return Retorno
                               
                                
                                indiceIzquierdo = columnaIzquierda.indice                                
                                tipoDatoIzquierdo = columnaIzquierda.tipoDato                                
                                tipoDatoDerecho = simboloCondicion.descripcionError

                                if tipoDatoIzquierdo == simboloColumna.TiposDatos.enum:
                                    tipoDatoIzquierdo = simboloColumna.TiposDatos.varchar
                                

                                indice = 0
                                for tupla in tablaDatos:
                                    valorIzquierdo = tupla[indiceIzquierdo]
                                    valorDerecho = simboloCondicion.valorRetorno
                                    expIzquierdo = Expresion()
                                    expIzquierdo.valorPrimitivo(valorIzquierdo,tipoDatoIzquierdo)
                                    expDerecho = Expresion()
                                    expDerecho.valorPrimitivo(valorDerecho,tipoDatoDerecho)
                                    operacion = Expresion()
                                    operacion.operacionBinaria(expIzquierdo,expDerecho,simboloCondicion.tipoOperacion)

                                    simboOperacion = operacion.ejecutar(tabalSimbolos,listaErrores)
                                    if simboOperacion != None:
                                        if simboOperacion.tipoDatoRetorno == simboloColumna.TiposDatos.boolean:
                                            if str(simboOperacion.valorRetorno).lower() == "true":
                                                listaIndices.append(indice)

                                    else:
                                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error al ejecutar la condición del update")
                                        listaErrores.append(nodoError)
                                        Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                        return Retorno 
                                    indice = indice + 1 
                            else:
                                #Se va a traer la información de la columna Derecha 
                                columnaDerecha = simTabla.obtenerSimboloColumna(nombreColumnaDerecha)                               

                                if columnaDerecha == None:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La columna con nombre: "+nombreColumnaDerecha+", no existe dentro de la tabla: "+self.nombreTabla)
                                    listaErrores.append(nodoError)
                                    Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return Retorno
                               
                                
                                indiceDerecho = columnaDerecha.indice                                
                                tipoDatoDerecho = columnaDerecha.tipoDato                                
                                tipoDatoIzquierdo = simboloCondicion.descripcionError

                                if indiceDerecho == simboloColumna.TiposDatos.enum:
                                    indiceDerecho = simboloColumna.TiposDatos.varchar
                                

                                indice = 0
                                for tupla in tablaDatos:
                                    valorIzquierdo = simboloCondicion.valorRetorno
                                    valorDerecho =  tupla[indiceIzquierdo]
                                    expIzquierdo = Expresion()
                                    expIzquierdo.valorPrimitivo(valorIzquierdo,tipoDatoIzquierdo)
                                    expDerecho = Expresion()
                                    expDerecho.valorPrimitivo(valorDerecho,tipoDatoDerecho)
                                    operacion = Expresion()
                                    operacion.operacionBinaria(expIzquierdo,expDerecho,simboloCondicion.tipoOperacion)

                                    simboOperacion = operacion.ejecutar(tabalSimbolos,listaErrores)
                                    if simboOperacion != None:
                                        if simboOperacion.tipoDatoRetorno == simboloColumna.TiposDatos.boolean:
                                            if str(simboOperacion.valorRetorno).lower() == "true":
                                                listaIndices.append[indice]

                                    else:
                                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error al ejecutar la condición del update")
                                        listaErrores.append(nodoError)
                                        Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                        return Retorno  
                                    indice = indice + 1

                            # se hacen los update
                            contador = 0
                            for miIndice in listaIndices:
                                
                                resultado = jsonMode.update(tabalSimbolos.useDataBase.nombre,self.nombreTabla,listaSets,[str(miIndice)])

                                if resultado == 0:
                                    contador = contador + 1
                                elif resultado == 1:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error al intentar actualiazar la información de la columna: "+self.nombreTabla)
                                    listaErrores.append(nodoError)
                                    retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return retorno
                                elif resultado == 2:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La base de datos con nombre: "+tabalSimbolos.useDataBase.nombre+", no existe")
                                    listaErrores.append(nodoError)
                                    retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return retorno
                                elif resultado == 3:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La tabla de datos con nombre: "+self.nombreTabla+", no existe")
                                    listaErrores.append(nodoError)
                                    retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return retorno
                                elif resultado == 4:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La llave primaria no se encontro, no se pudo realizar la actualización ")
                                    listaErrores.append(nodoError)
                                    retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return retorno
                                
                                
                            
                            tabalSimbolos.guardarMensajeEjecucion("Se actualizaron: "+str(contador)+" registros de la tabla: "+self.nombreTabla)
                            Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.NORMAL,None)
                            return Retorno

                        else:
                            #No hay condiciónn que comparar, se afecta a todos los registros 
                            indice = 0
                            contador = 0
                            for tupla in tablaDatos:
                                resultado = jsonMode.update(tabalSimbolos.useDataBase.nombre,self.nombreTabla,listaSets,[str(indice)])

                                if resultado == 0:
                                    contador = contador + 1
                                elif resultado == 1:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error al intentar actualiazar la información de la columna: "+self.nombreTabla)
                                    listaErrores.append(nodoError)
                                    retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return retorno
                                elif resultado == 2:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La base de datos con nombre: "+tabalSimbolos.useDataBase.nombre+", no existe")
                                    listaErrores.append(nodoError)
                                    retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return retorno
                                elif resultado == 3:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La tabla de datos con nombre: "+self.nombreTabla+", no existe")
                                    listaErrores.append(nodoError)
                                    retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return retorno
                                elif resultado == 4:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La llave primaria no se encontro, no se pudo realizar la actualización ")
                                    listaErrores.append(nodoError)
                                    retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return retorno
                                
                                indice = indice + 1
                            
                            tabalSimbolos.guardarMensajeEjecucion("Se actualizaron: "+str(contador)+" registros de la tabla: "+self.nombreTabla)
                            Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.NORMAL,None)
                            return Retorno
                    else:
                        tabalSimbolos.guardarMensajeEjecucion("Se actualizaron: 0 registros de la tabla: "+self.nombreTabla)
                        nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                        return nodoRetorno
                else:
                    #no hay condición se actualizan todos los registros
                    indice = 0
                    contador = 0
                    for tupla in tablaDatos:
                        resultado = jsonMode.update(tabalSimbolos.useDataBase.nombre,self.nombreTabla,listaSets,[str(indice)])

                        if resultado == 0:
                            contador = contador + 1
                        elif resultado == 1:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error al intentar actualiazar la información de la columna: "+self.nombreTabla)
                            listaErrores.append(nodoError)
                            retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return retorno
                        elif resultado == 2:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La base de datos con nombre: "+tabalSimbolos.useDataBase.nombre+", no existe")
                            listaErrores.append(nodoError)
                            retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return retorno
                        elif resultado == 3:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La tabla de datos con nombre: "+self.nombreTabla+", no existe")
                            listaErrores.append(nodoError)
                            retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return retorno
                        elif resultado == 4:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La llave primaria no se encontro, no se pudo realizar la actualización ")
                            listaErrores.append(nodoError)
                            retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return retorno
                        
                        indice = indice + 1
                    
                    tabalSimbolos.guardarMensajeEjecucion("Se actualizaron: "+str(contador)+" registros de la tabla: "+self.nombreTabla)
                    Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.NORMAL,None)
                    return Retorno



                    

        

