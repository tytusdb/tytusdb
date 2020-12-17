'''from scanner import lexer
lexer.input("1+4")
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
    print(type(tok))
'''

import grammarReview as g
from parse.errors import Error as our_error

f = open("./entrada.txt", "r")
input = f.read()
print("Input: " + input +"\n")
print("Executing AST root, please wait ...")
errors = []
instrucciones = g.toParse(input)

for instruccion in instrucciones:
    try:
        val = instruccion.execute(None,None)
        print("AST excute result: ", val)
    except our_error as named_error:
        errors.append(named_error)

print(errors)


