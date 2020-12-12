class Instruccion:
    'clase abstracta'

#CREATE TABLE
class CreateTable(Instruccion):
    def __init__(self, id, campos, idInherits):
        self.id = id
        self.campos = campos
        self.idInherits = idInherits

class Campo(Instruccion):
    '''#1 ID tipo
       #2 CONSTRAINT
       #3 FOREIGN
       #4 PRIMARY'''
    def __init__(self, caso, id, tipo, acompaniamiento, idFk, tablaR, idR):
        self.caso = caso
        self.id = id
        self.tipo = tipo
        self.acompaniamiento = acompaniamiento
        self.idFk = idFk
        self.tablaR = tablaR
        self.idR = idR

class Acompaniamiento(Instruccion):
    def __init__(self, tipo, valorDefault):
        self.tipo = tipo
        self.valorDefault = valorDefault

#TIPOS DE DATO
class Tipo(Instruccion):
    def __init__(self, tipo, longitud):
        self.tipo = tipo
        self.longitud = longitud

class IdId(Instruccion):
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2
        
#INSERT INTO
class InsertInto(Instruccion):
    def __init__(self, id, listaId, values):
        self.id = id
        self.listaId = listaId
        self.values = values

#WHERE
class Where(Instruccion):
    '''#1 not boolean
       #2 in
       #3 between'''
    def __init__(self, caso, boolean, listaValores, valor1, valor2):
        self.caso = caso
        self.boolean = boolean
        self.listaValores = listaValores
        self.valor1 = valor1
        self.valor2 = valor2        

#asignacion x = e
#puede venir id o id.id
class Asignacion(Instruccion):
    def __init__(self, id, expresion):
        self.id = id
        self.expresion = expresion

#DELETE
class Delete(Instruccion):
    def __init__(self, id, where):
        self.id = id
        self.where = where

#DROP
class Drop(Instruccion):
    '''#1 database
       #2 table'''
    def __init__(self, caso, exists, id):
        self.caso = caso
        self.exists = exists
        self.id = id

#CREATE [OR REPLACE] DATABASE
class CreateReplace(Instruccion):
    '''#1 create
       #2 create or replace'''
    def __init__(self, caso, exists, id, complemento):
        self.caso = caso
        self.exists = exists
        self.id = id
        self.complemento = complemento

#complemento de create or replace
class ComplementoCR(Instruccion):
    def __init__(self, idOwner, mode):
        self.idOwner = idOwner
        self.mode = mode

#SHOW DATABASE
class Show(Instruccion):
    def __init__(self, fv):
        self.fv = fv

#ALTER
class AlterDatabase(Instruccion):
    '''#1 rename
       #2 owner'''
    def __init__(self, caso, name, newName):
        self.caso = caso
        self.name = name
        self.newName = newName

class AlterTable(Instruccion):
    '''#1 ADD
       #2 DROP
       #3 ALTER'''
    def __init__(self, caso, id, columnConstraint, idAdd, tipoAdd, checkAdd, constraintId, columnId, listaFK, listaReferences, idDrop, columnAlter):
        self.caso = caso
        self.id = id
        self.columnConstraint = columnConstraint
        self.idAdd = idAdd
        self.tipoAdd = tipoAdd
        self.checkAdd = checkAdd
        self.constraintId = constraintId
        self.columnId = columnId
        self.listaFK = listaFK
        self.listaReferences = listaReferences 
        self.idDrop = idDrop
        self.columnAlter = columnAlter