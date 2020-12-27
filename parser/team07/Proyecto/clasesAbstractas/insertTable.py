from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import retornoInstruccion
from tabla_Simbolos import tipoSimbolo
from tabla_Simbolos import simboloColumna
import jsonMode

class InsertTable(InstruccionAbstracta):

    def __init__(self, nombreTabla, listaColumnas = [], listaExpresiones=[], defaultValues = False):
        self.nombreTabla = nombreTabla
        self.listaColumnas = listaColumnas
        self.listaExpresiones = listaExpresiones
        self.defaultValues = defaultValues     # True --> Inserta los valors Default



    

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
                # ********************************************************
                # ********************************************************
                listaInformacionEnviar = []
                columnasTabla = simTabla.columnas

                # Se evalua si es un insert con solo valores default
                if self.defaultValues == True:
                    # Se evalua si se especificaron columnas
                    if len(self.listaColumnas) == 0:
                        # Se evalua que todos las columnas tengan el valor default o bien sean null
                        # Falta manejar los unique y si es llave foránea

                        for columna in columnasTabla:

                            if columna.primaryKey == True:
                                nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La columna: "+columna.nombre+", es llave primaria no puede aceptar valores default ni null")
                                listaErrores.append(nodoError)
                                nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                return nodoRetorno
                            elif columna.defaultValue != None:
                                listaInformacionEnviar.append(columna.defaultValue)
                            elif columna.null == True:
                                listaInformacionEnviar.append(None)
                            else:
                                nodoError = errorReportar.ErrorReportar(self.fila, self.columna, "Ejecucion", "La columna con nombre: "+columna.nombre +", no tiene valor default asignado y tampoco acepta valores null")
                                listaErrores.append(nodoError)
                                nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                return nodoRetorno                        
                        
                        # ****************************************************
                        #        Se manda a ejecutar la funcion              *
                        # ****************************************************
                        resultado = jsonMode.insert(str(tabalSimbolos.useDataBase.nombre),str(self.nombreTabla),listaInformacionEnviar)

                        if resultado == 0:
                            tabalSimbolos.guardarMensajeEjecucion("Insercion de tupla realizada correctamente a la tabla: "+self.nombreTabla)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.NORMAL,None)
                            return nodoRetorno
                        elif resultado == 1:                           
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Error al intentar guardar la información")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno
                        elif resultado == 2:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La base se de datos no existe")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno
                            
                        elif resultado == 3:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La tabla con nombre: "+self.nombreTabla+" no existe")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno

                        elif  resultado == 4:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Llave primaria duplicada")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno
                        elif  resultado == 5:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Numero de columnas no coincide con el número de columnas a insertar")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno
                    else:
                        #Se evalua que las columnas seleccionas existan en la tabla
                        for colSel in self.listaColumnas:
                            if (simTabla.comprobarNombreColumna(str(colSel.valor))) == 0:
                                nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La columna con nombre: "+str(colSel.valor)+" no existe dentro de la tabla: "+self.nombreTabla)
                                listaErrores.append(nodoError)
                                nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                return nodoRetorno

                        # Se crea la tupla a insertar
                        for columna in columnasTabla:

                            if columna.primaryKey == True:
                                nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La columna: "+columna.nombre+", es llave primaria no puede aceptar valores default ni null")
                                listaErrores.append(nodoError)
                                nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                return nodoRetorno
                            elif columna.defaultValue != None:
                                listaInformacionEnviar.append(columna.defaultValue)
                            elif columna.null == True:
                                listaInformacionEnviar.append(None)
                            else:
                                nodoError = errorReportar.ErrorReportar(self.fila, self.columna, "Ejecucion", "La columna con nombre: "+columna.nombre +", no tiene valor default asignado y tampoco acepta valores null")
                                listaErrores.append(nodoError)
                                nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                return nodoRetorno                  
                    # **************************************************
                    # Se manda a ejecutar la funcion de Inserte del ingeniero   *
                    # **************************************************
                        resultado = jsonMode.insert(str(tabalSimbolos.useDataBase.nombre),str(self.nombreTabla),listaInformacionEnviar)

                        if resultado == 0:
                            tabalSimbolos.guardarMensajeEjecucion("Insercion de tupla realizada correctamente a la tabla: "+self.nombreTabla)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.NORMAL,None)
                            return nodoRetorno
                        elif resultado == 1:                           
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Error al intentar guardar la información")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno
                        elif resultado == 2:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La base se de datos no existe")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno
                            
                        elif resultado == 3:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La tabla con nombre: "+self.nombreTabla+" no existe")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno

                        elif  resultado == 4:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Llave primaria duplicada")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno
                        elif  resultado == 5:
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Numero de columnas no coincide con el número de columnas a insertar")
                            listaErrores.append(nodoError)
                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                            return nodoRetorno
                else:

                    if len(self.listaColumnas) == 0:
                        # Se mandan a ejecutar las expresiones a insertar por tuplas 
                        for tupla in self.listaExpresiones:
                            listaExp = tupla.hijos[0]
                            listaSimbolosEjecutados = []
                            listaValoresInsertar = []

                            # Se ejecutan las expresiones para insertar
                            for expresion in listaExp.hijos:
                                simb = expresion.ejecutar(tabalSimbolos,listaErrores)
                                if simb != None:
                                    listaSimbolosEjecutados.append(simb)
                                else:
                                    #El error ya fue reportado en la ejecución de la expresion
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno

                            #Se evalua que tengan el mismo número de columnas
                            if len(columnasTabla) == len(listaSimbolosEjecutados):
                                #Se evaluan los tipos de datos que sean igual
                                indice = 0
                                for column in columnasTabla:
                                    #Se obtiene el simbolo ejecutado
                                    valorInsertar = listaSimbolosEjecutados[indice]

                                    #Inicio Enum

                                    if column.tipoDato == simboloColumna.TiposDatos.enum:
                                    #Es un enum
                                        simboloEnum = column.tipoDatoNOprimitivo

                                        if simboloEnum != None:
                                            bandera = False
                                            for enumm in simboloEnum.posiblesValores:
                                                if (enumm.lower()==str(valorInsertar.valorRetorno).lower()):
                                                    bandera = True

                                            if bandera == False:
                                                NodoErr = errorReportar.ErrorReportar(self.fila, self.columna,"Ejecución","El valor a ingresar no se encuentra dentro del enumn: "+simboloEnum.nombre)
                                                listaErrores.append(NodoErr)
                                                retorr = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                                return retorr
                                            else:
                                                listaValoresInsertar.append(valorInsertar.valorRetorno) 
                                        
                                        else:
                                            nodoErr = errorReportar.ErrorReportar(self.fila,self.columna, "Ejecucion", "La columna esta declarada cono tipo de dato Enum, pero no tienen ningún enum asociado")
                                            listaErrores.append(nodoErr)
                                            retorr = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                            return retorr
                                    # Fin enum
                                    elif valorInsertar.tipoDatoRetorno == simboloColumna.TiposDatos.default:
                                        if column.defaultValue!=None:
                                            listaValoresInsertar.append(str(column.defaultValue))
                                        else:
                                            nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La columna con nombre: "+column.nombre+" no tiene valor por default asignado")
                                            listaErrores.append(nodoErr)
                                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                            return nodoRetorno

                                    elif valorInsertar.tipoDatoRetorno == simboloColumna.TiposDatos.nulo:
                                        if column.null == True:
                                            listaValoresInsertar.append(None)                                        
                                        else:
                                            nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion", "La columna con nombre: "+column.nombre+", no acepta valores nulos")
                                            listaErrores.append(nodoErr)
                                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                            return nodoRetorno

                                    else:                                                                                

                                        filaa = column.tipoDato.value
                                        columnaa =  valorInsertar.tipoDatoRetorno.value

                                        #Se realiza la comprobación de tipos
                                        comprobarTipos = tabalSimbolos.obtenerTipoDato(filaa,columnaa)
                                        simboloRecibido = comprobarTipos.operar(tipoSimbolo.TipoSimbolo.COLUMNA_DATO)

                                        if simboloRecibido != None:
                                            if simboloRecibido.descripcionError == None:
                                                # Falta evalular unique
                                                # Se guarda el valor como tal
                                                listaValoresInsertar.append(valorInsertar.valorRetorno)                                                
                                            else:
                                                nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion",simboloRecibido.descripcionError)
                                                listaErrores.append(nodoErr)
                                                nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                                return nodoRetorno


                                        else:
                                            nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error de tipos al intentar insertar valor a la columna: "+columna.nombre)
                                            listaErrores.append(nodoErr)
                                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                            return nodoRetorno                          
                                    indice = indice + 1

                                # ***********************************************
                                # *         Se inserta la tupa                  *
                                # ***********************************************
                                resultado = jsonMode.insert(str(tabalSimbolos.useDataBase.nombre),str(self.nombreTabla),listaValoresInsertar)

                                if resultado == 0:
                                    tabalSimbolos.guardarMensajeEjecucion("Insercion de tupla realizada correctamente a la tabla: "+self.nombreTabla)
                                   
                                elif resultado == 1:                           
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Error al intentar guardar la información")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno
                                elif resultado == 2:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La base se de datos no existe")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno
                                    
                                elif resultado == 3:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La tabla con nombre: "+self.nombreTabla+" no existe")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno

                                elif  resultado == 4:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Llave primaria duplicada")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno
                                elif  resultado == 5:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Numero de columnas no coincide con el número de columnas a insertar")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno                         
                                
                            else:
                                errorN = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","No ingreso todos los valores para las columnas de la tabla: "+self.nombreTabla)
                                listaErrores.append(errorN)
                                nodoRet = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                return nodoRet
                        
                        nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.NORMAL,None)
                        return nodoRetorno
                    else:
                        #Se evalua que las tuplas traigan la misma cantidad de columnas y que esta cantida
                        #se igual al número de columnas seleccionadas

                        #se setea el valor de la primar fila
                        contadorColumnas = 0
                        if len(self.listaExpresiones) > 0:
                            listaExp = self.listaExpresiones[0].hijos[0]
                            contadorColumnas = len(listaExp.hijos)                        
                                               
                        for tupla in self.listaExpresiones:
                            listaExp = tupla.hijos[0]
                            if len(listaExp.hijos) != contadorColumnas:
                                nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Todas las tuplas a insertar deben de tener el mismo número de columnas")
                                listaErrores.append(nodoError)
                                nodoRetor = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR, None)
                                return nodoRetor
                        
                        #Se evalua que el número de columnas sea igual al numero de columnas seleccionadas:
                        if contadorColumnas != len(self.listaColumnas):
                            nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Las tuplas a insertar deben de tener el mismo número de columnas seleccionadas")
                            listaErrores.append(nodoError)
                            nodoRetor = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR, None)
                            return nodoRetor

                        #Se evalua que no vengan columnas con el mismo nombre
                        for nombreColumna in self.listaColumnas:
                            contador = 0
                            for nombreCol2 in self.listaColumnas:
                                if nombreColumna.lower() == nombreCol2.lower():
                                    contador = contador + 1

                            if contador > 1:
                                nodoErro = errorReportar.ErrorReportar(self.fila, self.columna,"Ejecucion","Nombre de columna: "+str(nombreColumna)+" repetida")
                                listaErrores.append(nodoErro)
                                nodoRetornar = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR, None)
                                return nodoRetornar



                        
                        # Se mandan a ejecutar las expresiones a insertar por tuplas 
                        for tupla in self.listaExpresiones:
                            listaExp = tupla.hijos[0]
                            listaSimbolosEjecutados = []
                            listaValoresInsertar = []

                            # Se ejecutan las expresiones para insertar
                            for expresion in listaExp.hijos:
                                simb = expresion.ejecutar(tabalSimbolos,listaErrores)
                                if simb != None:
                                    listaSimbolosEjecutados.append(simb)
                                else:
                                    #El error ya fue reportado en la ejecución de la expresion
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno

                            #Se evalua que tengan el mismo número de columnas
                            if len(self.listaColumnas) == len(listaSimbolosEjecutados):
                                #Se evaluan los tipos de datos que sean igual
                                
                                for column in columnasTabla:

                                    #Se busca si esta columna fue seleccionada
                                    indice = 0
                                    bandera = False
                                    for nombreCol in self.listaColumnas:
                                        if nombreCol.lower() == column.nombre.lower():

                                            bandera = True
                                            valorInsertar = listaSimbolosEjecutados[indice]

                                            #Inicio Enum

                                            if column.tipoDato == simboloColumna.TiposDatos.enum:
                                            #Es un enum
                                                simboloEnum = column.tipoDatoNOprimitivo

                                                if simboloEnum != None:
                                                    bandera = False
                                                    for enumm in simboloEnum.posiblesValores:
                                                        if (enumm.lower()==str(valorInsertar.valorRetorno).lower()):
                                                            bandera = True

                                                    if bandera == False:
                                                        NodoErr = errorReportar.ErrorReportar(self.fila, self.columna,"Ejecución","El valor a ingresar no se encuentra dentro del enumn: "+simboloEnum.nombre)
                                                        listaErrores.append(NodoErr)
                                                        retorr = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                                        return retorr
                                                    else:
                                                        listaValoresInsertar.append(valorInsertar.valorRetorno) 
                                                
                                                else:
                                                    nodoErr = errorReportar.ErrorReportar(self.fila,self.columna, "Ejecucion", "La columna esta declarada cono tipo de dato Enum, pero no tienen ningún enum asociado")
                                                    listaErrores.append(nodoErr)
                                                    retorr = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                                    return retorr
                                            # Fin enum
                                            elif valorInsertar.tipoDatoRetorno == simboloColumna.TiposDatos.default:
                                                if column.defaultValue!=None:
                                                    listaValoresInsertar.append(str(column.defaultValue))
                                                else:
                                                    nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La columna con nombre: "+column.nombre+" no tiene valor por default asignado")
                                                    listaErrores.append(nodoErr)
                                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                                    return nodoRetorno

                                            elif valorInsertar.tipoDatoRetorno == simboloColumna.TiposDatos.nulo:
                                                if column.null == True:
                                                    listaValoresInsertar.append(None)                                        
                                                else:
                                                    nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion", "La columna con nombre: "+column.nombre+", no acepta valores nulos")
                                                    listaErrores.append(nodoErr)
                                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                                    return nodoRetorno

                                            else:                                                                                

                                                filaa = column.tipoDato.value
                                                columnaa =  valorInsertar.tipoDatoRetorno.value

                                                #Se realiza la comprobación de tipos
                                                comprobarTipos = tabalSimbolos.obtenerTipoDato(filaa,columnaa)
                                                simboloRecibido = comprobarTipos.operar(tipoSimbolo.TipoSimbolo.COLUMNA_DATO)

                                                if simboloRecibido != None:
                                                    if simboloRecibido.descripcionError == None:
                                                        # Falta evalular unique
                                                        # Se guarda el valor como tal
                                                        listaValoresInsertar.append(valorInsertar.valorRetorno)                                                
                                                    else:
                                                        nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion",simboloRecibido.descripcionError)
                                                        listaErrores.append(nodoErr)
                                                        nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                                        return nodoRetorno


                                                else:
                                                    nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error de tipos al intentar insertar valor a la columna: "+columna.nombre)
                                                    listaErrores.append(nodoErr)
                                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                                    return nodoRetorno     
                                        
                                        indice = indice + 1
                                    
                                    # Si la columna no fue seleccionada se manda a ver si tiene 
                                    # valor por default o acepta null
                                    if bandera == False:
                                        if column.defaultValue!=None:
                                            listaValoresInsertar.append(str(column.defaultValue))
                                        elif column.null == True:
                                            listaValoresInsertar.append(None)   
                                        else:
                                            nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La columna con nombre: "+column.nombre+" no tiene valor por default asignado, tampoco acepta valores nulos")
                                            listaErrores.append(nodoErr)
                                            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                            return nodoRetorno                             
                                        

                                # ***********************************************
                                # *         Se inserta la tupa                  *
                                # ***********************************************
                                resultado = jsonMode.insert(str(tabalSimbolos.useDataBase.nombre),str(self.nombreTabla),listaValoresInsertar)

                                if resultado == 0:
                                    tabalSimbolos.guardarMensajeEjecucion("Insercion de tupla realizada correctamente a la tabla: "+self.nombreTabla)
                                   
                                elif resultado == 1:                           
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Error al intentar guardar la información")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno
                                elif resultado == 2:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La base se de datos no existe")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno
                                    
                                elif resultado == 3:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La tabla con nombre: "+self.nombreTabla+" no existe")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno

                                elif  resultado == 4:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Llave primaria duplicada")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno
                                elif  resultado == 5:
                                    nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Numero de columnas no coincide con el número de columnas a insertar")
                                    listaErrores.append(nodoError)
                                    nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                    return nodoRetorno
                                
                            else:
                                errorN = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","No ingreso todos los valores para las columnas de la tabla de la tabla: "+self.nombreTabla)
                                listaErrores.append(errorN)
                                nodoRet = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                                return nodoRet
                        
                        nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.NORMAL,None)
                        return nodoRetorno
                        



                








              
        
        


 



       

