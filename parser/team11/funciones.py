from tkinter import ttk,scrolledtext,simpledialog,filedialog,messagebox,END,INSERT
import gramatica_asc as g
import Ast as ast
class Funciones2:

    def __init__(self, AST = None):
        self.AST = AST

    def analizar(self,editor,consola, output, errores):
        out = ''
        er = ''
        contador = 0
        if editor.get(1.0,END) != "\n":
            entrada = editor.get(1.0,'end')
            self.AST = g.parse(entrada)
            #print(len(self.AST.output))
            for e in self.AST.output:
                contador = contador + 1
                out += str(contador)+'. . . .\n' + str(e) +'. . . .' +'\n'
            output.insert('insert',out)
            contador = 0
            for a in self.AST.errors:
                contador = contador + 1
                er += str(contador) + '. . . .\n'+a.toString()+'. . . .' + '\n'
            errores.insert('insert', er)
            #print(entrada)
            self.AST.output[:] = []

        else:
            messagebox.showerror(message="Ingrese datos a analizar",title="TytusDB")