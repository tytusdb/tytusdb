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
    if str(t[1]).upper() == 'DEFAULT':
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
