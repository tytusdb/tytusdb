from Tokens import *

# Construccion del analizador léxico
import ply.lex as lex

lexer = lex.lex()

# Test it out
data = """
\\t
"""

# Give the lexer some input
lexer.input(data)

# Tokenize
f = open("test.txt", "w")
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    # print(tok)
    f.write(str(tok) + "\n")
f.close()