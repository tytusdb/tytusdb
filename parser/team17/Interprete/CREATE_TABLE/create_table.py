from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Tabla_de_simbolos import Tabla, Columna, Validacion
from StoreManager import jsonMode as dbms

#############################
# Patrón intérprete: CREATE#
#############################

# CREATE TABLE: crear una tabla


class CreateTable(NodoArbol):

    def __init__(self, id_, columnas_, especificaciones_=None, herencia_=None):
        self.id = id_
        self.columnas = columnas_
        self.especificaciones = especificaciones_
        self.herencia = herencia_

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        dbms.dropAll()

        # create database
        dbms.createDatabase('world')
        retorno = dbms.createTable('world', self.id, len(self.columnas))
        if retorno == 0:  # Operacion exitosa
            entorno.AgregarTabla(Tabla(self.id, self.columnas))  # Se agrega la nueva tabla a la tabla de simbolos
            self.crear_encabezados()  # Se crean los encabezados de las columnas
            dbms.showCollection()
        elif retorno == 1:  # Error en la operacion
            print("Nel error")
        elif retorno == 2:  # La base de datos no existe
            print("Nel no existe la bd")
        elif retorno == 3:  # La tabla ya existe
            print("Nel ya existe la tabla")

    def crear_encabezados(self):
        encabezados = []
        for columna in self.columnas:
            encabezados.append(columna.id)
        dbms.insert('world', self.id, encabezados)
