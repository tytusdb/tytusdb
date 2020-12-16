import grammarReview as g
from parse.errors import Error as our_error
f = open("./entrada.txt", "r")
input = f.read()
print("Input: " + input +"\n")
obj = g.toParse(input)
print("Executing AST root, please wait ...")
errors = []
try:
    val = obj.execute('TS',None)
    print("AST excute result: ", val)
except our_error as named_error:
    errors.append(named_error)

print(errors)


