from enum import Enum
from Instruccion import *
from random import *
from six import *

class TIPO_DATO(Enum) :
    ENTERO = 1
    FLOTANTE = 2
    CADENA = 3
    ARREGLO = 4
    CHAR = 5
    UNDEFINED=6
    REFERENCIA=7

class Simbolo() :
    
    def __init__(self, id, tipo,valor, dimension=[],ambito="",referencia=[]) :
        self.id = id
        self.tipo = tipo
        self.valor=valor
        self.dimension=dimension
        self.ambito=ambito
        self.referencia=referencia

class Funcion():
    
    def __init__(self,id,tipo,parametros=[],referencia=[]):
        self.id=id
        self.tipo=tipo
        self.parametros=parametros
        self.referencia=referencia

class TablaDeSimbolos():
    
    def __init__(self, Datos = {}, Tablas={}, BasesDatos={}, Tipos={}, Validaciones={}, ColumnasIndices = {}, Indices = {}, FuncProc = {}):
        self.Datos = Datos.copy()
        self.Tablas = Tablas.copy()
        self.Tipos = Tipos.copy()
        self.BasesDatos = BasesDatos.copy()
        self.Validaciones = Validaciones.copy()
        self.ColumnasIndices = ColumnasIndices
        self.Indices = Indices
        self.FuncProc = FuncProc

    def getDatos(self):
        return self.Datos

# ---------------------- BASES DE DATOS -----------------------------------
    def agregarBasesDatos(self, miBase):
        self.BasesDatos[miBase.idBase] = miBase

    def obtenerBasesDatos(self, id):
        if not id in self.BasesDatos:
            # print('Error: funcion ',id,' no definida.')
            return None
        return self.BasesDatos[id]


    def actualizarCreateDataBase(self, bd, nueva):
        if not bd in self.BasesDatos:
            print('Error: variable ',bd, ' no definida.')
            pass
        else :
            self.BasesDatos[bd] = nueva


    def EliminarBD(self, bd):
        if not bd in self.BasesDatos:
            print('Error: variable ',bd, ' no definida.')
        else :
            del self.BasesDatos[bd]

# ------------------ TABLAS ---------------------------------------
    def agregarTabla(self, tablaNueva):
        self.Tablas[tablaNueva.id] = tablaNueva

    def obtenerTabla(self, idTabla):
        if not idTabla in self.Tablas:
            # print('Error: funcion ',id,' no definida.')
            return None
        return self.Tablas[idTabla]

    def actualizarTabla(self, tabla, nuevaTabla):
        if not tabla in self.Tablas:
            print('Error: variable ',tabla, ' no definida.')
            pass
        else :
            self.BasesDatos[tabla] = nuevaTabla


    def EliminarTabla(self, tabla):
        if not tabla in self.Tablas:
            print('Error: variable ', tabla, ' no definida.')
        else :
            del self.Tablas[tabla]



# ------------------ CAMPOS ---------------------------------------
    def agregarCampo(self, campoN):
        self.Campos[campoN.id] = campoN



    def obtenerCampo(self, idCampo):
        if not idCampo in self.Campos:
            # print('Error: funcion ',id,' no definida.')
            return None
        return self.Campos[idCampo]

    def actualizarCampo(self, campo, nuevoCampo):
        if not campo in self.Campos:
            print('Error: variable ', ' no definida.')
            pass
        else :
            self.Campos[campo] = nuevoCampo

    def EliminarCampo(self, idCampo):
        if not idCampo in self.Campos:
            print('Error: variable ', ' no definida.')
        else :
            del self.Campos[idCampo]

# ------------------ Dato ---------------------------------------
    def agregarDato(self, miDato):
        rand = randint(1,50000)
        self.Datos[str(miDato.valor)+str(rand)] = miDato

    def obtenerDato(self, idDato):
        if not idDato in self.Datos:
            # print('Error: funcion ',id,' no definida.')
            return None
        return self.Datos[idDato]

    def EliminarDato(self, idDato):
        if not idDato in self.Datos:
            print(" No se elimino")
        else :
            del self.Datos[idDato]
            print(" Se elimino")

    def actualizarDato(self, dato, DatoN):
        if not dato in self.Datos:
            print(' >> SE ACTUALIZO EL ITEM.')
            pass
        else :
            self.Datos[dato] = DatoN

# ---------------------------- TIPOS ----------------------------
    def agregarTipo(self, miTipo):
        self.Tipos[miTipo.valor] = miTipo

    def obtenerTipo(self, miTipo):
        if not miTipo in self.Tipos:
            pass
            return None
        return self.Tipos[miTipo]

    def EliminarTipo(self, miTipo):
        if not miTipo in self.Tipos:
            print(" No se elimino")
        else :
            del self.Tipos[miTipo]
            print(" Se elimino")

# ---------------------------- Validaciones ----------------------------
    def agregarValidacion(self, miValidacion):
        rand = randint(1,50000)
        self.Validaciones[str(miValidacion.id) + str(rand)] = miValidacion

    def EliminarValidacion(self, miValidacion):
        if not miValidacion in self.Validaciones:
            print(" No se elimino")
        else :
            del self.Validaciones[miValidacion]
            print(" Se elimino")


# ----------------------------- Indices -------------------------------------------
    def obtenerIndice(self, id_indice):
        if not id_indice in self.Indices:
            return None
        else:
            return self.Indices[id_indice]



    def agregarIndice(self, indice):
        self.Indices[indice.id_indice] = indice

# ----------------------- Funciones y procedimientos ---------------------------------
    def obtenerFuncProc(self, id_fp):
        if not id_fp in self.FuncProc:
            return None
        else:
            return self.FuncProc[id_fp]

    def agregarFuncProc(self, funcion):
        self.FuncProc[funcion.Nombre] = funcion

    def eliminarFuncProc(self, idFP):
        if not idFP in self.FuncProc:
            print('Error: funcion ', ' no definida.')
        else:
            del self.FuncProc[idFP]



    def alterNameIndice(self,id_indice, new_indice):
        if not id_indice in self.Indices:
            print("No esta el indice")
        else:


            print("Estos datos llegan ")
            print(id_indice)
            print(new_indice)
            var:CrearIndice  = self.Indices.pop(id_indice)
            var.id_indice = new_indice
            self.Indices[new_indice] = var
            print("Este es el nuevo diccionario  ")
            print(self.Indices)



# ---------------  Eliminar el indice
    def alterColumnIndice(self, id_indice, no_col, Tipo):
        Contador = 0
        if not id_indice in self.Indices:
            print("No esta el indice")

        else:
            ob: CrearIndice = self.obtenerIndice(id_indice)


            if (isinstance(no_col,int)):
                # buscamos la columna con el numero asociado
                for l in ob.columnas:

                    if (Contador == no_col):

                        print("Este editaremos")
                        self.Indices[id_indice].columnas[Contador].statistics = Tipo
                        print("Se cambia el dato de la columna por el nuevo")

                        # buscar la tabla que contiene indice
                        nombret = self.Indices[id_indice].id_tabla
                        tabla: CreateTable = self.obtenerTabla(nombret)

                        if nombret is not None:
                            Contador2 = 0
                            # Recorrer la lista columnas  Segun indice

                            if (isinstance(Tipo, int)):
                                for col in tabla.cuerpo:
                                    if Contador2 == Tipo:
                                        nuevacol = col.id
                                        self.Indices[id_indice].columnas[no_col].id_columna = str(nuevacol)
                                        print("Este cambio hisee  INT <<<<<<<<<<<<")
                                        print(str(nuevacol))
                                        print("Este cambio hisee  INT <<<<<<<<<<<< 2")
                                        print(str(self.Indices[id_indice].columnas[no_col].id_columna))

                                    Contador2 += 1
                                # buscar el indice que nos mandan

                            elif (isinstance(Tipo, string_types)):
                                for col in tabla.cuerpo:
                                    if Tipo == col.id:
                                        nuevacol = col.id
                                        self.Indices[id_indice].columnas[no_col].id_columna = str(nuevacol)
                                    Contador2 += 1
                                # buscar el indice que nos mandan
                            else:
                                print("No se que error")
                        else:
                            print("Tabla no existe")

                    Contador += 1


            elif(isinstance(no_col,string_types)):

                # buscamos la columna con el numero asociado
                for l in ob.columnas:

                    if (l.id_columna == no_col):

                        print("Este editaremos")
                        self.Indices[id_indice].columnas[Contador].statistics = Tipo
                        print("Se cambia el dato de la columna por el nuevo")

                        # buscar la tabla que contiene indice
                        nombret = self.Indices[id_indice].id_tabla
                        tabla: CreateTable = self.obtenerTabla(nombret)

                        if nombret is not None:
                            Contador2 = 0
                            # Recorrer la lista columnas  Segun indice

                            if (isinstance(Tipo, int)):
                                for col in tabla.cuerpo:
                                    if Contador2 == Tipo:
                                        nuevacol = col.id

                                        #recorremos para encontrar el dato enviado en el indice

                                        Conta=0
                                        for dai in self.Indices[id_indice].columnas:
                                            if(dai.id_columna == no_col):
                                                #si encuentra el dato
                                                self.Indices[id_indice].columnas[Conta].id_columna = str(nuevacol)
                                                print("Este cambio hisee  INT <<<<<<<<<<<<")
                                                print(str(nuevacol))
                                                print("Este cambio hisee  INT <<<<<<<<<<<< 2")
                                                print(str(self.Indices[id_indice].columnas[Conta].id_columna))
                                            Conta+=1

                                    Contador2 += 1
                                # buscar el indice que nos mandan

                            elif (isinstance(Tipo, string_types)):
                                for col in tabla.cuerpo:
                                    if Tipo == col.id:
                                        nuevacol = col.id
                                        #Recorremos para ver si es la columna
                                        Conta=0
                                        for dai in self.Indices[id_indice].columnas:
                                            if(dai.id_columna == no_col):
                                                #si encuentra el dato
                                                self.Indices[id_indice].columnas[Conta].id_columna = str(nuevacol)
                                                print("Este cambio hisee  STRING <<<<<<<<<<<<")
                                                print(str(nuevacol))
                                                print("Este cambio hisee  STRING <<<<<<<<<<<< 2")
                                                print(str(self.Indices[id_indice].columnas[Conta].id_columna))
                                            Conta+=1
                                    Contador2 += 1
                                # buscar el indice que nos mandan
                            else:
                                print("No se que error")
                        else:
                            print("Tabla no existe")
                    Contador += 1
            else:
                print("Es otro tipo de dato.. ")





#---------------  Eliminar el indice
    def DropIndice(self, id_indice):
        if not id_indice in self.Indices:
            print("No esta el indice")
        else:
            del self.Indices[id_indice]
            print(self.Indices)
