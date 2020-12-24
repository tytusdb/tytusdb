from enum import Enum
from Instruccion import *
from random import *

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
    
    def __init__(self, Datos = {}, Tablas={}, BasesDatos={}, Tipos={}, Validaciones={}):
        self.Datos = Datos.copy()
        self.Tablas = Tablas.copy()
        self.Tipos = Tipos.copy()
        self.BasesDatos = BasesDatos.copy()
        self.Validaciones = Validaciones.copy()

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