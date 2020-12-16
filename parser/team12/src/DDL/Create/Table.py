import json
import sys, os.path
import os

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\storageManager')
sys.path.append(storage)

from jsonMode import *


class Column():
    def __init__(self):
        self.name = None
        self.type = None
        self.default = None
        self.isNull = None
        self.isUnique = None
        self.uniqueName = None
        self.checkExp = None
        self.checkName = None
        self.size = None
        self.isPrimary = None
        self.referencesTable = None

    def crearColumna(self, parent, enviroment):
        self.name = parent.hijos[0].valor
        self.type = parent.hijos[1].hijos[0].nombreNodo

        #Inicia la verificación de cada uno de los nodos.
        #Valor Default
        for hijo in parent.hijos:
            if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_DEFAULT":
                if self.default == None:
                    if self.isPrimary ==None:
                        self.default = hijo.hijos[0].execute(enviroment)
                    else:
                        print("La clave primaria no puede tener un valor default")
                else: 
                    print("Ya se declaró un default")
            elif hijo.nombreNodo == "OPCIONALES_NOT_NULL":
                if self.isNull == None : 
                    self.isNull = False
                else:
                    print("Ya se declaró un valor para null")
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_NULL":
                if self.isNull == None: 
                    if self.isPrimary == None:
                        self.isNull = True
                    else:
                        print("Una clave primaria no puede ser null")
                else:
                    print("Ya se declaró un valor para null")
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_UNIQUE":
                if self.isUnique == None : 
                    self.isUnique = True
                    if len(hijo.hijos) == 2:
                        self.uniqueName = hijo.hijos[0].hijos[0].valor
                else:
                    print("Ya se declaró un unique")
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_CHECK":
                if self.checkExp == None : 
                    if len(hijo.hijos) == 1:
                        self.checkExp = self.construirUnique(hijo.hijos[0])
                    elif len(hijo.hijos) == 2:
                        self.checkExp = self.construirUnique(hijo.hijos[1])
                        self.checkName = hijo.hijos[0].hijos[0].valor
                else:
                    print("Ya se declaró un check")
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_PRIMARY":
                if self.isPrimary == None : 
                    self.isPrimary = True
                else:
                    print("Ya se declaró un primary")
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_REFERENCES":
                if self.referencesTable == None : 
                    # Se debe verificar que exista la tabla y la columna con el mismo nombre
                    self.referencesTable = hijo.hijos[0].nombreNodo
                else:
                    print("Ya se declaró un primary")

    def construirUnique(self, parent):
        if len(parent.hijos) == 3 :
            obj1 = self.construirUnique(parent.hijos[0])
            obj2 = self.construirUnique(parent.hijos[2])
            jsonExpresion = {
                'E0' : obj1,
                'operador' : parent.hijos[1].nombreNodo,
                'E1' : obj2
            }
            return jsonExpresion
        elif len(parent.hijos) == 2:
            jsonExpresion = {
                'nodo0' : self.construirUnique(parent.hijos[0]),
                'nodo1' : self.construirUnique(parent.hijos[1])
            }
            return jsonExpresion
        elif len(parent.hijos) == 1:
            jsonExpresion = {
                'nombre' : parent.hijos[0].nombreNodo,
                'valor' : parent.hijos[0].valor
            }
            return jsonExpresion

class Constraints():
    def __init__(self):
        self.nombre = None
        self.listaColumnas = []

    def crearConstraintPrimary(self, parent, columns):
        varIDs=[]
        for hijo in parent.hijos:
            for col in columns:
                if hijo.valor.upper() == col.name.upper():
                    varIDs.append(hijo.valor.upper())
        print(len(varIDs))
        print(len(parent.hijos))
        if len(varIDs) == len(parent.hijos) :
            for hijo in parent.hijos:
                for col in columns:
                    print(col.isPrimary)
                    if hijo.valor.upper() == col.name.upper():
                        if col.isPrimary == None:
                            col.isPrimary == True
                        else:
                            print("Esta columna ya está definida como primaria")
                            return False
        else :
            print("La definicion de las columnas no coinciden con las columnas existentes")
            return False
        return True
    
    def crearConstraintForeign(self, parent, columns):
        # Buscar dentro de las tablas realizadas
        print(parent.nombreNodo)





class Table():
    def __init__(self):
        self.name = None
        self.isNull = None
        self.columnas = []
        
    def execute(self, parent, enviroment):
        for hijo in parent.hijos:
            if hijo.nombreNodo == "IDENTIFICADOR" :
                self.name = hijo.nombreNodo
            elif hijo.nombreNodo == "ATRIBUTO_COLUMNA" :
                nuevaColumna = Column()
                nuevaColumna.crearColumna(hijo,enviroment)
                self.columnas.append(nuevaColumna)
            elif hijo.nombreNodo == "ATRIBUTO_PRIMARY_KEY" :
                nuevaConstraint = Constraints()
                nuevaConstraint.crearConstraintPrimary(hijo, self.columnas)
            elif hijo.nombreNodo == "ATRIBUTO_FOREIGN_KEY" :
                nuevaConstraint = Constraints()
                nuevaConstraint.crearConstraintForeign(hijo, self.columnas)
                

            