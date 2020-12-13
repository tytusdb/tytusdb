from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb
from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog, font
import tkinter as tk

from main import *

class query_tool:
    def __init__(self, window):
        self.vp = window
        self.rutaArchivo = ""
        self.nombreArchivo = ""
        self.extension = ""
        self.texto =""
        self.txtConsola = ""
        self. TextoActual=""
        

        ###################################################### INTERFAZ GRÁFICA ######################################################
        #Ventana Principal
        self.vp.title("Tytus - Query Tool")
        self.barraMenu = Menu(self.vp)
        self.vp.configure(menu = self.barraMenu)     
        
        #Labels
        tk.Label(self.vp, fg = "white",  bg ="#154360", text="TYTUS - Query Tool", font=("Arial Bold", 15)).grid(row=0, column = 1 , sticky=E+W)
        tk.Label(self.vp, fg = "white",  bg ="#154360", text="Linea : 1 Columna : 1", font=("Arial Bold", 10)).grid(row=2, column = 1 , sticky=E+W)
        actualizarPuntero = tk.Button(self.vp, text="Posicion actual", command = self.cursor).grid(row=3, column = 1 )
        
        
        #Canvas
        self.canvas1 = tk.Canvas(self.vp, width=1300, height=300)
        self.canvas1.grid(row=4, column = 1, sticky=E+W)

        self.canvas2 = tk.Canvas(self.vp, width=1200, height=275)
        self.canvas2.grid(row=5, column = 1 , sticky='news')

        #Frames
        self.frame1 = tk.LabelFrame(self.canvas1, bg="#154360", text="Entrada:", font=("Arial Bold", 10), foreground="white")
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.frame2 = tk.LabelFrame(self.canvas2, bg="#154360", text="Resultados:", font=("Arial Bold", 10), foreground="white")
        self.frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

        #TextArea
        self.entrada = tk.Text(self.frame1, font=9)
        self.entrada.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.9)
        
        self.scrollbarEntradaX = tk.Scrollbar(self.entrada, orient=tk.HORIZONTAL)
        self.scrollbarEntradaX.pack(side="bottom", fill="x")

        self.scrollbarEntradaY = tk.Scrollbar(self.entrada)
        self.scrollbarEntradaY.pack(side="right", fill="y")
        
        self.entrada.config(wrap= "none", xscrollcommand = self.scrollbarEntradaX.set, yscrollcommand = self.scrollbarEntradaY.set)
        self.scrollbarEntradaY.config(command = self.entrada.yview)
        self.scrollbarEntradaX.config(command = self.entrada.xview)

        #Consola
        self.consola = tk.Text(self.frame2, font=9, background="black", foreground = "green")
        self.consola.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.9)

        self.scrollbarConsolaX = tk.Scrollbar(self.consola, orient=tk.HORIZONTAL)
        self.scrollbarConsolaX.pack(side="bottom", fill="x")

        self.scrollbarConsolaY = tk.Scrollbar(self.consola)
        self.scrollbarConsolaY.pack(side="right", fill="y")
        
        self.consola.config(wrap= "none", xscrollcommand = self.scrollbarConsolaX.set, yscrollcommand = self.scrollbarConsolaY.set)
        self.scrollbarConsolaY.config(command = self.consola.yview)
        self.scrollbarConsolaX.config(command = self.consola.xview)

        # Menu Archivo
        self.archivoMenu = Menu(self.barraMenu, tearoff=0)
        self.archivoMenu.add_command(label = "Nuevo", command = self.nuevo)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label = "Abrir", command = self.abrir)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label = "Guardar", command = self.guardar )
        self.archivoMenu.add_command(label = "Guardar como...", command = self.guardarComo)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label = "Salir", command = self.vp.quit)
        # Menu Run
        self.runMenu = Menu(self.barraMenu, tearoff=0)
        self.runMenu.add_command(label = "Ejecutar", command = self.ejecutar)
        #Menu Help
        self.helpMenu = Menu(self.barraMenu, tearoff=0)
        self.helpMenu.add_command(label = "About",command = self.seeAbout)
        # Barra de Menú
        self.barraMenu.add_cascade(label = "Archivo",  menu = self.archivoMenu)
        self.barraMenu.add_cascade(label = "Run",      menu = self.runMenu)
        self.barraMenu.add_cascade(label = "Help",     menu = self.helpMenu)

        self.vp.columnconfigure(0, weight=0)
        self.vp.columnconfigure(1, weight=1)

        self.entrada.focus()


    ###################################################### METODOS ######################################################

    #Permite actualizar la posicion actual del puntero en el text de entrada
    def cursor(self):
        puntero=self.entrada.index(tk.INSERT)
        p = puntero.split(".")
        col=p[1]
        t = "Linea: " + p[0] + " Columna: " + str(int(col)+1)
        tk.Label(self.vp, fg = "white",  bg ="#154360", text=t, font=("Arial Bold", 10)).grid(row=2, column = 1 , sticky=E+W)
    
    #Archivo - Nuevo
    def nuevo(self):
        self.rutaArchivo = ""
        self.texto =""
        self.extension = ""
        self.entrada.delete(1.0, END)

    #Archivo - Abrir
    def abrir(self):
        self.txtConsola = ""
        self.consola.delete(1.0,END)
        self.rutaArchivo = filedialog.askopenfilename(title = "Open File")

        getNameAndExtensionFile(self)

        fileAbierto = open(self.rutaArchivo, encoding="utf-8")
        self.texto = fileAbierto.read()
        self.entrada.delete(1.0,END)
        self.entrada.insert(INSERT,self.texto)
        fileAbierto.close();
    

    # Archivo - Guardar como
    def guardarComo(self):
        ruta = filedialog.asksaveasfilename(title = "Save As...")
        fguardar = open(ruta, "w+", encoding="utf-8")
        fguardar.write(self.entrada.get(1.0, END))
        fguardar.close()
        self.rutaArchivo = ruta
        getNameAndExtensionFile(self)

    # Archivo - Guardar
    def guardar(self):
        if self.rutaArchivo == "":
            self.guardarComo()
        else:
            archivoA = open(self.rutaArchivo, "w", encoding="utf-8")
            archivoA.write(self.entrada.get(1.0, END))
            archivoA.close()

    # Archivo - Guardar
    
    def ejecutar(self):
        self.TextoActual = self.entrada.get("1.0","end")
        main1 = main(self.TextoActual)

    def seeAbout(self):
        mb.showinfo("About", "TYTUS\n Universidad de San Carlos de Guatemala \nOLC 2\nCuso de vacaciones \nDiciembre \nAño 2020\nCoautores: \n\t201020126 - Sandy Fabiola Merida Hernandez  \n\t201020252 - Sergio Ariel Ramirez Castro \n\t201020260 - Victor Augusto Lopez Hernandez \n\t201020697 - Esteban Palacios Kestler ")


def getNameAndExtensionFile(self):
        rutaSpliteada = self.rutaArchivo.split("/")
        ultimaPos = len(rutaSpliteada)-1
        self.nombreArchivo = rutaSpliteada[ultimaPos]

        ext = self.nombreArchivo.split(".")
        self.extension = ext[1]

def updateConsola(self):
        self.consola.delete(1.0,END)
        self.consola.insert(INSERT,self.txtConsola)







if __name__ == '__main__':
    window = Tk()
    window.resizable(1,0)
    app = query_tool(window)
    window.mainloop()