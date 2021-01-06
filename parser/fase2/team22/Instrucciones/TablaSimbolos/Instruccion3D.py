from Optimizador.C3D import *

t = -1
e = -1

def getEncabezado():
    content = "from goto import with_goto\n"
    content += "from Instrucciones.TablaSimbolos.Tabla import Tabla\n"
    content += "from Instrucciones.Sql_insert import insertTable\n"
    content += "from Instrucciones.TablaSimbolos.Arbol import Arbol\n"
    content += "from storageManager.jsonMode import *\n"
    content += "import sintactico\n\n"
    
    content += "tablaGlobal = Tabla(None)\n"
    content += "arbol = Arbol()\n\n"

    content += "def call_funcion_intermedia():\n"
    content += "    dropAll()\n"
    content += "    input = \"\"\n"
    content += "    for i in stack:\n"
    content += "        input += stack[i] + \"\\n\"\n"
    content += "    print(input)\n"
    content += "    inst = sintactico.ejecutar_analisis(input)\n"
    content += "    arbol = Arbol(inst)\n"
    content += "    for i in arbol.instrucciones:\n"
    content += "        resultado = i.ejecutar(tablaGlobal,arbol)\n\n"

    #Funcion para insertar elementos en tabla c3d
    content += "def call_insert_table():\n"
    content += "    arbolAux = arbol\n"
    content += "    arbolAux.bdUsar = heap[p-3]\n"
    content += "    tabla = insertTable.insertTable(heap[p-2], None, heap[p-1], heap[p], '', 0, 0)\n"
    content += "    tabla.ejecutar(tablaGlobal, arbolAux)\n\n"


    content += "stack = {}\nheap = {}\n"
    content += "p = 0\nh = 0\n\n"

    content += "@with_goto\n"
    content += "def exec():\n"
    content += "    global p"

    return content

def getPie():
    content = "\n\nexec()\n"
    content += "call_funcion_intermedia()"
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