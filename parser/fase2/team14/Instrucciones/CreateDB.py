from Instrucciones.Instruccion import Instruccion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.variablesestaticas import variables
from tkinter import *
from Expresion.variablesestaticas import variables
from reportes import *


class CreateDb(Instruccion):
    def __init__(self, id: str, orreplace, ifnotexist, ownermode):
        self.id = id
        self.orreplace = orreplace
        self.ifnotexist = ifnotexist
        self.ownermode = ownermode

    def ejecutar(self, ent):
        self.traducir(ent)
        if self.orreplace == 'or replace' and self.ifnotexist == 'if not exists':
            resultado = DBMS.createDatabase(self.id)
            # print("crear base de datos con if not existe y replace ",resultado)

            if (resultado == 2):
                print("ya existe base de datos pero no da error ")
            else:
                variables.consola.insert(INSERT, 'La base de datos: (' + self.id + ') ha sido creada con exito\n')
                return

        elif self.orreplace == 'or replace' and self.ifnotexist == '':

            resultado = DBMS.dropDatabase(self.id)
            # print("crear base de datos o reemplazarlo",resultado)
            if (resultado == 2):
                print('')
            else:
                ent.eliminarDataBase(self.id)

            res = DBMS.createDatabase(self.id)
            if (res == 2):
                print("ya existe base de datos pero debio reemplazarlo :( ")
            else:
                variables.consola.insert(INSERT, 'La base de datos: (' + self.id + ') ha sido creada con exito\n')
                return

        elif self.orreplace == 'databases' and self.ifnotexist == 'if not exists':
            resultado = DBMS.createDatabase(self.id)
            # print("crear base de datos con if not existe",resultado)
            if (resultado == 2):
                print("ya existe base de datos pero no da error ")
            else:
                variables.consola.insert(INSERT, 'La base de datos: (' + self.id + ') ha sido creada con exito\n')
                return
        else:
            res = DBMS.createDatabase(self.id)
            # print("Crear base de datos sin replace y sin exist",res)
            if (res == 2):

                variables.consola.insert(INSERT,
                                         'ERROR >> En la instrucción Create Databasem' + self.id + ' , La base de datos YA EXISTE\n')
                reporteerrores.append(Lerrores("Error Semantico",
                                               'Instrucción Create Database ' + self.id + '  La base de datos YA EXISTE',
                                               '', ''))
                return

            else:
                variables.consola.insert(INSERT, 'La base de datos: (' + self.id + ' ) ha sido creada con exito\n')
                return

    def traducir(self, ent):
        cad = 'ci.ejecutarsql(\"'
        if self.orreplace == 'or replace' and self.ifnotexist == 'if not exists':
            cad += 'create or replace database if not exists ' + self.id

        elif self.orreplace == 'or replace' and self.ifnotexist == '':
            cad += 'create or replace database ' + self.id

        elif self.orreplace == 'databases' and self.ifnotexist == 'if not exists':
            cad += 'create database if not exists ' + self.id

        else:
            cad += 'create database ' + self.id

        cad += ' ' + self.ownermode + ';\") \n'
        self.codigo3d = cad

        print(self.codigo3d)
        return self


class DropDb(Instruccion):
    def __init__(self, id: str, ifexist):
        self.id = id
        self.ifexist = ifexist

    def ejecutar(self, ent):
        self.traducir(ent)
        resultado = DBMS.dropDatabase(self.id)
        if (resultado == 2):
            variables.consola.insert(INSERT,
                                     'ERROR >> En la instrucción Drop Database ' + self.id + ', La base de datos a eliminar NO EXISTE\n')
            reporteerrores.append(
                Lerrores("Error Semantico", 'Instrucción Drop Database ' + self.id + '  La base de datos NO EXISTE', '',
                         ''))
            return
        else:
            ent.eliminarDataBase(self.id)
            variables.consola.insert(INSERT, 'La base de datos: (' + self.id + ' ) ha sido eliminada con exito\n')
            return

    def traducir(self, ent):
        cad = 'ci.ejecutarsql(\"'
        if self.ifexist == 'if exists':
            cad += 'drop database if exists ' + self.id
        else:
            cad += 'drop database ' + self.id

        cad += ' ' + ';\") \n'
        self.codigo3d = cad

        print(self.codigo3d)
        return self


class ShowDb(Instruccion):
    def __init__(self):
        print("---------------")

    def ejecutar(self, ent):
        self.traducir(ent)
        data = DBMS.showDatabases()
        variables.consola.insert(INSERT, "Ejecutando Show Databases \n")
        variables.x.add_column("Databases", data)
        variables.consola.insert(INSERT, variables.x)
        variables.x.clear()
        variables.consola.insert(INSERT, "\n")
        variables.consola.insert(INSERT, 'Show database Exitoso\n')
        return

    def traducir(self, ent):
        cad = 'ci.ejecutarsql(\" show databases; \")\n'
        self.codigo3d = cad
        print(self.codigo3d)
        return self


class AlterDb(Instruccion):
    def __init__(self, id: str, newdb, cadena):
        self.id = id
        self.newdb = newdb
        self.cadena = cadena

    def ejecutar(self, ent):
        self.traducir(ent)
        result = DBMS.alterDatabase(self.id, self.newdb)

        if (result == 2):
            variables.consola.insert(INSERT,
                                     "ERROR >> En la instrucción Alter Database " + self.id + ", La base de datos que desea renombrar NO EXISTE\n")
            reporteerrores.append(Lerrores("Error Semantico",
                                           "Instrucción Alter Database " + self.id + ", La base de datos que desea renombrar NO EXISTE",
                                           '', ''))
            return
        elif (result == 3):
            variables.consola.insert(INSERT,
                                     "ERROR >> En la instrucción Alter Database " + self.id + ", ya exite una basde de datos con ese nombre\n")
            reporteerrores.append(Lerrores("Error Semantico",
                                           "Instrucción Alter Database " + self.id + ", ya exite una basde de datos con ese nombre",
                                           '', ''))
            return

        elif (result == 0):
            ent.renombrarDatabase(self.id, self.newdb)
            DBMS.showCollection()
            variables.consola.insert(INSERT, "Base de datos renombrada a : " + self.newdb + " EXITOSAMENTE\n")
            return

    def traducir(self, ent):
        cad = 'ci.ejecutarsql(\" ' + self.cadena + ';\" )\n'
        self.codigo3d = cad
        print(self.codigo3d)
        return self


class Use(Instruccion):
    def __init__(self, id: str):
        self.id = id

    def ejecutar(self, ent: Entorno):
        self.traducir(ent)
        bases = DBMS.showDatabases()
        existe = False
        for db in bases:
            if db == self.id:
                ent.database = self.id;
                existe = True
                break
        if existe:
            variables.consola.insert(INSERT, "Base de datos: " + ent.database + " en uso actualmente\n")
            return
        else:
            return "ERROR >> En la instrucción Use " + self.id + ", La base de datos a utilizar NO EXISTE"

    def traducir(self, ent):
        cad = 'ci.ejecutarsql(\" use ' + self.id + ';\" )\n'
        self.codigo3d = cad
        print(self.codigo3d)
        return self


class ShowCollection(Instruccion):
    def __init__(self):
        print("--SHOW COLLECTION--")

    def ejecutar(self, ent):
        print("ejecutar show collection")
        return DBMS.showCollection()