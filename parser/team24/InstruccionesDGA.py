import storage as func
import tablaDGA as TS

#VARIABLES GLOBALES
resultadotxt = ""
tabla = TS.Tabla()
cont = 0
contambito = 0
NombreDB = ""
contregistro = 0

def Textoresultado():
    global tabla
    global resultadotxt
    print(resultadotxt)
    for simbolo in tabla.simbolos:
        print("ID: " + str(tabla.simbolos[simbolo].id) + " Nombre: " + tabla.simbolos[simbolo].nombre + " Ambito: " + str(tabla.simbolos[simbolo].ambito))
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
                resultadotxt += "Se creo la base de datos " + self.iden + "\n"
                return "Se creo la base de datos " + self.iden + "\n"
            elif resultado == 2 and not self.replacedb:
                resultadotxt += "Ya existe la base de datos " + self.iden + "\n"
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
                return "Se reemplazo la base de datos: " + self.iden + "\n"
            else:
                resultadotxt += "Error al crear base de datos: " + self.iden + "\n"
                return "Error al crear base de datos: " + self.iden + "\n"
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
                resp =""
                resp += "\nBases de datos existentes:\n"
                for base in resultado:
                    resultadotxt += str(contador) + ". " + base + "\n"
                    resp += str(contador) + ". " + base + "\n"
                    contador += 1
                return resp
            else:
                resultadotxt += "No existen bases de datos"
                return "No existen bases de datos"
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
                    resultadotxt += "No existe la base de datos " + self.alterdb2.iden + "\n"
                    return "No existe la base de datos " + self.alterdb2.iden + "\n"
                if resultado == 3:
                    resultadotxt += "Ya existe la base de datos " + self.alterdb2.alterdb3.iden + "\n"
                    return "Ya existe la base de datos " + self.alterdb2.alterdb3.iden + "\n"
                else:
                    buscar = tabla.BuscarNombre(self.alterdb2.iden)
                    buscar.nombre = self.alterdb2.alterdb3.iden
                    tabla.actualizar(buscar)
                    resultadotxt += "Se actualizo la base de datos " + self.alterdb2.iden + " a " + self.alterdb2.alterdb3.iden + "\n"
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

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        try:       
            resultado = func.dropDatabase(self.iden)
            if(resultado == 2):
                resultadotxt += "No existe la base de datos " + self.iden + "\n"
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
                return "Se elimino la base de datos " + self.iden + "\n"
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
        resultadotxt += "Usando la base de datos " + self.iden + "\n"
        return "Usando la base de datos " + self.iden + "\n"

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
        resultadotxt = ""
        try:       
            resultado = func.createTable(NombreDB, self.iden,0)
            if(resultado == 2):
                resultadotxt += "No existe la base de datos: " + NombreDB + "\n"
            elif(resultado == 3):
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
                            resultadotxt += "No existe la base de datos " + NombreDB + "\n"
                        elif resultado == 3:
                            resultadotxt += "No existe la tabla " + self.iden + "\n"
                        elif resultado == 4:
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
                                    resultadotxt += "No existe la base de datos " + NombreDB + "\n"
                                elif resultado == 3:
                                    resultadotxt += "No existe la tabla " + self.iden + "\n"
                                elif resultado == 4:
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
                        resultadotxt += "No existe la tabla " + self.inherits + "\n"
                resultadotxt += "Se creo la tabla: " + self.iden + " En la base de datos: " + NombreDB + "\n"
        except:
            """ERROR SEMANTICO"""
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

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        resultadotxt = ""
        try:       
            resultado = func.dropTable(NombreDB, self.iden)
            if(resultado == 2):
                resultadotxt += "No existe la base de datos " + NombreDB + "\n"
            elif(resultado == 3):
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
        return resultadotxt

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
        resultadotxt = ""
        for alteracion in self.altertb2:
            if alteracion.texto and alteracion.texto.lower() == "add":
                if alteracion.addprop.texto and alteracion.addprop.texto.lower() == "column":
                        NuevaColumna = alteracion.addprop.lista
                        try:
                            resultado = func.alterAddColumn(NombreDB,self.iden,NuevaColumna.iden)
                            if resultado == 2:
                                resultadotxt += "No existe la base de datos " + NombreDB + "\n"
                            elif resultado == 3:
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
                        resultadotxt += "La base de datos " + NombreDB + " No existe \n"
                    elif resultado == 3:
                        resultadotxt += "No se encontro la tabla " + self.iden + " en la base de datos " + NombreDB + "\n"
                    elif resultado == 4:
                        resultadotxt += "La columna " + ColumnaABorrar.nombre + " Es llave primaria" + "\n"
                    elif resultado == 5:
                        resultadotxt += "La columna " + ColumnaABorrar.nombre + " No existe" + "\n"
                    else:
                        tabla.simbolos.pop(ColumnaABorrar.id)
                        OrdenarColumnas(self.iden)
                        resultadotxt += "Se elimino la columna " + ColumnaABorrar.nombre + " de la tabla " + self.iden + "\n"
                except:
                    """ERROR SEMANTICO"""
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
            for simbolo in tabla.simbolos:
                if tabla.simbolos[simbolo].ambito == tablas.id and not tabla.simbolos[simbolo].tipo == TS.TIPO.DATABASE and not tabla.simbolos[simbolo].tipo == TS.TIPO.TABLE and not tabla.simbolos[simbolo].tipo == TS.TIPO.TUPLA:
                    columnasdetabla.append(tabla.simbolos[simbolo])
            colcorrecta = []
            iter = 0
            for columna in columnasdetabla:
                if VerificarTipo(columna.tipocol, self.valores[iter]):
                    colcorrecta.append(self.valores[iter])
                else:
                    resultadotxt += "El tipo de valor no coincide con la columna"
                iter+=1
            resultado = func.insert(NombreDB,self.iden,colcorrecta)
            if resultado == 2:
                resultadotxt += "No existe la base de datos " + NombreDB + "\n"
            elif resultado == 3:
                resultadotxt += "No existe la base tabla " + NombreDB + "\n"
            elif resultado == 5:
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
        return resultadotxt

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
            Condicion = self.wherecond.tipo
            NombreColumna = self.cond.iden
            columnacond = self.wherecond.iden
            try:
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

    def ejecutar(self):
        global resultadotxt
        global cont
        global tabla
        global NombreDB
        resultadotxt = ""
        try:
            TablaActual = tabla.BuscarNombre(self.iden)
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
                cond2 = self.wherecond.tipo2
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