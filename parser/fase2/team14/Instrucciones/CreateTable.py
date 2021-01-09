from Instrucciones.Instruccion import Instruccion
from Instrucciones.AtrColumna import AtributosColumna
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.variablesestaticas import variables
from tkinter import *
from reportes import *


class CreateTable(Instruccion):
    def __init__(self, id: str, listaDef):
        self.id = id
        self.listaDef = listaDef
        self.herencia = None
        self.listPK = []
        self.codigo3d = "ci.ejecutarsql(\"create table " + self.id + " ( " + listaDef[0].stringsql

    def ejecutar(self, ent: Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            tam = len(self.listaDef)
            nuevaTabla = Simbolo(TipoSimbolo.TABLA, (self.id + "_" + dbActual))
            listaColumnas = []
            listaAtrCol = []
            hayPrimaria = False
            hayForanea = False
            primariaAdd: Primaria = None
            foraneaAdd: Foranea = None
            inicioHerencia = 0

            if self.herencia != None:
                r: Simbolo = ent.buscarSimbolo(self.herencia + "_" + dbActual)
                if r != None:
                    for colPadre in r.valor:
                        listaColumnas.append(colPadre)
                        if colPadre.atributos.get('primary') != None:
                            coPrimary: Simbolo = ent.buscarSimbolo(colPadre.atributos.get('primary'))
                            if coPrimary != None:
                                self.listPK = coPrimary.valor

                    inicioHerencia = len(r.valor)

                else:
                    variables.consola.insert(INSERT, "La tabla padre '" + self.herencia + "' no existe")
                    reporteerrores.append(
                        Lerrores("Error Semántico", "La tabla padre '" + self.herencia + "' no existe", "", ""))

            for x in range(0, tam, 1):
                tt = self.listaDef[x]
                if tt.tipo == AtributosColumna.COLUMNA_SIMPLE:
                    nuevaColumna = Simbolo(tt.tipoDato, tt.identificador)
                    if tt.lista != None:  # aca se mete si viene por ejemplo: columna1 integer references tabla2
                        tamano = len(tt.lista)
                        for y in range(tamano):
                            hayAtr = False
                            nuevoSym = Simbolo("tipo", "nombre")
                            nuevoSym.baseDatos = dbActual
                            nuevoSym.tabla = self.id
                            atrColumna: Atributo = tt.lista[y]
                            if atrColumna.tipo == AtributosColumna.UNICO:
                                hayAtr = True
                                nuevoSym.tipo = TipoSimbolo.CONSTRAINT_UNIQUE
                                if atrColumna.valor != None:  # forma de: constraint id UNIQUE
                                    # formato de nombre: U_database_tabla_nombreColumna_idConstraint
                                    nuevoSym.nombre = str(
                                        "U_" + dbActual + "_" + self.id + "_" + tt.identificador + "_" + atrColumna.valor)
                                    nuevaColumna.atributos.update({'unique': str(
                                        "U_" + dbActual + "_" + self.id + "_" + tt.identificador + "_" + atrColumna.valor)})
                                else:
                                    # forma de: nombreColumna tipo UNIQUE
                                    # formato: U_database_tabla_nombreColumna
                                    nuevoSym.nombre = str("U_" + dbActual + "_" + self.id + "_" + tt.identificador)
                                    nuevaColumna.atributos.update(
                                        {'unique': str("U_" + dbActual + "_" + self.id + "_" + tt.identificador)})
                                nuevoSym.valor = tt.identificador
                            elif atrColumna.tipo == AtributosColumna.CHECK:
                                hayAtr = True
                                nuevoSym.tipo = TipoSimbolo.CONSTRAINT_CHECK
                                nuevoSym.valor = atrColumna.exp
                                if atrColumna.valor != None:  # forma de: constraint id check cond < cond
                                    # formato: C_database_tabla_nombreColumna_idConstraint
                                    nuevoSym.nombre = str(
                                        "C_" + dbActual + "_" + self.id + "_" + tt.identificador + "_" + atrColumna.valor)
                                    nuevaColumna.atributos.update({'check': str(
                                        "C_" + dbActual + "_" + self.id + "_" + tt.identificador + "_" + atrColumna.valor)})
                                else:
                                    # cuando viene: nombreColumna tipo CHECK cond < cond
                                    # formato: C_database_tabla_nombreColumna
                                    nuevoSym.nombre = str("C_" + dbActual + "_" + self.id + "_" + tt.identificador)
                                    nuevaColumna.atributos.update(
                                        {'check': str("C_" + dbActual + "_" + self.id + "_" + tt.identificador)})
                            elif atrColumna.tipo == AtributosColumna.DEFAULT:
                                nuevaColumna.atributos.update({'default': atrColumna.valor})
                            elif atrColumna.tipo == AtributosColumna.NO_NULO:
                                nuevaColumna.atributos.update({'not null': True})
                            elif atrColumna.tipo == AtributosColumna.NULO:
                                nuevaColumna.atributos.update({'null': True})
                            elif atrColumna.tipo == AtributosColumna.PRIMARY:
                                hayPrimaria = True
                                nuevaColumna.atributos.update(
                                    {'primary': str("PK_" + dbActual + "_" + self.id)})  # PK_database_tabla
                            elif atrColumna.tipo == AtributosColumna.REFERENCES:
                                rr = DBMS.extractTable(dbActual, atrColumna.valor)
                                if rr == None:
                                    return str(
                                        "La tabla \'" + atrColumna.valor + "\' a la que está referenciando, no existe")
                                else:
                                    tablaReferencia: Simbolo = ent.buscarSimbolo(atrColumna.valor + "_" + dbActual)
                                    colRef = tablaReferencia.valor
                                    for col in colRef:
                                        nomConstraintPK = col.atributos.get('primary')
                                        if nomConstraintPK != None:
                                            consPK: Simbolo = ent.buscarSimbolo(nomConstraintPK)
                                            arrPk = consPK.valor
                                            if len(arrPk) == 1:
                                                if tablaReferencia.valor[arrPk[0]].tipo.tipo == nuevaColumna.tipo.tipo:
                                                    nombre: str = str(
                                                        "FK_" + dbActual + "_" + self.id + "_" + atrColumna.valor)
                                                    hayForanea = True
                                                    hayAtr = True
                                                    nuevoSym.tipo = TipoSimbolo.CONSTRAINT_FOREIGN
                                                    # FK_database_tabla_tablaReferencia
                                                    nuevoSym.nombre = nombre
                                                    nuevaColumna.atributos.update({'foreign': nombre})
                                                    break

                                    if not hayForanea:
                                        variables.consola.insert(INSERT,
                                                                 "No se puede establecer llave foranea entre tabla '" + self.id + "' y '" + atrColumna.valor + "'\n")
                                        reporteerrores.append(Lerrores("Error Semántico",
                                                                       "No se puede establecer llave foranea entre tabla '" + self.id + "' y '" + atrColumna.valor + "'",
                                                                       "", ""))

                            if hayAtr: listaAtrCol.append(nuevoSym)

                    listaColumnas.append(nuevaColumna)

                if tt.tipo == AtributosColumna.PRIMARY:
                    if hayPrimaria:
                        variables.consola.insert(INSERT, str(
                            "La tabla \'" + self.id + "\' ya contiene llave primaria declarada\n"))
                        reporteerrores.append(Lerrores("Error Semántico",
                                                       "La tabla \'" + self.id + "\' ya contiene llave primaria declarada",
                                                       "", ""))
                    else:
                        primariaAdd: Primaria = tt

                if tt.tipo == AtributosColumna.REFERENCES:
                    if hayForanea:
                        variables.consola.insert(INSERT, str(
                            "La tabla \'" + self.id + "\' ya contiene llave foranea declarada\n"))
                        reporteerrores.append(Lerrores("Error Semántico",
                                                       "La tabla \'" + self.id + "\' ya contiene llave foranea declarada",
                                                       "", ""))
                    else:
                        foraneaAdd: Foranea == tt
                        rr = DBMS.extractTable(dbActual, foraneaAdd.tabla)

                if tt.tipo == AtributosColumna.CONSTRAINT:
                    if tt.contenido.tipo == AtributosColumna.PRIMARY:
                        if hayPrimaria:
                            variables.consola.insert(INSERT, str(
                                "La tabla \'" + self.id + "\' ya contiene llave primaria declarada\n"))
                            reporteerrores.append(Lerrores("Error Semántico",
                                                           "La tabla \'" + self.id + "\' ya contiene llave primaria declarada",
                                                           "", ""))
                        else:
                            primariaAdd: Primaria = tt.contenido
                            primariaAdd.idConstraint = tt.id
                    elif tt.contenido.tipo == AtributosColumna.REFERENCES:
                        if hayForanea:
                            variables.consola.insert(INSERT, str(
                                "La tabla \'" + self.id + "\' ya contiene llave foranea declarada\n"))
                            reporteerrores.append(Lerrores("Error Semántico",
                                                           "La tabla \'" + self.id + "\' ya contiene llave foranea declarada",
                                                           "", ""))
                        else:
                            foraneaAdd: Foranea = tt
                            rr = DBMS.extractTable(dbActual, foraneaAdd.tabla)
                    elif tt.contenido.tipo == AtributosColumna.UNICO:
                        listUnicas = tt.contenido.unicos
                        for x in listUnicas:
                            for col in listaColumnas:
                                if col.nombre == x.valor:
                                    # formato: U_database_tabla_nombreColumna_idConstraint
                                    col.atributos.update({'unique': str(
                                        "U_" + dbActual + "_" + self.id + "_" + col.nombre + "_" + tt.id)})
                                    sym = Simbolo(TipoSimbolo.CONSTRAINT_UNIQUE,
                                                  str("U_" + dbActual + "_" + self.id + "_" + col.nombre + "_" + tt.id))
                                    ent.nuevoSimbolo(sym)
                    elif tt.contenido.tipo == AtributosColumna.CHECK:
                        # formato: C_database_tabla_nombreColumna_idConstraint
                        nombreColCheck = str(tt.contenido.condiciones.exp1.valor)
                        for x in listaColumnas:
                            if x.nombre == nombreColCheck:
                                x.atributos.update(
                                    {'check': str("C_" + dbActual + "_" + self.id + "_" + x.nombre + "_" + tt.id)})
                                sym = Simbolo(TipoSimbolo.CONSTRAINT_CHECK,
                                              str("C_" + dbActual + "_" + self.id + "_" + x.nombre + "_" + tt.id))
                                sym.tabla = self.id
                                sym.baseDatos = dbActual
                                sym.valor = tt.contenido.condiciones
                                listaAtrCol.append(sym)
                                break

            nuevaTabla.valor = listaColumnas
            estado = DBMS.createTable(dbActual, self.id, len(listaColumnas))
            if estado == 0:
                nuevaTabla.baseDatos = dbActual
                r = ent.nuevoSimbolo(nuevaTabla)
                if r == "ok":
                    xx: Simbolo
                    for xx in listaAtrCol:
                        ent.nuevoSimbolo(xx)

                    alreadyPrimary = False
                    for x in range(inicioHerencia, len(listaColumnas), 1):
                        if not alreadyPrimary:
                            pk = listaColumnas[x].atributos.get('primary')
                            if pk != None:
                                self.listPK.append(x)
                                rrr = DBMS.alterAddPK(dbActual, self.id, self.listPK)
                                if rrr != 0:
                                    variables.consola.insert(INSERT,
                                                             "No se ha podido agregar PK en tabla \'" + self.id + "\'\n")
                                    reporteerrores.append(Lerrores("Error Semántico",
                                                                   "No se ha podido agregar PK en tabla \'" + self.id + "'",
                                                                   "", ""))
                                else:
                                    alreadyPrimary = True
                                    sym1 = Simbolo(TipoSimbolo.CONSTRAINT_PRIMARY,
                                                   str("PK_" + dbActual + "_" + self.id))
                                    sym1.valor = self.listPK
                                    sym1.tabla = self.id
                                    sym1.baseDatos = dbActual
                                    ent.nuevoSimbolo(sym1)

                    if not alreadyPrimary:
                        tablaB: Simbolo = ent.buscarSimbolo(nuevaTabla.nombre)
                        if tablaB != None:
                            if primariaAdd != None:
                                listaPrim = primariaAdd.primarias
                                for p in listaPrim:
                                    for col in range(len(tablaB.valor)):
                                        if p.valor == tablaB.valor[col].nombre:
                                            self.listPK.append(col)
                                        # print(p.valor)
                                        # print(col.nombre)

                                if len(self.listPK) > 0:
                                    n = DBMS.alterAddPK(dbActual, self.id, self.listPK)
                                    if n != 0:
                                        variables.consola.insert(INSERT,
                                                                 "No se ha podido agregar PK en tabla \'" + self.id + "\'\n")
                                        reporteerrores.append(Lerrores("Error Semántico",
                                                                       "No se ha podido agregar PK en tabla \'" + self.id + "'",
                                                                       "", ""))
                                    else:
                                        idPk = ""
                                        alreadyPrimary = True
                                        sym: Simbolo = None
                                        if primariaAdd.idConstraint != "":
                                            idPk = str(
                                                "PK_" + dbActual + "_" + self.id + "_" + primariaAdd.idConstraint)
                                            sym = Simbolo(TipoSimbolo.CONSTRAINT_PRIMARY, idPk)
                                        else:
                                            idPk = str("PK_" + dbActual + "_" + self.id)
                                            sym = Simbolo(TipoSimbolo.CONSTRAINT_PRIMARY, idPk)

                                        for y in self.listPK:
                                            tablaB.valor[y].atributos.update({'primary': idPk})

                                        sym.valor = self.listPK
                                        sym.tabla = self.id
                                        sym.baseDatos = dbActual
                                        ent.nuevoSimbolo(sym)

                    DBMS.showCollection()
                    variables.consola.insert(INSERT, str("Tabla " + self.id + " creada exitosamente\n"))
                    return

                return r
            # elif estado == 1:

    def traducir(self, ent: Entorno):
        for i in range(1, len(self.listaDef), 1):
            self.codigo3d += ', ' + self.listaDef[i].stringsql

        self.codigo3d += ')'
        if self.herencia != None:
            self.codigo3d += ' inherits (' + str(self.herencia) + ')'

        self.codigo3d += ";\")\n"
        return self


class CreateType(Instruccion):
    def __init__(self, iden, lexp):
        self.id = iden
        self.contenido = lexp

    def ejecutar(self, ent: Entorno):
        # formato para el enum: ENUM_database_identificador
        nuevoType: Simbolo = Simbolo(TipoSimbolo.TYPE_ENUM, ("ENUM_" + ent.getDataBase() + "_" + self.id),
                                     self.contenido)
        nuevoType.baseDatos = ent.getDataBase()
        r = ent.nuevoSimbolo(nuevoType)
        if r == "ok":
            variables.consola.insert(INSERT, "Nuevo tipo '" + self.id + "' creado\n")
            return

        variables.consola.insert(INSERT, "El tipo '" + self.id + "' ya existe declarado\n")
        reporteerrores.append(Lerrores("Error Semántico", "El tipo '" + self.id + "' ya existe declarado", "", ""))

    def traducir(self, ent: Entorno):
        self.codigo3d = 'ci.ejecutarsql(" create type ' + self.id + ' as enum (' + str(self.contenido[0].traducir(ent).stringsql)
        for i in range(1, len(self.contenido), 1):
            self.codigo3d += ',' + str(self.contenido[i].traducir(ent).stringsql)
        self.codigo3d += ');")\n'

        return self


class Check(CreateTable):
    def __init__(self, condiciones):
        self.condiciones = condiciones
        self.tipo = AtributosColumna.CHECK
        self.stringsql = 'check (' + condiciones.stringsql + ')'


class Unique(CreateTable):
    def __init__(self, unicos):
        self.unicos = unicos
        self.tipo = AtributosColumna.UNICO
        self.stringsql = 'unique (' + str(unicos[0].valor)
        for i in range(1, len(unicos), 1):
            self.stringsql += ',' + str(unicos[i].valor)

        self.stringsql += ')'


class Foranea(CreateTable):
    def __init__(self, foraneas, tabla: str, ref_lista):
        self.foraneas = foraneas
        self.tabla = tabla
        self.ref_lista = ref_lista
        self.tipo = AtributosColumna.REFERENCES
        self.idConstraint = ""
        self.stringsql = 'foreign key (' + str(foraneas[0].valor)
        for i in range(1, len(foraneas), 1):
            self.stringsql += ',' + str(foraneas[i].valor)
        self.stringsql += ') references ' + self.tabla + ' (' + str(ref_lista[0].valor)
        for i in range(1, len(ref_lista), 1):
            self.stringsql += ',' + str(ref_lista[i].valor)
        self.stringsql += ')'


class Primaria(CreateTable):
    def __init__(self, primarias):
        self.primarias = primarias
        self.tipo = AtributosColumna.PRIMARY
        self.idConstraint = ""
        self.stringsql = 'primary key (' + str(primarias[0].valor)
        for i in range(1, len(primarias), 1):
            self.stringsql += ',' + str(primarias[i].valor)
        self.stringsql += ')'


class Atributo(CreateTable):
    def __init__(self, tipo: AtributosColumna, valor=None, exp=None):
        self.tipo = tipo
        self.valor = valor
        self.exp = exp
        if tipo == AtributosColumna.REFERENCES:
            self.stringsql = 'references ' + valor
        elif tipo == AtributosColumna.PRIMARY:
            self.stringsql = 'primary key'
        elif tipo == AtributosColumna.NULO:
            self.stringsql = 'null'
        elif tipo == AtributosColumna.NO_NULO:
            self.stringsql = 'not null'
        elif tipo == AtributosColumna.DEFAULT:
            self.stringsql = 'default ' + str(valor.traducir(None).stringsql)
        elif tipo == AtributosColumna.CHECK:
            self.stringsql = ''
            if valor != None:
                self.stringsql += 'constraint ' + str(valor) + ' '
            self.stringsql += 'check (' + exp.stringsql + ')'
        elif tipo == AtributosColumna.UNICO:
            self.stringsql = ''
            if valor != None:
                self.stringsql += 'constraint ' + str(valor) + ' '
            self.stringsql += 'unique'


class Constraint(CreateTable):
    def __init__(self, identificador: str, objeto):
        self.id = identificador
        self.contenido = objeto
        self.tipo = AtributosColumna.CONSTRAINT
        self.stringsql = 'constraint ' + identificador + ' ' + objeto.stringsql


class Columna(CreateTable):
    def __init__(self, identificador: str, tipoDato, lista=[]):
        self.identificador = identificador
        self.lista = lista  # este recibe una lista
        self.tipoDato = tipoDato
        self.tipo = AtributosColumna.COLUMNA_SIMPLE
        self.stringsql = identificador + ' ' + tipoDato.devString()
        for opc in lista:
            self.stringsql += ' ' + opc.stringsql


class CondicionCheck(CreateTable):
    def __init__(self, exp1, simbolo, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        self.simbolo = simbolo
        self.stringsql = str(exp1.traducir(None).stringsql) + " " + simbolo + " " + str(exp2.traducir(None).stringsql)


class ShowTables(Instruccion):
    def __init__(self, id):
        self.id = id

    def ejecutar(self, ent):
        variables.consola.insert(INSERT, "Ejecutando Show Tables para la base de datos: " + self.id + " \n")
        resultado = DBMS.showTables(self.id)
        if (resultado == None):
            variables.consola.insert(INSERT,
                                     "ERROR >> En la instrucción Show Tables(" + self.id + "), base de datos: " + self.id + " NO existe\n")
            reporteerrores.append(Lerrores("Error Semántico",
                                           "En la instrucción Show Tables(" + self.id + "), base de datos: " + self.id + " NO existe",
                                           "", ""))
        else:
            variables.x.title = "DB: " + self.id
            variables.x.add_column("Tables", resultado)
            variables.consola.insert(INSERT, variables.x)
            variables.x.clear()
            variables.consola.insert(INSERT, "\n")
            return "Show Tables Exitoso"

    def traducir(self, ent):
        self.codigo3d = 'ci.ejecutarsql(\'show tables (' + str(self.id) + ');\')'
        return self