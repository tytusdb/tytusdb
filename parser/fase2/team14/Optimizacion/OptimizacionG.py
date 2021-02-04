from Optimizacion.Etiqueta import Etiqueta
from Optimizacion.CondicionIF import CondicionIF
from Optimizacion.Asignacion import Asignacion
reservadas = {
    'goto':'gotos',
    'print':'print',
    'label':'label',
    'import':'import',
    'with_goto':'with_goto',
    'from': 'r_from',
    'not': 'not',
    'null': 'null',
    'or': 'or',
    'if': 'if',
    'true': 'true',
    'false': 'false',
    'and': 'and',
    'as': 'as',
    'returns': 'returns',
    'return': 'return',
    'function': 'function'

}

tokens = [
             'mas',
             'menos',
             'elevado',
             'multiplicacion',
             'division',
             'modulo',
             'menor',
             'mayor',
             'igual',
             'menor_igual',
             'mayor_igual',
             'diferente1',
             'diferente2',
             'ptcoma',
             'para',
             'coma',
             'int',
             'decimales',
             'cadena',
             'cadenaString',
             'parc',
             'id',
             'idPunto',
             'dospuntos',
             'dolarn',
             'punto',
             'corchetea',
             'corchetec',
             'arroba',
             'igual_igual'
             #'tabulador',
             #'nueval'
 
         ] + list(reservadas.values())

# Tokens
t_mas = r'\+'
t_menos = r'\-'
t_elevado = r'\^'
t_multiplicacion = r'\*'
t_division = r'/'
t_modulo = r'%'
t_menor = r'<'
t_mayor = r'>'
t_igual = r'='
t_menor_igual = r'<='
t_mayor_igual = r'>='
t_diferente1 = r'<>'
t_diferente2 = r'!='
t_para = r'\('
t_parc = r'\)'
t_ptcoma = r';'
t_coma = r','
t_dospuntos = r':'
t_punto=r'\.'
t_corchetea=r'\['
t_corchetec=r']'
t_arroba=r'\@'
t_igual_igual=r'=='
#t_tabulador = r'\t+'
#t_nueval=r'\n+'


def t_decimales(t):
    r'\d+\.\d+([e][+-]\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error no se puede convertir %d", t.value)
        t.value = 0
    return t


def t_int(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
        t.value = 0
    return t


def t_PUNTOPUNTO(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*\.([a-zA-Z_][a-zA-Z_0-9]*|\*)'
    t.type = reservadas.get(t.value.lower(), 'idPunto')
    return t


def t_DOLARN(t):
    r'[$]\d+ | [$][$]'
    t.type = reservadas.get(t.value.lower(), 'dolarn')
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'id')
    return t


def t_cadena(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


def t_cadenaString(t):
    r'".*?"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*/*([^\*/]|[^\*]/|\*[^/])*\**\*/'
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
    #print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as analizador_lexico

lexer = analizador_lexico.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left', 'or'),
    ('left', 'and'),
    ('right', 'not'),
    ('left', 'mayor', 'menor', 'mayor_igual', 'menor_igual', 'igual_igual', 'diferente1', 'diferente2'),
    ('left', 'mas', 'menos'),
    ('left', 'multiplicacion', 'division', 'modulo'),
    ('left', 'elevado'),
    ('right', 'umenos', 'umas'),
   

)

# ----------------------------------------------DEFINIMOS LA GRAMATICA------------------------------------------
# Definición de la gramática

def p_init(t):
    'init            : LISTACONTENIDO'
    t[0] = t[1]
    print("ok")
    return t[0]


def p_LISTACONTENIDO(t):
    'LISTACONTENIDO : LISTACONTENIDO CONTENIDO'
    t[1].append(t[2])
    t[0] = t[1]


def p_LISTACONTENIDO1(t):
    'LISTACONTENIDO : CONTENIDO'
  
    t[0] = [t[1]]



def p_CONTENIDO1(t):
    '''CONTENIDO :  ETIQUETA 
    '''
    t[0] = t[1]

def p_CONTENIDO2(t):
    '''CONTENIDO :  SALTO 
    '''
    t[0] = t[1]

def p_CONTENIDO3(t):
    '''CONTENIDO : IMPORTACIONES 
    '''
    t[0] = t[1]

def p_CONTENIDO4(t):
    '''CONTENIDO : METODOS 
    '''
    t[0] = t[1]

def p_CONTENIDO5(t):
    '''CONTENIDO :  ASIGNACION 
    '''
    t[0] = t[1]

def p_CONTENIDO6(t):
    '''CONTENIDO :  CONDICIONIF 
    '''
    t[0] = t[1]

def p_CONTENIDO7(t):
    '''CONTENIDO :  PRINTF 
    '''
    t[0] = t[1]

'''def p_CONTENIDO8(t):
    CONTENIDO : nueval
            | tabulador
    t[0] = t[1]'''


def p_PRINTF(t):
    ''' PRINTF : print para EXP parc
    '''
    print("PRINTF")

def p_IF(t):
    ''' CONDICIONIF : if OPERACION dospuntos  SALTO 
    '''
    vector=t[2]
    #t[0]=CondicionIF(vector[0],vector[1],vector[2],t[5],t[6],t.lexer.lineno).Optimizar()
    print("IFS")

def p_IF2(t):
    ''' CONDICIONIF : if EXP dospuntos   SALTO 
    '''

    #t[0]=CondicionIF(t[2],'','',t[5],t[6],t.lexer.lineno).Optimizar()
    print("IFS")

def p_ASIGNACION(t):
    '''ASIGNACION : id  igual OPERACION 
    '''
    vector=t[3]
    t[0]=Asignacion(t[1],vector[0],vector[1],vector[2],t.lexer.lineno).Optimizar()
    print("ASIGNACION OPERACION")

def p_ASIGNACION2(t):
    '''ASIGNACION : id  igual EXP 
    '''
    #t[0]=Asignacion(t[1],None,t[2],None,t.lexer.lineno).Optimizar()
def p_ASIGNACION3(t):
    '''ASIGNACION : id  igual METODOS 
    '''
    #t[0]=Asignacion(t[1],None,t[2],None,t.lexer.lineno).Optimizar()
    
    print("ASIGNACION")
def p_ASIGNACION1(t):
    '''ASIGNACION : VECTOR  igual OPERACION 
    '''
    print("ASIGNACION")

def p_metodos(t): 
    '''METODOS : id id para parc dospuntos
    ''' 
    print("METODOS")
def p_metodos1(t): 
    '''METODOS : idPunto para EXP parc 
    ''' 
    print("METODOS")
def p_metodos2(t): 
    '''METODOS : id para EXP parc 
    ''' 
    print("METODOS")
def p_metodos3(t): 
    '''METODOS : id para parc 
    ''' 
    print("METODOS")

def p_importaciones(t):
    '''IMPORTACIONES : r_from idPunto import id  
                       | import idPunto  as id  
                       | import idPunto   id 
                       | r_from id import id  
                       | import id  as id  
                       | import id   id 
                       | r_from idPunto import multiplicacion
                       | r_from id import multiplicacion
                       | r_from gotos import with_goto
                       | arroba with_goto
    '''

def p_SALTO(t): 
    ''' SALTO : gotos punto id 
    '''
    t[0]=t[1]+t[3]

def p_ETIQUETA (t): 
    '''ETIQUETA : label  punto id 
    '''

    #t[0]= Etiqueta(t[2]+t[3],t.lexer.lineno).Optimizar()

  
def p_VECTOR (t): 
    '''VECTOR : id  corchetea EXP corchetec 
    '''
    t[0]=t[1]+'['+str(t[3])+']'
def p_VECTOR1 (t): 
    '''VECTOR : id  corchetea  corchetec 
    '''
    t[0]=t[1]+'[]'



def p_EXP3(t):
    '''OPERACION : EXP mas EXP 
            | EXP menos EXP 
            | EXP multiplicacion EXP
            | EXP division EXP 
            | EXP modulo EXP
            | EXP elevado EXP
            | EXP and EXP 
            | EXP or EXP 
            | EXP mayor EXP 
            | EXP menor EXP 
            | id igual_igual EXP 
            | EXP mayor_igual EXP 
            | EXP menor_igual EXP 
            | EXP diferente1 EXP
            | EXP diferente2 EXP 
            | corchetea EXP corchetec 
            | corchetea corchetec
            | VECTOR
    '''
    if(len(t)== 4):
        vector=[]
        vector.append(str(t[1]))
        vector.append(str(t[2]))
        vector.append(str(t[3]))
        t[0]=vector
    elif(len(t)==3):
        vector=[]
        vector.append(str(t[1]))
        vector.append(str(t[2]))
        vector.append('')
        
        t[0]=vector
    else:
        vector=[]
        vector.append('[')
        vector.append('')
        vector.append('')
        t[0]=vector
        


def p_EXP1(t):
    '''EXP : mas EXP %prec umas
            | menos EXP %prec umenos
            | not EXP
    '''
    t[0]=str(t[1]+str(t[2]))


def p_EXPT1(t):
    'EXP : int'
    t[0]=str(t[1])




def p_EXPT2(t):
    'EXP : decimales'
    t[0]=str(t[1])

  

def p_EXPT3(t):
    'EXP : cadena'
    t[0]=str(t[1])




def p_EXPT4(t):
    'EXP : cadenaString'
    t[0]=str(t[1])



def p_EXPT7(t):
    'EXP : id'
    t[0]=str(t[1])

def p_EXPT9(t):
    'EXP : null'
    t[0]=str(t[1])



def p_EXPT17(t):
    'EXP : idPunto'
    t[0]=str(t[1])



def p_error(t):
    ''
    print(t)
    print("Error sintáctico en '%s'" % t.value)
   
import ply.yacc as analizador_sintactico

par = analizador_sintactico.yacc()


def lexico(input):
    return par.parse(input)

