from Ast import Nodo

# Función que crea el Nodo para la producción Alter Table
def getAlterTableNode(t):
    childs = []
    g = '<alter_instr> ::= ALTER TABLE ID '
    if len(t) == 5:
        g += '<list_alter_column>\n'
        childs.append(Nodo('Operacion','ALTER COLUMN',t[4],t.lexer.lineno,0,g))
    elif len(t) == 7:
        g += str(t[4])+' COLUMN <listtablas>\n'
        childs.append(Nodo('Operacion',t[4]+' '+t[5],t[6],t.lexer.lineno,0,g))
    elif len(t) == 9:
        if str(t[4]).upper() == 'RENAME':
            g += '\"RENAME\" COLUMN ID TO ID\n'
            n1 = Nodo('ID',t[6],[],t.lexer.lineno)
            n2 = Nodo('ID',t[8],[],t.lexer.lineno)
            childs.append(Nodo('Operacion',t[4]+' '+t[5],[n1,n2],t.lexer.lineno,0,g))
        else:
            g += '\"ADD\" \"CHECK\" \"PARIZQ\" <condicion> \"PARDER\"\n'  
            childs.append(Nodo('Operacion',t[4]+' '+t[5],[t[7]],t.lexer.lineno,0,g))
    elif len(t) == 11:
        g += '\"ADD\" \"CONSTRAINT\" ID \"UNIQUE\" \"PARIZQ\" ID \"PARDER\"\n'
        n1 = Nodo('ID',t[6],[],t.lexer.lineno)
        n2 = Nodo('ID',t[9],[],t.lexer.lineno)
        childs.append(Nodo('Operacion',t[4]+' '+t[5],[n1,n2],t.lexer.lineno,0,g))
    elif len(t) == 12:
        g += '\"ADD\" \"FOREIGN\" \"KEY\" \"PARIZQ\" ID \"PARDER\" \"REFERENCES\" ID\n'
        n1 = Nodo('Columna',t[8],[],t.lexer.lineno)
        n2 = Nodo('Referencia',t[11],[],t.lexer.lineno)
        childs.append(Nodo('Operacion',t[4]+' '+t[5]+' '+t[6],[n1,n2],t.lexer.lineno,0,g))
    elif len(t) == 10:
        g += '\"ALTER\" \"COLUMN\" ID \"SET\" \"NOT\" \"NULL\"\n'
        n = Nodo('Columna',t[6],[],t.lexer.lineno)
        childs.append(Nodo('Operacion',t[7]+' '+t[8]+' '+t[9],[n],t.lexer.lineno,0,g))
    else:
        childs.append(Nodo('Error','getAlterTable',[],t.lexer.lineno)) 
    return  Nodo('ALTER TABLE',t[3],childs,t.lexer.lineno)

# Función para crear el Nodo del tipo de la Columna
def getColumnTypeNode(t):
    if len(t) == 2:
        return Nodo('Tipo', t[1], [], t.lexer.lineno)
    elif len(t) == 3:
        return Nodo('Tipo', t[1], [t[2]], t.lexer.lineno)
    elif len(t) == 5:
        n = Nodo('Limite',str(t[3]),[],t.lexer.lineno)
        return Nodo('Tipo', t[1], [n], t.lexer.lineno)
    elif len(t) == 6:
        n = Nodo('Limite',str(t[4]),[],t.lexer.lineno)
        return Nodo('Tipo', t[1]+' '+t[2], [n], t.lexer.lineno)
    elif len(t) == 7:
        n1 = Nodo('Digitos',str(t[3]),[],t.lexer.lineno)
        n2 = Nodo('Cifras',str(t[5]),[],t.lexer.lineno)
        return Nodo('Tipo',t[1],[n1,n2],t.lexer.lineno)
    else:
        return Nodo('Error','getColumType',[],t.lexer.lineno)
 
# Función para obtener el nodo Parametro de la produccion Insert-Into
def getParamNode(t):
    g = '<parametroinsert> ::= '
    if len(t) == 4:
        g += 'NOW PARIZQ PADER\n'
        n = Nodo('NOW()','',[],t.lexer.lineno,0,'')
        return Nodo('Parametro','',[n],t.lexer.lineno,0,g)
    elif len(t) == 5:
        print('MD5')
        g += '\"MD5\" PARIZQ <cualquiercadena> PARDER\n'
        n = Nodo('MD5','',[t[3]],t.lexer.lineno,0,'')
        return Nodo('Parametro','',[n],t.lexer.lineno,0,g)
    elif str(t[1]).upper() == 'DEFAULT':
        g += '\"DEFAULT\"\n'
        return Nodo('Parametro','DEFAULT',[],t.lexer.lineno,0,g)
    else:
        g += '<expresion>\n'
        return Nodo('Parametro','',[t[1]],t.lexer.lineno,0,g)

# Función para crear el Nodo para la producción 'asignacion'
def getAssignNode(t):
    g = '<asignacion> ::= ID \"IGUAL\" <expresion>\n'
    n1 = Nodo('ID',t[1],[],t.lexer.lineno)
    return Nodo('Asignacion','',[n1,t[3]],t.lexer.lineno,0,g)

# Función para crear el Nodo para FBC2
def getStringFunctionNode2(t):
    if len(t) == 9:
        g = '<func_bin_strings_2> ::= \"'+t[1]+'\" \"PARIZQ\" <cadena> \"COMA\" <cualquiernumero> \"COMA\" <cualquiernumero> \"PARDER\"\n'
        return Nodo('FUNCION STR',t[1],[t[3], t[5], t[7]],t.lexer.lineno,0,g)
    else:
        g = '<func_bin_strings_2> ::= \"TRIM\" \"PARIZQ\" <cadena> \"PARDER\"\n'
        return Nodo('FUNCION STR','TRIM',[t[3]],t.lexer.lineno,0,g)

# Función para crear el Nodo para FBC4
def getStringFunctionNode4(t):
    childs = []
    g = '<func_bin_strings_4> ::= '
    if len(t) == 5:
        v = '<alias>' if str(t[1]).upper() == 'CONVERT' else '<cadena>'
        g += '\"'+str(t[1])+'\" \"PARIZQ\"'+v+'\"PARDER\"\n'
        childs = [ t[3] ]
    elif len(t) == 7:
        v = 'ENTERO' if str(t[1]).upper() == 'GET_BYTE' else '<cadena>'
        g += '\"'+t[1]+'\" \"PARIZQ\" <cadena> \"COMA\" '+v+' \"PARDER\"\n'
        childs = [ t[3], t[5] ]
    elif len(t) == 9:
        g += '\"SET_BYTE\" \"PARIZQ\" <cadena> \"COMA\" ENTERO \"COMA\" ENTERO \"PARDER\"\n'
        childs = [ t[3], t[5], t[7] ]
    return Nodo('FUNCION STR',t[1],childs,t.lexer.lineno,0,g)

# Función para crear el nodo para la instruccion Create Table
def getCreateTableNode(t):
    g = '<create_table> : \"CREATE\" \"TABLE\" ID \"PARIZQ\" <list_columns_x> \"PARDER\" <end_create_table>'
    n = Nodo('COLUMNAS','',t[5],t.lexer.lineno)
    if t[7] != None:
        return Nodo('CREATE TABLE',t[3],[n,t[7]],t.lexer.lineno,0,g)
    return Nodo('CREATE TABLE',t[3],[n],t.lexer.lineno,0,g)

# Función para crear una columna
def getKeyOrColumnNode(t):
    g =  '<key_column> ::= \"PRIMARY\" \"KEY\" \"PARIZQ\" <listtablas> \"PARDER\"\n'
    g += '<key_column> ::= ID <type_column> <attributes>\n'
    if len(t) == 6:
        return Nodo('PRIMARY KEY','',t[4],t.lexer.lineno,0,g)
    return Nodo('COLUMN',t[1],[t[2],t[3]],t.lexer.lineno,0,g)

# Función para crear un Nodo atributo
def getAttributesNode(t):
    g = '<attributes> ::= <default_value> <null_field> <constraint_field> <null_field> <primary_key>\n'
    childs = []
    if t[1] != None:
        childs.append(t[1])
    if t[2] != None:
        childs.append(t[2])
    if t[3] != None:
        childs.append(t[3])
    if t[4] != None:
        childs.append(t[4])
    if t[5] != None:
        childs.append(t[5])
    return Nodo('ATRIBUTOS','',childs,t.lexer.lineno,0,g)

# Función para crear un Nodo de atributo Null
def getNullFieldNode(t):
    g = ''
    if len(t) == 3:
        g = '<null_field> ::= \"NOT\" \"NULL\"\n'
        return Nodo('NOT NULL','',[],t.lexer.lineno,0,g)
    elif t[1] != None:
        g = '<null_field> ::= \"NULL\"\n'
        return Nodo('NULL','',[],t.lexer.lineno,0,g)
    return None

# Función para crear el nodo para Constraint
def getConstraintFieldNode(t):
    g  = '<constraint_field> ::= \"UNIQUE\"\n'
    g += '<constraint_field> ::= \"CONSTRAINT\" ID <check_unique>\n'
    g += '<constraint_field> ::= \"CHECK\" \"PARIZQ\" <condiciones> \"PARDER\"\n'
    g += '<constraint_field> ::= <empty>\n'
    if len(t) == 2:
        if t[1] != None:
            return Nodo('UNIQUE','',[],t.lexer.lineno,0,g)
    elif len(t) == 4:
        if t[3] != None:
            return Nodo('CONSTRAINT',t[2],[t[3]],t.lexer.lineno,0,g)
        else:
            return Nodo('CONSTRAINT',t[2],[],t.lexer.lineno,0,g)
    elif len(t) == 5:
        return Nodo('CHECK','',[t[3]],t.lexer.lineno,0,g)
    return None

# Función para crear el nodo para el atributo Check | Unique
def getCheckUnique(t):
    g  = '<check_unique> ::= \"UNIQUE\"\n'
    g += '<check_unique> ::= \"CHECK\" \"PARIZQ\" <condiciones> \"PARDER\"\n'
    g += '<check_unique> ::= <empty>\n'
    if len(t) == 5:
        return Nodo('CHECK','',[t[3]],t.lexer.lineno,0,g)
    elif t[1] != None:
        return Nodo('UNIQUE','',[],t.lexer.lineno,0,g)
    return None

############################################ Funciones AST Querys ########################################

# Función que crea el Nodo para la producción Select
def getSelect(t):
    gramatica = '<select_instr> ::= \"SELECT\" '
    childs = []
    if t[2] != None:
        childs.append(t[2])
        gramatica += '<termdistinct> '
    childs.append(t[3])
    gramatica += '<select_list> '
    if t[4] != None:
        gramatica += '\"FROM\" '
        a = t[4]
        if a[0] != None:
            childs.append(a[0])
            gramatica += '<listatablasselect> '
        if a[1] != None:
            childs.append(a[1])
            gramatica += '<whereselect> '
        if a[2] != None:
            childs.append(a[2])
            gramatica += '<groupby> '
        if a[3] != None:
            childs.append(a[3])
            gramatica += '<orderby> '
    gramatica += '\"PTCOMA\" '
    return Nodo('SELECT', '', childs, t.lexer.lineno, 0, gramatica)

def getSelectSimple(t):
    childs = Nodo('Rows', '', t[2], t.lexer.lineno)     # pendiente 
    return Nodo('SELECT', '', [childs], t.lexer.lineno)

def getDistinct(t) : 
    if t[1] != None:                                    # pendiente
        t[0] = Nodo('DISTINC', '', [], t.lexer.lineno, 0, '<termdistinct> ::= \"DISTINCT\" ')
    return t[0]

def getSelectList(t):
    if t[1] == '*':
        gramatica = '<selectlist> ::= \"ASTERISCO\"'
        return Nodo('ASTERISCO', '*', [], t.lexer.lineno, 0, gramatica)
    else :
        gramatica = '<selectlist> ::= <listaselect> \n'
        gramatica += '<listaselect> ::= <listaselect> \"COMA\" <valselect> \n'
        gramatica += '<listaselect> ::= <valselect>'
        return Nodo('ROWS', '', t[1], t.lexer.lineno, 0, gramatica)

def getValSelect(t, etiqueta) :
    if etiqueta == 'ID':
        if t[2] != None :
            gramatica = '<valselect> ::= \"'+str(t[1])+'\" <alias>'
            return Nodo('ID', t[1], [t[2]], t.lexer.lineno,0, gramatica)
        else :
            gramatica = '<valselect> ::= \"'+str(t[1])+'\" '
            return Nodo('ID', t[1], [], t.lexer.lineno, 0, gramatica)

    elif etiqueta == 'ID.ID':
        childs = []
        gramatica = ''
        if t[4] != None :
            gramatica = '<valselect> ::= \"'+str(t[1])+'\" \"PUNTO\" \"'+str(t[3])+'\" <alias> '
            childs.append(Nodo('ID', t[3], [t[4]], t.lexer.lineno))
        else :
            gramatica = '<valselect> ::= \"'+str(t[1])+'\" \"PUNTO\" \"'+str(t[3])+'\" '
            childs.append(Nodo('ID', t[3], [], t.lexer.lineno))
        return Nodo('AliasTabla', t[1], childs, t.lexer.lineno, 0, gramatica)

    elif etiqueta == 'ID.*':
        childs = Nodo('All', '.*', [], t.lexer.lineno)
        gramatica = '<valselect> ::= \"'+str(t[1])+'\" \"PUNTO\" \"ASTERISCO\"'
        return Nodo('AliasTabla', t[1], [childs], t.lexer.lineno, 0, gramatica)

    elif etiqueta == 'funmat_ws':
        if t[2] != None :
            t[1].hijos.append(t[2])
        t[1].gramatica = '<valselect> ::= <funcion_matematica_ws> <alias>\n' + t[1].gramatica
        return t[1]

    elif etiqueta == 'funmat_s':
        if t[2] != None :
            t[1].hijos.append(t[2])
        t[1].gramatica = '<valselect> ::= <funcion_matematica_s> <alias>\n' + t[1].gramatica
        return t[1]

    elif etiqueta == 'funmat_trig':
        if t[2] != None :
            t[1].hijos.append(t[2])
        t[1].gramatica = '<valselect> ::= <funcion_trigonometrica> <alias>\n' + t[1].gramatica
        return t[1]

    elif etiqueta == 'funcbinstring1':
        if t[2] != None :
            t[1].hijos.append(t[2])
        return t[1]

    elif etiqueta == 'funcbinstring2':
        if t[2] != None :
            t[1].hijos.append(t[2])
        return t[1]

    elif etiqueta == 'funcbinstring4':
        if t[2] != None :
            t[1].hijos.append(t[2])
        return t[1]

    elif etiqueta == 'subquery':
        if t[4] != None :
            gramatica = '<valselect> ::=  \"PARIZQ\" <select_instr1> \"PARDER\" <alias> '
            return Nodo('Subquery', '', [t[2], t[4]], t.lexer.lineno, 0, gramatica)
        else :
            gramatica = '<valselect> ::=  \"PARIZQ\" <select_instr1> \"PARDER\"'
            return Nodo('Subquery', '', [t[2]], t.lexer.lineno, 0, gramatica)  

    elif etiqueta == 'agregacion':
        if t[5] != None :
            gramatica = '<valselect> ::=  <agregacion> \"PARIZQ\" <cualquieridentificador> \"PARDER\" <alia> \n'
            gramatica += '<agregacion> ::= \"' + str(t[1]) + '\" '
            return Nodo('Agregacion', t[1], [t[3], t[5]], t.lexer.lineno, 0, gramatica)
        else :
            gramatica = '<valselect> ::=  <agregacion> \"PARIZQ\" <cualquieridentificador> \"PARDER\" \n'
            gramatica += '<agregacion> ::= \"' + str(t[1]) + '\"'
            return Nodo('Agregacion', t[1], [t[3]], t.lexer.lineno, 0, gramatica)  

    elif etiqueta == 'count_ast':
        childs = Nodo('Asterisco', '*', [], t.lexer.lineno)
        if t[5] != None :
            gramatica = '<valselect> ::=  \"COUNT\" \"PARIZQ\" \"ASTERISCO\" \"PARDER\" <alia>'
            return Nodo('Agregacion', t[1], [childs, t[5]], t.lexer.lineno, 0, gramatica)
        else :
            gramatica = '<valselect> ::=  \"COUNT\" \"PARIZQ\" \"ASTERISCO\" \"PARDER\"'
            return Nodo('Agregacion', t[1], [childs], t.lexer.lineno,0, gramatica)  

    else : #'count_val'
        if t[5] != None :
            gramatica = '<valselect> ::=  \"COUNT\" \"PARIZQ\" <cualquieridentificador> \"PARDER\" <alia>'
            return Nodo('Agregacion', t[1], [t[3], t[5]], t.lexer.lineno, 0, gramatica)
        else :
            gramatica = '<valselect> ::=  \"COUNT\" \"PARIZQ\" <cualquieridentificador> \"PARDER\"'
            return Nodo('Agregacion', t[1], [t[3]], t.lexer.lineno, 0, gramatica) 


def getTablaSelect(t) :
    if len(t) == 3:
        if t[2] != None:
            return Nodo('Tabla', t[1], [t[2]], t.lexer.lineno, 0, '<tablaselect> ::= \"'+str(t[1])+'\" <alias>')
        else :
            return Nodo('Tabla', t[1], [], t.lexer.lineno, 0, '<tablaselect> ::= \"'+str(t[1])+'\"')
    else:
        if t[4] != None :
            gramatica = '<tablaselect> ::= \"PARIZQ\" <select_instr1> \"PARDER\" <alias>'
            return Nodo('Subquery', '', [t[2], t[4]], t.lexer.lineno, 0, gramatica)
        else :
            gramatica = '<tablaselect> ::= \"PARIZQ\" <select_instr1> \"PARDER\"'
            return Nodo('Subquery', '', [t[2]], t.lexer.lineno, 0, gramatica)  

def getAlias(t):
    if t[1] == None:
        return t[1]
    elif t[1].lower() == 'as':
        gramatica = '<alias> ::= \"AS\" \"' + str(t[2]) + '\"'
        return Nodo('Alias', t[2], [], t.lexer.lineno, 0, gramatica)
    else :
        gramatica = '<alias> ::= \"'+ str(t[1]) + '\"'
        return Nodo('Alias', t[1], [], t.lexer.lineno, 0, gramatica)

def getSubstring(t):
    childs = [t[3]]
    gramatica = '<condicionwhere> ::= <wheresubstring>\n'
    gramatica += '<wheresubstring> ::= \"SUBSTRING\" \"PARIZQ\" <cadenastodas> \"COMA\" \"ENTERO\" \"COMA\" \"ENTERO\" \"PARDER\" \"IGUAL\" \"CADENASIMPLE\"'
    childs.append(Nodo('DE', str(t[5]), [], t.lexer.lineno))
    childs.append(Nodo('HASTA', str(t[7]), [], t.lexer.lineno))
    childs.append(Nodo('IGUAL', t[9], [], t.lexer.lineno))
    childs.append(Nodo('CADENA', t[10], [], t.lexer.lineno))
    return Nodo("SUBSTRING", '', childs, t.lexer.lineno, 0, gramatica)

def getOpRelacional(t):
    if t[2] == '<>':
        gramatica = '<condicion> ::= <expresion> \"DIFERENTE\" <expresion>'
        return Nodo('OPREL', '\\<\\>', [t[1], t[3]], t.lexer.lineno, 0, gramatica)
    gramatica = '<condicion> ::= <expresion> \"' +t[2]+'\" <expresion>'
    return Nodo('OPREL', '\\'+str(t[2]), [t[1], t[3]], t.lexer.lineno, 0, gramatica)

def getGroupby(t):
    if len(t) == 4:
        gramatica = '<groupby> ::= \"GROUP\" \"BY\" <listagroupby>' 
        childs = Nodo('LISTA', '', t[3], t.lexer.lineno)
        return Nodo('GROUPBY', '', [childs], t.lexer.lineno, 0, gramatica) 
    else:
        gramatica = '<groupby> ::= \"GROUP\" \"BY\" <listagroupby> \"HAVING\" <condicioneshaving>'
        childs = [Nodo('LISTA', '', t[3], t.lexer.lineno)]
        childs.append(Nodo('HAVING', '', [t[5]], t.lexer.lineno))
        return Nodo('GROUPBY', '', childs, t.lexer.lineno, 0, gramatica) 

def getOrderBy(t) :
    if len(t) == 4:
        gramatica = '<orderby> ::= \"ORDER\" \"BY\" <listaorderby>'
        childs = Nodo('LISTA', '', t[3], t.lexer.lineno)
        return Nodo('ORDERBY', '', [childs], t.lexer.lineno, 0, gramatica)
    else:
        gramatica = '<orderby> ::= \"ORDER\" \"BY\" <listaorderby> <instrlimit>'
        childs = [Nodo('LISTA', '', t[3], t.lexer.lineno)]
        childs.append(t[4])
        return Nodo('ORDERBY', '', childs, t.lexer.lineno, 0, gramatica)

def getValOrder(t):
    if t[3] != None:
        gramatica = '<valororderby> ::= <cualquieridentificador> <ascdesc> <anular>'
        return Nodo('COLUMN', '', [t[1], t[2], t[3]], t.lexer.lineno, 0, gramatica)
    else : 
        gramatica = '<valororderby> ::= <cualquieridentificador> <ascdesc>'
        return Nodo('COLUMN', '', [t[1], t[2]], t.lexer.lineno, 0, gramatica)

def getAscDesc(t) :
    if t[1] != None:
        gramatica = '<ascdesc> ::= \"' + t[1] +'\"'
        return Nodo(t[1], '', [], t.lexer.lineno, 0, gramatica)
    else:
        return Nodo('ASC', '', [], t.lexer.lineno)

def getLimit(t):
    if t[3] != None:
        gramatica = '<instrlimit> ::= \"LIMIT\" \"'+str(t[2])+'\" <instroffset>'
        return Nodo(t[1], str(t[2]), [t[3]], t.lexer.lineno, 0, gramatica)
    else:
        gramatica = '<instrlimit> ::= \"LIMIT\" \"'+t[2]+'\"'
        return Nodo(t[1], str(t[2]), [], t.lexer.lineno, 0, gramatica)

def getIdentificador(t):
    if len(t) == 2:
        gramatica = '<cualquieridentificador> ::= \"'+str(t[1])+'\"'
        return Nodo('ID', t[1], [], t.lexer.lineno,0, gramatica)
    else :
        gramatica = '<cualquieridentificador> ::= \"'+str(t[1])+'\" \"PUNTO\" \"'+str(t[3])+'\"'
        childs = [Nodo('ID', t[3], [], t.lexer.lineno)]
        return Nodo('AliasTabla', t[1], childs, t.lexer.lineno, 0, gramatica)

def getValorNumerico(t):
    if isinstance(t[1], float):
        gramatica = '<cualquiernumero> ::= \"'+str(t[1])+'\"'
        return Nodo('DECIMAL', str(t[1]), [], t.lexer.lineno, 0, gramatica)     
    else:
        gramatica = '<cualquiernumero> ::= \"'+str(t[1])+'\"'
        return Nodo('ENTERO', str(t[1]), [], t.lexer.lineno, 0, gramatica)

def getFuncionMatematica(t):
    if len(t) == 4:
        gramatica = '<funcion_matematica_s> ::= \"'+str(t[1])+'\" \"PARIZQ\" \"PARDER\"'
        return Nodo('PI', '', [], t.lexer.lineno, 0, gramatica)
    elif len(t) == 5:
        gramatica = '<funcion_matematica_s> ::= \"'+str(t[1])+'\" \"PARIZQ\" <expresionaritmetica> \"PARDER\"'
        return Nodo('Matematica', t[1], [t[3]], t.lexer.lineno, 0, gramatica)
    else :
        gramatica = '<funcion_matematica_s> ::= \"'+str(t[1])+'\" \"PARIZQ\" <expresionaritmetica> \"COMA\" <expresionaritmetica>\"PARDER\"'
        return Nodo('Matematica', t[1], [t[3], t[5]], t.lexer.lineno, 0, gramatica)

def getBetween(t):
    if len(t) == 6:
        gramatica = '<condicionwhere> ::= <between_state>\n'
        gramatica += '<between_state> ::= <cualquiernumero> \"BETWEEN\" <valores> \"AND\" <valores>'
        return Nodo('BETWEEN', '', [t[1], t[3], t[5]], t.lexer.lineno, 0, gramatica)
    else: 
        gramatica = '<condicionwhere> ::= <not_between_state>\n'
        gramatica += '<between_state> ::= <cualquiernumero> \"NOT\" \"BETWEEN\" <valores> \"AND\" <valores>'
        return Nodo('NOT BETWEEN', '', [t[1], t[4], t[6]], t.lexer.lineno, 0, gramatica)

def getPredicates(t):
    gramatica = '<condicionwhere> ::= <predicates_state>\n' 
    if len(t) == 3:
        gramatica += '<predicates_state> ::= <valores> \"' + t[2]+'\"'
        return Nodo(t[2], '', [t[1]], t.lexer.lineno, 0, gramatica)
    elif len(t) == 4:
        gramatica += '<predicates_state> ::= <valores> \"IS\" \"NULL\"'
        return Nodo('IS NULL', '', [t[1]], t.lexer.lineno, 0, gramatica)
    else :
        gramatica += '<predicates_state> ::= <valores> \"IS\" \"NOT\" \"NULL\"'
        return Nodo('IS NOT NULL', '', [t[1]], t.lexer.lineno, 0, gramatica)

def getDistinctFrom(t) :
    gramatica = '<condicionwhere> ::= <is_distinct_state>\n' 
    if len(t) == 6: 
        gramatica += '<is_distinct_state> ::= <valores> \"IS\" \"DISTINCT\" \"FROM\" <valores>'
        return Nodo('IS DISTINCT', '', [t[1], t[5]], t.lexer.lineno, 0, gramatica)
    else :
        gramatica += '<is_distinct_state> ::= <valores> \"IS\" \"NOT\" \"DISTINCT\" \"FROM\" <valores>'
        return Nodo('IS NOT DISTINCT', '', [t[1], t[6]], t.lexer.lineno, 0, gramatica)


################################# funciones para crear AST de PL/pgsql ############################

def getlistexpresiones(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[3])
        return t[1]

def getfuncion_procedimiento(t):
    g = '<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>'
    childs = []
    if t[5] != None:
        childs.append(Nodo('PARAMETROS', '', t[5], t.lexer.lineno))
    if t[7] != None:
        childs.append(t[7])
    if t[8] != None:
        childs.append(t[8])
    return Nodo(t[2], t[3], childs, t.lexer.lineno, 0, g)

def getparametrosfunc(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[3])
        return t[1]

def getparfunc(t):
    if len(t) == 4:
        g = '<parfunc> ::= OUT ID <type_column1>'
        return Nodo(t[1], t[2], [t[3]], t.lexer.lineno, g)
    elif len(t) == 3:
        g = '<parfunc> ::= ID <type_column1>'
        return Nodo('ID', t[1], [t[2]], t.lexer.lineno, g)
    else:
        return t[1]

def gettypecolumn(t):
    if len(t) == 2:
        return Nodo('TYPE COLUMN', t[1], [], t.lexer.lineno)
    elif len(t) == 5:
        if t[1].lower() == 'table':
            n1 = Nodo('PARAMETROS', '', t[3])
            return Nodo('TYPE COLUMN', t[1], [n1], t.lexer.lineno)
        a = Nodo('ENTERO', str(t[3]), [], t.lexer.lineno)
        return Nodo('TYPE COLUMN', t[1], [a], t.lexer.lineno)
    elif len(t) == 6:
        a = Nodo('ENTERO', t[4], [], t.lexer.lineno)
        return Nodo('TYPE COLUMN', t[1], [a], t.lexer.lineno)
    else:
        a = Nodo('ENTERO', str(t[3]), [], t.lexer.lineno)
        b = Nodo('ENTERO', str(t[5]), [], t.lexer.lineno)
        return Nodo('TYPE COLUMN', t[1], [a, b], t.lexer.lineno)

def getretornofuncion(t):
    if t[1] == None:
        return None
    elif t[1].lower() == 'returns':
        g = '<tiporetorno> ::= RETURNS <type_columnn1> AS'
        return Nodo(t[1], '', [t[2]], t.lexer.lineno, g)
    elif t[1].lower() == 'language':
        g = '<tiporetorno> ::= LANGUAGE PLPGSQL AS'
        return Nodo(t[1], t[2], [], t.lexer.lineno, g)
    elif t[1].lower() == 'as':
        g = '<tiporetorno> ::= AS'
        return Nodo('AS', '', [], t.lexer.lineno)
    return None

def getCuerpoFuncion(t):
    childs = []
    childs.append(Nodo('$$', '', []))
    if t[2] != None:
        childs.append(t[2])
    childs.append(t[3])
    childs.append(Nodo('$$', '', []))
    return Nodo('CUERPO', '', childs, t.lexer.lineno)

def getlistadeclaraciones(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[2])
        return t[1]


def getdeclaraciones(t):
    childs = [Nodo('ID', t[1], [], t.lexer.lineno)]
    if t[2] != None:
        childs.append(t[2])
    childs.append(t[3])
    if t[4] != None:
        childs.append(t[4])
    if t[5] != None:
        childs.append(t[5])
    return Nodo('Declaracion', '', childs, t.lexer.lineno)

def getdeclaraciones1(t):
    childs = [Nodo('ID', t[1], [], t.lexer.lineno)]
    childs.append(Nodo('ALIAS FOR', '', [], t.lexer.lineno))
    if len(t) == 7:
        childs.append(Nodo('$', str(t[5]), [], t.lexer.lineno))
    else:
        childs.append(Nodo('ID', str(t[4]), [], t.lexer.lineno))
    return Nodo('Declaracion', '', childs, t.lexer.lineno)

def getdeclaraciones2(t):
    childs = [Nodo('ID', t[1], [], t.lexer.lineno)]
    childs.append(t[2])
    childs.append(Nodo('%', t[4], [], t.lexer.lineno))
    return Nodo('Declaracion', '', childs, t.lexer.lineno)

def getconstant(t):
    if t[1] != None:
        g = '<constantintr> ::= CONSTANT'
        return Nodo(t[1], '', [], t.lexer.lineno, g)
    return None

def getnotnull(t):
    if t[1] != None:
        g = '<notnullinst> ::= NOT NULL'
        return Nodo('NOT NULL', '', [], t.lexer.lineno,g )
    return None

def getasignavalor(t):
    if t[1] == None:
        return None
    elif t[1] == '=':
        g = '<asignavalor> ::= IGUAL <expresion>'
        return Nodo('IGUAL', '=', [t[2]], t.lexer.lineno, g)
    elif t[1] == ':=':
        g = '<asignavalor> ::= PTIGUAL <expresion>'
        return Nodo('PTIGUAL', ':=', [t[2]], t.lexer.lineno, g)
    else:
        g = '<asignavalor> ::= DEFAULT <expresion>'
        return Nodo('DEFAULT', '', [t[2]], t.lexer.lineno, g)

def getcuerpo(t):
    childs = []
    if t[2] != None:
        childs.append(Nodo('LISTA', '', t[2], t.lexer.lineno))
    childs.append(Nodo('END', '', [], t.lexer.lineno))
    return Nodo('BEGIN', '', childs, t.lexer.lineno)

def getinstlistabloque(t):
    if t[1] == None:
        return None
    return t[1]

def getlistabloque(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[2])
        return t[1]

def getraisenotice(t):
    if len(t) == 5:
        return Nodo('RAISE NOTICE', t[3], [], t.lexer.lineno)
    else:
        n1 = Nodo('ID', t[5], [], t.lexer.lineno)
        return Nodo('RAISE NOTICE', t[3], [n1], t.lexer.lineno)

def getasignacionbloque(t):

    n1 = Nodo('ID', t[1], [], t.lexer.lineno)
    return Nodo('ASIGNACION', t[2], [n1, t[3]], t.lexer.lineno)

def getsubbloque(t):
    childs = []
    if t[1] != None:
        childs.append(t[1])
    childs.append(t[2])
    return Nodo('SUBBLOQUE', '', childs, t.lexer.lineno)

def getcuerposubbloque(t):
    childs = [Nodo('BEGIN', '', [], t.lexer.lineno)]
    if t[2] != None:
        childs.append(Nodo('LISTA', '', t[2], t.lexer.lineno))
    childs.append(Nodo('END', '', [], t.lexer.lineno))
    return Nodo('CUERPO', '', childs, t.lexer.lineno)

def getlistasubbloque(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[2])
        return t[1]

def getraisenoticesubbloque(t):
    if len(t) == 5:
        g = '<raisenotice1> ::= RAISE NOTICE CADENASIMPLE PTCOMA'
        return Nodo('RAISE NOTICE', t[3], [], t.lexer.lineno, g)
    elif len(t) == 7:
        g = '<raisenotice1> ::= RAISE NOTICE CADENASIMPLE COMA ID PTCOMA'
        n1 = Nodo('ID', t[5], [], t.lexer.lineno)
        return Nodo('RAISE NOTICE', t[3], [n1], t.lexer.lineno, g)
    else:
        g = '<raisenotice1> ::= RAISE NOTICE CADENASIMPLE COMA OUTERBLOCK PUNTO ID PTCOMA'
        n1 = Nodo('OUTERBLOCK', t[7], [], t.lexer.lineno)
        return Nodo('RAISE NOTICE', t[3], [n1], t.lexer.lineno, g)

def getinstrexecute(t):
    childs = [t[3]]
    if t[5] != None:
        childs.append(t[5])
    if t[6] != None:
        childs.append(t[6])
    return Nodo('EXECUTE', '', childs, t.lexer.lineno)

def getinstrexecute1(t):
    childs = [t[5]]
    if t[8] != None:
        childs.append(t[8])
    if t[9] != None:
        childs.append(t[9])
    return Nodo('EXECUTE FORMAT', '', childs, t.lexer.lineno)

def getintotarget(t):
    if t[1] == None:
        return None
    else:
        return Nodo(t[1], t[2], [], t.lexer.lineno)

def getusingexpresion(t):
    if t[1] == None:
        return None
    else:
        return Nodo('USING', '', t[2], t.lexer.lineno)

def getinstrif(t):
    g = '<instrif>   : IF <condiciones> THEN <instrlistabloque> END IF PTCOMA'
    childs = [Nodo('CONDICIONES', '', [t[2]], t.lexer.lineno)]
    if t[4] != None:
        childs.append(Nodo('THEN', '', t[4], t.lexer.lineno))
    childs.append(Nodo('END IF', '', []))
    return Nodo('IF', '', childs, t.lexer.lineno, 0, g)

def getinstrif1(t):
    g = '<instrif>   : IF <condiciones> THEN <instrlistabloque> ELSE <instrlistabloque> END IF PTCOMA'
    childs = [Nodo('CONDICIONES', '', [t[2]], t.lexer.lineno)]
    if t[4] != None:
        childs.append(Nodo('THEN', '', t[4], t.lexer.lineno))
    if t[6] != None:
        childs.append(Nodo('ELSE', '', t[6], t.lexer.lineno))
    childs.append(Nodo('END IF', '', [], t.lexer.lineno))
    return Nodo('IF', '', childs, t.lexer.lineno, 0, g)

def getinstrif2(t):
    g = '<instrif>   : IF <condiciones> THEN <instrlistabloque> <instrelseif> END IF PTCOMA'
    childs = [Nodo('CONDICIONES', '', [t[2]], t.lexer.lineno)]
    if t[4] != None:
        childs.append(Nodo('THEN', '', t[4], t.lexer.lineno))
    if t[5] != None:
        childs.append(Nodo('LISTA ELSIF', '', t[5], t.lexer.lineno))
    childs.append(Nodo('END IF', '', [], t.lexer.lineno))
    return Nodo('IF', '', childs, t.lexer.lineno, 0, g)

def getinstrif3(t):
    g = '<instrif>    : IF <condiciones> THEN <instrlistabloque> <instrelseif> ELSE <instrlistabloque> END IF PTCOMA'
    childs = [Nodo('CONDICIONES', '', [t[2]], t.lexer.lineno)]
    if t[4] != None:
        childs.append(Nodo('THEN', '', t[4], t.lexer.lineno))
    if t[5] != None:
        childs.append(Nodo('LISTA ELSIF', '', t[5], t.lexer.lineno))
    if t[7] != None:
        childs.append(Nodo('ELSE', '', t[7], t.lexer.lineno))
    childs.append(Nodo('END IF', '', [], t.lexer.lineno))
    return Nodo('IF', '', childs, t.lexer.lineno, 0, g)

def getinstrelseif(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[2])
        return t[1]

def getinstrcase(t):
    childs = [t[2]]
    n1 = Nodo('LISTA WHEN', '', t[3], t.lexer.lineno)
    childs.append(n1)
    if t[4] != None:
        childs.append(t[4])
    n2 = Nodo('END CASE', '', [], t.lexer.lineno)
    childs.append(n2)
    return Nodo('CASE', '', childs, t.lexer.lineno)
    
def getlistawhen1(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[2])
        return t[1]

def getwhen1(t):
    childs = [Nodo('EXPRESIONES', '', t[2], t.lexer.lineno)]
    childs.append(Nodo('THEN', '', t[4], t.lexer.lineno))
    return Nodo('WHEN', '', childs, t.lexer.lineno)

def getinstrcase2(t):
    childs = [Nodo('LISTA WHEN', '', t[2], t.lexer.lineno)]
    if t[3] != None:
        childs.append(t[3])
    n2 = Nodo('END CASE', '', [], t.lexer.lineno)
    childs.append(n2)
    return Nodo('CASE', '', childs, t.lexer.lineno)

def getwhen21(t):
    n1 = Nodo('ENTERO', str(t[4]), [], t.lexer.lineno)
    n2 = Nodo('ENTERO', str(t[6]), [], t.lexer.lineno)
    childs = [Nodo('ID', t[2], [], t.lexer.lineno)]
    childs.append(Nodo('BETWEEN', '', [n1, n2], t.lexer.lineno))
    childs.append(Nodo('THEN', '', t[8], t.lexer.lineno))
    return Nodo('WHEN', '', childs, t.lexer.lineno)

def getwhen22(t):
    'when2  : WHEN condiciones THEN instrlistabloque'
    childs = [Nodo('CONDICIONES', '', t[2], t.lexer.lineno)]
    childs.append(Nodo('THEN', '', t[4], t.lexer.lineno))
    return Nodo('WHEN', '', childs, t.lexer.lineno)