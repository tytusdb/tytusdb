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
print("Input: " + input +"\n")
obj = g.toParse(input)
print("Executing AST root, please wait ...")
val = obj.execute(None,None)
print("AST excute result: ",val)
