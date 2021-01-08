from tkinter import ttk,scrolledtext,simpledialog,filedialog,messagebox,END,INSERT
import gramatica_asc as g
import generadorC3D.gramaticaC3D as g3
import Ast as ast
from optimizacion import Optimizacion
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
    
    def traducir(self,editor,consola, output, errores, c3dconsole, notebook):

        if editor.get(1.0,END) != "\n":
            entrada = editor.get(1.0,'end')
            g3.parse(entrada)
            self.crearArchivo(g3.C3Direcciones)    
            ruta_c3d= "codigoEn3D.py"
            fichero = open(ruta_c3d, 'r', encoding= "utf-8")
            contenido = fichero.read()
            c3dconsole.delete(1.0, 'end')
            #print(contenido)
            c3dconsole.insert('insert', contenido)
            fichero.close()    
            notebook.select(c3dconsole)
            messagebox.showinfo(message = "Las instrucciones SQL/PLSQL han sido traduccidas a C3D", title="TytusDB")

        else:
            messagebox.showerror(message="Ingrese datos a analizar",title="TytusDB")

    def opt(self, optConsole, notebook):
        hola = g3.C3Direcciones           
        contenidoOp = []
        Optimizacion(hola, contenidoOp)
        # contenido = Optimizacion.optimizando(hola)
        # for inst in contenidoOp:
        #     # textoopt.insert('insert', inst)
        #     print("->", inst)
        self.crearArchivo2(contenidoOp)    
        ruta_opt= "codigoEn3D_OPTIMIZADO.py"
        fichero = open(ruta_opt, 'r', encoding= "utf-8")
        contenidoOp = fichero.read()
        optConsole.delete(1.0, 'end')
        #print(contenido)
        optConsole.insert('insert', contenidoOp)
        fichero.close()   
        notebook.select(optConsole)
        messagebox.showinfo(message = "El Codigo de tres direcciones ha sido optimizado", title="TytusDB")
        