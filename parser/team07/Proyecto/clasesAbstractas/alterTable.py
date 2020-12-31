from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import tablaSimbolos,simboloTabla,simboloBaseDatos,simboloColumna
import jsonMode

class alterTable(InstruccionAbstracta):

    def __init__(self, nombre, instrucciones = []):
        self.nombre = nombre
        self.instrucciones = instrucciones
    

    def ejecutar(self, tabalSimbolos, listaErrores):   
        baseDatos =  tabalSimbolos.useDataBase
        bandera = baseDatos.comprobarNombreTabla(self.nombre)
        if bandera == 1:
            #Tabla Existe
            nodoAlter = self.instrucciones
            if nodoAlter[0].nombreNodo == "ADD":
                nodoAdd = nodoAlter[1].hijos
                if nodoAdd[0].nombreNodo == "CHECK":
                    tabla = baseDatos.obtenerTabla(self.nombre)
                    respuesta = tabla.comprobarNombreColumna(nodoAdd[1].hijos[0].valor)
                    if respuesta == 1:
                        #Existe la columna
                        columna = tabla.obtenerColumna(nodoAdd[1].hijos[0].valor)
                        columna.setCheck(nodoAdd[1])
                    elif respuesta == 0:
                        errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error, columna no existe: " + str(nodoAdd[1].hijos[0].valor))
                        listaErrores.append(errorEnviar)
                        return
                elif nodoAdd[0].nombreNodo == "CONSTRAINT":
                    tabla = baseDatos.obtenerTabla(self.nombre)
                    constr = nodoAdd[2].hijos
                    if constr[0].nombreNodo == "UNIQUE":
                        print("setear unique")
                        respuesta = tabla.comprobarNombreColumna(constr[1].valor)
                        if respuesta == 1:
                            #Existe la columna
                            columna = tabla.obtenerColumna(constr[1].valor)
                            columna.setPropiedadUnique()
                        elif respuesta == 0:
                            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error, columna no existe: " + str(constr[1].valor))
                            listaErrores.append(errorEnviar)
                            return
                    elif constr[0].nombreNodo == "PRIMARY":
                        print("setear llave primaria")
                        encontro = False
                        for nodoId in constr[1].hijos:
                            for columnaEvaluar in tabla.columnas:
                                if nodoId.valor.lower() == columnaEvaluar.nombre.lower():
                                    encontro = True
                                    columnaEvaluar.crearLlavePrimaria()
                            if encontro == False:
                                #Id de columna llamado en llave no existe Error 42703
                                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42703")
                                listaErrores.append(errorEnviar)
                                return
                            elif encontro == True:
                                encontro == False
                    elif constr[0].nombreNodo == "FOREIGN":
                        print("setear llave foranea")
                elif nodoAdd[0].nombreNodo == "COLUMN":
                    tabla = baseDatos.obtenerTabla(self.nombre)
                    respuesta = tabla.comprobarNombreColumna(nodoAdd[1].valor)
                    if respuesta == 0:
                        #no existe la tabla
                        indice = tabla.obtenerUltimoIndice()
                        respJson = jsonMode.alterAddColumn(baseDatos.nombre,self.nombre,None)
                        if respJson == 0:
                            nuevaColumna = simboloColumna.SimboloColumna(indice,nodoAdd[1].valor,nodoAdd[2].valor)
                        elif respJson == 1:
                            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error en la operacion")
                            listaErrores.append(errorEnviar)
                            return
                        elif respJson == 2:
                            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Base de datos no existente")
                            listaErrores.append(errorEnviar)
                            return
                        elif respJson == 3:
                            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Tabla no existente")
                            listaErrores.append(errorEnviar)
                            return

                        #Es un tipo de dato no primitivo
                        if nuevaColumna.tipoDato == simboloColumna.TiposDatos.enum:
                            simboloNuevo = baseDatos.obtenerTipoDatoNoPrimitivo(nodoAdd[2].valor)
                            if simboloNuevo != None:
                                # seteas la instancia de nodo simboloNuevoTipo
                                nuevaColumna.tipoDatoNOprimitivo = simboloNuevo                                
                            else:
                                #mandas error
                                print("mandas error")
                                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42704: Tipo de dato no existe")
                                listaErrores.append(errorEnviar)
                                return
                        tabla.agregarColumna(nuevaColumna)
                    elif respuesta == 1:
                        #si existe la columna
                        errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La columna ya existe")
                        listaErrores.append(errorEnviar)
                        return
            elif nodoAlter[0].nombreNodo == "DROP":
                #DROP CONSTRAINT
                print("Drop constraint")
                tabla = baseDatos.obtenerTabla(self.nombre)
                for columna in tabla.columnas:
                    if columna.nombreConstraint.lower() == nodoAlter[2].valor.lower():
                        columna.setNombreConstraint(None)
                        return
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error el constraint" + str(nodoAlter[2].valor) + " no existe tabla: " + str(self.nombre))
                listaErrores.append(errorEnviar)
                return   
            elif nodoAlter[0].nombreNodo == "alter_column_instr":
                #ALTER O DROP columns
                print("")
                tabla = baseDatos.obtenerTabla(self.nombre)
                #Lista de ALTER O DROP columns
                for nodoLista in nodoAlter[0].hijos:
                    if nodoLista[0].nombreNodo == "ALTER":
                        #Modificar columna
                        respuesta = tabla.comprobarNombreColumna(nodoLista[1].valor)
                        if respuesta == 1:
                            #columna si existe
                            print("")
                            columna = tabla.obtenerColumna(nodoLista[1].valor)
                            nodoCambiar = nodoLista[2].hijos
                            if nodoCambiar[0].nombreNodo == "SET":
                                if nodoCambiar[1].nombreNodo == "NULL":
                                    columna.setPropiedadNull()
                                elif nodoCambiar[1].nombreNodo == "NOTNULL":
                                    columna.setPropiedadNotNull()
                            elif nodoCambiar[0].nombreNodo == "TYPE":
                                columnaPivote = simboloColumna.SimboloColumna(0,"pivote",nodoCambiar[0].valor)

                                #Es un tipo de dato no primitivo
                                if columnaPivote.tipoDato == simboloColumna.TiposDatos.enum:
                                    simboloNuevo = baseDatos.obtenerTipoDatoNoPrimitivo(nodoCambiar[0].valor)
                                    if simboloNuevo != None:
                                        # seteas la instancia de nodo simboloNuevoTipo
                                        columna.setTipoDato(nodoCambiar[0].valor)
                                        columna.tipoDatoNOprimitivo = simboloNuevo
                                        return                                
                                    else:
                                        #mandas error
                                        print("mandas error")
                                        errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42704: Tipo de dato no existe")
                                        listaErrores.append(errorEnviar)
                                        return
                                columna.setTipoDato(nodoCambiar[0].valor)
                        elif respuesta == 0:
                            #Columna no existe
                            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Columna " + str(nodoLista[1].valor) + " no existe")
                            listaErrores.append(errorEnviar)
                            return
                    elif nodoLista[0].nombreNodo == "DROP":
                        #Eliminar columna
                        respuesta = tabla.obtenerColumna(nodoLista[2].valor)
                        if respuesta == None:
                            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Columna " + str(nodoLista[2].valor) + " no existe")
                            listaErrores.append(errorEnviar)
                            return
                        else:
                            respJson = jsonMode.alterDropColumn(baseDatos.nombre,self.nombre,respuesta.indice)
                            if respJson == 0:
                                tabla.eliminarColumna(nodoLista[2].valor)
                            elif respJson == 1:
                                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion"," error en la operación")
                                listaErrores.append(errorEnviar)
                                return
                            elif respJson == 2:
                                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","database no existente")
                                listaErrores.append(errorEnviar)
                                return
                            elif respJson == 3:
                                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","table no existente")
                                listaErrores.append(errorEnviar)
                                return
                            elif respJson == 4:
                                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","llave no puede eliminarse o tabla quedarse sin columna")
                                listaErrores.append(errorEnviar)
                                return
                            elif respJson == 5:
                                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","columna fuera de límites")
                                listaErrores.append(errorEnviar)
                                return

        else:
            #Tabla no existe
            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P01, tabla no existe: " + str(self.nombre))
            listaErrores.append(errorEnviar)
            return
        pass      
