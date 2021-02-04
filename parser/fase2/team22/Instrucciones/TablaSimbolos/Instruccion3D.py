from Optimizador.C3D import *

t = -1
e = -1

def getEncabezado():
    content = "from goto import with_goto\n"
    content += "from Instrucciones.TablaSimbolos.Tabla import Tabla\n"
    content += "from Instrucciones.Sql_insert import insertTable\n"
    content += "from Instrucciones.Sql_drop import DropTable,DropDatabase\n"
    content += "from Instrucciones.Sql_alter import AlterDatabase,AlterDBOwner,AlterTableAddColumn,AlterTableAddConstraintFK,AlterTableAddFK\n"
    content += "from Instrucciones.TablaSimbolos.Arbol import Arbol\n"
    content += "from storageManager.jsonMode import *\n"
    content += "import sintactico\n\n"

    content += "dropAll()\n\n"
    
    content += "tablaGlobal = Tabla(None)\n"
    content += "arbol = Arbol()\n\n"

    content += "stack = {}\nheap = {}\n"
    content += "p = 0\nh = 0\n\n"

    content += "def call_funcion_intermedia():\n"
    content += "    global p, h, arbol\n"
    content += "    print(stack[p])\n"
    content += "    inst = sintactico.ejecutar_analisis(stack[p])\n"
    content += "    arbol.instrucciones = inst\n"
    content += "    for i in arbol.instrucciones:\n"
    content += "        resultado = i.ejecutar(tablaGlobal,arbol)\n"
    content += "    p = h\n\n"

    content += "@with_goto\n"
    content += "def exec():\n"
    content += "    global p, h"

    return content

'''
    #Funcion para insertar elementos en tabla c3d
    content += "def call_insert_table():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.bdUsar = heap[p-3]\n"
    content += "    tabla = insertTable.insertTable(heap[p-2], None, heap[p-1], heap[p], '', 0, 0)\n"
    content += "    tabla.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion drop table para c3d
    content += "def call_drop_table():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 1])\n"
    content += "    drop = DropTable.DropTable(heap[p],None, '', 0, 0)\n"
    content += "    drop.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion drop database para c3d
    content += "def call_drop_database():\n"
    content += "    arbolAux = arbol\n"
    content += "    drop = DropDatabase.DropDatabase(heap[p - 2],None,heap[p - 1],heap[p],'',0,0)\n"
    content += "    drop.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter database para c3d
    content += "def call_alter_database():\n"
    content += "    arbolAux = arbol\n"
    content += "    alter = AlterDatabase.AlterDatabase(heap[p - 2], None, heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter owner database para c3d
    content += "def call_alterowner_database():\n"
    content += "    arbolAux = arbol\n"
    content += "    alter = AlterDBOwner.AlterDBOwner(heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter table add check para c3d
    content += "def call_alterTable_addCheck():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 2])\n"
    content += "    alter = AlterTableAddCheck.AlterTableAddCheck(heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter table add column para c3d
    content += "def call_alterTable_addColumn():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 2])\n"
    content += "    alter = AlterTableAddColumn.AlterTableAddColumn(heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter table add constraint para c3d
    content += "def call_alterTable_addConstraint():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 3])\n"
    content += "    alter = AlterTableAddConstraint.AlterTableAddConstraint(heap[p - 2], heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter table add constrainst fk para c3d
    content += "def call_alterTable_addConstraintFK():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 5])\n"
    content += "    alter = AlterTableAddConstraintFK.AlterTableAddConstraintFK(heap[p - 4], heap[p - 3], heap[p - 2], heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter table add fk para c3d
    content += "def call_alterTable_addFK():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 4])\n"
    content += "    alter = AlterTableAddFK.AlterTableAddFK(heap[p - 3], heap[p - 2], heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter table alter column para c3d
    content += "def call_alterTable_alterColumn():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 2])\n"
    content += "    alter = AlterTableAlterColumn.AlterTableAlterColumn(heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter table alter column type para c3d
    content += "def call_alterTable_columnType():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 2])\n"
    content += "    alter = AlterTableAlterColumnType.AlterTableAlterColumnType(heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter table drop column para c3d
    content += "def call_alterTable_dropColumn():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 2])\n"
    content += "    alter = AlterTableDropColumn.AlterTableDropColumn(heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"

    #Funcion alter table drop constraint para c3d
    content += "def call_alterTable_dropConstraint():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.setBaseDatos(heap[p - 2])\n"
    content += "    alter = AlterTableDropColumn.AlterTableDropColumn(heap[p - 1], heap[p], '' ,0,0)\n"
    content += "    alter.ejecutar(tablaGlobal, arbolAux)\n\n"
'''
    

def getPie():
    content = "\n\nexec()\n"
    content += "print('****************************** Consola ******************************')\n"
    content += "for line in arbol.consola:\n"
    content += "    print(line)"
    #content += "call_funcion_intermedia()"
    return content

def getTemporal():
    global t
    t += 1
    return 't' + str(t)

def getLastTemporal():
    global t
    return 't' + str(t)

def getEtiqueta():
    global e
    e += 1
    return 'L' + str(e)

def asignacionString(temporal, valor):
        return Asignacion(Identificador(temporal), Valor('"' + valor + '"', "STRING"))

def asignacionH():
        return Asignacion(Identificador("h"), Identificador("p"))

def aumentarP():
        return Asignacion(Identificador("p"), Operacion(Identificador("p"), Valor(1, "INTEGER"), OP_ARITMETICO.SUMA))

def operacion(temporal, op1, op2, operador):
        return Asignacion(Identificador(temporal), Operacion(op1, op2, operador))

def asignacionStack(valor, tipo):
    if tipo == "STRING" and valor != None:
        valor = "\"" + str(valor) + "\""
    return Asignacion(Arreglo(Identificador("stack"), Identificador("p")), Valor(valor, tipo))

def asignacionTemporalStack(id):
    return Asignacion(Arreglo(Identificador("stack"), Identificador("p")), Identificador(id))