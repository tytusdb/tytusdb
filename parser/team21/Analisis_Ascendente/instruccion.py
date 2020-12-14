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
    def __init__(self, id, alter):
        self.id = id
        self.alter = alter

class Alter(Instruccion):
    def __init__(self, accion, ccc, id, tipo, check, id2, typeSet):
        self.accion = accion
        self.ccc = ccc
        self.id = id 
        self.tipo = tipo
        self.check = check
        self.id2 = id2
        self.typeSet = typeSet

#UPDATE
class Update(Instruccion):
    def __init__(self, id, asignaciones, where):
        self.id = id
        self.asignaciones = asignaciones
        self.where = where 

#SELECT
#-----------------------
#TIME
class Time(Instruccion):
    '''#1 EXTRACT
       #2 NOW
       #3 date_part
       #4 current_date
       #5 current_time
       #6 TIMESTAMP'''
    def __init__(self, caso, momento, cadena, cadena2):
        self.caso = caso
        self.momento = momento
        self.cadena = cadena
        self.cadena2 = cadena2




#COMBINACION QUERIES
class Combinacion(Instruccion):
    '''#1 union
       #2 intersect
       #3 except'''
    def __init__(self, caso, all, querie1, querie2):
        self.caso = caso
        self.all = all
        self.querie1 = querie1
        self.querie2 = querie2


 #MATH
class Math_(Instruccion):
    def __init__(self, nombre, E1, E2):
        self.nombre = nombre
        self.E1 = E1
        self.E2 = E2

class Trigonometrica(Instruccion):
    def __init__(self, trig, E):
        self.trig = trig
        self.E = E
