class instruccion:
    """INSTRUCCION"""

#PRODUCCIONES GENERALES
class inicio(instruccion):
    def __init__(self,inicio,inst):
        self.inicio = inicio
        self.inst = inst

class inicio2(instruccion):
    def __init__(self,inst):
        self.inst = inst

class inst(instruccion):
    def __init__(self,param1):
        self.param1 = param1

class iden(instruccion):
    def __init__(self,iden):
        self.iden = iden

class tipo(instruccion):
    def __init__(self,tipo):
        self.tipo = tipo

class cond(instruccion):
    def __init__(self,iden, signo,tipo):
        self.iden = iden
        self.signo = signo
        self.tipo = tipo

class wherecond(instruccion):
    def __init__(self,iden, tipo, tipo2):
        self.iden = iden
        self.tipo = tipo
        self.tipo2 = tipo2

class wherecond1(instruccion):
    def __init__(self,iden, tipo):
        self.iden = iden
        self.tipo = tipo

#MANIPULACION DE BASES DE DATOS
#CREATEDB----------------------------
class createdb(instruccion):
    def __init__(self,replacedb,ifnotexists,iden,owner,mode):
        self.replacedb = replacedb
        self.ifnotexists = ifnotexists
        self.iden = iden
        self.owner = owner
        self.mode = mode

class replacedb(instruccion):
    def __init__(self, nombre):
        self.nombre = nombre

class replacedb1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class ifnotexists(instruccion):
    def __init__(self, nombre):
        self.nombre = nombre

class ifnotexists1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class owner(instruccion):
    def __init__(self,iden):
        self.iden = iden

class owner1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class mode(instruccion):
    def __init__(self,iden):
        self.iden = iden

class mode1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

#SHOWDB----------------------------------
class showdb(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

#ALTERDB------------------------------------
class alterdb(instruccion):
    def __init__(self,alterdb2):
        self.alterdb2 = alterdb2

class alterdb2(instruccion):
    def __init__(self,iden, alterdb3):
        self.iden = iden
        self.alterdb3 = alterdb3

class alterdb21(instruccion):
    def __init__(self,iden):
        self.iden = iden

class alterdb3(instruccion):
    def __init__(self,iden):
        self.iden = iden

class alterdb31(instruccion):
    def __init__(self,iden, iden2, iden3):
        self.iden = iden
        self.iden2 = iden2
        self.iden3 = iden3

#DROPDB--------------------------------------
class dropdb(instruccion):
    def __init__(self,ifexists, iden):
        self.ifexists = ifexists
        self.iden =iden

class ifexists(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class ifexists1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

#MANIPULACION DE TABLAS
#CREATE TABLE---------------------------------------
class createtb(instruccion):
    def __init__(self,iden, coltb, inherits):
        self.iden = iden
        self.coltb = coltb
        self.inherits = inherits

class inherits(instruccion):
    def __init__(self,iden):
        self.iden = iden

class inherits1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class coltb(instruccion):
    columna = []
    def __init__(self,columna:[]):
        self.columna = columna

class coltb1(instruccion):
    def __init__(self,columna):
        self.columna = columna

class columna(instruccion):
    def __init__(self,iden, tipo, key, references, default, notnull, constraint):
        self.iden = iden
        self.tipo = tipo
        self.key = key
        self.references = references
        self.default = default
        self.notnull = notnull
        self.constraint = constraint

class references(instruccion):
    def __init__(self,iden):
        self.iden = iden

class references1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class key(instruccion):
    def __init__(self,colkey):
        self.colkey = colkey

class key1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class colkey(instruccion):
    def __init__(self,colkey2):
        self.colkey2 = colkey2

class colkey1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class colkey2(instruccion):
    def __init__(self,colkey2, iden):
        self.colkey2 = colkey2
        self.iden = iden

class cokley21(instruccion):
    def __init__(self,iden):
        self.iden = iden

class default(instruccion):
    def __init__(self,iden):
        self.iden = iden

class default1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class notnull(instruccion):
    def __init__(self,notn):
        self.notn = notn

class notnull1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class note(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class note1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class constraint(instruccion):
    def __init__(self,const):
        self.const = const

class constraint1(instruccion):
    def __init__(self,const, cond):
        self.const = const
        self.cond = cond

class constraint11(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

class const(instruccion):
    def __init__(self,iden):
        self.iden = iden

class const1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

#DROP TABLE--------------------------------------
class droptb(instruccion):
    def __init__(self,iden):
        self.iden = iden

#ALTER TABLE-------------------------------------
class altertb(instruccion):
    def __init__(self,iden, altertb2):
        self.iden = iden
        self.altertb2 = altertb2

class altertb2(instruccion):
    def __init__(self,iden, tipo):
        self.iden = iden
        self.tipo = tipo

class altertb21(instruccion):
    def __init__(self,iden):
        self.iden = iden

class altertb211(instruccion):
    def __init__(self,addprop):
        self.addprop = addprop

class alterdb2111(instruccion):
    def __init__(self,altcol):
        self.altcol = altcol

class addprop(instruccion):
    def __init__(self,cond):
        self.cond = cond

class addprop1(instruccion):
    def __init__(self,iden, iden2):
        self.iden = iden
        self.iden2 = iden2

class addprop11(instruccion):
    def __init__(self,colkey, colkey2):
        self.colkey = colkey
        self.colkey2 = colkey2

class altcol(instruccion):
    def __init__(self,altcol, alter):
        self.altcol = altcol
        self.alter = alter

class altcol1(instruccion):
    def __init__(self,alter):
        self.alter = alter

class alter(instruccion):
    def __init__(self,iden, propaltcol):
        self.iden = iden
        self.propaltcol = propaltcol

class propaltcol(instruccion):
    def __init__(self,tipo):
        self.tipo = tipo

class propaltcol1(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

#MANIPULACION DE DATOS
#INSERT-------------------------------------
class insert(instruccion):
    def __init__(self,iden, valores):
        self.iden = iden
        self.valores = valores

class valores(instruccion):
    def __init__(self,valores, tipo):
        self.valores = valores
        self.tipo = tipo

class valores1(instruccion):
    def __init__(self,tipo):
        self.tipo = tipo

#UPDATE-----------------------------------------
class update(instruccion):
    def __init__(self,iden, cond, wherecond):
        self.iden = iden
        self.cond = cond
        self.wherecond = wherecond

#DELETE-------------------------------------------
class delete(instruccion):
    def __init__(self,iden, wherecond):
        self.iden = iden
        self.wherecond = wherecond