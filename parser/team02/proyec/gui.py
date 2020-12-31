from tkinter import *
import tkinter.messagebox
from functools import partial
import Reportes.Tabla as ReporteTabla
import ascendente as asc
import ast.Entorno as Entorno
import ast.Ast as Ast
import Reportes.Errores as Reporte


def reportetabla(self):
        reporteTablas = ReporteTabla.Tabla()
        reporteTablas.write(self.ent,self.ast)

def reporteerr(self):
        Reporte.write(self)


def scan1(self):
       inputValue=self.tex.get("1.0","end-1c")
       tkinter.messagebox.showwarning(title=None, message=inputValue)
     #  asc.texto = inputValue.lower()
       asc.texto ="CREATE DATABASE casa";
       sentencias = asc.parse(inputValue)
       self.sentencias = sentencias

       tkinter.messagebox.showwarning(title=None, message="1 asc")
       Ent = Entorno.Entorno(None)

       ast = Ast.Ast(sentencias)

       bandera = False
       if(sentencias != None):
                for x in sentencias:
                    try:
                            a = True
                            if(ast.exist_label(x)):
                                valueaagregar = Error("SEMANTICO","Ya existe la variable "+x.value,x.line,x.column)
                                Reporte.agregar(valueaagregar)
                            else:
                                ast.agregarlabel(x)
                    except:
                            pass
       tkinter.messagebox.showwarning(title=None, message="2")

       A = ast.getlabels()
       if(A != None):

                for W in A:
                    try:
                        if(W.ejecutar(Ent,ast) == True):
                            break
                    except:
                        pass

       else:
                valueaagregar = Error("SEMANTICO","Arbol vacio para compilar ",0,0)
                Reporte.agregar(valueaagregar)

       self.ent = Ent
       self.ast = ast



class gui:


    def outmensajes(a):
       tkinter.messagebox.showwarning(title=None, message=a)


    def __init__(self):
            super().__init__()
             # outmensajes("start")
             #iniciar(self)





    def iniciar(self):

            window = Tk()


            window.title("Proyecto")

            window.geometry('650x600')



                #btn = Button(window, text="scan", command = scan)
            btn = Button(window, text="scan", command = partial(scan1, self))



            btn.grid(column=1, row=0)

            btn2 = Button(window, text="table", command = partial(reportetabla, self))
            btn2.grid(column=1, row=1)

            btn3= Button(window, text="Errores", command = partial(reporteerr, self))
            btn3.grid(column=2, row=1)

            tex = Text(master=window)
            scr=Scrollbar(window, orient=VERTICAL, command=tex.yview)
            scr.grid(row=2, column=2, rowspan=15, columnspan=1, sticky=NS)
            tex.grid(row=2, column=1, sticky=W)
            tex.config(yscrollcommand=scr.set, font=('Arial', 11))

            self.tex = tex



            window.mainloop()


obj = gui()
obj.iniciar()
