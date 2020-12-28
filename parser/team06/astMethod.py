import os
import tkinter
from tkinter import messagebox

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
        state_script_dir = os.getcwd()
        file_path = state_script_dir + "\\AST\\ast"
        print(file_path)
        file = open(file_path+'.dot', 'w')
        if file:
            file.write('digraph d {\n')
            tourAST(node, file)
            file.write('\n}')
        file.close()
        os.system("dot -Tpng "+file_path+".dot -o "+file_path +".png")
        os.startfile(file_path +".png")
    except ValueError:
        box_tilte ="Value Error"
        box_msg = "Error con algun valor de la entrada"
        messagebox.showerror(box_tilte,box_msg)
    except:
        file.close()
        box_tilte ="File Error"
        box_msg = "El archivo que trata de acceder no existe"
        messagebox.showerror(box_tilte,box_msg)