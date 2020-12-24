from tkinter import *
import tkinter.messagebox
from functools import partial
import Reportes.Tabla as ReporteTabla
import ascendente as asc
import ast.Entorno as Entorno
import ast.Ast as Ast
import Reportes.Errores as Reporte
from Reportes.Datos import Datos
import Reportes.ReporteD as Sentencias
import Reportes.Nodo as N
from tkinter import filedialog


def astreporte(self):
        execr = N.Nodo()
        execr.ending()
        

def abrir_txt(self):
        path = filedialog.askopenfilename( title="Abrir Archivo", filetypes=(("Archivos de texto", "*.txt"), ))
        file = open(path, 'r')
        texto = file.read()

        #txtEntrada.insert(END, texto)

        file.close()

        self.tex.delete("1.0", "end-1c")
        self.tex.insert("1.0", texto)

def guardar_txt(self):
	path = filedialog.askopenfilename(title="Guardar Archivo", filetypes=(("Archivos de texto", "*.txt"), ))
	file = open(path,'w')
	file.write(self.tex.get(1.0,END))
	file.close()

def reportetabla(self):
        reporteTablas = ReporteTabla.Tabla()
        reporteTablas.write(self.ent,self.ast)

def reporteerr(self):
        Reporte.write(self)

def reporteR(self):
        SentenciasR = Sentencias.ReporteD()
        SentenciasR.Mostrar(self.ent,self.ast)

def scan1(self):
       SentenciasR = Sentencias.ReporteD()
       SentenciasR.Abrir()
       ast = [] 
       Ent = [] 

       execr = N.Nodo()
       execr.start()
        
       inputValue=self.tex.get("1.0","end-1c")
       tkinter.messagebox.showwarning(title=None, message=inputValue)
     #  asc.texto = inputValue.lower()
       asc.texto ="CREATE DATABASE casa"
       sentencias = asc.parse(inputValue)
       self.sentencias = sentencias

       #tkinter.messagebox.showwarning(title=None, message="1 asc")
       Ent = Entorno.Entorno(None)
       print("recorrera")

       ast = Ast.Ast(sentencias)

       bandera = False
       if(sentencias != None):
                for x in sentencias:
                    try:
                            a = True

                            print("testeara --- ")
                            print(x.id)

                            if(ast.exist_label(x)):
                                print("Ya existe la variable  ")
                                print("Ya existe la variable  ",x.id)

                                valueaagregar = Datos("SEMANTICO","Ya existe la variable "+x.id,x.line,x.column)
                                Reporte.agregar(valueaagregar)
                            else:
                                print("testeara -exist_label ")
                                print(x.id)


                                ast.agregarlabel(x)
                    except:
                            pass
       #tkinter.messagebox.showwarning(title=None, message="2")
       print("parseara")

       A = ast.getlabels()
       if(A != None):
                print("1 ")

                for W in A:

                    try:
                            print("ejecutara2 ---------------------- ", W)
                         
                                
                    except:
                        pass
                for W in A:

                    try:
                            print("ejecutara ---------------------- ", W)
                            print("2 ")
                        
                            print("3 ")   
                            try:              
                               W.ejecutar(Ent,ast)
                               print("4b ")
                            except:
                               print("3b ")                               
                               pass    
                             
                                
                    except:
                        pass
                print("4 ") 

       else:
                valueaagregar = Datos("SEMANTICO","Arbol vacio para compilar ",0,0)
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

        window.geometry('800x600')

        lblTitulo = Label(window, text ="AREA DE COMANDOS")
        lblTitulo.grid(column=1, row = 0)

        #btn = Button(window, text="scan", command = scan)
        btn = Button(window, text="scan", width=15, height=2, command = partial(scan1, self))
        btn.place(x=5, y=475)
        #btn.grid(column=1, row=0)

        btnx = Button(window, text="Open", width=15, height=2, command = partial(abrir_txt, self))
        btnx.grid(column=5, row = 0)
        #btnx.grid(column=1, row=1)

        btnGuardar = Button(window, text="Guardar",  width=15, height=2, command =partial(guardar_txt, self))
        btnGuardar.grid(column=5, row = 1)

        btn2 = Button(window, text="table", width=15, height=2, command = partial(reportetabla, self))
        btn2.place(x=125, y=475)
        #btn2.grid(column=1, row=2)

        btn3= Button(window, text="Errores", width=15, height=2, command = partial(reporteerr, self))
        btn3.place(x=245, y=475)
        #btn3.grid(column=2, row=0)

        btn4 = Button(window, text="Reportes", width=15, height=2, command = partial(reporteR, self))
        btn4.place(x=365, y=475)
        #btn4.grid(column=2, row=1)

        btn5 = Button(window, text="Ast", width=15, height=2, command = partial(astreporte, self))
        btn5.place(x=485, y=475)
        #btn5.grid(column=5, row=3)

        btnSalir = Button(window, text="Salir", width=49, height=2,  command = window.destroy)
        btnSalir.place(x=125, y=525)
        #btnSalir.grid(column=5, row = 3)

        tex = Text(master=window)
        scr=Scrollbar(window, orient=VERTICAL, command=tex.yview)
        scr.grid(row=1, column=2, rowspan=15, columnspan=1, sticky=NS)
        tex.grid(row=1, column=1, sticky=W)
        tex.config(yscrollcommand=scr.set, font=('Arial', 11))

        self.tex = tex

        window.mainloop()


obj = gui()
obj.iniciar()
