
# -----------------------------------------------------------------------------
# Rainman Sián
# 26-02-2020
#
# Ejemplo interprete sencillo con Python utilizando ply en Ubuntu
# -----------------------------------------------------------------------------
reporte_optimizar = []
respuesta = []
pila = []
bandera1=[False,'',False]
reservadas = {
    'def' : 'DEF',
    'import' : 'IMPORT',
    'from' : 'FROM',
    'goto' : 'GOTO',
    'with_goto' : 'WITH_GOTO',
    'if' : 'IF',
    'label' : 'LABEL'
}

tokens  = [
    'PTCOMA',
    'ARROBA',
    'LLAVIZQ',
    'LLAVDER',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'CONCAT',
    'MENQUE',
    'MAYQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'DOSPT',
    'ID',
    'PUNTO'
] + list(reservadas.values())

# Tokens
t_DOSPT    = r':'
t_PTCOMA    = r';'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_CONCAT    = r'&'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_IGUALQUE  = r'=='
t_NIGUALQUE = r'!='
t_ARROBA    = r'@'
t_PUNTO     = r'.'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import Optimizador.ply.lex as lex
lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left','CONCAT'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

# Definición de la gramática



def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_fromfoto(t): 
    '''instruccion      :  import '''
    t[0]=t[1]
def p_instruccion(t) :
    '''import      : import_instr
                        | definicion_instr
                        | asignacion_instr
                        | fromS
                        | arrobas 
                        | llamada 
                        | ifI
                        | gotoI 
                        | labels'''    

    t[0] = t[1]

    if bandera1[0] :
        reglas(pila)
        #if  (reglas(pila)==False):
            #respuesta.append(bandera1[1])
    elif bandera1[2]:
        respuesta.append(bandera1[1])
        bandera1[2]=False
        bandera1[1]=''

    bandera1[0]=False
    pila.clear()

def p_from(t) :
    ''' fromS     : FROM GOTO IMPORT WITH_GOTO  '''
    respuesta.append(str(t[1])+' '+str(t[2])+' '+str(t[3])+' '+str(t[4])+'\n')
    t[0]=t[1]

def p_arroba(t) :
    ''' arrobas     : ARROBA WITH_GOTO '''
    respuesta.append(str(t[1])+str(t[2])+'\n')
    t[0]=t[1]

def p_funciones(t) :
    ''' llamada     : ID PARIZQ PARDER  '''
    if t[1]=='main':
        respuesta.append(str(t[1])+' '+str(t[2])+str(t[3])+'\n')
    else:
        respuesta.append('    '+str(t[1])+str(t[2])+str(t[3])+'\n')
    t[0]=t[1]

def p_funciones_aux(t) :
    ''' llamada     : ID PUNTO ID PARIZQ PARDER  '''
    respuesta.append('    '+str(t[1])+str(t[2])+str(t[3])+str(t[4])+str(t[5])+'\n')
    t[0]=t[3]

def p_ifS(t) :
    ''' ifI         : IF expression  DOSPT GOTO   PUNTO ID'''
    respuesta.append('\n    '+str(t[1])+' '+str(t[2])+' '+str(t[3])+' '+str(t[4])+' '+str(t[5])+str(t[6])+'\n')
    t[0]=t[1]

def p_gotoS(t) :
    ''' gotoI       : GOTO   PUNTO ID'''
    respuesta.append('\n    '+str(t[1])+' '+str(t[2])+str(t[3])+'\n')
    t[0]=t[1]

def p_labelS(t) :
    ''' labels       : LABEL   PUNTO ID'''
    respuesta.append('\n    '+str(t[1])+' '+str(t[2])+str(t[3])+'\n')
    t[0]=t[1]


def p_instruccion_import(t) :
    'import_instr     : IMPORT ID '
    respuesta.append(str(t[1])+' '+str(t[2])+'\n')
    t[0] = []

def p_instruccion_definicion(t) :
    'definicion_instr   : DEF ID PARIZQ PARDER DOSPT'
    respuesta.append(str(t[1])+' '+str(t[2])+str(t[3])+str(t[4])+' '+str(t[5])+'\n')
    t[0] = []

def p_asignacion_instr(t) :
    'asignacion_instr   : ID IGUAL expression '
    pila.append(t[2])
    pila.append(t[1])
    t[0]=t[1]
    bandera1[1] = ('\n    '+str(t[1])+' '+str(t[2])+' '+str(t[3])+'\n')
    bandera1[2]=True
    #respuesta.append(+'\t'+str(t[1])+' '+str(t[2]))

def p_asignacion_instr_aux(t) :
    'asignacion_instr   : ID PUNTO ID IGUAL expression '
    respuesta.append('    '+str(t[1])+str(t[2])+str(t[3])+' '+str(t[4])+' '+str(t[5])+'\n')
    t[0] = t[3]

def p_expresion_binaria(t):
    '''expression : expression MAS expression
                        | expression MENOS expression
                        | expression POR expression
                        | expression DIVIDIDO expression'''
    if t[2] == '+'  : 
        bandera1[0]=True
        pila.append(t[2])
        t[0] = (str(t[1])+str(t[2])+str(t[3]))
    elif t[2] == '-': 
        bandera1[0]=True
        pila.append(t[2])
        t[0] = (str(t[1])+str(t[2])+str(t[3]))
    elif t[2] == '*': 
        bandera1[0]=True
        pila.append(t[2])
        t[0] = (str(t[1])+str(t[2])+str(t[3]))
    elif t[2] == '/': 
        bandera1[0]=True
        pila.append(t[2])
        t[0] = (str(t[1])+str(t[2])+str(t[3]))

def p_expresion_binaria_aux(t):
    '''expression : expression MENQUE expression
                        | expression MAYQUE expression
                        | expression IGUALQUE expression'''
    if t[2] == '<': 
        bandera1[0]=True
        pila.append(t[2])
        t[0] = (str(t[1])+str(t[2])+str(t[3]))
    elif t[2] == '>': 
        bandera1[0]=True
        pila.append(t[2])
        t[0] = (str(t[1])+str(t[2])+str(t[3]))
    elif t[2] == '==': 
        bandera1[0]=True
        pila.append(t[2])
        t[0] = (str(t[1])+str(t[2])+str(t[3]))

def p_expresion_unaria(t):
    'expression : MENOS expression %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])

def p_expresion_agrupacion(t):
    'expression : PARIZQ expression PARDER'
    
    t[0] = (' '+str(t[1])+str(t[2])+str(t[3])+' ')

def p_expresion_number(t):
    '''expression : ENTERO
                        | DECIMAL
                        | CADENA'''
    pila.append(t[1])
    t[0] = (t[1])

def p_expresion_id(t):
    'expression   : ID'
    pila.append(t[1])
    t[0] = (t[1])

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import Optimizador.ply.yacc as yacc
parser = yacc.yacc()

def reglas(auxP):
    try:
        izquierda = auxP[0]
        derecha = auxP[1]
        operador = auxP[2]
        igual = auxP[3]
        idP = auxP[4]
        
        if str(operador)=='+' :
            if str(derecha) == '0' :            
                if (str(izquierda)!=str(idP)):  # REGLA 12
                    respuesta.append('\n    '+str(idP)+' = '+str(izquierda))
                    reporte_optimizar.append(["Regla 12", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , str(idP)+' = '+str(izquierda)])
                    return True
                elif (str(izquierda)==str(idP)):    # REGLA 8
                    reporte_optimizar.append(["Regla 8", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , "Se elimina"])
                    return True
            
        elif str(operador) == '-' :
            if str(derecha) == '0' :
                if (str(izquierda)!=str(idP)):  # REGLA 13
                    respuesta.append('\n    '+str(idP)+' = '+str(izquierda))
                    reporte_optimizar.append(["Regla 13", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , str(idP)+' = '+str(izquierda)])
                    return True
                elif (str(izquierda)==str(idP)):    # REGLA 9
                    reporte_optimizar.append(["Regla 9", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , "Se elimina"])
                    return True
        elif str(operador) == '*' :
            if str(derecha) == '1' :
                if (str(izquierda)!=str(idP)):  # REGLA 14
                    respuesta.append('\n    '+str(idP)+' = '+str(izquierda))
                    reporte_optimizar.append(["Regla 14", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , str(idP)+' = '+str(izquierda)])
                    return True
                elif (str(izquierda)==str(idP)):    # REGLA 10
                    reporte_optimizar.append(["Regla 10", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , "Se elimina"])
                    return True
            elif str(derecha) == '0':   # REGLA 17
                respuesta.append('\n    '+str(idP)+' = 0')
                reporte_optimizar.append(["Regla 17", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , str(idP)+' = 0'])
                return True
            elif str(derecha) == '2' :  # REGLA 16
                respuesta.append('\n    ' + str(idP) + ' = ' + str(izquierda) + ' + ' + str(izquierda))
                reporte_optimizar.append(["Regla 16", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , str(idP) + ' = ' + str(izquierda) + ' + ' + str(izquierda)])
                return True
        elif str(operador) == '/' :
            if str(derecha) == '1' :
                if (str(izquierda)!=str(idP)):  # REGLA 15
                    respuesta.append('\n    '+str(idP)+' = '+str(izquierda))
                    reporte_optimizar.append(["Regla 15", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , str(idP)+' = '+str(izquierda)])
                    return True
                elif (str(izquierda)==str(idP)):    # REGLA 11
                    reporte_optimizar.append(["Regla 11", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , "Se elimina"])
                    return True
            elif str(izquierda) == '0' :    # REGLA 18
                respuesta.append('\n    '+str(idP)+' = 0')
                reporte_optimizar.append(["Regla 18", str(idP) + " = " + str(izquierda) + str(operador) + str(derecha) , str(idP)+' = 0'])
                return True
        respuesta.append('\n    '+str(idP) + ' = ' + str(izquierda) + str(operador) + str(derecha))
        return True
    except:
        return False
    

def parse(input) :
    return parser.parse(input)
