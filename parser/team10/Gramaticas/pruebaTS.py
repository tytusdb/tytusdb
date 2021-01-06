from ReporteErrores import *
from funcionesTS import *
from parse import *
from RevisionTipos import *
from VerificarDatos import *


class MainWindow():
    # print("Agregando a tabla de simbolos")

    agregaraTS('0', 'base1', 'base', 'global', '', '')
    agregaraTS('1', 'tabla1', 'tabla', 'base1', '', '')
    agregaraTS('2', 'var2', 'varchar(10)', 'tabla1', 'base1', '')
    agregaraTS('3', 'var3', 'char(2)', 'tabla1', 'base1', '')
    agregaraTS('4', 'var4', 'text',  'tabla1', 'base1', '')
    agregaraTS('5', 'var5', 'boolean',  'tabla1', 'base1', '')
    agregaraTS('6', 'sum', 'funcion', 'tabla6', 'base1', '')
    agregaraTS('7', 'base2', 'base', 'global', '', '')
    agregaraTS('8', 'tabla1', 'tabla', 'base2', '', '')
    agregaraTS('9', 'campo', 'varchar(10)', 'tabla1', 'base2', '')
    agregaraTS('10', 'nueva', 'varchar(10)', 'tabla1', 'base1', '')


    # print("antes de escribir archivo")

    #modificarNombreTabla_TS("base1", "tabla1", "nuevaTabla")

    # eliminarTS_Base("base1")

    generarts()

    # print("antes de crear archivo")

    if len(tsgen) > 0:
        print("Encontrando los valores")
        verts()
    # Leer archivo
    # ejecutar()

    # ver_lexicos()
    # ver_sintacticos()

    # tipoColumna("var4", "tabla1", "holaaa", "base")

    # verificarTablaDuplicada("tabla1", "base1")
    # verificarBasesDuplicada("base1")

    # existeCampo("tabla", "var2")

    # ver_semanticos()

    # campos = (devolverCampos("base1", "tabla1"))

    # for i in campos:
    #     print(i)
