#REPORTE GRAMATICAL

----------

init   ::=   instrucciones

    	 t[0] = t[1]

instrucciones  ::=   instrucciones instruccion

    	 nodo = t[1]
    	 nodo.hijos.append(t[2])
    	 t[0] = nodo

instruccion  ::=   update_table

        	 t[0] = t[1]

update_table     ::=   UPDATE ID SET lista_seteos WHERE exp_operacion PTCOMA

        	 nodoUpdate = updateTable.UpdateTable(t[2], t[4].hijos, t[6])
        	 hijos.append(nodoId)
        	 hijos.append(t[4])
        	 hijos.append(t[6])
        	 nodoUpdate.setearValores(linea, columna, "UPDATE_TABLE", nNodo, , hijos)
        	 t[0] = nodoUpdate

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

exp_relacional   ::=   exp_relacional IGUAL exp_relacional

            	 nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.IGUALACION)
            	 nodoMas = crear_nodo_general("IGUALACION", "=", linea, columna)
            	 nodoExp.hijos.append(t[1])
            	 nodoExp.hijos.append(nodoMas)
            	 nodoExp.hijos.append(t[3])
            	 t[0] = nodoExp  

primitivo  ::=   ENTERO

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

primitivo  ::=   ID

    	 linea = str(t.lexer.lineno)
    	 nodoId = crear_nodo_general("NombreColumna", t[1], linea, columna)
    	 hijos = []
    	 nNodo = incNodo(numNodo)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.NOMBRE_COLUMNA)
    	 hijos.append(nodoId)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], hijos)
    	 t[0] = nodoPri

lista_seteos     ::=   set_columna

        	 nodoLista = crear_nodo_general("LISTA_SETEOS", "", linea, columna)
        	 nodoLista.hijos.append(t[1])
        	 t[0] = nodoLista

set_columna    ::=   ID IGUAL exp_operacion

    	 linea = str(t.lexer.lineno)
    	 nodoId = crear_nodo_general("ID", t[1], linea, columna)
    	 nNodo = incNodo(numNodo)
    	 hijos = []
    	 nodoSet = updateColumna.UpdateColumna(t[1], t[3])
    	 hijos.append(nodoId)
    	 hijos.append(t[3])
    	 nodoSet.setearValores(linea, columna, "set_columna", nNodo, , hijos)
    	 t[0] = nodoSet

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

instrucciones  ::=   instrucciones instruccion

    	 nodo = t[1]
    	 nodo.hijos.append(t[2])
    	 t[0] = nodo

instruccion  ::=   use_dabatabase

        	 t[0] = t[1]

delete_table   ::=   DELETE FROM ID WHERE exp_operacion PTCOMA

        	 nodoDelete = deleteTable.DeleteTable(t[3], t[5])
        	 hijos.append(nodoId)
        	 hijos.append(t[5])
        	 nodoDelete.setearValores(linea, columna, "DELETE_FROM", nNodo, , hijos)
        	 t[0] = nodoDelete

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

exp_relacional   ::=   exp_relacional IGUAL exp_relacional

            	 nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.IGUALACION)
            	 nodoMas = crear_nodo_general("IGUALACION", "=", linea, columna)
            	 nodoExp.hijos.append(t[1])
            	 nodoExp.hijos.append(nodoMas)
            	 nodoExp.hijos.append(t[3])
            	 t[0] = nodoExp  

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

primitivo  ::=   ID

    	 linea = str(t.lexer.lineno)
    	 nodoId = crear_nodo_general("NombreColumna", t[1], linea, columna)
    	 hijos = []
    	 nNodo = incNodo(numNodo)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.NOMBRE_COLUMNA)
    	 hijos.append(nodoId)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], hijos)
    	 t[0] = nodoPri

instrucciones  ::=   instrucciones instruccion

    	 nodo = t[1]
    	 nodo.hijos.append(t[2])
    	 t[0] = nodo

instruccion  ::=   insert_table

        	 t[0] = t[1]

insert_table   ::=   INSERT INTO ID VALUES lista_valores PTCOMA

        	 instru = insertTable.InsertTable(t[3], [], t[5].hijos)
        	 hijos.append(nodoId)
        	 hijos.append(t[5])
        	 instru.setearValores(str(linea), columna,"Insert_table", nNodo, , hijos)
        	 t[0] = instru

lista_valores  ::=   lista_valores COMA tupla

        	 nodoLista = t[1]
        	 nodoLista.hijos.append(t[3])
        	 t[0] = nodoLista

tupla  ::=   PARIZQUIERDO lista_expresiones PARDERECHO

    	 nodoTupla = crear_nodo_general("Tupla", , str(t.lexer.lineno), columna)
    	 nodoTupla.hijos.append(t[2])
    	 t[0] = nodoTupla

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   exp_operacion

    	 nodoLista = crear_nodo_general("lista_expresiones",,str(t.lexer.lineno),columna)
    	 nodoLista.hijos.append(t[1])
    	 t[0] = t[1]

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   ENTERO

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_valores  ::=   lista_valores COMA tupla

        	 nodoLista = t[1]
        	 nodoLista.hijos.append(t[3])
        	 t[0] = nodoLista

tupla  ::=   PARIZQUIERDO lista_expresiones PARDERECHO

    	 nodoTupla = crear_nodo_general("Tupla", , str(t.lexer.lineno), columna)
    	 nodoTupla.hijos.append(t[2])
    	 t[0] = nodoTupla

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   exp_operacion

    	 nodoLista = crear_nodo_general("lista_expresiones",,str(t.lexer.lineno),columna)
    	 nodoLista.hijos.append(t[1])
    	 t[0] = t[1]

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   ENTERO

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_valores  ::=   tupla

        	 nodoLista = crear_nodo_general("Lista_valores", , str(t.lexer.lineno), columna)
        	 nodoLista.hijos.append(t[1])
        	 t[0] = nodoLista

tupla  ::=   PARIZQUIERDO lista_expresiones PARDERECHO

    	 nodoTupla = crear_nodo_general("Tupla", , str(t.lexer.lineno), columna)
    	 nodoTupla.hijos.append(t[2])
    	 t[0] = nodoTupla

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   exp_operacion

    	 nodoLista = crear_nodo_general("lista_expresiones",,str(t.lexer.lineno),columna)
    	 nodoLista.hijos.append(t[1])
    	 t[0] = t[1]

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   ENTERO

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

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

    	 nodoColumnas = t[1]
    	 nodoColumna = t[3]
    	 nodoColumnas.hijos.append(nodoColumna)
    	 t[0] = nodoColumnas

columna ::= ID tipos opcional

    	 linea = str(t.lexer.lineno)
    	 nodoColumna = crear_nodo_general("columna",,linea,columna)
    	 nodoId = crear_nodo_general("ID",t[1],linea,columna)
    	 nodoId.hijos = []
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

'tipos ::= varchar' 

    	 nodoType = crear_nodo_general("TYPE", t[1], str(t.lexer.lineno), columna)
    	 nodoType.hijos = []
    	 t[0] = nodoType

columnas ::= columnas COMA columna

    	 nodoColumnas = t[1]
    	 nodoColumna = t[3]
    	 nodoColumnas.hijos.append(nodoColumna)
    	 t[0] = nodoColumnas

columna ::= ID tipos opcional

    	 linea = str(t.lexer.lineno)
    	 nodoColumna = crear_nodo_general("columna",,linea,columna)
    	 nodoId = crear_nodo_general("ID",t[1],linea,columna)
    	 nodoId.hijos = []
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

'tipos ::= varchar' 

    	 nodoType = crear_nodo_general("TYPE", t[1], str(t.lexer.lineno), columna)
    	 nodoType.hijos = []
    	 t[0] = nodoType

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
    	 nodoId.hijos = []
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

'tipos ::= numeric' 

    	 nodoType = crear_nodo_general("TYPE", t[1], str(t.lexer.lineno), columna)
    	 nodoType.hijos = []
    	 t[0] = nodoType

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

#REPORTE GRAMATICAL

----------

init   ::=   instrucciones

    	 t[0] = t[1]

instrucciones  ::=   instrucciones instruccion

    	 nodo = t[1]
    	 nodo.hijos.append(t[2])
    	 t[0] = nodo

instruccion  ::=   update_table

        	 t[0] = t[1]

update_table     ::=   UPDATE ID SET lista_seteos WHERE exp_operacion PTCOMA

        	 nodoUpdate = updateTable.UpdateTable(t[2], t[4].hijos, t[6])
        	 hijos.append(nodoId)
        	 hijos.append(t[4])
        	 hijos.append(t[6])
        	 nodoUpdate.setearValores(linea, columna, "UPDATE_TABLE", nNodo, , hijos)
        	 t[0] = nodoUpdate

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

exp_relacional   ::=   exp_relacional IGUAL exp_relacional

            	 nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.IGUALACION)
            	 nodoMas = crear_nodo_general("IGUALACION", "=", linea, columna)
            	 nodoExp.hijos.append(t[1])
            	 nodoExp.hijos.append(nodoMas)
            	 nodoExp.hijos.append(t[3])
            	 t[0] = nodoExp  

primitivo  ::=   ENTERO

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

primitivo  ::=   ID

    	 linea = str(t.lexer.lineno)
    	 nodoId = crear_nodo_general("NombreColumna", t[1], linea, columna)
    	 hijos = []
    	 nNodo = incNodo(numNodo)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.NOMBRE_COLUMNA)
    	 hijos.append(nodoId)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], hijos)
    	 t[0] = nodoPri

lista_seteos     ::=   set_columna

        	 nodoLista = crear_nodo_general("LISTA_SETEOS", "", linea, columna)
        	 nodoLista.hijos.append(t[1])
        	 t[0] = nodoLista

set_columna    ::=   ID IGUAL exp_operacion

    	 linea = str(t.lexer.lineno)
    	 nodoId = crear_nodo_general("ID", t[1], linea, columna)
    	 nNodo = incNodo(numNodo)
    	 hijos = []
    	 nodoSet = updateColumna.UpdateColumna(t[1], t[3])
    	 hijos.append(nodoId)
    	 hijos.append(t[3])
    	 nodoSet.setearValores(linea, columna, "set_columna", nNodo, , hijos)
    	 t[0] = nodoSet

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

instrucciones  ::=   instrucciones instruccion

    	 nodo = t[1]
    	 nodo.hijos.append(t[2])
    	 t[0] = nodo

instruccion  ::=   use_dabatabase

        	 t[0] = t[1]

delete_table   ::=   DELETE FROM ID WHERE exp_operacion PTCOMA

        	 nodoDelete = deleteTable.DeleteTable(t[3], t[5])
        	 hijos.append(nodoId)
        	 hijos.append(t[5])
        	 nodoDelete.setearValores(linea, columna, "DELETE_FROM", nNodo, , hijos)
        	 t[0] = nodoDelete

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

exp_relacional   ::=   exp_relacional IGUAL exp_relacional

            	 nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.IGUALACION)
            	 nodoMas = crear_nodo_general("IGUALACION", "=", linea, columna)
            	 nodoExp.hijos.append(t[1])
            	 nodoExp.hijos.append(nodoMas)
            	 nodoExp.hijos.append(t[3])
            	 t[0] = nodoExp  

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

primitivo  ::=   ID

    	 linea = str(t.lexer.lineno)
    	 nodoId = crear_nodo_general("NombreColumna", t[1], linea, columna)
    	 hijos = []
    	 nNodo = incNodo(numNodo)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.NOMBRE_COLUMNA)
    	 hijos.append(nodoId)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], hijos)
    	 t[0] = nodoPri

instrucciones  ::=   instrucciones instruccion

    	 nodo = t[1]
    	 nodo.hijos.append(t[2])
    	 t[0] = nodo

instruccion  ::=   insert_table

        	 t[0] = t[1]

insert_table   ::=   INSERT INTO ID VALUES lista_valores PTCOMA

        	 instru = insertTable.InsertTable(t[3], [], t[5].hijos)
        	 hijos.append(nodoId)
        	 hijos.append(t[5])
        	 instru.setearValores(str(linea), columna,"Insert_table", nNodo, , hijos)
        	 t[0] = instru

lista_valores  ::=   lista_valores COMA tupla

        	 nodoLista = t[1]
        	 nodoLista.hijos.append(t[3])
        	 t[0] = nodoLista

tupla  ::=   PARIZQUIERDO lista_expresiones PARDERECHO

    	 nodoTupla = crear_nodo_general("Tupla", , str(t.lexer.lineno), columna)
    	 nodoTupla.hijos.append(t[2])
    	 t[0] = nodoTupla

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   exp_operacion

    	 nodoLista = crear_nodo_general("lista_expresiones",,str(t.lexer.lineno),columna)
    	 nodoLista.hijos.append(t[1])
    	 t[0] = t[1]

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   ENTERO

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_valores  ::=   lista_valores COMA tupla

        	 nodoLista = t[1]
        	 nodoLista.hijos.append(t[3])
        	 t[0] = nodoLista

tupla  ::=   PARIZQUIERDO lista_expresiones PARDERECHO

    	 nodoTupla = crear_nodo_general("Tupla", , str(t.lexer.lineno), columna)
    	 nodoTupla.hijos.append(t[2])
    	 t[0] = nodoTupla

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   exp_operacion

    	 nodoLista = crear_nodo_general("lista_expresiones",,str(t.lexer.lineno),columna)
    	 nodoLista.hijos.append(t[1])
    	 t[0] = t[1]

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   ENTERO

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_valores  ::=   tupla

        	 nodoLista = crear_nodo_general("Lista_valores", , str(t.lexer.lineno), columna)
        	 nodoLista.hijos.append(t[1])
        	 t[0] = nodoLista

tupla  ::=   PARIZQUIERDO lista_expresiones PARDERECHO

    	 nodoTupla = crear_nodo_general("Tupla", , str(t.lexer.lineno), columna)
    	 nodoTupla.hijos.append(t[2])
    	 t[0] = nodoTupla

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   lista_expresiones COMA exp_operacion

    	 nodoLista = t[1]
    	 nodoLista.hijos.append(t[3])
    	 t[0] = nodoLista

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   CADENA

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

lista_expresiones  ::=   exp_operacion

    	 nodoLista = crear_nodo_general("lista_expresiones",,str(t.lexer.lineno),columna)
    	 nodoLista.hijos.append(t[1])
    	 t[0] = t[1]

exp_operacion  ::=  exp_logica

    	 nodoExp = crear_nodo_general("Exp_OPERACION", , str(t.lexer.lineno), columna)
    	 nodoExp.hijos.append(t[1])
    	 t[0] = t[1]

exp_logica     ::=     exp_relacional

        	 t[0] = t[1]

primitivo  ::=   ENTERO

    	 nNodo = incNodo(numNodo)
    	 linea = str(t.lexer.lineno)
    	 nodoPri = expresion.Expresion()
    	 nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    	 nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    	 t[0] = nodoPri

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

    	 nodoColumnas = t[1]
    	 nodoColumna = t[3]
    	 nodoColumnas.hijos.append(nodoColumna)
    	 t[0] = nodoColumnas

columna ::= ID tipos opcional

    	 linea = str(t.lexer.lineno)
    	 nodoColumna = crear_nodo_general("columna",,linea,columna)
    	 nodoId = crear_nodo_general("ID",t[1],linea,columna)
    	 nodoId.hijos = []
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

'tipos ::= varchar' 

    	 nodoType = crear_nodo_general("TYPE", t[1], str(t.lexer.lineno), columna)
    	 nodoType.hijos = []
    	 t[0] = nodoType

columnas ::= columnas COMA columna

    	 nodoColumnas = t[1]
    	 nodoColumna = t[3]
    	 nodoColumnas.hijos.append(nodoColumna)
    	 t[0] = nodoColumnas

columna ::= ID tipos opcional

    	 linea = str(t.lexer.lineno)
    	 nodoColumna = crear_nodo_general("columna",,linea,columna)
    	 nodoId = crear_nodo_general("ID",t[1],linea,columna)
    	 nodoId.hijos = []
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

'tipos ::= varchar' 

    	 nodoType = crear_nodo_general("TYPE", t[1], str(t.lexer.lineno), columna)
    	 nodoType.hijos = []
    	 t[0] = nodoType

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
    	 nodoId.hijos = []
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

'tipos ::= numeric' 

    	 nodoType = crear_nodo_general("TYPE", t[1], str(t.lexer.lineno), columna)
    	 nodoType.hijos = []
    	 t[0] = nodoType

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

