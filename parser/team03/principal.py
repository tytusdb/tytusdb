import grammarReview as g

f = open("./entrada.txt", "r")
input = f.read()
print("Input: " + input +"\n")
obj = g.toParse(input)
print("Executing AST root, please wait ...")
val = obj.execute(None,None)
print("AST excute result: ",val)
