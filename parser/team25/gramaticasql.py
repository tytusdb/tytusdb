from lexicosql import  tokens

#_______________________________________________________________________________________________________________________________
#                                                          PARSER
#_______________________________________________________________________________________________________________________________

#---------------- MANEJO DE LA PRECEDENCIA
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','IGUAL', 'DIFERENTE'),
    ('left','MENOR','MAYOR','MENORIGUAL','MAYORIGUAL'),
    ('left','OR'),
    ('left','MAS', 'MENOS'),
    ('left','ASTERISCO','DIVISION','AND','OR'),
    ('left','XOR','MODULO'),
    ('right','UMENOS','NOT'), #,'UMAS'
) 

def p_init(p):
    'init : instrucciones'
    p[0] = [p[1]]
    
def p_instrucciones_list(p):
    '''instrucciones    : instrucciones instruccion '''
    p[1].append(p[2])
    p[0] = p[1]

def p_instrucciones_instruccion(p):
    'instrucciones  :   instruccion'
    p[0] = [p[1]]

def p_instruccion(p):
    '''instruccion :  sentenciaUpdate PTCOMA 
                    | sentenciaDelete PTCOMA
                    | sentenciaInsert PTCOMA'''
    p[0] = p[1]
#__________________________________________update  
def p_update(p):
    '''sentenciaUpdate : UPDATE ID SET lista_asignaciones WHERE expresion 
                       | UPDATE ID SET lista_asignaciones '''
    if (len(p) == 6) :
        print('update LARGO')
        p[0] = p[1]
    else:
        print('update CORTO')
        p[0] = p[1]
 #__________________________________________INSERT
 
def p_sentenciaInsert(p):
    ''' sentenciaInsert : INSERT INTO ID parametros VALUES parametros'''
    p[0] = p[1] 
#___________________________________________PARAMETROS
def p_parametros(p):
    ''' parametros : PABRE lista_ids  PCIERRA'''
    p[0] = p[1]   
#__________________________________________lista ids
def p_lista_ids(p):
    ''' lista_ids : lista_ids COMA  ID
                  | ID '''
                  
    if (len(p) == 3):
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

#__________________________________________DELETE 
def p_sentenciaDelete(p):
    ''' sentenciaDelete : DELETE FROM ID WHERE expresion
                        | DELETE FROM ID '''
    p[0] = p[1] 
  
                      

#___________________________________________ASIGNACION____________________________________

def p_lista_asignaciones(p):
    '''lista_asignaciones : lista_asignaciones COMA asignacion
                          | asignacion'''
    if (len(p) == 3) :
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_asignacion(p):
    ''' asignacion : ID IGUAL expresion'''
    print('asignacion de campo') 
    p[0] = p[1]
    


#______________________________________________EXPRESION_______________________________


def p_expresiones_unarias(p):
    ''' expresion : MENOS expresion %prec UMENOS 
                  | NOT expresion '''
    print('expresion: '+str(p[1]) +'.'+str(p[3])) # solo para ver que viene
    p[0] = p[2]
    
def p_expreion_entre_parentesis(p):
    'expresion : PABRE expresion  PCIERRA' 
    p[0] = p[2]
    
def p_expresion_cadena(p):
    'expresion : CADENA '
    p[0] = p[1]

def p_expresion_id(p):
    'expresion : ID'
    p[0] =p[1]
    
def p_expresion_numero(p):
    'expresion : NUMERO'
    p[0] = p[1]
    
def p_expresion_decimal(p):
    'expresion : DECIMAL'
    p[0] = p[1]

def p_expresion_tabla_campo(p):
    'expresion : ID PUNTO ID'
    print('expresion: '+str(p[1]) +'.'+str(p[3])) # solo para ver que viene
    p[0] = p[1]
            
def p_expresion_con_dos_nodos(p):
    '''expresion : expresion MAS expresion 
                 | expresion MENOS expresion
                 | expresion ASTERISCO expresion
                 | expresion DIVISION expresion 
                 | expresion MAYOR expresion 
                 | expresion MENOR expresion
                 | expresion MAYORIGUAL expresion
                 | expresion MENORIGUAL expresion
                 | expresion DIFERENTE expresion
                 | expresion IGUAL expresion
                 | expresion XOR expresion
                 | expresion MODULO expresion
                 | expresion OR expresion
                 | expresion AND expresion

                 '''
    print('expresion:'+str(p[1])+str(p[2])+str(p[3])) # solo para ver que viene
    if p[2] == '+':  p[0] = p[1]+p[2]
    elif p[2] == '-': p[0] = p[1]-p[2]
    elif p[2] == '*': p[0] = p[1]*p[2]
    elif p[2] == '/': p[0] = p[1]/p[2]
    elif p[2] == '>': print('mayor')
    elif p[2] == '<': print('menor')
    elif p[2] == '>=': print('MAYOR_igual')
    elif p[2] == '<=': print('menor_igual')
    elif p[2] == '^': print('POTENCIA o CIRCUNFLEJO')
    elif p[2] == '%': print('modulo')
    elif p[2] == '=': print('igual')
    elif p[2] == '<>': print('distino')

def p_error(p):
    print(p)
    print("Error sintáctico en '%s'" % p.value)

import ply.yacc as yacc
parser = yacc.yacc()

def analizarEntrada(entrada):
    return parser.parse(entrada)


# print(analizarEntrada('''
                      
# update tabla set campo = id ;

#                       '''))





# FUNCIONES NATIVAS:
#  count, sum, avg (average), max (maximum) and min (minimum)
# abs, cbrt, ceil, ceiling, degrees, div, exp, factorial, floor, gcd, lcm, ln, log, log10, min_scale, mod, pi, power, radians, round, scale, sign, sqrt, trim_scale, truc, width_bucket, random, setseed
# acos, acosd, asin, asind, atan, atand, atan2, atan2d, cos, cosd, cot, cotd, sin, sind, tan, tand, sinh, cosh, tanh, asinh, acosh, atanh
# ||, length, substring, trim, get_byte, md5, set_byte, sha256, substr, convert, encode, decode
# GREATEST(value [, ...])
# LEAST(value [, ...])