import os

def tourAST(node,fileName):
    if node:
        if node.son:
            fileName.write('nodo' + str(id(node)) + ' [shape=record,style=filled,fillcolor="#C3A7A4",label=\"{'
                                                          'Token:' + str(node.token).replace(">","\\>").replace("<","\\<") + '|'
                                                          'Lexema:' + str(node.lexeme).replace(">","\\>").replace("<","\\<") + '}\"];\n')
        elif not node.son:
            fileName.write('nodo' + str(id(node)) + ' [shape=record,style=filled,fillcolor="#33FF76",label=\"{'
                                                          'Token:' + str(node.token).replace(">","\\>").replace("<","\\<") + '|'
                                                          'Lexema:' + str(node.lexeme).replace(">","\\>").replace("<","\\<") + '}\"];\n')

        for obj in node.son:
            tourAST(obj, fileName)
            fileName.write('nodo' + str(id(node)) + ' -> nodo' + str(id(obj)) + ';\n')

def astFile(fileName, node):
    try:
        file = open(fileName+'.dot', 'w')
        if file:
            file.write('digraph d {\n')
            tourAST(node, file)
            file.write('\n}')
        file.close()
        os.system("dot -Tpng "+fileName+".dot -o "+fileName +".png")
        print("AST generado")
    except ValueError:
        print("Error valor")
    except:
        file.close()
        print("Error")