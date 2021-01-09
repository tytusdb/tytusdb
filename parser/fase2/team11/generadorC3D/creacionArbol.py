from generadorC3D.clases import Nodo

################################# funciones para crear AST de PL/pgsql ############################

def getlistexpresiones(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[3])
        return t[1]

def getfuncion_procedimiento(t):
    g = '<plsql_instr> : CREATE <procedfunct> ID PARIZQ <parametrosfunc> PARDER <tiporetorno> <cuerpofuncion>'
    g += '\n<procedfunct>  : PROCEDURE'
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
    g = '<parfunc>    : ID <type_column1>'
    if len(t) == 4:
        return Nodo(t[1], t[2], [t[3]], t.lexer.lineno,0, g)
    elif len(t) == 3:
        return Nodo('ID', t[1], [t[2]], t.lexer.lineno,0, g)
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
    g = '<tiporetorno>  : RETURNS <type_column1> AS'
    if t[1] == None:
        return None
    elif t[1].lower() == 'returns':
        return Nodo(t[1], '', [t[2]], t.lexer.lineno, 0, g)
    elif t[1].lower() == 'language':
        return Nodo(t[1], t[2], [], t.lexer.lineno)
    elif t[1].lower() == 'as':
        return Nodo('AS', '', [], t.lexer.lineno)
    return None

def getCuerpoFuncion(t):
    g = '<cuerpofuncion>  : CADDOLAR <declaraciones> <cuerpo> CADDOLAR LANGUAGE PLPGSQL PTCOMA'
    childs = []
    childs.append(Nodo('$$', '', []))
    if t[2] != None:
        childs.append(t[2])
    childs.append(t[3])
    childs.append(Nodo('$$', '', []))
    return Nodo('CUERPO', '', childs, t.lexer.lineno, 0, g)

def getlistadeclaraciones(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[2])
        return t[1]


def getdeclaraciones(t):
    g = '<declaracion> : ID <constantintr> type_column1 <notnullinst> <asignavalor> PTCOMA'
    childs = [Nodo('ID', t[1], [], t.lexer.lineno)]
    if t[2] != None:
        childs.append(t[2])
    childs.append(t[3])
    if t[4] != None:
        childs.append(t[4])
    if t[5] != None:
        childs.append(t[5])
    return Nodo('Declaracion', '', childs, t.lexer.lineno, 0, g)

def getdeclaraciones1(t):
    g = '<declaracion> : ID ALIAS1 FOR DOLAR ENTERO PTCOMA'
    childs = [Nodo('ID', t[1], [], t.lexer.lineno)]
    childs.append(Nodo('ALIAS FOR', '', [], t.lexer.lineno))
    if len(t) == 7:
        childs.append(Nodo('$', str(t[5]), [], t.lexer.lineno))
    else:
        childs.append(Nodo('ID', str(t[4]), [], t.lexer.lineno))
    return Nodo('Declaracion', '', childs, t.lexer.lineno, 0, g)

def getdeclaraciones2(t):
    g = 'declaracion : ID cualquieridentificador MODULO TYPE PTCOMA'
    childs = [Nodo('ID', t[1], [], t.lexer.lineno)]
    childs.append(t[2])
    childs.append(Nodo('%', t[4], [], t.lexer.lineno))
    return Nodo('Declaracion', '', childs, t.lexer.lineno, 0, g)

def getconstant(t):
    if t[1] != None:
        g = 'constantintr : CONSTANT'
        return Nodo(t[1], '', [], t.lexer.lineno, 0, g)
    return None

def getnotnull(t):
    if t[1] != None:
        return Nodo('NOT NULL', '', [], t.lexer.lineno)
    return None

def getasignavalor(t):
    if t[1] == None:
        return None
    elif t[1] == '=':
        g = '<asignavalor>      : DEFAULT <expresion>'
        return Nodo('IGUAL', '=', [t[2]], t.lexer.lineno, 0, g)
    elif t[1] == ':=':
        g = '<asignavalor>      : DEFAULT <expresion>'
        return Nodo('PTIGUAL', ':=', [t[2]], t.lexer.lineno, 0, g)
    else:
        return Nodo('DEFAULT', '', [t[2]], t.lexer.lineno)

def getcuerpo(t):
    g = '<cuerpo>     : BEGIN <instrlistabloque> END PTCOMA'
    childs = []
    if t[2] != None:
        childs.append(Nodo('LISTA', '', t[2], t.lexer.lineno))
    childs.append(Nodo('END', '', [], t.lexer.lineno))
    return Nodo('BEGIN', '', childs, t.lexer.lineno, 0, g)

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
    g = '<asignacionbloque> : ID IGUAL <expresion> PTCOMA'
    n1 = Nodo('ID', t[1], [], t.lexer.lineno)
    return Nodo('ASIGNACION', t[2], [n1, t[3]], t.lexer.lineno, 0, g)

def getsubbloque(t):
    childs = []
    if t[1] != None:
        childs.append(t[1])
    childs.append(t[2])
    return Nodo('SUBBLOQUE', '', childs, t.lexer.lineno)

def getcuerposubbloque(t):
    g = '<cuerposub> : BEGIN <listasubbloque> END PTCOMA'
    childs = [Nodo('BEGIN', '', [], t.lexer.lineno)]
    if t[2] != None:
        childs.append(Nodo('LISTA', '', t[2], t.lexer.lineno))
    childs.append(Nodo('END', '', [], t.lexer.lineno))
    return Nodo('CUERPO', '', childs, t.lexer.lineno, 0, g)

def getlistasubbloque(t):
    if len(t) == 2:
        return [t[1]]
    else:
        t[1].append(t[2])
        return t[1]

def getraisenoticesubbloque(t):
    if len(t) == 5:
        return Nodo('RAISE NOTICE', t[3], [], t.lexer.lineno)
    elif len(t) == 7:
        n1 = Nodo('ID', t[5], [], t.lexer.lineno)
        return Nodo('RAISE NOTICE', t[3], [n1], t.lexer.lineno)
    else:
        n1 = Nodo('OUTERBLOCK', t[7], [], t.lexer.lineno)
        return Nodo('RAISE NOTICE', t[3], [n1], t.lexer.lineno)

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




def getOpRelacional(t):
    if t[2] == '<>':
        gramatica = '<condicion> ::= <expresion> \"DIFERENTE\" <expresion>'
        return Nodo('OPREL', '\\<\\>', [t[1], t[3]], t.lexer.lineno, 0, gramatica)
    gramatica = '<condicion> ::= <expresion> \"' +t[2]+'\" <expresion>'
    return Nodo('OPREL', '\\'+str(t[2]), [t[1], t[3]], t.lexer.lineno, 0, gramatica)

def getValorNumerico(t):
    if isinstance(t[1], float):
        gramatica = '<cualquiernumero> ::= \"'+str(t[1])+'\"'
        return Nodo('DECIMAL', str(t[1]), [], t.lexer.lineno, 0, gramatica)     
    else:
        gramatica = '<cualquiernumero> ::= \"'+str(t[1])+'\"'
        return Nodo('ENTERO', str(t[1]), [], t.lexer.lineno, 0, gramatica)

def getIdentificador(t):
    if len(t) == 2:
        gramatica = '<cualquieridentificador> ::= \"'+str(t[1])+'\"'
        return Nodo('ID', t[1], [], t.lexer.lineno,0, gramatica)
    else :
        gramatica = '<cualquieridentificador> ::= \"'+str(t[1])+'\" \"PUNTO\" \"'+str(t[3])+'\"'
        childs = [Nodo('ID', t[3], [], t.lexer.lineno)]
        return Nodo('AliasTabla', t[1], childs, t.lexer.lineno, 0, gramatica)

def getFuncionMatematica(t):
    if len(t) == 4:
        gramatica = '<funcion_matematica_s> ::= \"'+str(t[1])+'\" \"PARIZQ\" \"PARDER\"'
        return Nodo('Matematica', 'Pi', [], t.lexer.lineno, 0, gramatica)
    elif len(t) == 5:
        gramatica = '<funcion_matematica_s> ::= \"'+str(t[1])+'\" \"PARIZQ\" <expresionaritmetica> \"PARDER\"'
        return Nodo('Matematica', t[1], [t[3]], t.lexer.lineno, 0, gramatica)
    else :
        gramatica = '<funcion_matematica_s> ::= \"'+str(t[1])+'\" \"PARIZQ\" <expresionaritmetica> \"COMA\" <expresionaritmetica>\"PARDER\"'
        return Nodo('Matematica', t[1], [t[3], t[5]], t.lexer.lineno, 0, gramatica)


def getAlias(t):
    if t[1] == None:
        return t[1]
    elif t[1].lower() == 'as':
        gramatica = '<alias> ::= \"AS\" \"' + str(t[2]) + '\"'
        return Nodo('Alias', t[2], [], t.lexer.lineno, 0, gramatica)
    else :
        gramatica = '<alias> ::= \"'+ str(t[1]) + '\"'
        return Nodo('Alias', t[1], [], t.lexer.lineno, 0, gramatica)

def getStringFunctionNode2(t):
    if len(t) == 9:
        return Nodo('Binaria',t[1],[t[3], t[5], t[7]],t.lexer.lineno)
    else:
         return Nodo('Binaria','TRIM',[t[3]],t.lexer.lineno)

