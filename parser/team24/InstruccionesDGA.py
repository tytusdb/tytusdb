import jsonMode as func
import tablaDGA as TS

#VARIABLES GLOBALES
resultadotxt = ""
tabla = TS.Tabla()
cont = 1
contambito = 0
NombreDB = ""

def Textoresultado():
    global tabla
    global resultadotxt
    print(resultadotxt)
    for simbolo in tabla.simbolos:
        print("id: " + str(tabla.simbolos[simbolo].id) + " Valor: " + tabla.simbolos[simbolo].valor + " Ambito: " + str(tabla.simbolos[simbolo].ambito))
    print("\n")
    resultadotxt = ""

class instruccion:
    """INSTRUCCION"""

"""RODUCCIONES GENERALES"""
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

"""MANIPULACION DE BASES DE DATOS"""
#CREATEDB----------------------------
class createdb(instruccion):
    def __init__(self,replacedb,ifnotexists,iden,owner,mode):
        self.replacedb = replacedb
        self.ifnotexists = ifnotexists
        self.iden = iden
        self.owner = owner
        self.mode = mode

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global contambito
        contambito+=1
        try:       
            resultado = func.createDatabase(self.iden)
            if resultado == 0:
                resultadotxt += "Se creo la base de datos: " + self.iden + "\n"
                simbolo = TS.Simbolo(cont,TS.TIPO.DATABASE, self.iden, contambito)
                cont+=1
                tabla.agregar(simbolo)
            elif resultado == 2 and not self.replacedb:
                resultadotxt += "Ya existe la base de datos: " + self.iden + "\n"
            elif resultado == 2 and self.replacedb:
                func.dropDatabase(self.iden)
                buscar = tabla.BuscarNombre(self.iden)
                tabla.simbolos.pop(buscar.id)
                func.createDatabase(self.iden)
                simbolo = TS.Simbolo(cont,TS.TIPO.DATABASE, self.iden, contambito)
                cont+=1
                tabla.agregar(simbolo)
                resultadotxt += "Se reemplazo la base de datos: " + self.iden + "\n"
            else:
                resultadotxt += "Error al crear base de datos: " + self.iden + "\n"
        except:
            """ERROR SEMANTICO"""
    
#SHOWDB----------------------------------
class showdb(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        contador = 0
        try:
            resultado = func.showDatabases()
            if len(resultado) > 0:
                resultadotxt += "\nBases de datos existentes:\n"
                for base in resultado:
                    resultadotxt += str(contador) + ". " + base + "\n"
                    contador += 1
            else:
                resultadotxt += "No existen bases de datos"
        except:
            """ERROR SEMANTICO"""

#ALTERDB------------------------------------
class alterdb(instruccion):
    def __init__(self,alterdb2):
        self.alterdb2 = alterdb2

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        try:
            if self.alterdb2.iden != "" and self.alterdb2.alterdb3.iden != "":
                resultado = func.alterDatabase(self.alterdb2.iden, self.alterdb2.alterdb3.iden)
                if resultado == 2:
                    resultadotxt += "No existe la base de datos: " + self.alterdb2.iden + "\n"
                if resultado == 3:
                    resultadotxt += "Ya existe la base de datos: " + self.alterdb2.alterdb3.iden + "\n"
                else:
                    resultadotxt += "Se actualizo la base de datos: " + self.alterdb2.iden + " a " + self.alterdb2.alterdb3.iden + "\n"
                    buscar = tabla.BuscarNombre(self.alterdb2.iden)
                    buscar.valor = self.alterdb2.alterdb3.iden
                    tabla.actualizar(buscar)
        except:
            """ERROR SEMANTICO"""
        
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

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        try:       
            resultado = func.dropDatabase(self.iden)
            if(resultado == 2):
                resultadotxt += "No existe la base de datos: " + self.iden + "\n"
            else:
                resultadotxt += "Se elimino la base de datos: " + self.iden + "\n"
                buscar = tabla.BuscarNombre(self.iden)
                tabla.simbolos.pop(buscar.id)
        except:
            """ERROR SEMANTICO"""

#USEDB----------------------------------------
class usedb(instruccion):
    def __init__(self, iden):
        self.iden =iden

    def ejecutar(self):
        global resultadotxt
        global NombreDB
        NombreDB = self.iden
        resultadotxt += "Usando la base de datos: " + self.iden + "\n"

#MANIPULACION DE TABLAS
#CREATE TABLE---------------------------------------
class createtb(instruccion):
    def __init__(self,iden, coltb, inherits):
        self.iden = iden
        self.coltb = coltb
        self.inherits = inherits

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        try:       
            resultado = func.createTable(NombreDB, self.iden,len(self.coltb))
            if(resultado == 2):
                resultadotxt += "No existe la base de datos: " + NombreDB + "\n"
            elif(resultado == 3):
                resultadotxt += "La tabla ya existe: " + self.iden + "\n"
            else:
                resultadotxt += "Se creo la tabla: " + self.iden + " En la base de datos: " + NombreDB + "\n"
                buscar = tabla.BuscarNombre(NombreDB)
                simbolo = TS.Simbolo(cont,TS.TIPO.TABLE, self.iden, buscar.id)
                cont+=1
                tabla.agregar(simbolo)
                """SE CREAN LAS COLUMNAS PARA LA TABLA"""
                inicio = 1
                for columna in self.coltb:
                    ncolumna = TS.Simbolo(cont,columna.tipo,columna.iden,simbolo.id,inicio)
                    inicio+=1
                    cont+=1
                    tabla.agregar(ncolumna)
        except:
            """ERROR SEMANTICO"""

class columna(instruccion):
    def __init__(self,iden, tipo, key, references, default, notnull, constraint):
        self.iden = iden
        self.tipo = tipo
        self.key = key
        self.references = references
        self.default = default
        self.notnull = notnull
        self.constraint = constraint

#DROP TABLE--------------------------------------
class droptb(instruccion):
    def __init__(self,iden):
        self.iden = iden

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        try:       
            resultado = func.dropTable(NombreDB, self.iden)
            if(resultado == 2):
                resultadotxt += "No existe la base de datos: " + NombreDB + "\n"
            elif(resultado == 3):
                resultadotxt += "La tabla " + self.iden + " no existe en " + NombreDB + "\n"
            else:
                resultadotxt += "Se elimino la tabla: " + self.iden + " de la base de datos: " + NombreDB + "\n"
                buscar = tabla.BuscarNombre(self.iden)
                tabla.simbolos.pop(buscar.id)
        except:
            """ERROR SEMANTICO"""

#ALTER TABLE-------------------------------------
class altertb(instruccion):
    def __init__(self,iden, altertb2):
        self.iden = iden
        self.altertb2 = altertb2

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        if self.altertb2.text.lower() == "add column":
            try:
                resultado = func.alterAddColumn(NombreDB,self.iden,self.altertb2.iden)
                if resultado == 2:
                    resultadotxt += "No existe la base de datos: " + NombreDB + "\n"
                elif resultado == 3:
                    resultadotxt += "No existe la tabla: " + self.iden + "\n"
                else:
                    resultadotxt += "Se agrego la columna " + self.altertb2.iden + " a la tabla " + self.iden + "\n"
                    buscar = tabla.BuscarNombre(self.iden)
                    ncolumna = TS.Simbolo(cont,self.altertb2.tipo,self.altertb2.iden,buscar.id)
                    cont+=1
                    tabla.agregar(ncolumna)
            except:
                """ERROR SEMANTICO"""
        elif self.altertb2.text.lower() == "drop column":
            try:
                basedatos = tabla.BuscarNombre(NombreDB)
                tablas = tabla.BuscarNombre(self.iden)
                print("BUSCANDO: " + self.altertb2.iden)
                bcol = tabla.BuscarNombre(self.altertb2.iden)
                print("ENCONTRADO: " + bcol.valor)
                if basedatos:
                    print("AAAAAAAAA")
                    if tabla:
                        print("BBBBBBBBB")
                        if bcol:
                            print("CCCCCCCCCCC")
                            tabla.simbolos.pop(bcol.id)
                            resultadotxt += "Se elimino la columna " + self.altertb2.iden + " de la tabla " + self.iden + "\n"
                        else:
                            resultadotxt += "No se encontro la columna: " + self.altertb2.iden + " en la tabla " + self.iden + "\n"
                    else:
                        resultadotxt += "No se encontro la tabla: " + self.iden + " en la base de datos " + NombreDB + "\n"
                else:
                    resultadotxt += "La base de datos " + NombreDB + " No existe \n"
            except:
                """ERROR SEMANTICO"""

class altertb2(instruccion):
    def __init__(self,text,iden, tipo):
        self.text = text
        self.iden = iden
        self.tipo = tipo

class altertb21(instruccion):
    def __init__(self,text,iden):
        self.text = text
        self.iden = iden

class altertb211(instruccion):
    def __init__(self,addprop):
        self.addprop = addprop

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

class alter(instruccion):
    def __init__(self,iden, propaltcol):
        self.iden = iden
        self.propaltcol = propaltcol

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