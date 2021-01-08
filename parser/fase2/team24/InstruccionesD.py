import storage as func
import tablaDGA as TS
import reportError as errores
import mathtrig as mt
import hashlib
from datetime import date

from reportTable import *

from variables import cont
from variables import tabla
from variables import NombreDB


from procedural import llamadaF

#VARIABLES GLOBALES
resultadotxt = ""

contambito = 0

contregistro = 0


def Textoresultado():

    for simbolo in tabla.simbolos:
        print("ID: " + str(tabla.simbolos[simbolo].id) + " Nombre: " + tabla.simbolos[simbolo].nombre + " Ambito: " + str(tabla.simbolos[simbolo].ambito) + " Tipo indice: " + str(tabla.simbolos[simbolo].tipoind) + " Orden Indice: " + str(tabla.simbolos[simbolo].ordenind) + " Columna ind: " + str(tabla.simbolos[simbolo].columnaind) + " Tabla indice: " + str(tabla.simbolos[simbolo].tablaind))
    print("\n")

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
    def __init__(self,iden, tipo,signo):
        self.iden = iden
        self.tipo = tipo
        self.signo = signo

class reservadatipo(instruccion):
    def __init__(self,restipo,cantn):
        self.restipo = restipo
        self.cantn = cantn

"""MANIPULACION DE BASES DE DATOS"""
#CREATEDB----------------------------
class createdb(instruccion):

    def __init__(self,replacedb,ifnotexists,iden,owner,mode):
        self.replacedb = replacedb
        self.ifnotexists = ifnotexists
        self.iden = iden
        self.owner = owner
        self.mode = mode

    def traducir(self):

        #global traduccion
        traduccion = '\t'
        traduccion += 'sql.execute("CREATE DATABASE'
        if self.ifnotexists != "":
            traduccion += ' IF NOT EXISTS'
        traduccion += ' '+self.iden
        if self.owner != "":
            traduccion += ' OWNER =' + self.owner
        if self.mode != "":
            traduccion += ' MODE =' + self.mode
        traduccion += ';")'
        return traduccion + '\n'

    def ejecutar(self):

        global resultadotxt
        global cont
        global tabla
        global contambito
        try:
            resultado = func.createDatabase(self.iden)
            if resultado == 0:
                NuevoSimbolo = TS.Simbolo(cont,self.iden,TS.TIPO.DATABASE,contambito)
                cont+=1
                contambito += 1
                tabla.agregar(NuevoSimbolo)
                print("2 luego de ejecutar en DGA",id(tabla))


                #resultadotxt += "Se creo la base de datos " + self.iden + "\n"
                print("Se creo la base de datos " + self.iden + "\n")
                return "Se creo la base de datos " + self.iden + "\n"
            elif resultado == 2 and not self.replacedb:
                e = errores.CError(0,0,"Ya existe la base de datos " + self.iden,'Semantico')
                errores.insert_error(e)
                resultadotxt += "Ya existe la base de datos " + self.iden + "\n"
                print("Ya existe la base de datos " + self.iden + "\n")
                return "Ya existe la base de datos " + self.iden + "\n"
            elif resultado == 2 and self.replacedb:
                func.dropDatabase(self.iden)
                buscar = tabla.BuscarNombre(self.iden)
                tabla.simbolos.pop(buscar.id)
                func.createDatabase(self.iden)
                NuevoSimbolo = TS.Simbolo(cont,self.iden,TS.TIPO.DATABASE,contambito)
                cont+=1
                contambito+=1
                tabla.agregar(NuevoSimbolo)
                resultadotxt += "Se reemplazo la base de datos: " + self.iden + "\n"
                print("Se reemplazo la base de datos: " + self.iden + "\n")
                return "Se reemplazo la base de datos: " + self.iden + "\n"
            else:
                e = errores.CError(0,0,"Error al crear base de datos: " + self.iden,'Semantico')
                errores.insert_error(e)
                resultadotxt += "Error al crear base de datos: " + self.iden + "\n"
                print("Error al crear base de datos: " + self.iden + "\n")

                return "Error al crear base de datos: " + self.iden + "\n"

        except:
            NuevoSimbolo = TS.Simbolo(cont,self.iden,TS.TIPO.DATABASE,contambito)
            cont+=1
            contambito += 1
            tabla.agregar(NuevoSimbolo)
            print("2 luego de ejecutar en DGA",id(tabla))
            """ERROR SEMANTICO"""

#SHOWDB----------------------------------
class showdb(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

    def traducir(self):
        traduccion = '\t'
        traduccion += 'sql.execute("SHOW DATABASES;")'
        traduccion += '\n'

        return traduccion

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        contador = 0
        try:
            resultado = func.showDatabases()
            if len(resultado) > 0:
                resultadotxt += "\nBases de datos existentes:\n"
                resp =""
                resp += "\nBases de datos existentes:\n"
                for base in resultado:
                    resultadotxt += str(contador) + ". " + base + "\n"
                    resp += str(contador) + ". " + base + "\n"
                    contador += 1
                print(resp)
                return resp
            else:
                resultadotxt += "No existen bases de datos"
                print("No existen bases de datos")
                return "No existen bases de datos"
        except:
            """ERROR SEMANTICO"""

#ALTERDB------------------------------------
class alterdb(instruccion):
    def __init__(self,alterdb2):
        self.alterdb2 = alterdb2

    def traducir(self):
        traduccion = '\t'
        traduccion += 'sql.execute("ALTER DATABASE'
        if self.alterdb2 != None:
            traduccion += ' ' + self.alterdb2.iden
        if self.alterdb2.alterdb3 != None:
            traduccion += ' RENAME TO ' + self.alterdb2.alterdb3.iden
        traduccion += ';")'
        traduccion += '\n'

        return traduccion

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        try:
            if self.alterdb2.iden != "" and self.alterdb2.alterdb3.iden != "":
                resultado = func.alterDatabase(self.alterdb2.iden, self.alterdb2.alterdb3.iden)
                if resultado == 2:
                    e = errores.CError(0,0,"No existe la base de datos " + self.alterdb2.iden,'Semantico')
                    errores.insert_error(e)
                    resultadotxt += "No existe la base de datos " + self.alterdb2.iden + "\n"
                    print("No existe la base de datos " + self.alterdb2.iden + "\n")
                    return "No existe la base de datos " + self.alterdb2.iden + "\n"
                if resultado == 3:
                    e = errores.CError(0,0,"Ya existe la base de datos " + self.alterdb2.alterdb3.iden,'Semantico')
                    errores.insert_error(e)
                    resultadotxt += "Ya existe la base de datos " + self.alterdb2.alterdb3.iden + "\n"
                    print("Ya existe la base de datos " + self.alterdb2.alterdb3.iden + "\n")
                    return "Ya existe la base de datos " + self.alterdb2.alterdb3.iden + "\n"
                else:
                    buscar = tabla.BuscarNombre(self.alterdb2.iden)
                    buscar.nombre = self.alterdb2.alterdb3.iden
                    tabla.actualizar(buscar)
                    resultadotxt += "Se actualizo la base de datos " + self.alterdb2.iden + " a " + self.alterdb2.alterdb3.iden + "\n"
                    print("Se actualizo la base de datos " + self.alterdb2.iden + " a " + self.alterdb2.alterdb3.iden + "\n")
                    return "Se actualizo la base de datos " + self.alterdb2.iden + " a " + self.alterdb2.alterdb3.iden + "\n"
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

    def traducir(self):
        traduccion = '\t'
        traduccion += 'sql.execute("DROP DATABASE'
        if self.ifexists != "":
            traduccion += ' IF EXISTS'
        traduccion += ' ' + self.iden
        traduccion += ';)"'
        traduccion += '\n'

        return traduccion

    def ejecutar(self):
        global NombreDB
        global resultadotxt
        global cont
        global tabla
        try:
            resultado = func.dropDatabase(self.iden)
            if(resultado == 2):
                e = errores.CError(0,0,"No existe la base de datos " + str(self.iden),'Semantico')
                errores.insert_error(e)
                resultadotxt += "No existe la base de datos " + self.iden + "\n"
                print("No existe la base de datos " + self.iden + "\n")
                return "No existe la base de datos " + self.iden + "\n"
            else:
                BaseDatos = tabla.BuscarNombre(self.iden)
                eliminar = []
                for simbolo in tabla.simbolos:
                    if tabla.simbolos[simbolo].ambito == BaseDatos.id and not tabla.simbolos[simbolo].tipo == TS.TIPO.DATABASE:
                        TablaExistente = tabla.simbolos[simbolo]
                        eliminar.append(TablaExistente)
                        for simbolo2 in tabla.simbolos:
                            if tabla.simbolos[simbolo2].ambito == TablaExistente.id and not tabla.simbolos[simbolo2].tipo == TS.TIPO.DATABASE and not tabla.simbolos[simbolo2].tipo == TS.TIPO.TABLE:
                                eliminar.append(tabla.simbolos[simbolo2])
                for element in eliminar:
                    tabla.simbolos.pop(element.id)
                tabla.simbolos.pop(BaseDatos.id)
                if self.iden == NombreDB:
                    NombreDB = ""
                resultadotxt += "Se elimino la base de datos " + self.iden + "\n"
                print("Se elimino la base de datos " + self.iden + "\n")
                return "Se elimino la base de datos " + self.iden + "\n"
        except:
            """ERROR SEMANTICO"""

#USEDB----------------------------------------
class usedb(instruccion):
    def __init__(self, iden):
        self.iden =iden

    def traducir(self):
        traduccion = '\t'
        traduccion += 'sql.execute("USE DATABASE '+ self.iden
        traduccion += ';")'
        traduccion += '\n'
        traduccion += '\tNombreDB = ts.nameDB\n'

        return traduccion

    def ejecutar(self):
        global resultadotxt
        global NombreDB
        global tabla

        tabla.nameDB = self.iden
        NombreDB = self.iden
        resultadotxt += "Usando la base de datos " + self.iden + "\n"
        print("Usando la base de datos " + self.iden + "\n")
        return "Usando la base de datos " + self.iden + "\n"

#MANIPULACION DE TABLAS
#CREATE TABLE---------------------------------------
class createtb(instruccion):
    def __init__(self,iden, coltb, inherits):
        self.iden = iden
        self.coltb = coltb
        self.inherits = inherits

    def traducir(self):
        traduccion = '\t'
        traduccion += 'sql.execute("CREATE TABLE '+ self.iden +'('
        for column in self.coltb:
            if isinstance(column, columna):
                if isinstance(column.tipo, str):
                    traduccion += column.iden + ' ' + column.tipo
                elif isinstance(column.tipo, reservadatipo):
                    traduccion += column.iden + ' ' + str(column.tipo.restipo)
                    if (column.tipo.cantn is not None):
                        traduccion += '(' + str(column.tipo.cantn) +')'
                if column.notnull != "":
                    traduccion += ' ' + 'NOT NULL'
                if str('PRIMARY KEY').lower() in str(column.key).lower():
                    traduccion +=  ' ' + 'PRIMARY KEY'
                traduccion += ','
        traduccion += ');")'
        traduccion = traduccion.replace(',)',')')
        traduccion += '\n'
        #self.ejecutar()
        return traduccion


    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        resultadotxt = ""
        try:
            resultado = func.createTable(NombreDB, self.iden,0)
            if(resultado == 2):
                e = errores.CError(0,0,"No existe la base de datos: " + NombreDB,'Semantico')
                errores.insert_error(e)
                resultadotxt += "No existe la base de datos: " + NombreDB + "\n"
            elif(resultado == 3):
                e = errores.CError(0,0,"La tabla ya existe: " + self.iden,'Semantico')
                errores.insert_error(e)
                resultadotxt += "La tabla ya existe: " + self.iden + "\n"
            else:
                buscar = tabla.BuscarNombre(NombreDB)
                NuevoSimbolo = TS.Simbolo(cont,self.iden,TS.TIPO.TABLE,buscar.id,0)
                cont+=1
                tabla.agregar(NuevoSimbolo)
                """SE CREAN LAS COLUMNAS PARA LA TABLA"""
                inicio = 0
                for columna in self.coltb:
                    try:
                        if "primary key " in columna.key.lower():
                            NuevaColumna = TS.Simbolo(cont,columna.iden,TS.TIPO.COLUMN,NuevoSimbolo.id,0,columna.tipo,1,columna.references,columna.default,False,columna.constraint,inicio)
                            listacol = []
                            listacol.append(NuevaColumna.numcol)
                            resultado2 = func.alterAddColumn(NombreDB,self.iden,columna)
                            resultado = func.alterAddPK(NombreDB,NuevoSimbolo.nombre,listacol)
                        else:
                            NuevaColumna = TS.Simbolo(cont,columna.iden,TS.TIPO.COLUMN,NuevoSimbolo.id,0,columna.tipo,0,columna.references,columna.default,False,columna.constraint,inicio)
                            resultado = func.alterAddColumn(NombreDB,self.iden,columna)
                        if resultado == 2:
                            e = errores.CError(0,0,"No existe la base de datos " + NombreDB,'Semantico')
                            errores.insert_error(e)
                            resultadotxt += "No existe la base de datos " + NombreDB + "\n"
                        elif resultado == 3:
                            e = errores.CError(0,0,"No existe la tabla " + self.iden,'Semantico')
                            errores.insert_error(e)
                            resultadotxt += "No existe la tabla " + self.iden + "\n"
                        elif resultado == 4:
                            e = errores.CError(0,0,"Ya existe una llave primaria en " + self.iden,'Semantico')
                            errores.insert_error(e)
                            resultadotxt += "Ya existe una llave primaria en " + self.iden + "\n"
                        else:
                            if columna.notnull.lower() == "not null":
                                NuevaColumna.nullcol = True
                            else:
                                NuevaColumna.nullcol = False
                            cont+=1
                            inicio+=1
                            NuevoSimbolo.coltab+=1
                            tabla.actualizar(NuevoSimbolo)
                            tabla.agregar(NuevaColumna)
                            resultadotxt += "Se agrego la columna " + columna.iden + " a la tabla " + self.iden + "\n"
                    except:
                        """ERROR SEMANTICO"""
                if self.inherits != "":
                    TablaInherits = tabla.BuscarNombre(self.inherits)
                    if TablaInherits:
                        ColumnasInherits = []
                        for simbolo in tabla.simbolos:
                            if tabla.simbolos[simbolo].ambito == TablaInherits.id and tabla.simbolos[simbolo].tipo == TS.TIPO.COLUMN :
                                ColumnasInherits.append(tabla.simbolos[simbolo])
                        #AGREGAR COLUMNAS DE INHERITS A TABLA
                        for columna in ColumnasInherits:
                            try:
                                if columna.llavecol == 1:
                                    NuevaColumna = TS.Simbolo(cont,columna.nombre,TS.TIPO.COLUMN,NuevoSimbolo.id,0,columna.tipocol,columna.llavecol,columna.refcol,columna.defcol,columna.nullcol,columna.constcol,inicio)
                                    listacol = []
                                    listacol.append(NuevaColumna.numcol)
                                    resultado2 = func.alterAddColumn(NombreDB,self.iden,columna)
                                    resultado = func.alterAddPK(NombreDB,NuevoSimbolo.nombre,listacol)
                                else:
                                    NuevaColumna = TS.Simbolo(cont,columna.nombre,TS.TIPO.COLUMN,NuevoSimbolo.id,0,columna.tipocol,columna.llavecol,columna.refcol,columna.defcol,columna.nullcol,columna.constcol,inicio)
                                    resultado = func.alterAddColumn(NombreDB,self.iden,columna)
                                if resultado == 2:
                                    e = errores.CError(0,0,"No existe la base de datos " + NombreDB,'Semantico')
                                    errores.insert_error(e)
                                    resultadotxt += "No existe la base de datos " + NombreDB + "\n"
                                elif resultado == 3:
                                    e = errores.CError(0,0,"No existe la tabla " + self.iden,'Semantico')
                                    errores.insert_error(e)
                                    resultadotxt += "No existe la tabla " + self.iden + "\n"
                                elif resultado == 4:
                                    e = errores.CError(0,0,"Ya existe una llave primaria en " + self.iden,'Semantico')
                                    errores.insert_error(e)
                                    resultadotxt += "Ya existe una llave primaria en " + self.iden + "\n"
                                else:
                                    cont+=1
                                    inicio+=1
                                    NuevoSimbolo.coltab+=1
                                    tabla.actualizar(NuevoSimbolo)
                                    tabla.agregar(NuevaColumna)
                                    resultadotxt += "Se agrego la columna " + columna.nombre + " a la tabla " + self.iden + "\n"
                            except:
                                """ERROR SEMANTICO"""
                    else:
                        e = errores.CError(0,0,"No existe la tabla " + self.inherits,'Semantico')
                        errores.insert_error(e)
                        resultadotxt += "No existe la tabla " + self.inherits + "\n"
                resultadotxt += "Se creo la tabla: " + self.iden + " En la base de datos: " + NombreDB + "\n"
        except:
            """ERROR SEMANTICO"""
        print(resultadotxt)
        return resultadotxt

class columna(instruccion):
    def __init__(self,iden, tipo, notnull, key, references, default, constraint):
        self.iden = iden
        self.tipo = tipo
        self.notnull = notnull
        self.key = key
        self.references = references
        self.default = default
        self.constraint = constraint

#DROP TABLE--------------------------------------
class droptb(instruccion):
    def __init__(self,iden):
        self.iden = iden

    def traducir(self):
        traduccion = '\t'
        traduccion += 'sql.execute("DROP TABLE '+ self.iden + ';")'
        traduccion += '\n'

        return traduccion

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        resultadotxt = ""
        try:
            resultado = func.dropTable(NombreDB, self.iden)
            if(resultado == 2):
                e = errores.CError(0,0,"No existe la base de datos " + NombreDB,'Semantico')
                errores.insert_error(e)
                resultadotxt += "No existe la base de datos " + NombreDB + "\n"
            elif(resultado == 3):
                e = errores.CError(0,0,"La tabla " + self.iden + " no existe en " + NombreDB,'Semantico')
                errores.insert_error(e)
                resultadotxt += "La tabla " + self.iden + " no existe en " + NombreDB + "\n"
            else:
                buscar = tabla.BuscarNombre(self.iden)
                eliminar = []
                for simbolo in tabla.simbolos:
                    if tabla.simbolos[simbolo].ambito == buscar.id and not tabla.simbolos[simbolo].tipo == TS.TIPO.DATABASE and not tabla.simbolos[simbolo].tipo == TS.TIPO.TABLE:
                        eliminar.append(tabla.simbolos[simbolo])
                for element in eliminar:
                    tabla.simbolos.pop(element.id)
                tabla.simbolos.pop(buscar.id)
                resultadotxt += "Se elimino la tabla: " + self.iden + " de la base de datos: " + NombreDB + "\n"
        except:
            """ERROR SEMANTICO"""
        print(resultadotxt)
        return resultadotxt

#ALTER TABLE-------------------------------------
class altertb(instruccion):
    def __init__(self,iden, altertb2):
        self.iden = iden
        self.altertb2 = altertb2

    def traducir(self):
        traduccion = ''
        for alteracion in self.altertb2:
            subtraduccion = '\t' + 'sql.execute("ALTER TABLE '+ self.iden + ' '
            #Este es un Add
            if isinstance(alteracion, alteracion11):
                subtraduccion += ' ' + alteracion.texto + ' '
                if isinstance(alteracion.addprop, addprop):
                    temp = alteracion.addprop
                    subtraduccion += temp.texto
                    if isinstance(temp.lista, columna):
                        temp2 = temp.lista
                        subtraduccion += ' ' + temp2.iden + ' '
                        if isinstance(temp2.tipo, str):
                            subtraduccion += ' ' + temp2.tipo + ' '
                        elif isinstance(temp2.tipo, reservadatipo):
                            subtraduccion += temp2.iden + ' ' + str(temp2.tipo.restipo)
                            if (temp2.tipo.cantn is not None):
                                subtraduccion += '(' + str(temp2.tipo.cantn) +')'
                subtraduccion += ';")'
                subtraduccion += '\n'
                traduccion += subtraduccion
            #Este es un drop
            if isinstance(alteracion, alteracion1):
                subtraduccion = '\t' + 'sql.execute("ALTER TABLE '+ self.iden + ' '
                subtraduccion += ' ' + alteracion.texto + ' ' + alteracion.iden + ' '
                subtraduccion += ';")'
                subtraduccion += '\n'
                traduccion += subtraduccion

        return traduccion


    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        resultadotxt = ""
        for alteracion in self.altertb2:
            try:
                if alteracion.texto and alteracion.texto.lower() == "add":
                    if alteracion.addprop.texto and alteracion.addprop.texto.lower() == "column":
                        NuevaColumna = alteracion.addprop.lista
                        try:
                            resultado = func.alterAddColumn(NombreDB,self.iden,NuevaColumna.iden)
                            if resultado == 2:
                                e = errores.CError(0,0,"No existe la base de datos " + NombreDB,'Semantico')
                                errores.insert_error(e)
                                resultadotxt += "No existe la base de datos " + NombreDB + "\n"
                            elif resultado == 3:
                                e = errores.CError(0,0,"No existe la tabla " + self.iden,'Semantico')
                                errores.insert_error(e)
                                resultadotxt += "No existe la tabla " + self.iden + "\n"
                            else:
                                BuscarTabla = tabla.BuscarNombre(self.iden)
                                BuscarTabla.coltab+=1
                                tabla.actualizar(BuscarTabla)
                                NuevoSimboloColumna = TS.Simbolo(cont,NuevaColumna.iden,TS.TIPO.COLUMN,BuscarTabla.id,0,NuevaColumna.tipo,0,"","",False,"",(BuscarTabla.coltab-1))
                                cont+=1
                                tabla.agregar(NuevoSimboloColumna)
                                resultadotxt += "Se agrego la columna " + NuevoSimboloColumna.nombre + " a la tabla " + self.iden + "\n"
                        except:
                            """ERROR SEMANTICO"""
                if alteracion.texto and alteracion.texto.lower() == "drop column":
                    try:
                        ColumnaABorrar = tabla.BuscarNombre(alteracion.iden)
                        resultado = func.alterDropColumn(NombreDB,self.iden,ColumnaABorrar.numcol)
                        if resultado == 2:
                            e = errores.CError(0,0,"La base de datos " + NombreDB + " No existe",'Semantico')
                            errores.insert_error(e)
                            resultadotxt += "La base de datos " + NombreDB + " No existe \n"
                        elif resultado == 3:
                            e = errores.CError(0,0,"No se encontro la tabla " + self.iden + " en la base de datos " + NombreDB,'Semantico')
                            errores.insert_error(e)
                            resultadotxt += "No se encontro la tabla " + self.iden + " en la base de datos " + NombreDB + "\n"
                        elif resultado == 4:
                            e = errores.CError(0,0,"La columna " + ColumnaABorrar.nombre + " Es llave primaria",'Semantico')
                            errores.insert_error(e)
                            resultadotxt += "La columna " + ColumnaABorrar.nombre + " Es llave primaria" + "\n"
                        elif resultado == 5:
                            e = errores.CError(0,0,"La columna " + ColumnaABorrar.nombre + " No existe",'Semantico')
                            errores.insert_error(e)
                            resultadotxt += "La columna " + ColumnaABorrar.nombre + " No existe" + "\n"
                        else:
                            tabla.simbolos.pop(ColumnaABorrar.id)
                            OrdenarColumnas(self.iden)
                            resultadotxt += "Se elimino la columna " + ColumnaABorrar.nombre + " de la tabla " + self.iden + "\n"
                    except:
                        """ERROR SEMANTICO"""
            except:
                """ERROR"""
        print(resultadotxt)
        return resultadotxt

def OrdenarColumnas(NombreTabla):
    TablaActual = tabla.BuscarNombre(NombreTabla)
    ListaColumnas = []
    for simbolo in tabla.simbolos:
        if tabla.simbolos[simbolo].ambito == TablaActual.id and tabla.simbolos[simbolo].tipo == TS.TIPO.COLUMN:
            ListaColumnas.append(tabla.simbolos[simbolo])

    contador = 0
    for columna in ListaColumnas:
        columna.numcol = contador
        contador+=1
        tabla.actualizar(columna)

class alteracion1(instruccion):
    def __init__(self,texto, iden):
        self.texto = texto
        self.iden = iden

class alteracion11(instruccion):
    def __init__(self,texto, addprop):
        self.texto = texto
        self.addprop = addprop

class addprop(instruccion):
    def __init__(self,texto, lista):
        self.texto = texto
        self.lista = lista

class alter(instruccion):
    def __init__(self,iden, propaltcol):
        self.iden = iden
        self.propaltcol = propaltcol

class alteracion11111(instruccion):
    def __init__(self,texto, iden, colkey):
        self.iden = iden
        self.texto = texto
        self.colkey = colkey

#MANIPULACION DE DATOS
#INSERT-------------------------------------
class insert(instruccion):
    def __init__(self,iden, valores):
        self.iden = iden
        self.valores = valores

    def traducir(self):
        c3d = ''
        traduccion = ''
        traduccion += '\tsql.execute("INSERT INTO '+ self.iden + ' VALUES('

        for v in self.valores:

            if isinstance(v, llamadaF):
                print(v)
                c = v.traducir()
                c3d += '\t'+str(c[0]).replace('\n','\n\t')
                c3d += '\n'
                traduccion += "\"+"+str(c[1])+ "+\","
            else:
                if isinstance(v , (int, float, complex)):
                    traduccion += str(v) + ","
                elif isinstance(v, str):
                    traduccion += "'"+ v + "'" + ","
                elif isinstance(v, bool):
                    traduccion += str(v) + ","
                elif "ejecutar" in dir(v) :
                    traduccion += str(v.ejecutar()) + ","

        traduccion = traduccion.replace(",)",")")
        traduccion += ');")'
        traduccion += '\n'
        c3d += traduccion


        return c3d.replace(',)',')')

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        global contregistro
        resultadotxt = ""
        try:
            columnasdetabla = []
            tablas = tabla.BuscarNombre(self.iden)
            if not tablas:
                e = errores.CError(0,0,"No existe la tabla " + self.iden,'Semantico')
                errores.insert_error(e)
                return "No existe la tabla " + self.iden + "\n"
            for simbolo in tabla.simbolos:
                if tabla.simbolos[simbolo].ambito == tablas.id and not tabla.simbolos[simbolo].tipo == TS.TIPO.DATABASE and not tabla.simbolos[simbolo].tipo == TS.TIPO.TABLE and not tabla.simbolos[simbolo].tipo == TS.TIPO.TUPLA:
                    columnasdetabla.append(tabla.simbolos[simbolo])
            colcorrecta = []
            iter = 0
            for columna in columnasdetabla:
                if VerificarTipo(columna.tipocol, self.valores[iter]):
                    try:
                        if self.valores[iter].exp:
                            valcorrecto = self.valores[iter].ejecutar()
                            if isinstance(valcorrecto,errores.CError):
                                e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                                errores.insert_error(e)
                                return "Funcion Erronea"
                            else:
                                colcorrecta.append(str(valcorrecto))
                    except:
                        try:
                            if self.valores[iter].exp1:
                                valcorrecto = self.valores[iter].ejecutar()
                                if isinstance(valcorrecto,errores.CError):
                                    e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                                    errores.insert_error(e)
                                    return "Funcion Erronea"
                                else:
                                    colcorrecta.append(str(valcorrecto))
                        except:
                            colcorrecta.append(self.valores[iter])
                else:
                    resultadotxt += "El tipo de valor no coincide con la columna"
                iter+=1
            resultado = func.insert(NombreDB,self.iden,colcorrecta)
            if resultado == 2:
                e = errores.CError(0,0,"No existe la base de datos " + NombreDB,'Semantico')
                errores.insert_error(e)
                resultadotxt += "No existe la base de datos " + NombreDB + "\n"
            elif resultado == 3:
                e = errores.CError(0,0,"No existe la base tabla " + NombreDB,'Semantico')
                errores.insert_error(e)
                resultadotxt += "No existe la base tabla " + NombreDB + "\n"
            elif resultado == 5:
                e = errores.CError(0,0,"La cantidad de valores no coincide con la cantidad de columnas",'Semantico')
                errores.insert_error(e)
                resultadotxt += "La cantidad de valores no coincide con la cantidad de columnas\n"
            else:
                nombrereg = "registro" + str(contregistro)
                NuevoRegistro = TS.Simbolo(cont,nombrereg,TS.TIPO.TUPLA,tablas.id,0,"",0,"","",False,"",0,colcorrecta)
                contregistro+=1
                cont+=1
                tabla.agregar(NuevoRegistro)

                resultadotxt += "El registro  " + nombrereg + " fue agregado a la tabla " + self.iden + "\n"
        except:
            """ERRORES SEMANTICOS"""
        print(resultadotxt)
        return resultadotxt

#FUNCIONES MATH
class funcionesmath():
    'Abstract Class'

class math_abs2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return abs(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_cbrt2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return mt.cbrt(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_ceil2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return mt.ceil(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_degrees2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return mt.degrees(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_div2(funcionesmath):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self):
        try:
            num1 = float(self.exp1)
            num2 = float(self.exp2)
            return mt.div(num1 , num2)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_exp2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def ejecutar(self):
        try:
            num = int(self.exp)
            return mt.exp(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_factorial2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = int(self.exp)
            return mt.factorial(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_floor2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return mt.floor(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_gcd2(funcionesmath):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self):
        try:
            num1 = int(self.exp1)
            num2 = int(self.exp2)
            return mt.gcd(num1,num2)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_lcm2(funcionesmath):
    def __init__(self,exp1,exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self):
        try:
            num1 = int(self.exp1)
            num2 = int(self.exp2)
            return mt.lcm(num1,num2)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_ln2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return mt.ln(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_log2(funcionesmath):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self):
        try:
            num1 = int(self.exp1)
            num2 = int(self.exp2)
            return mt.log(num1,num2)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_log102(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        num = float(self.exp)
        return mt.log10(num)

class math_min_scale2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = int(self.exp)
            return mt.min_scale(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_scale2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            return mt.scale(str(self.exp))
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_mod2(funcionesmath):
    def __init__(self, exp1,exp2):
        self.exp1 = exp1
        self.exp2  = exp2

    def ejecutar(self):
        try:
            num1 = float(self.exp1)
            num2 = float(self.exp2)
            return mt.mod(num1,num2)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_pi2(funcionesmath):
    def __init__(self):
        self.val = mt.pi()

    def ejecutar(self):
        try:
            return self.val
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_power2(funcionesmath):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self):
        try:
            num1 = int(self.exp1)
            num2 = int(self.exp2)
            return mt.power(num1,num2)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_radians2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return mt.radians(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_round2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return round(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_sign2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return mt.sign(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_sqrt2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return mt.sqrt(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_trim_scale2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def ejecutar(self):
        try:
            num = int(self.exp)
            return mt.trim_scale(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_widthBucket2(funcionesmath):
    def __init__(self, exp1, exp2, exp3, exp4):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4

    def ejecutar(self):
        #xd
        try:
            return mt.width_bucket(9,8,7,6)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_trunc2(funcionesmath):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):
        #no es diccionario
        try:
            num = float(self.exp)
            return mt.trunc(num)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

class math_random2(funcionesmath):
    def __init__(self):
        """VACIO"""

    def ejecutar(self):
        return mt.random()

class math_setseed2(funcionesmath):
    def __init__(self,exp):
        self.exp = exp

    def ejecutar(self):
        try:
            mt.setseed(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion matematica",'Semantico')
            errores.insert_error(e)
            return e

#FUNCIONES TRIGONOMETRICAS
class funcionestrig():
    'Abstract Class'

class trig_acos2(funcionestrig):
    def __init__(self, exp):
        self.exp = exp

    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.acos(float(temp))
        return trim

class trig_acosd2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.acosd(float(temp))

        return trim

class trig_asin2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.asin(float(temp))

        return trim

class trig_asind2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

            trim = mt.asind(float(temp))

            return trim

class trig_atan2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

            trim = mt.atan(float(temp))

            return trim

class trig_atand2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp



    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

            trim = mt.atand(float(temp))

            return trim

class trig_atan22(funcionestrig):
    def __init__(self, exp1, exp2 ):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self):

        try:
            temp1 = float(self.exp1)
            temp2 = float(self.exp2)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.atan2(temp1,temp2)

        return trim

class trig_atan2d2(funcionestrig):
    def __init__(self, exp1, exp2 ):
        self.exp1 = exp1
        self.exp2 = exp2


    def ejecutar(self):

        try:
            temp1 = float(self.exp1)
            temp2 = float(self.exp2)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.atan2d(temp1,temp2)

        return trim

class trig_cos2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.cos(float(temp))

        return trim

class trig_cosd2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.cosd(float(temp))

        return trim

class trig_cot2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.cot(float(temp))

        return trim

class trig_cotd2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.cotd(float(temp))

        return trim

class trig_sin2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.sin(float(temp))

        return trim

class trig_sind2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.sind(float(temp))

        return trim

class trig_tan2(funcionestrig):
    def __init__(self, exp ):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.tan(float(temp))

        return trim

class trig_tand2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp



    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.tand(float(temp))

        return trim

class trig_sinh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp

    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.sinh(float(temp))

        return trim

class trig_cosh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.cosh(float(self.exp))

        return trim

class trig_tanh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.tanh(float(temp))

        return trim

class trig_asinh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.asinh(float(temp))

        return trim

class trig_acosh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.acosh(float(temp))

        return trim

class trig_atanh2(funcionestrig):
    def __init__ (self,exp):
        self.exp = exp


    def ejecutar(self):

        try:
            temp = float(self.exp)
        except ValueError:
            e = errores.CError(0,0,"Error en funcion trigonometrica",'Semantico')
            errores.insert_error(e)
            return e

        trim = mt.atanh(float(temp))

        return trim

#FUNCIONES GENERALES
class funciongen():
    'clase Abstracta'

class fun_length2(funciongen):
    def __init__ (self,exp):
        self.exp = exp

    def ejecutar(self):

        #saco el substring y lo devuelvo
        temp =  str(self.exp )
        trim = len(temp)

        return trim

class fun_trim2(funciongen):
    def __init__ (self,exp):
        self.exp = exp

    def ejecutar(self):

        temp =  str(self.exp)
        trim =  temp.strip()

        return trim

class fun_md52(funciongen):
    def __init__ (self,exp):
        self.exp = exp

    def ejecutar(self):

        #saco el substring y lo devuelvo
        temp =  str(self.exp )
        crypt = hashlib.md5()
        crypt.update(temp.encode('utf-8'))
        r = crypt.hexdigest()

        return r

class fun_sha2562(funciongen):
    def __init__ (self,exp):
        self.exp = exp

    def ejecutar(self):

        #saco el substring y lo devuelvo
        temp =  str(self.exp)
        crypt = hashlib.sha256()
        crypt.update(temp.encode('utf-8'))
        r = crypt.hexdigest()

        return r

class fun_substr2(funciongen):
    def __init__ (self,exp,min,max):
        self.exp = exp
        self.min = min
        self.max = max

    def ejecutar(self):

        #saco el substring y lo devuelvo
        temp =  str(self.exp)
        sub = temp[self.min:self.max]

        return sub

class fun_greatest2(funciongen):
    def __init__ (self,lexps):
        self.lexps = lexps

    def ejecutar(self):

        try:
            maximo = float(self.lexps[0])

            for dato in self.lexps:
                temp = float(dato)

                if maximo < temp:
                    maximo = temp


                return maximo
        except:
            e = errores.CError(0,0,"Funcion least necesita una lista",'Semantico')
            errores.insert_error(e)
            return e

class fun_least2(funciongen):
    def __init__ (self,lexps):
        self.lexps = lexps

    def ejecutar(self):

        try:
            maximo = float(self.lexps[0])

            for dato in self.lexps:
                temp = float(dato)

                if maximo > temp:
                    maximo = temp


                return maximo
        except:
            e = errores.CError(0,0,"Funcion least necesita una lista",'Semantico')
            errores.insert_error(e)
            return e

class dato2(funciongen):
    def __init__ (self,val):
        self.val = val

class fun_now2(funciongen):
    def __init__ (self,exp):
        self.exp = exp

    def ejecutar(self):
        # dd/mm/YY
        today = date.today()
        d1 = today.strftime("%Y-%m-%d %H:%M:%S")
        return d1

def VerificarTipo(TipoColumna,ValorColumna):
    """try:
        if float(ValorColumna):
            TipoRegistro = definir_tipo(float(ValorColumna))
        elif int(ValorColumna):
            TipoRegistro = definir_tipo(int(ValorColumna))
    except:
        TipoRegistro = definir_tipo(ValorColumna)
    if TipoRegistro == "smallint" and TipoColumna == "integer":
        TipoRegistro = "integer"
    try:
        if TipoColumna.restipo.lower() == TipoRegistro:
            return True
        else:
            return False
    except:
        if TipoColumna.lower() == TipoRegistro:
            return True
        else:
            return False"""
    return True

def definir_tipo(entrada):
    """if isinstance(entrada,int) or isinstance(entrada,float):
        if entrada < 32767 and entrada > -32768:
            return "smallint"
        elif entrada < 214783648 and entrada > -214783648:
            return "integer"
        elif entrada < 9223372036854775808 and entrada > -9223372036854775808:
            return "bigint"
        elif entrada < 92233720368547758.08  and entrada > -92233720368547758.08 :
            return "money"
        else:
            return "decimal"
    elif isinstance(entrada,bool):
        return "boolean"
    else:
        g = entrada.count('-')
        dp = entrada.count(':')
        if len(entrada) == 1:
            return "char"
        elif g == 3 and dp == 3:
            return "time"
        elif g == 3 and dp == 0:
            return "date"
        else:
            return "varchar"""

#UPDATE-----------------------------------------
class update(instruccion):
    def __init__(self,iden, cond, wherecond):
        self.iden = iden
        self.cond = cond
        self.wherecond = wherecond

    def traducir(self):
        traduccion = '\t'
        traduccion += 'sql.execute("UPDATE'
        traduccion += ' ' + self.iden
        NombreColumna = self.cond.iden
        traduccion += ' SET ' + NombreColumna
        traduccion += ' = '
        if isinstance(self.cond.tipo , (int, float, complex)):
            traduccion += str(self.cond.tipo)
        elif isinstance(self.cond.tipo , str):
            traduccion += "'" + self.cond.tipo + "'"
        elif isinstance(self.cond.tipo, bool):
            traduccion += str(self.cond.tipo )
        else:
            try:
                temp = self.cond.tipo.ejecutar()
                if isinstance(temp, (int, float, complex)):
                    traduccion += str(temp)
                elif isinstance(temp, str):
                    traduccion += temp
                elif isinstance(temp, bool):
                    traduccion += str(temp)
            except:
                '''error'''

        traduccion += ' WHERE '
        tempwherw = self.wherecond

        if isinstance(tempwherw,wherecond1):
            traduccion += ' ' + tempwherw.iden
            traduccion += ' ' + tempwherw.signo
            if isinstance(tempwherw.tipo, str):
                traduccion += " '" + tempwherw.tipo + "'"
            elif isinstance(tempwherw.tipo, (int, float, complex)):
                traduccion += ' ' + str(tempwherw.tipo)
            if "ejecutar" in dir(self.wherecond.tipo):
                traduccion += ' ' + str(self.wherecond.tipo.ejecutar())
        if isinstance(tempwherw, wherecond):
            traduccion += ' ' + tempwherw.iden + ' BETWEEN'
            try:
                traduccion += ' ' + str(tempwherw.tipo.ejecutar())
            except:
                traduccion += ' ' + tempwherw.tipo
            traduccion += ' AND '
            try:
                traduccion += ' ' + str(tempwherw.tipo2.ejecutar()) + ' '
            except:
                traduccion += ' ' + str(tempwherw.tipo2) + ' '

        traduccion += ';")'
        traduccion += '\n'

        return traduccion

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        resultadotxt = ""
        try:
            TuplasTabla = []
            ColumnasTabla = []
            #OBTENER LAS TUPLAS Y COLUMNAS DE LA TABLA
            TablaActual = tabla.BuscarNombre(self.iden)
            for simbolo in tabla.simbolos:
                if tabla.simbolos[simbolo].ambito == TablaActual.id and tabla.simbolos[simbolo].tipo == TS.TIPO.TUPLA:
                    TuplasTabla.append(tabla.simbolos[simbolo])
                if tabla.simbolos[simbolo].ambito == TablaActual.id and tabla.simbolos[simbolo].tipo == TS.TIPO.COLUMN:
                    ColumnasTabla.append(tabla.simbolos[simbolo])
            #OBTENER CAMPO DE CONDICION

            #Condicion = self.wherecond.tipo

            try:
                if self.wherecond.tipo.exp:
                    Condicion = self.wherecond.tipo.ejecutar()
                    if isinstance(Condicion,errores.CError):
                        e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                        errores.insert_error(e)
                        return "Funcion Erronea"
            except:
                try:
                    if self.wherecond.tipo.exp1:
                        Condicion = self.wherecond.tipo.ejecutar()
                        if isinstance(Condicion,errores.CError):
                            e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                            errores.insert_error(e)
                            return "Funcion Erronea"
                except:
                    Condicion = self.wherecond.tipo
            NombreColumna = self.cond.iden
            columnacond = self.wherecond.iden
            try:
                #cond2 = self.wherecond.tipo2

                try:
                    if self.wherecond.tipo2.exp:
                        cond2 = self.wherecond.tipo2.ejecutar()
                        if isinstance(cond2,errores.CError):
                            e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                            errores.insert_error(e)
                            return "Funcion Erronea"
                except:
                    try:
                        if self.wherecond.tipo2.exp1:
                            cond2 = self.wherecond.tipo2.ejecutar()
                            if isinstance(cond2,errores.CError):
                                e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                                errores.insert_error(e)
                                return "Funcion Erronea"
                    except:
                        cond2 = self.wherecond.tipo2

                TuplasMod = []
                for columna in ColumnasTabla:
                    if columna.nombre == NombreColumna:
                        ColumnaModificar = columna
                        break
                for columna in ColumnasTabla:
                    if columna.nombre == columnacond:
                        ColumnaCondicion = columna
                        break
                for tupla in TuplasTabla:
                    if Condicion <= tupla.registro[ColumnaCondicion.numcol] and tupla.registro[ColumnaCondicion.numcol] <= cond2:
                        TuplasMod.append(tupla)
                for registro in TuplasMod:
                    registro.registro[ColumnaModificar.numcol] = self.cond.tipo
                    tabla.actualizar(registro)
                func.update(NombreDB,self.iden,TuplasMod,ColumnasTabla)
                resultadotxt += "Los registros fueron actualizados\n"
            except:
                for tupla in TuplasTabla:
                    for registro in tupla.registro:
                        if Condicion == registro:
                            TuplaModificar = tupla
                            break
                for columna in ColumnasTabla:
                    if columna.nombre == NombreColumna:
                        ColumnaModificar = columna
                        break
                TuplaModificar.registro[ColumnaModificar.numcol] = self.cond.tipo
                tabla.actualizar(TuplaModificar)
                #SE ACTUALIZA EL ARCHIVO JSON
                TuplasTabla = []
                for simbolo in tabla.simbolos:
                    if tabla.simbolos[simbolo].ambito == TablaActual.id and tabla.simbolos[simbolo].tipo == TS.TIPO.TUPLA:
                        TuplasTabla.append(tabla.simbolos[simbolo])
                func.update(NombreDB,self.iden,TuplasTabla,ColumnasTabla)
                resultadotxt += "Los registros fueron actualizados\n"
        except:
            """ERROR"""
        return resultadotxt

#DELETE-------------------------------------------
class delete(instruccion):
    def __init__(self,iden, wherecond):
        self.iden = iden
        self.wherecond = wherecond

    def traducir(self):
        tempwherw = self.wherecond
        traduccion = '\t'
        traduccion += 'sql.execute("DELETE FROM ' + self.iden + ' WHERE '
        if isinstance(tempwherw,wherecond1):
            traduccion += ' ' + tempwherw.iden
            traduccion += ' ' + tempwherw.signo
            if isinstance(tempwherw.tipo, str):
                traduccion += " '" + tempwherw.tipo + "'"
            elif isinstance(tempwherw.tipo, (int, float, complex)):
                traduccion += ' ' + str(tempwherw.tipo)
            if "ejecutar" in dir(self.wherecond.tipo):
                traduccion += ' ' + str(self.wherecond.tipo.ejecutar())
        if isinstance(tempwherw, wherecond):
            traduccion += ' ' + tempwherw.iden + ' BETWEEN'
            try:
                traduccion += ' ' + str(tempwherw.tipo.ejecutar())
            except:
                traduccion += ' ' + tempwherw.tipo
            traduccion += ' AND '
            try:
                traduccion += ' ' + str(tempwherw.tipo2.ejecutar()) + ' '
            except:
                traduccion += ' ' + str(tempwherw.tipo2) + ' '

        traduccion += ';")'
        traduccion += '\n'

        return traduccion

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        resultadotxt = ""
        try:
            TablaActual = tabla.BuscarNombre(self.iden)
            if not TablaActual:
                e = errores.CError(0,0,"No existe la tabla " + self.iden,'Semantico')
                errores.insert_error(e)
                return "No existe la tabla " + self.iden
            TuplasTabla = []
            ColumnasTabla = []
            for simbolo in tabla.simbolos:
                if tabla.simbolos[simbolo].ambito == TablaActual.id and tabla.simbolos[simbolo].tipo == TS.TIPO.TUPLA:
                    TuplasTabla.append(tabla.simbolos[simbolo])
                if tabla.simbolos[simbolo].ambito == TablaActual.id and tabla.simbolos[simbolo].tipo == TS.TIPO.COLUMN:
                    ColumnasTabla.append(tabla.simbolos[simbolo])
            resultado = func.delete(NombreDB,self.iden,ColumnasTabla)
            try:
                #BETWEEN
                #cond2 = self.wherecond.tipo2

                try:
                    if self.wherecond.tipo2.exp:
                        cond2 = self.wherecond.tipo2.ejecutar()
                        if isinstance(cond2,errores.CError):
                            e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                            errores.insert_error(e)
                            return "Funcion Erronea"
                except:
                    try:
                        if self.wherecond.tipo2.exp1:
                            cond2 = self.wherecond.tipo.ejecutar()
                            if isinstance(cond2,errores.CError):
                                e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                                errores.insert_error(e)
                                return "Funcion Erronea"
                    except:
                        cond2 = self.wherecond.tipo2

                #cond1 = self.wherecond.tipo

                try:
                    if self.wherecond.tipo.exp:
                        cond1 = self.wherecond.tipo.ejecutar()
                        if isinstance(cond1,errores.CError):
                            e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                            errores.insert_error(e)
                            return "Funcion Erronea"
                except:
                    try:
                        if self.wherecond.tipo.exp1:
                            cond1 = self.wherecond.tipo.ejecutar()
                            if isinstance(cond1,errores.CError):
                                e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                                errores.insert_error(e)
                                return "Funcion Erronea"
                    except:
                        cond1 = self.wherecond.tipo

                campocond = self.wherecond.iden
                for columna in ColumnasTabla:
                    if columna.nombre == campocond:
                        ColumnaMod = columna
                        break
                ListaTuplaDelete = []
                for tupla in TuplasTabla:
                    if tupla.registro[ColumnaMod.numcol] >= cond1 and tupla.registro[ColumnaMod.numcol] <= cond2:
                        ListaTuplaDelete.append(tupla)
                for tupla in ListaTuplaDelete:
                    tabla.simbolos.pop(tupla.id)
                resultadotxt += "Se eliminaron los registros de la tabla\n"
            except:

                #cond = self.wherecond.tipo

                try:
                    if self.wherecond.tipo.exp:
                        cond = self.wherecond.tipo.ejecutar()
                        if isinstance(cond,errores.CError):
                            e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                            errores.insert_error(e)
                            return "Funcion Erronea"
                except:
                    try:
                        if self.wherecond.tipo.exp1:
                            cond = self.wherecond.tipo.ejecutar()
                            if isinstance(cond,errores.CError):
                                e = errores.CError(0,0,"Funcion Erroneo",'Semantico')
                                errores.insert_error(e)
                                return "Funcion Erronea"
                    except:
                        cond = self.wherecond.tipo

                campocond = self.wherecond.iden
                for columna in ColumnasTabla:
                    if columna.nombre == campocond:
                        ColumnaMod = columna
                        break
                ListaTuplaDelete = []
                for tupla in TuplasTabla:
                    if tupla.registro[ColumnaMod.numcol] == cond:
                        ListaTuplaDelete.append(tupla)
                for tupla in ListaTuplaDelete:
                    tabla.simbolos.pop(tupla.id)
                resultadotxt += "Se eliminaron los registros de la tabla\n"
        except:
            """ERROR"""
        return resultadotxt

#--------------------------------------------CLASES PARA LOS INDICES--------------------------------------------------
class IndexCreate(instruccion):
    'Clase principal para la creacion de indices'

    def __init__(self,uniqueind, id1, id2, createind2):
        self.uniqueind = uniqueind
        self.id1 = id1
        self.id2 = id2
        self.createind2 = createind2

    def traducir(self):
        traduccion = '\t'
        traduccion += 'sql.execute("CREATE UNIQUE INDEX ' + self.id1 + ' ON ' + self.id2 + '('

        if isinstance(self.createind2, createind3):
            temp = self.createind2.listacolind
            for x in temp:
                #falta ver si puede ser una llamada
                if isinstance(x, str):
                    traduccion += ' '+ x + ','
                if isinstance(x, llamadaF):
                    traduccion += ' ' + x.id + ','

        traduccion = traduccion.replace(',)',')')
        traduccion += ');")'
        traduccion += '\n'
        return traduccion.replace(',)',')')

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        global contambito
        try:
            NuevoIndice = TS.Simbolo(cont,self.id1,TS.TIPO.INDICE,contambito)
            cont+=1
            contambito+=1
            NuevoIndice.uniqueind = self.uniqueind
            NuevoIndice.tablaind = self.id2
            if self.uniqueind != "":
                NuevoIndice.tipoind = "UNIQUE INDEX"
            else:
                NuevoIndice.tipoind = "INDEX"
            if isinstance(self.createind2, createind3):
                "createind2 es createind3"
                columnasdeindice = []
                columnastexto = ""
                for columna in self.createind2.listacolind:
                    if isinstance(columna, columnaind):
                        "ES UN OBJETO"
                        if isinstance(columna.propiedad, ordenind):
                            if NuevoIndice.ordenind == "":
                                NuevoIndice.ordenind = columna.propiedad.orden
                                columnasdeindice.append(columna.id)
                            else:
                                NuevoIndice.ordenind = "Ninguno"
                                columnasdeindice.append(columna.id)
                        else:
                            NuevoIndice.ordenind = "Ninguno"
                            columnasdeindice.append(columna.propiedad)
                    else:
                        if NuevoIndice.ordenind == "":
                            NuevoIndice.ordenind = "Ninguno"
                        columnasdeindice.append(columna)
                for elemento in columnasdeindice:
                    columnastexto += elemento + " "
                NuevoIndice.columnaind = columnastexto
                NuevoIndice.listacolind = columnasdeindice
            tabla.agregar(NuevoIndice)
            return "Se agrego el indice " + self.id1 + " a la tabla de simbolos"
        except:
            return "Error al crear indice"

class createind3(instruccion):
    def __init__(self,listacolind, indwhere):
        self.listacolind = listacolind
        self.indhwere = indwhere

class columnaind(instruccion):
    def __init__(self,id, propiedad):
        self.id = id
        self.propiedad = propiedad

class ordenind(instruccion):
    def __init__(self,orden):
        self.orden = orden

class indwhere(instruccion):
    def __init__(self,indnot, indwherecond):
        self.indnot = indnot
        self.indwherecond = indwherecond

class notval(instruccion):
    def __init__(self, id1, signo, id2, valortipo):
        self.id1 = id1
        self.signo = signo
        self.id2 = id2
        self.valortipo = valortipo

class indwherecond(instruccion):
    def __init__(self, id, signo, valortipo):
        self.id = id
        self.signo = signo
        self.valortipo = valortipo
#----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------CLASES PARA DROP INDICES--------------------------------------------------
class IndexDrop(instruccion):
    def __init__(self, tipo, listaindices, orden):
        self.tipo = tipo
        self.listaindices = listaindices
        self.orden = orden

    def traducir(self):
        traduccion = ''
        for x in self.listaindices:
            traduccion += '\tsql.execute("DROP INDEX ' + x + ';")'+ '\n'
        return traduccion

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        global contambito
        textores = ""
        try:
            eliminar = []
            for indice in self.listaindices:
                if tabla.BuscarNombre(indice):
                    eliminarindice = tabla.BuscarNombre(indice)
                    eliminar.append(eliminarindice)
                else:
                    textores += "No se encontro el indice " + indice + "\n"
            for simbolo in eliminar:
                if simbolo.tipo == TS.TIPO.INDICE:
                    tabla.simbolos.pop(simbolo.id)
                    textores += "Se elimino el indice " + simbolo.nombre + " de la tabla de simbolos\n"
            return textores
        except:
            return "Error en " + self.tipo

#--------------------------------------------CLASES PARA ALTER INDICES-------------------------------------------------
class IndexAlter(instruccion):
    def __init__(self, tipo, alterind2):
        self.tipo = tipo
        self.alterind2 = alterind2

    def traducir(self):
        return ''

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        global contambito
        try:
            if self.alterind2.tipocambio.lower() == "alter" or self.alterind2.tipocambio.lower() == "alter column":
                if isinstance(self.alterind2.listacol, alterind):
                    if tabla.BuscarNombre(self.alterind2.id):
                        Indice = tabla.BuscarNombre(self.alterind2.id)
                        iter = 0
                        for col in Indice.listacolind:
                            if col == self.alterind2.listacol.buscarid:
                                Indice.listacolind[iter] = self.alterind2.listacol.nuevoid
                                break
                            iter+=1

                        columnastexto = ""
                        for elemento in Indice.listacolind:
                            columnastexto += elemento + " "
                        Indice.columnaind = columnastexto
                        tabla.actualizar(Indice)
                        if Indice.listacolind[iter] == self.alterind2.listacol.buscarid:
                            return "No existe la columna " +  self.alterind2.listacol.buscarid + " en el indice " + self.alterind2.id
                        return "Se cambio la columna " + self.alterind2.listacol.buscarid + " por " + self.alterind2.listacol.nuevoid + " del indice " + self.alterind2.id
                    else:
                        return "No existe el indice" + self.alterind2.id
            else:
                NuevoAlterIndex = TS.Simbolo(cont,self.alterind2.id,TS.TIPO.INDICE,contambito)
                cont+=1
                contambito+=1
                NuevoAlterIndex.tipoind = self.tipo
                NuevoAlterIndex.indicesind = self.alterind2.id
                NuevoAlterIndex.ordenind = self.alterind2.tipocambio
                NuevoAlterIndex.tablaind = "Ninguno"
                coltexto = ""
                for col in self.alterind2.listacol:
                    coltexto += col + " "
                NuevoAlterIndex.columnaind = coltexto
                tabla.agregar(NuevoAlterIndex)
                return "Se agrego el " + self.tipo + " a la tabla de simbolos"
        except:
            return "Error en " + self.tipo

class propalter(instruccion):
    def __init__(self, tipocambio, id, listacol):
        self.tipocambio = tipocambio
        self.id = id
        self.listacol = listacol

class alterind(instruccion):
    def __init__(self,buscarid,nuevoid):
        self.buscarid = buscarid
        self.nuevoid = nuevoid


