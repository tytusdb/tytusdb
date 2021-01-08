from ply import *
from LexRecolectorC3D import *
from C3D import *
from OptimizadorMirilla import *

lista_lexicos = lista_errores_lexico

#Asociación de operacion y presedencia
precedence = (
    ('left', 'ESIGUAL', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL', 'DIFERENTE'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'POTENCIA'),
    ('left', 'POR', 'DIVISION'),
    ('right', 'UMENOS')
)

def p_init(t):
    'init   : instrucciones'
    primeraPasada = OptMirilla(t[1], [])
    segundaPasada = OptMirilla(primeraPasada.ListaOptimizada, primeraPasada.reporteOptimizado)
    lensegunda = len(segundaPasada.reporteOptimizado)
    for l in range(0, lensegunda):
        primeraPasada = OptMirilla(segundaPasada.ListaOptimizada, segundaPasada.reporteOptimizado)
        segundaPasada = OptMirilla(primeraPasada.ListaOptimizada, primeraPasada.reporteOptimizado)
        lensegunda = len(segundaPasada.reporteOptimizado)
    segundaPasada.generarReporte()
    t[0] = segundaPasada.GenerarCodigo3D(segundaPasada.ListaOptimizada)

def p_instrucciones(t):
    'instrucciones  : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones2(t):
    'instrucciones  : instruccion'
    t[0] = [t[1]]

def p_instruccion_asignacion(t):
    'instruccion    : ID IGUAL valor'
    t[0] = Asignacion(Identificador(t[1]), t[3])

def p_instruccion_asignacion_listaPosicion(t):
    'instruccion    : ID CORIZQ ID CORDER IGUAL valor'
    t[0] = Asignacion(ListaPosicion(Identificador(t[1]), Identificador(t[3])), t[6])

def p_isntruccion_llamFuncion(t):
    'instruccion    : ID PARIZQ PARDER'
    t[0] = LlamFuncion(Identificador(t[1]))

def p_instruccion_if(t):
    'instruccion    : IF condicion GOTO ID'
    t[0] = SentenciaIF(t[2], Identificador(t[4]))

def p_instruccion_goto(t):
    'instruccion    : GOTO ID'
    t[0] = Goto(Identificador(t[2]))

def p_instruccion_etiqueta(t):
    'instruccion    : ID DOS_PUNTOS'
    t[0] = Etiqueta(Identificador(t[1]))

def p_valor_operacion_suma(t):
    'valor  : valorOp SUMA valorOp'
    t[0] = Operacion(t[1], t[3], OP_ARITMETICO.SUMA)

def p_valor_operacion_resta(t):
    'valor  : valorOp RESTA valorOp'
    t[0] = Operacion(t[1], t[3], OP_ARITMETICO.RESTA)

def p_valor_operacion_multiplicacion(t):
    'valor  : valorOp POR valorOp'
    t[0] = Operacion(t[1], t[3], OP_ARITMETICO.MULTIPLICACION)

def p_valor_operacion_division(t):
    'valor  : valorOp DIVISION valorOp'
    t[0] = Operacion(t[1], t[3], OP_ARITMETICO.DIVISION)

def p_valor_operacion_potencia(t):
    'valor  : valorOp POTENCIA valorOp'
    t[0] = Operacion(t[1], t[3], OP_ARITMETICO.POTENCIA)

def p_valor_Condicion(t):
    'valor  : condicion'
    t[0] = t[1]

def p_valor_valorOp(t):
    'valor  : valorOp'
    t[0] = t[1]

def p_valor_menos(t):
    'valor      : RESTA valorOp %prec UMENOS'

def p_valorOp_valor_cadena(t):
    'valorOp    : CADENA'
    t[0] = Valor(t[1], 'CADENA')

def p_valorOp_valor_entero(t):
    'valorOp    : ENTERO'
    t[0] = Valor(t[1], 'ENTERO')

def p_valorOp_valor_decimal(t):
    'valorOp    : DECIMAL'
    t[0] = Valor(t[1], 'DECIMAL')

def p_valorOp_valor_caracter(t):
    'valorOp    : CARACTER'
    t[0] = Valor(t[1], 'CARACTER')

def p_valorOp_valor_id(t):
    'valorOp    : ID'
    t[0] = Identificador(t[1])

def p_valorOp_valor_true_false(t):
    '''valorOp      : TRUE
                    | FALSE'''
    t[0] = Valor(t[1], 'BOOLEAN')

def p_valorOp_valor_lista(t):
    '''valorOp  : CORIZQ valorOp CORDER'''
    t[0] = ValorLista(t[2])

def p_condicion_mayor(t):
    'condicion  : valorOp MAYOR valorOp'
    t[0] = Condicion(t[1], t[3], OP_RELACIONAL.MAYOR_QUE)

def p_condicion_menor(t):
    'condicion  : valorOp MENOR valorOp'
    t[0] = Condicion(t[1], t[3], OP_RELACIONAL.MENOR_QUE)

def p_condicion_mayorigual(t):
    'condicion  : valorOp MAYORIGUAL valorOp'
    t[0] = Condicion(t[1], t[3], OP_RELACIONAL.MAYOR_IGUAL_QUE)

def p_condicion_menorigual(t):
    'condicion  : valorOp MENORIGUAL valorOp'
    t[0] = Condicion(t[1], t[3], OP_RELACIONAL.MENOR_IGUAL_QUE)

def p_condicion_igual(t):
    'condicion  : valorOp ESIGUAL valorOp'
    t[0] = Condicion(t[1], t[3], OP_RELACIONAL.IGUAL)

def p_condicion_diferente(t):
    'condicion  : valorOp DIFERENTE valorOp'
    t[0] = Condicion(t[1], t[3], OP_RELACIONAL.DIFERENTE)

def find_column(input,token):
    last_cr = str(input).rfind('\n',0,token.lexpos)
    if last_cr < 0:
	    ast_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

def p_error(p):
    if not p:
        print("Fin del Archivo!")
        return
    print(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {p.value}", p.lexer.lineno, find_column(lexer.lexdata,p))
    while True:
        
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'PUNTO_COMA':
            if not tok:
                print("FIN DEL ARCHIVO")
                return
            else:
                print("Se recupero con ;")
                break
        print(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {tok.value}", p.lexer.lineno, find_column(lexer.lexdata,tok))
        
    parser.restart()

parser = yacc.yacc()

def ejecutarEscaneo(texto):
    columna = 0
    lexer.lineno= 0
    return parser.parse(texto)