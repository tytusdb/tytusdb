"""
  Tipos Numericos reservados del lenguaje SQL 'T_'
"""
r_types = {
    "SMALLINT": "T_SMALLINT",
    "INTEGER": "T_INTEGER",
    "BIGINT": "T_BIGINT",
    "DECIMAL": "T_DECIMAL",
    "NUMERIC": "T_NUMERIC",
    "REAL": "T_REAL",
    "DOUBLE": "T_DOUBLE",
    "PRECISION": "T_PRECISION",
    "MONEY": "T_MONEY",
    "CHARACTER": "T_CHARACTER",
    "VARYING": "T_VARYING",
    "VARCHAR": "T_VARCHAR",
    "CHAR": "T_CHAR",
    "TEXT": "T_TEXT",
    "DATE": "T_DATE",
    "TIME": "T_TIME",
    "BOOLEAN": "T_BOOLEAN",
}

"""
  Palabras reservadas del lenguaje SQL 'R_'
"""
reservadas = {
    "CREATE": "R_CREATE",
    "REPLACE": "R_REPLACE",
    "TABLE": "R_TABLE",
    "DATABASE": "R_DATABASE",
    "TYPE": "R_TYPE",
    "AS": "R_AS",
    "ENUM": "R_ENUM",
    "INHERITS": "R_INHERITS",
    "IF": "R_IF",
    "EXISTS": "R_EXISTS",
    "CHECK": "R_CHECK",
    "UNIQUE": "R_UNIQUE",
    "KEY": "R_KEY",
    "PRIMARY": "R_PRIMARY",
    "FOREIGN": "R_FOREIGN",
    "REFERENCES": "R_REFERENCES",
    "CONSTRAINT": "R_CONSTRAINT",
    "DEFAULT": "R_DEFAULT",
    "NULL": "R_NULL",
    "NULLS": "R_NULLS",
    "OWNER": "R_OWNER",
    "MODE": "R_MODE",
    "ALTER": "R_ALTER",
    "RENAME": "R_RENAME",
    "TO": "R_TO",
    "CURRENT_USER": "R_CURRENT_USER",
    "SESSION_USER": "R_SESSION_USER",
    "ADD": "R_ADD",
    "DROP": "R_DROP",
    "COLUMN": "R_COLUMN",
    "SELECT": "R_SELECT",
    "DISTINCT": "R_DISTINCT",
    "UNION": "R_UNION",
    "INTERSECT": "R_INTERSECT",
    "EXCEPT": "R_EXCEPT",
    "EXTRACT": "R_EXTRACT",
    "FROM": "R_FROM",
    "TIMESTAMP": "R_TIMESTAMP",
    "INTERVAL": "R_INTERVAL",
    "YEAR": "R_YEAR",
    "MONTH": "R_MONTH",
    "DAY": "R_DAY",
    "HOUR": "R_HOUR",
    "MINUTE": "R_MINUTE",
    "SECOND": "R_SECOND",
    "DATE_PART": "R_DATE_PART",
    "NOW": "R_NOW",
    "CURRENT_DATE": "R_CURRENT_DATE",
    "CURRENT_TIME": "R_CURRENT_TIME",
    "BETWEEN": "R_BETWEEN",
    "NOT": "R_NOT",
    "AND": "R_AND",
    "OR": "R_OR",
    "SYMMETRIC": "R_SYMMETRIC",
    "IS": "R_IS",
    "ISNULL": "R_ISNULL",
    "NOTNULL": "R_NOTNULL",
    "TRUE": "R_TRUE",
    "FALSE": "R_FALSE",
    "UNKNOWN": "R_UNKNOWN",
    "LIKE": "R_LIKE",
    "ALL": "R_ALL",
    "ANY": "R_ANY",
    "SOME": "R_SOME",
    "IN": "R_IN",
    "JOIN": "R_JOIN",
    "ON": "R_ON",
    "USING": "R_USING",
    "NATURAL": "R_NATURAL",
    "INNER": "R_INNER",
    "LEFT": "R_LEFT",
    "OUTER": "R_OUTER",
    "RIGHT": "R_RIGHT",
    "FULL": "R_FULL",
    "WHERE": "R_WHERE",
    "GROUP": "R_GROUP",
    "BY": "R_BY",
    "HAVING": "R_HAVING",
    "ORDER": "R_ORDER",
    "ASC": "R_ASC",
    "DESC": "R_DESC",
    "FIRST": "R_FIRST",
    "LAST": "R_LAST",
    "OFFSET": "R_OFFSET",
    "LIMIT": "R_LIMIT",
    "INSERT": "R_INSERT",
    "INTO": "R_INTO",
    "VALUES": "R_VALUES",
    "UPDATE": "R_UPDATE",
    "SET": "R_SET",
    "DELETE": "R_DELETE",
    "TRUNCATE": "R_TRUNCATE",
    "SHOW": "R_SHOW",
    "DATABASES": "R_DATABASES",
    "USE": "R_USE",
    "SUM": "R_SUM",
    "PROM": "R_PROM",
    "COUNT": "R_COUNT",
    "CASE": "R_CASE",
    "WHEN": "R_WHEN",
    "THEN": "R_THEN",
    "ELSE": "R_ELSE",
    "END": "R_END",
    "INDEX": "R_INDEX",
    "HASH": "R_HASH",
    "BTREE": "R_BTREE",
    "GIST": "R_GIST",
    "SPGIST": "R_SPGIST",
    "GIN": "R_GIN",
    "BRIN": "R_BRIN",
}

reservadas.update(r_types)

"""
  Lista de tokens a reconocer:
  'O_': Operadores
  'OL_': Operadores Logicos
  'OC_': Operadores de Cadena Binarias
  'S_': Simbolos
"""
tokens = [
    # Operadores
    "O_SUMA",
    "O_RESTA",
    "O_PRODUCTO",
    "O_DIVISION",
    "O_EXPONENTE",
    "O_MODULAR",
    # Operadores Logicos
    "OL_ESIGUAL",
    "OL_DISTINTODE",
    "OL_MAYORQUE",
    "OL_MENORQUE",
    "OL_MAYORIGUALQUE",
    "OL_MENORIGUALQUE",
    # Operadores de cadena
    "OC_CONCATENAR",
    "OC_AND",
    "OC_OR",
    "OC_XOR",
    "OC_NOT",
    "OC_SHIFTL",
    "OC_SHIFTR",
    # Simbolos
    "S_PARIZQ",
    "S_PARDER",
    "S_COMA",
    "S_PUNTOCOMA",
    "S_PUNTO",
    "S_IGUAL",
    # Tokens
    "ID",
    "DECIMAL",
    "INTEGER",
    "COMMENT",
    "STRING",
    "CHARACTER",
] + list(reservadas.values())

"""
  Reguex para el reconocimiento de los tokens
"""
t_O_SUMA = r"\+"
t_O_RESTA = r"-"
t_O_PRODUCTO = r"\*"
t_O_DIVISION = r"/"
t_O_EXPONENTE = r"\^"
t_O_MODULAR = r"%"

t_OL_DISTINTODE = r"!=|<>"
t_OL_MAYORQUE = r">"
t_OL_MENORQUE = r"<"
t_OL_MAYORIGUALQUE = r">="
t_OL_MENORIGUALQUE = r"<="

t_OC_CONCATENAR = r"\|\|"
t_OC_AND = r"&"
t_OC_OR = r"\|"
t_OC_XOR = r"\#"
t_OC_NOT = r"~"
t_OC_SHIFTL = r"<<"
t_OC_SHIFTR = r">>"

t_S_PARIZQ = r"\("
t_S_PARDER = r"\)"
t_S_COMA = r","
t_S_PUNTOCOMA = r";"
t_S_PUNTO = r"\."
t_S_IGUAL = r"="

"""
  Caracteres ignorados por el lexer
"""
t_ignore = " \t"

# Funcion para evaluar si el token reconocido es un ID
def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    # Verificamos si no es una palabra reservada
    t.type = reservadas.get(t.value.upper(), "ID")
    if t.type != "ID":
        t.value = t.value.upper()
    else:
        t.value = t.value.lower()
    return t


# Funcion para evaluar si el token reconocido es un DECIMAL
def t_DECIMAL(t):
    r"\d+\.\d+(e(-|\+)?\d+)?|\d+(e(-|\+)?\d+)"
    try:
        t.value = float(t.value)
    except ValueError:
        print("No se pudo convertir %d", t.value)
        t.value = 0
    return t


# Funcion para evaluar si el token reconocido es un INTEGER
def t_INTEGER(t):
    r"\d+"
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Funcion para evaluar si el token reconocido es un CHARACTER
def t_CHARACTER(t):
    r"(\"\\?.\"|\'\\?.\')"
    t.value = t.value[1:-1]
    return t


# Funcion para evaluar si el token reconocido es un STRING
def t_STRING(t):
    r"(\'.*?\'|\".*?\")"
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


# Funcion para evaluer si el token reconocido es un comentario
def t_COMMENT(t):
    r"\-\-(.*)\n|/\*(.|\n)*?\*/"
    t.lexer.lineno += t.value.count("\n")
    t.lexer.skip(0)


# Funcion para obsorver los enters
def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


syntax_errors = list()

# Funcion de error para el lexer
def t_error(t):
    """ print("Illegal character '%s'" % t.value[0]) """
    syntax_errors.insert(
        len(syntax_errors), ["Illegal character '%s'" % t.value[0], t.lineno]
    )
    t.lexer.skip(1)


def returnLexicalErrors():
    global syntax_errors
    temp = syntax_errors
    syntax_errors = list()
    return temp
