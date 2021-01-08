from goto import with_goto
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Sql_insert import insertTable
from Instrucciones.Sql_drop import DropTable,DropDatabase
from Instrucciones.Sql_alter import AlterDatabase,AlterDBOwner,AlterTableAddColumn,AlterTableAddConstraintFK,AlterTableAddFK
from Instrucciones.TablaSimbolos.Arbol import Arbol
from storageManager.jsonMode import *
import sintactico

tablaGlobal = Tabla(None)
arbol = Arbol()

def call_funcion_intermedia():
    dropAll()
    input = ""
    for i in stack:
        input += stack[i] + "\n"
    print(input)
    inst = sintactico.ejecutar_analisis(input)
    arbol = Arbol(inst)
    for i in arbol.instrucciones:
        resultado = i.ejecutar(tablaGlobal,arbol)

def call_insert_table():
    arbolAux = arbol
    arbolAux.bdUsar = heap[p-3]
    tabla = insertTable.insertTable(heap[p-2], None, heap[p-1], heap[p], '', 0, 0)
    tabla.ejecutar(tablaGlobal, arbolAux)

def call_drop_table():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 1])
    drop = DropTable.DropTable(heap[p],None, '', 0, 0)
    drop.ejecutar(tablaGlobal, arbolAux)

def call_drop_database():
    arbolAux = arbol
    drop = DropDatabase.DropDatabase(heap[p - 2],None,heap[p - 1],heap[p],'',0,0)
    drop.ejecutar(tablaGlobal, arbolAux)

def call_alter_database():
    arbolAux = arbol
    alter = AlterDatabase.AlterDatabase(heap[p - 2], None, heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterowner_database():
    arbolAux = arbol
    alter = AlterDBOwner.AlterDBOwner(heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterTable_addCheck():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 2])
    alter = AlterTableAddCheck.AlterTableAddCheck(heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterTable_addColumn():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 2])
    alter = AlterTableAddColumn.AlterTableAddColumn(heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterTable_addConstraint():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 3])
    alter = AlterTableAddConstraint.AlterTableAddConstraint(heap[p - 2], heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterTable_addConstraintFK():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 5])
    alter = AlterTableAddConstraintFK.AlterTableAddConstraintFK(heap[p - 4], heap[p - 3], heap[p - 2], heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterTable_addFK():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 4])
    alter = AlterTableAddFK.AlterTableAddFK(heap[p - 3], heap[p - 2], heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterTable_alterColumn():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 2])
    alter = AlterTableAlterColumn.AlterTableAlterColumn(heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterTable_columnType():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 2])
    alter = AlterTableAlterColumnType.AlterTableAlterColumnType(heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterTable_dropColumn():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 2])
    alter = AlterTableDropColumn.AlterTableDropColumn(heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

def call_alterTable_dropConstraint():
    arbolAux = arbol
    arbolAux.setBaseDatos(heap[p - 2])
    alter = AlterTableDropColumn.AlterTableDropColumn(heap[p - 1], heap[p], '' ,0,0)
    alter.ejecutar(tablaGlobal, arbolAux)

stack = {}
heap = {}
p = 0
h = 0

@with_goto
def exec():
    global p

exec()
call_funcion_intermedia()