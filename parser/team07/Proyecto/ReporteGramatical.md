#REPORTE GRAMATICAL

----------

init   ::=   instrucciones

    	 t[0] = t[1]

instrucciones  ::=   instrucciones instruccion

    	 nodo = t[1]
    	 nodo.hijos.append(t[2])
    	 t[0] = nodo

instruccion  ::=   crear_instr

    	 t[0] = t[1]

crear_instr ::= CREATE TABLE ID PARIZQUIERDO columnas PARDERECHO herencia PTCOMA

    	 linea = str(t.lexer.lineno)
    	 hijos = []
    	 nNodo = incNodo(numNodo)
    	 nodoId = crear_nodo_general("ID", t[3], linea, columna)
    	 nodoColumnas = t[5]
    	 nodoHerencia = t[7]
    	 instru = createTable.createTable(t[3], t[7], t[5].hijos)
    	 hijos.append(nodoId)
    	 hijos.append(nodoColumnas)
    	 hijos.append(nodoHerencia)
    	 instru.setearValores(linea, columna, "CREATE_TABLE", nNodo, , hijos)
    	 t[0] = instru

herencia : empty

    	 t[0] = None

columnas ::= columnas COMA columna

    	 linea = str(t.lexer.lineno)
    	 nodoColumnas = t[1]
    	 nodoColumna = t[3]
    	 nodoColumnas.hijos.append(nodoColumna)
    	 t[0] = nodoColumnas

columna ::= ID tipos opcional

    	 linea = str(t.lexer.lineno)
    	 nodoColumna = crear_nodo_general("columna",,linea,columna)
    	 nodoId = crear_nodo_general("ID",t[1],linea,columna)
    	 nodoTipo = t[2]
    	 nodoOpcional = t[3]
    	 nodoColumna.hijos = []
    	 nodoColumna.hijos.append(nodoId)
    	 nodoColumna.hijos.append(nodoTipo)
    	 nodoColumna.hijos.append(nodoOpcional)
    	 t[0] = nodoColumna

opcional ::= opcionNull

    	 linea = str(t.lexer.lineno)
    	 nodoOpcional = crear_nodo_general("opcional",,linea,columna)
    	 nodoOpNull = t[1]
    	 nodoOpcional.hijos = []
    	 nodoOpcional.hijos.append(nodoOpNull)
    	 t[0] = nodoOpcional

opcionNull ::= NOT NULL opConstraint

    	 linea = str(t.lexer.lineno)
    	 nodoOpNull = crear_nodo_general("opcionNull",,linea,columna)
    	 nodoNull = crear_nodo_general("NOTNULL","NOT NULL",linea,columna)
    	 nodoNull.hijos = []
    	 nodoOpConstraint = t[3]
    	 nodoOpNull.hijos = []
    	 nodoOpNull.hijos.append(nodoNull)
    	 nodoOpNull.hijos.append(nodoOpConstraint)
    	 t[0] = nodoOpNull

opConstraint ::= opUniqueCheck

    	 linea = str(t.lexer.lineno)
    	 nodoOpUnique = t[1]
    	 nodoOpConstraint = crear_nodo_general("opConstraint",,linea,columna)
    	 nodoOpConstraint.hijos = []
    	 nodoOpConstraint.hijos.append(nodoOpUnique)
    	 t[0] = nodoOpConstraint

opUniqueCheck ::= empty

    	 t[0] = None

columnas ::= columnas COMA columna

    	 linea = str(t.lexer.lineno)
    	 nodoColumnas = t[1]
    	 nodoColumna = t[3]
    	 nodoColumnas.hijos.append(nodoColumna)
    	 t[0] = nodoColumnas

columna ::= ID tipos opcional

    	 linea = str(t.lexer.lineno)
    	 nodoColumna = crear_nodo_general("columna",,linea,columna)
    	 nodoId = crear_nodo_general("ID",t[1],linea,columna)
    	 nodoTipo = t[2]
    	 nodoOpcional = t[3]
    	 nodoColumna.hijos = []
    	 nodoColumna.hijos.append(nodoId)
    	 nodoColumna.hijos.append(nodoTipo)
    	 nodoColumna.hijos.append(nodoOpcional)
    	 t[0] = nodoColumna

opcional ::= opcionNull

    	 linea = str(t.lexer.lineno)
    	 nodoOpcional = crear_nodo_general("opcional",,linea,columna)
    	 nodoOpNull = t[1]
    	 nodoOpcional.hijos = []
    	 nodoOpcional.hijos.append(nodoOpNull)
    	 t[0] = nodoOpcional

opcionNull ::= NOT NULL opConstraint

    	 linea = str(t.lexer.lineno)
    	 nodoOpNull = crear_nodo_general("opcionNull",,linea,columna)
    	 nodoNull = crear_nodo_general("NOTNULL","NOT NULL",linea,columna)
    	 nodoNull.hijos = []
    	 nodoOpConstraint = t[3]
    	 nodoOpNull.hijos = []
    	 nodoOpNull.hijos.append(nodoNull)
    	 nodoOpNull.hijos.append(nodoOpConstraint)
    	 t[0] = nodoOpNull

opConstraint ::= opUniqueCheck

    	 linea = str(t.lexer.lineno)
    	 nodoOpUnique = t[1]
    	 nodoOpConstraint = crear_nodo_general("opConstraint",,linea,columna)
    	 nodoOpConstraint.hijos = []
    	 nodoOpConstraint.hijos.append(nodoOpUnique)
    	 t[0] = nodoOpConstraint

opUniqueCheck ::= empty

    	 t[0] = None

columnas ::= columna

    	 linea = str(t.lexer.lineno)
    	 nodoColumna = t[1]
    	 nodoColumnas = crear_nodo_general("columnas",,linea,columna)
    	 nodoColumnas.hijos = []
    	 nodoColumnas.hijos.append(nodoColumna)
    	 t[0] = nodoColumnas

columna ::= ID tipos opcional

    	 linea = str(t.lexer.lineno)
    	 nodoColumna = crear_nodo_general("columna",,linea,columna)
    	 nodoId = crear_nodo_general("ID",t[1],linea,columna)
    	 nodoTipo = t[2]
    	 nodoOpcional = t[3]
    	 nodoColumna.hijos = []
    	 nodoColumna.hijos.append(nodoId)
    	 nodoColumna.hijos.append(nodoTipo)
    	 nodoColumna.hijos.append(nodoOpcional)
    	 t[0] = nodoColumna

opcional ::= opcionNull

    	 linea = str(t.lexer.lineno)
    	 nodoOpcional = crear_nodo_general("opcional",,linea,columna)
    	 nodoOpNull = t[1]
    	 nodoOpcional.hijos = []
    	 nodoOpcional.hijos.append(nodoOpNull)
    	 t[0] = nodoOpcional

opcionNull ::= opConstraint 

    	 linea = str(t.lexer.lineno)
    	 nodoOpNull = crear_nodo_general("opcionNull",,linea,columna)
    	 nodoOpConstraint = t[1]
    	 nodoOpNull.hijos = []
    	 nodoOpNull.hijos.append(nodoOpConstraint)
    	 t[0] = nodoOpNull

opConstraint ::= opUniqueCheck

    	 linea = str(t.lexer.lineno)
    	 nodoOpUnique = t[1]
    	 nodoOpConstraint = crear_nodo_general("opConstraint",,linea,columna)
    	 nodoOpConstraint.hijos = []
    	 nodoOpConstraint.hijos.append(nodoOpUnique)
    	 t[0] = nodoOpConstraint

opUniqueCheck ::= PRIMARY KEY

    	 nodoPrimary = crear_nodo_general("PRIMARY","PRIMARY KEY",str(t.lexer.lineno),columna)
    	 nodoPrimary.hijos = []
    	 nodoOpPrimary = crear_nodo_general("opUniqueCheck",,str(t.lexer.lineno),columna)
    	 nodoOpPrimary.hijos = []
    	 nodoOpPrimary.hijos.append(nodoPrimary)
    	 t[0] = nodoOpPrimary

instrucciones  ::=   instrucciones instruccion

    	 nodo = t[1]
    	 nodo.hijos.append(t[2])
    	 t[0] = nodo

instruccion  ::=   crear_instr

    	 t[0] = t[1]

crear_instr ::= CREATE opReplace DATABASE opExists ID opDatabase PTCOMA

    	 linea = str(t.lexer.lineno)
    	 hijos = []
    	 nNodo = incNodo(numNodo)
    	 nodoId = crear_nodo_general("ID", t[5], linea, columna)
    	 nodoOpciones = t[6]
    	 instru = createDatabase.createDatabase(t[5], t[6].hijos)
    	 hijos.append(nodoId)
    	 hijos.append(nodoOpciones)
    	 instru.setearValores(linea, columna, "CREATE_DATABASE", nNodo, , hijos)
    	 t[0] = instru

opDatabase ::= mode

        	 linea = str(t.lexer.lineno)
        	 nodoOpDatabase = crear_nodo_general("opDatabase",,linea,columna)
        	 nodoOpDatabase.hijos = []
        	 nodoModo = t[1]
        	 nodoOpDatabase.hijos.append(nodoModo)
        	 t[0] = nodoOpDatabase

mode ::= empty

    	 t[0] = None

opExists ::= empty

    	 t[0] = None

opReplace ::= empty

    	 t[0] = None

instrucciones  ::=   instrucciones instruccion

    	 nodo = t[1]
    	 nodo.hijos.append(t[2])
    	 t[0] = nodo

instruccion  ::=   use_dabatabase

        	 t[0] = t[1]

use_dabatabase : USE ID PTCOMA

    	 linea = str(t.lexer.lineno)
    	 nodoId = crear_nodo_general("ID", t[2], str(linea), columna)
    	 nNodo = incNodo(numNodo)
    	 nodoUse = useDataBase.UseDataBase(t[2])
    	 hijos = []
    	 hijos.append(nodoId)
    	 nodoUse.setearValores(linea,columna,"Use_DataBase",nNodo,,hijos)
    	 t[0] = nodoUse

instrucciones  ::=   instruccion

    	 nodo = crear_nodo_general("init", , str(t.lexer.lineno), columna)
    	 nodo.hijos.append(t[1])
    	 t[0] = nodo

instruccion  ::=   crear_instr

    	 t[0] = t[1]

crear_instr ::= CREATE opReplace DATABASE opExists ID opDatabase PTCOMA

    	 linea = str(t.lexer.lineno)
    	 hijos = []
    	 nNodo = incNodo(numNodo)
    	 nodoId = crear_nodo_general("ID", t[5], linea, columna)
    	 nodoOpciones = t[6]
    	 instru = createDatabase.createDatabase(t[5], t[6].hijos)
    	 hijos.append(nodoId)
    	 hijos.append(nodoOpciones)
    	 instru.setearValores(linea, columna, "CREATE_DATABASE", nNodo, , hijos)
    	 t[0] = instru

opDatabase ::= mode

        	 linea = str(t.lexer.lineno)
        	 nodoOpDatabase = crear_nodo_general("opDatabase",,linea,columna)
        	 nodoOpDatabase.hijos = []
        	 nodoModo = t[1]
        	 nodoOpDatabase.hijos.append(nodoModo)
        	 t[0] = nodoOpDatabase

mode ::= empty

    	 t[0] = None

opExists ::= empty

    	 t[0] = None

opReplace ::= empty

    	 t[0] = None

