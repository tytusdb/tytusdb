from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import tablaSimbolos,simboloTabla,simboloBaseDatos,simboloColumna
import jsonMode

class createTable(InstruccionAbstracta):
    '''
        Esta clase representa la instrucción crear tabla.
        La instrucción crear tabla tiene un ID y una lista de columnas y una posible herencia de otra tabla
    '''
    def __init__(self, identificador, herencia, columnas=[]):
        self.identificador = identificador
        self.columnas = columnas
        self.herencia = herencia


    def ejecutar(self, tabalSimbolos, listaErrores): 
        baseDatos =  tabalSimbolos.useDataBase
        bandera = baseDatos.comprobarNombreTabla(self.identificador)
        if bandera == 1:
            #Tabla ya existe
            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P07")
            listaErrores.append(errorEnviar)
            return
        else:
            #Nombre de tabla no existe en base de datos
            numColumnas = 0
            for columna in self.columnas:
                try:
                    if columna.hijos[0].nombreNodo == "ID":
                        numColumnas = numColumnas + 1
                except:
                    pass
            respuesta = jsonMode.createTable(tabalSimbolos.useDataBase.nombre,self.identificador,numColumnas)
            #Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos inexistente, 3 tabla existente.
            
            if respuesta == 2:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error, base de datos inexistente")
                listaErrores.append(errorEnviar)
                return
            elif respuesta == 3:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P07")
                listaErrores.append(errorEnviar)
                return
            elif respuesta == 1:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error en la operacion")
                listaErrores.append(errorEnviar)
                return
            elif respuesta == 0:
                #modificar el nombre que se envia de base de datos
                tablaGuardar = simboloTabla.SimboloTablas(self.identificador)
                try:
                    if self.herencia[0].hijos[0].nombreNodo == "ID":
                        comprobar = baseDatos.comprobarNombreTabla(self.herencia[0].hijos[0].valor)
                        if comprobar == 1:
                            tablaHerencia = baseDatos.obtenerTabla(self.herencia[0].hijos[0].valor)
                            tablaGuardar.columnas = tablaHerencia.columnas
                except:
                    pass
                indice = len(tablaGuardar.columnas)
                for columna in self.columnas:
                    try:
                        if columna.hijos[0].nombreNodo == "ID":
                            nuevaColumna = simboloColumna.SimboloColumna(indice,columna.hijos[0].valor,columna.hijos[1].valor)
                            
                            #Es un tipo de dato no primitivo
                            if nuevaColumna.tipoDato == simboloColumna.TiposDatos.enum:
                                simboloNuevo = baseDatos.obtenerTipoDatoNoPrimitivo(columna.hijos[1].valor)
                                if simboloNuevo != None:
                                    # seteas la instancia de nodo simboloNuevoTipo
                                    nuevaColumna.tipoDatoNOprimitivo = simboloNuevo                                
                                else:
                                    #mandas error
                                    errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42704: Tipo de dato no existe")
                                    listaErrores.append(errorEnviar)
                                    return
                                    pass


                            self.especificarColumnas(columna.hijos[2],nuevaColumna,baseDatos,listaErrores)
                            tablaGuardar.agregarColumna(nuevaColumna)
                        elif columna.hijos[0].nombreNodo == "PRIMARY":
                            encontro = False
                            for nodoId in columna.hijos[1].hijos:
                                for columnaEvaluar in tablaGuardar.columnas:
                                    if nodoId.valor.lower() == columnaEvaluar.nombre.lower():
                                        encontro = True 
                                        columnaEvaluar.crearLlavePrimaria()
                                        print("setear llave primaria si existen las columnas: " + nodoId.valor.lower())
                                if encontro == False:
                                    #Id de columna llamado en llave no existe Error 42703
                                    errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42703")
                                    listaErrores.append(errorEnviar)
                                    print("Id de columna llamado en llave no existe: " + nodoId.valor.lower())
                                    return
                                elif encontro == True:
                                    encontro = False  
                                        
                        elif columna.hijos[0].nombreNodo == "FOREIGN":
                            print("setear llave foranea si existen las columnas") 
                        elif columna.hijos[0].nombreNodo == "UNIQUE":
                            print("setear llave foranea si existen las columnas")
                    except:
                        pass         
                    
                    indice = indice + 1
                baseDatos.agregarTabla(tablaGuardar)
                return
        pass

    def especificarColumnas(self,nodoActual,columna,baseDatos,listaErrores):
            if nodoActual != None:
                for i in range(len(nodoActual.hijos)):
                    self.especificarColumnas(nodoActual.hijos[i],columna,baseDatos,listaErrores)
                    try:
                        if nodoActual.hijos[i].nombreNodo == "DEFAULT":
                            #print("setear valor default a columna: " + str(nodoActual.hijos[i+1].valor))
                            columna.setDefaultValue(str(nodoActual.hijos[i+1].valor))
                        elif nodoActual.hijos[i].nombreNodo == "NULL":
                            #print("setear valor TRUE a NULL en columna: ")
                            columna.setPropiedadNull()
                        elif nodoActual.hijos[i].nombreNodo == "NOTNULL":
                            #print("setear valor FALSE a NULL en columna: ")
                            columna.setPropiedadNotNull()
                        elif nodoActual.hijos[i].nombreNodo == "CONSTRAINT":
                            #print("setear constaint a columna:" + str(nodoActual.hijos[i+1].valor))
                            columna.setNombreConstraint(str(nodoActual.hijos[i+1].valor))
                        elif nodoActual.hijos[i].nombreNodo == "UNIQUE":
                            #print("setear TRUE a UNIQUE en columna:")
                            columna.setPropiedadUnique()
                        elif nodoActual.hijos[i].nombreNodo == "CHECK":
                            #print("setear condicion --nodoActual.hijos[i+2].hijos-- a check en columna:")
                            columna.setCheck(nodoActual.hijos[i+2])
                        elif nodoActual.hijos[i].nombreNodo == "PRIMARY":
                            #print("setear TRUE a primary key en columna:")
                            columna.crearLlavePrimaria()
                        elif nodoActual.hijos[i].nombreNodo == "REFERENCES":
                            #print("hacer referencia a llave primaria si existe tabla Error 42P01 "+ nodoActual.hijos[i+1].valor)
                            tablaReferencia = baseDatos.obtenerTabla(nodoActual.hijos[i+1].valor)
                            if tablaReferencia != None:
                                contador = 0
                                for columnaActual in tablaReferencia.columnas:
                                    if columnaActual.primaryKey == True:
                                        contador = contador + 1
                                if contador == 1:
                                    for columnaActual in tablaReferencia.columnas:
                                        if columnaActual.primaryKey == True:
                                            columna.setearTablaForanea(tablaReferencia.nombre)
                                            columna.setearColumnaForanea(columnaActual.nombre)
                                else:
                                    #Numero de referencias no concuerdan
                                    errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42830")
                                    listaErrores.append(errorEnviar)
                            else:
                                #No existe la tabla 
                                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P01")
                                listaErrores.append(errorEnviar)
                    except:
                        pass 
