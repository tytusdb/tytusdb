from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as FiledDialog
from tkinter import ttk
import Instruccion as INST
from io import open
import Gramatica as Gram
#Parte de Importaciones para el analisis etc
import interprete as Inter
import Ast2 as ast
from Instruccion import *

import sys
from io import StringIO
import contextlib


# ------------------------------------------- VENTANA PRINCIPAL ------------------------------------------------------ #
class Aplicacion:

# ruta del fichero
    ruta = ""
    global selected
    selected = False
# ----------------------------------------- FUNCIONES MENU ARCHIVO --------------------------------------------------- #
    def nuevo(self):
        global ruta
        ruta = ""
        # Borra desde el primer caracter hasta el final del texto.
        self.entrada.delete(1.0, "end")
        self.consola.delete(1.0, "end")
        Lista.clear()
        self.miVentana.title("TytusDB G16")

    def abrir(self):
        global ruta
        ruta = FiledDialog.askopenfilename(initialdir='.', filetype=(("Archivos SQL", "*.sql"),), title="Abrir")
        if ruta != "":
            fichero = open(ruta, 'r')
            contenido = fichero.read()
            self.entrada.delete(1.0, "end")
            self.entrada.insert('insert', contenido)
            fichero.close()
            self.miVentana.title(ruta + " - TytusDB G16")

    def guardar(self):
        # Si tiene una ruta
        if ruta != "":
            contenido = self.entrada.get(1.0, "end")
            fichero = open(ruta, 'w+')
            fichero.write(contenido)
            fichero.close()
            # Mensaje de que se guardo el archivo.
        # Si no tiene una ruta
        else:
            self.guardarComo()

    def guardarComo(self):
        global ruta
        fichero = FiledDialog.asksaveasfile(title="Guardar archivo", mode="w", defaultextension=".sql")
        if fichero is not None:  # Si no se cancela
            ruta = fichero.name  # guardamos ruta accediendo con name
            contenido = self.entrada.get(1.0, "end-1c")  # se lee sin el ultimo caracter
            fichero = open(ruta, 'w+')
            fichero.write(contenido)
            fichero.close()
        else:
            ruta = ""


    def enviarDatos(self):
        contenido = self.entrada.get(1.0, "end-1c")
        self.consola.insert('insert', contenido)
        #self.consola.config(state=DISABLED)
        Inter.inicializarEjecucionAscendente(contenido)


    def Seleccionar(self):
        cadena=""
        cadena2=""
        self.consola.delete(1.0, "end")
        self.miVentana.title("TytusDB G16")
        Lista.clear()
        listaGeneral.clear()
        Modificaciones.clear()
        listaGeneralSubQuery.clear()
        Ejecucion=""

        try:
            cadena = self.entrada.get(SEL_FIRST, SEL_LAST)
            nueva = str(cadena).upper()
            print(nueva)
            Inter.inicializarEjecucionAscendente(cadena)
            if len(Lista) >0:
                self.consola.insert('insert', Lista[0])
                #self.consola.config(state=DISABLED)

            else:
                return
        except:
            cadena2 = self.entrada.get(1.0, "end-1c")
            nuevaV = str(cadena2).upper()
            print(nuevaV)
            Inter.inicializarEjecucionAscendente(cadena2)

            if len(Lista) >0:
                self.consola.insert('insert', Lista[0])
                #self.consola.config(state=DISABLED)

            else:
                return

    def SeleccionarQuery(self):
        global selected
        
        cadena=""
        cadena2=""
        self.consola.delete(1.0, "end")
        self.miVentana.title("TytusDB G16")
        Lista.clear()
        listaGeneral.clear()
        Modificaciones.clear()
        listaGeneralSubQuery.clear()
        Ejecucion=""

        try:
            if self.entrada.selection_get():
                selected = self.entrada.selection_get()
                cadena = selected
                nueva = str(cadena).upper()
                print(nueva)
                Inter.inicializarEjecucionAscendente(cadena)
                if len(Lista) >0:
                    self.consola.insert('insert', Lista[0])
                    #self.consola.config(state=DISABLED)

                else:
                    return
        except:
            if self.entrada.selection_get():
                selected = self.entrada.selection_get()
                cadena2 = selected
                nuevaV = str(cadena2).upper()
                print(nuevaV)
                Inter.inicializarEjecucionAscendente(cadena2)

                if len(Lista) >0:
                    self.consola.insert('insert', Lista[0])
                    #self.consola.config(state=DISABLED)

                else:
                    return


    def reporte_gramatical_(self):     
            try:
               Gram.reporte_gramatical()
            except:
                print("error en el reporte gramatical :(")
                
    def reporte_AST_(self):     
            try:
               Gram.reporte_AST_GLOB()
            except:
                print("error en el reporte gramatical :(")


    def graficaTabla(self):
        INST.tabla_simbolos()

    def Errores(self):
        Inter.reporte_errores()

    def traducir3D(self):
        f = open("texto3D.py", "r")
        texto3D = f.read()
        self.entrada2.insert(1.0,texto3D)

    @contextlib.contextmanager
    def stdoutIO(self,stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    def compilar3D(self):
        try:
            cadena = self.entrada2.get("1.0",'end-1c')
            with self.stdoutIO() as s:
                exec(cadena)

            self.consola.insert('insert',s.getvalue())
            #self.consola.config(state=DISABLED)

        except:
            pass

    def __init__(self):
        self.miVentana = Tk()
        self.miVentana.title("TytusDB G16")
        self.miVentana.config(bd=3)
        self.miVentana.state('zoomed')
        self.w, self.h = self.miVentana.winfo_screenwidth(), self.miVentana.winfo_screenheight()
        
        # Menu
        self.barraMenu = Menu(self.miVentana)

        self.menuArchivo = Menu(self.barraMenu, tearoff=0)
        self.menuArchivo.add_command(label="Nuevo", command=self.nuevo)
        self.menuArchivo.add_command(label="Abrir", command=self.abrir)
        self.menuArchivo.add_command(label="Guardar", command=self.guardar)
        self.menuArchivo.add_command(label="Guardar Como", command=self.guardarComo)
        self.menuArchivo.add_separator()
        self.menuArchivo.add_command(label="Salir de TytusDB", command=self.miVentana.quit())

        self.menuAnalizar = Menu(self.barraMenu, tearoff=0)
        #self.menuAnalizar.add_command(label="Run", command=self.enviarDatos)
        self.menuAnalizar.add_command(label="Ejecucion", command=self.Seleccionar)
        self.menuAnalizar.add_command(label="Ejecucion Comando", command=self.SeleccionarQuery)
        self.menuAnalizar.add_command(label="Graficar Arbol", command=self.reporte_AST_)

        self.menuReportes = Menu(self.barraMenu, tearoff=0)
        self.menuReportes.add_command(label="Reporte Errores", command=self.Errores)
        self.menuReportes.add_command(label="Tabla de simbolos", command=self.graficaTabla)
        self.menuReportes.add_command(label="Reporte gramatical", command=self.reporte_gramatical_)


        self.barraMenu.add_cascade(menu=self.menuArchivo, label="Archivo")
        self.barraMenu.add_cascade(menu=self.menuAnalizar, label="Run")
        self.barraMenu.add_cascade(menu=self.menuReportes, label="Reportes")

        self.toolbar_frame = Frame(self.miVentana)
        self.toolbar_frame.pack(fill = X)
        
        self.analizar_button = Button(self.toolbar_frame)
        self.photoCompila = PhotoImage(file="iconos/all.png")
        self.analizar_button.config(image=self.photoCompila, width="50", height="50", activebackground="black",command=self.Seleccionar)
        self.analizar_button.grid(row = 0, column = 0, sticky = W)

        self.analizar_step_step = Button(self.toolbar_frame)
        self.photoCompila1 = PhotoImage(file="iconos/select.png")
        self.analizar_step_step.config(image=self.photoCompila1, width="50", height="50", activebackground="black",command=self.SeleccionarQuery)
        self.analizar_step_step.grid(row = 0, column = 1, sticky = W)
        
        self.translate = Button(self.toolbar_frame)
        self.photoCompila2 = PhotoImage(file="iconos/translate.png")
        self.translate.config(image=self.photoCompila2, width="50", height="50", activebackground="black",command=self.traducir3D)
        self.translate.grid(row = 0, column = 2, sticky = W)

        self.python3d = Button(self.toolbar_frame)
        self.photoCompila3 = PhotoImage(file="iconos/python.png")
        self.python3d.config(image=self.photoCompila3, width="50", height="50", activebackground="black",command=self.compilar3D)
        self.python3d.grid(row = 0, column = 3, sticky = W)

        # Area de texto
        #self.entrada = scrolledtext.ScrolledText(self.miVentana)

        # fill desde la raiz y se expande = True/1
        #self.entrada.pack(fill="both", expand=1)
        # Borde de 0px, padding X = 10px, padding Y = 5 y fuente
        #self.entrada.config(bd=0, padx=10, pady=5,wrap = "none",)

        self.text_frames = Frame(self.miVentana)
        self.text_frames.pack()

        self.entrada_h = int(self.h * 0.038)
        self.entrada_w = int(self.w * 0.060)
        self.text_frame = Frame(self.text_frames,width=self.entrada_w, height=self.entrada_h)
        self.text_frame.pack( side = LEFT )
        
        self.text_scroll = Scrollbar(self.text_frame)
        self.text_scroll.pack(side = RIGHT, fill = Y)
        # HORIZONTAL SCROLL BAR
        self.hor_scroll = Scrollbar(self.text_frame, orient = 'horizontal')
        self.hor_scroll.pack(side = BOTTOM, fill = X)
        self.entrada = Text(self.text_frame, width=self.entrada_w, height=self.entrada_h, selectforeground="black", undo=True, yscrollcommand=self.text_scroll.set, wrap = "none", xscrollcommand = self.hor_scroll.set)
        self.entrada.pack()

        self.text_scroll.config(command = self.entrada.yview)
        self.hor_scroll.config(command = self.entrada.xview)


        #VENTANA2

        self.text_frame2 = Frame(self.text_frames,width=self.entrada_w, height=self.entrada_h)
        self.text_frame2.pack( side = LEFT )
        
        self.text_scroll2 = Scrollbar(self.text_frame2)
        self.text_scroll2.pack(side = RIGHT, fill = Y)
        # HORIZONTAL SCROLL BAR
        self.hor_scroll2 = Scrollbar(self.text_frame2, orient = 'horizontal')
        self.hor_scroll2.pack(side = BOTTOM, fill = X)
        self.entrada2 = Text(self.text_frame2, width=self.entrada_w, height=self.entrada_h, selectforeground="black", undo=True, yscrollcommand=self.text_scroll2.set, wrap = "none", xscrollcommand = self.hor_scroll2.set)
        self.entrada2.pack()

        self.text_scroll2.config(command = self.entrada2.yview)
        self.hor_scroll2.config(command = self.entrada2.xview)


        #VENTANA 2


        self.sepa = ttk.Separator(self.miVentana, orient=HORIZONTAL)
        self.sepa.pack(fill="x", expand=1)
        # Consola salida
        mensaje = StringVar()
        mensaje.set("Consola: ")
        self.labelConsola = Label(self.miVentana, textvar=mensaje, justify='left')
        self.labelConsola.pack(side="left")
        self.consola = Text(self.miVentana, width=50, height=10)
        self.consola.pack(fill="both", expand=0)
        '''self.consola = scrolledtext.ScrolledText(self.miVentana, width=50, height=10)
        self.consola.pack(fill="both", expand=0)  '''     
        

        # Loop ventana
        self.miVentana.config(menu=self.barraMenu)
        self.miVentana.mainloop()

principal = Aplicacion()
