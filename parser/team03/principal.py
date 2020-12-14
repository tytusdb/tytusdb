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

f = open("./entrada.txt", "r")
input = f.read()
print("entrada: " + input +"\n")
obj = g.toParse(input)
print(obj,":")
print("Executing AST root ...")
val = obj.execute(None,None)
print("AST excute result: ",val)
