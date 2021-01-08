reservadas = {
    'def': 'DEF',
    'if': 'IF',
    # PROPIO
    'goto': 'GOTO',
    'label': 'LABEL',
    # ESPECIALES
    'False': 'FALSE',
    'True': 'TRUE',
    'or': 'OR',
    'and': 'AND',
    # Pass
    'pass': 'PASS'
}


tokens = [
    # LITERALES
    "ID",
    "ENTERO",
    "DECIMAL",
    "COMMENT",
    "CADENA",
    # IGUAL
    "ASIGNACION",
    # OPERADOR ARITMETICOS
    "SUMA",
    "RESTA",
    "MULTI",
    "DIV",
    "POTENCIA",
    # OPERADORES RELACIONALES
    "MAYORQUE",
    "MENORQUE",
    "IGUAL",
    "DIFERENTE",
    "IGMAYORQUE",
    "IGMENORQUE",
    # CONTENEDORES
    "PARIZQ",
    "PARDER",
    "CORIZQ",
    "CORDER",
    # PUNTUACION
    "DOSPUNTOS",
    "PUNTO",
    "COMA",
    # ESPECIALES
    "WITHGOTO",
    "ETIQUETA",
    # IGNORAR
    "IMPORTACIONES"
] + list(reservadas.values())

def t_IMPORTACIONES(t):
    r"from(.*)\n"
    t.lexer.lineno += t.value.count("\n")
    t.lexer.skip(0)
t_ETIQUETA = r"\.L\d+"
t_WITHGOTO = r"@with_goto"

# NORMAL
t_ASIGNACION = r"="
# OPERACIONES ARITMETICAS
t_POTENCIA = r"\*\*"
t_SUMA = r"\+"
t_RESTA = r"-"
t_MULTI = r"\*"
t_DIV = r"/"
# OPERACIONES RELACIONALES
t_MAYORQUE = r">"
t_MENORQUE = r"<"
t_IGMAYORQUE = r">="
t_IGMENORQUE = r"<="
t_IGUAL = r"=="
t_DIFERENTE = r"!="
# CONTENEDORES
t_PARIZQ = r"\("
t_PARDER = r"\)"
t_CORIZQ = r"\["
t_CORDER = r"\]"
# PUNTUACION
t_DOSPUNTOS = r":"
t_PUNTO = r"\."
t_COMA = r","

t_CADENA = r"(\'.*?\'|\".*?\")"


def t_DECIMAL(t):
    r"-?\d+\.\d+(e(-|\+)?\d+)?|\d+(e(-|\+)?\d+)"
    try:
        t.value = float(t.value)
    except ValueError:
        print("No se pudo convertir %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r"-?\d+"
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    # Verificamos si no es una palabra reservada
    t.type = reservadas.get(t.value, "ID")
    return t

def t_COMMENT(t):
    r"\#(.*)\n"
    t.lexer.lineno += t.value.count("\n")
    t.lexer.skip(0)

def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")

# Funcion de error para el lexer
def t_error(t):
    print("Illegal character '%s'" % t.value[0]) 
    t.lexer.skip(1)

t_ignore = " \t"

"""import ply.lex as lex

lexer = lex.lex()

#para debugger los nuevos tokens
lexer.input('''
-5 - -9
''')
while not False:
    token = lexer.token()
    if not token:
        break
    print(f'tipo: {token.type} valor: {token.value}  linea:{token.lineno} col:{token.lexpos}')"""