from RevisionTipos import *
from ReporteTS import *


# Al crear una tabla, verificar si no se repiten los campos
def verificarColumnaDuplicada(nombreCol, nombreTabla, nombreBase):
    verificar = 0

    for i in tsgen:
        if str(tsgen[i]['declarada_en']) == str(nombreTabla) and str(tsgen[i]['nombre']) == str(nombreCol) and str(
                tsgen[i]['ambito']) == str(nombreBase):
            verificar = 1

    if verificar == 1:
        errorsem.append("Duplicate Column. Msg: 42701. La columna \"" + nombreCol + "\" ya existe")
        print("Error, la columna " + nombreCol + " ya existe")
        return 0
    else:
        print("Todo bien con la columna, se puede crear")
        return 1


# Al crear una tabla verificar si no existe ese nombre
def verificarTablaDuplicada(nombrTabla, nombreBase):
    verificar = 0

    for i in tsgen:
        if str(tsgen[i]['declarada_en']) == str(nombreBase):
            print("base encontrada")
            if str(tsgen[i]['tipo']) == str('tabla') and str(tsgen[i]['nombre']) == str(nombrTabla):
                verificar = 1

    if verificar == 1:
        errorsem.append("Duplicate Table. Msg: 42P07. La tabla \"" + nombrTabla + "\" ya existe")
        print("Error, la tabla " + nombrTabla + " ya existe")
        return 0
    else:
        print("Todo bien con la tabla, se puede crear")
        return 1


# Al crear una base verificar si no existe ese nombre
def verificarBasesDuplicada(nombreBase):
    verificar = 0

    for i in tsgen:
        if str(tsgen[i]['tipo']) == str('base') and str(tsgen[i]['nombre']) == str(nombreBase):
            print("Base encontrada")
            verificar = 1

    if verificar == 1:
        errorsem.append("Duplicate Database. Msg: 42P04. La base " + nombreBase + " ya existe")
        print("Error, la base " + nombreBase + " ya existe")
        return 0
    else:
        print("Todo bien con la base, se puede crear")
        return 1

# Al usar una tabla, verificar que exista
def existeTabla(nombrTabla, nombreBase):
    verificar = 0

    for i in tsgen:
        if str(tsgen[i]['declarada_en']) == str(nombreBase):
            print("base encontrada")
            if str(tsgen[i]['tipo']) == str('tabla') and str(tsgen[i]['nombre']) == str(nombrTabla):
                verificar = 1

    if verificar == 0:
        errorsem.append("Undefined Table. Msg: 42P01. La tabla \"" + nombrTabla + "\" no existe")
        print("Error, la tabla " + nombrTabla + " no existe")
        return 0
    else:
        print("Todo bien con la tabla, se puede usar")
        return 1


# Al usar un columna, verificar que existe
def existeCampo(nombreCol, nombreTabla, base):
    verificar = 0

    for i in tsgen:
        print("comparando " + tsgen[i]['declarada_en'] + " - " + str(nombreTabla))
        if str(tsgen[i]['declarada_en']) == str(nombreTabla) and str(tsgen[i]['nombre']) == str(nombreCol) and str(tsgen[i]['ambito']) == str(base):
            verificar = 1

    if verificar == 0:
        errorsem.append("Undefined Column. Msg 42703. La columna \"" + nombreCol + "\" no existe")
        print("Error, la columna " + nombreCol + " no existe")
        return 0
    else:
        print("Todo bien con la columna, se puede usar")
        return 1


# Al usar una base verificar que existe
def existeBase(nombreBase):
    verificar = 0

    for i in tsgen:
        if str(tsgen[i]['tipo']) == str('base') and str(tsgen[i]['nombre']) == str(nombreBase):
            print("Base encontrada")
            verificar = 1

    if verificar == 0:
        errorsem.append("Undefined database. La base " + nombreBase + " no existe")
        print("Error, la base " + nombreBase + " no existe")
        return 0
    else:
        print("Todo bien con la base, se puede crear")
        return 1


def error_division_cero():
    errorsem.append("Division By Zero. Msg: 22012")


def error_potencia():
    errorsem.append("Invalid Argument For Power Function. Msg: 2201F")


def error_substring():
    errorsem.append("Substring Error. Msg: 22011")


def error_group():
    errorsem.append("Grouping Error. Msg: 42803")


def error_llave_foranea():
    errorsem.append("Invalid Foreign Key. Msg: 42830")


def error_nombre_invalido():
    errorsem.append("Invalid Name. Msg 42602")


def error_columna_indefinida():
    errorsem.append("Undefined Column. Msg 42703")


def error_tabla_indefinida():
    errorsem.append("Undefined Table. Msg: 42P01")


def error_base_duplicada():
    errorsem.append("Duplicate Database. Msg: 42P04")


def error_alias_duplicado():
    errorsem.append("Duplicate Alias. Msg: 42712")


def error_columna_duplicada():
    errorsem.append("Duplicate Column. Msg: 42701")


def error_tabla_duplicada():
    errorsem.append("Duplicate Table. Msg: 42P07")
