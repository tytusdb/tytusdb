
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class PantallaPrincipal:
    def __init__(self):
        self.PantallaPrincipal = Tk()
        self.PantallaPrincipal.title("Tytus")
        self.PantallaPrincipal.geometry("200x125")
        self.PantallaPrincipal.configure(bg="snow")
        self.isPantalla1 = 0
        self.isPantallaBases = 0
        self.pantalla1()

    def pantalla1(self):
        if self.isPantalla1 == 1:
            self.FrameBases.destroy()
        elif self.isPantalla1 == 2:
            self.FrameFunciones.destroy()
        self.isPantalla1 = 0
        self.FrameInicial = Frame()
        self.FrameInicial.config(width="300", height="200")
        self.FrameInicial.config(bg = "snow")
        self.FrameInicial.pack()

        self.Texto = Label(self.FrameInicial, text="Tytus", fg="gray1", font=("Times New Roman", 20))
        self.Texto.configure(bg="snow")
        self.Texto.pack(padx=0, pady=0)

        self.BotonBD = Button(self.FrameInicial, text="Ingresar a una base de datos", command=self.AccederPestañaBases)
        self.BotonBD.configure(bg="DarkGoldenrod2")
        self.BotonBD.pack()

        self.BotonFunc = Button(self.FrameInicial, text="Opción funciones", command=self.AccederPestañaFunciones)
        self.BotonFunc.configure(bg="DarkGoldenrod2")
        self.BotonFunc.pack()

        self.PantallaPrincipal.mainloop()


    def AccederPestañaBases(self):
        self.FrameInicial.destroy()
        self.isPantalla1 = 1
        if self.isPantallaBases != 0:
            self.FrameTablas.destroy()
        self.isPantallaBases = 0
        self.FrameBases = Frame()
        self.FrameBases.config(width="600", height="400")
        self.FrameBases.config(bg="snow")
        self.FrameBases.pack()

        self.Texto = Label(self.FrameBases ,text = "Tytus", fg="gray1", font=("Times New Roman",20))
        self.Texto.configure(bg="snow")
        self.Texto.pack(padx=0, pady=0)
        
        self.BasesBox = ttk.Combobox(self.FrameBases,state = "readonly")
        self.BasesBox["values"] = ["Base1", "Base2", "Base3", "Base4"]
        self.BasesBox.pack()
        
        self.Boton = Button(self.FrameBases, text="Seleccione una base de datos", command=self.AccederPestañaTablas)
        self.Boton.configure(bg="DarkGoldenrod2")
        self.Boton.pack()

        self.BotonRegresar = Button(self.FrameBases, text="Regresar", command=self.pantalla1)
        self.BotonRegresar.configure(bg="DarkGoldenrod2")
        self.BotonRegresar.pack()

    def AccederPestañaFunciones(self):
        self.FrameInicial.destroy()
        self.isPantalla1 = 2
        self.FrameFunciones = Frame()
        self.FrameFunciones.config(width="600", height="400")
        self.FrameFunciones.config(bg="snow")
        self.FrameFunciones.pack()

        self.Texto = Label(self.FrameFunciones, text="Tytus", fg="gray1", font=("Times New Roman", 20))
        self.Texto.configure(bg="snow")
        self.Texto.pack(padx=0, pady=0)
        
        self.FuncionesBox = ttk.Combobox(self.FrameFunciones, state="readonly")
        self.FuncionesBox["values"] = ["Función1", "Función2", "Función3", "Función4"]
        self.FuncionesBox.pack()
        
        self.Boton = Button(self.FrameFunciones, text="Seleccione una función")
        self.Boton.configure(bg="DarkGoldenrod2")
        self.Boton.pack()

        self.BotonRegresar = Button(self.FrameFunciones, text= "Regresar", command = self.pantalla1)
        self.BotonRegresar.configure(bg="DarkGoldenrod2")
        self.BotonRegresar.pack()

    def AccederPestañaTablas(self):
        if self.BasesBox.get() != "":
            self.FrameBases.destroy()
            self.isPantallaBases = 1
            self.FrameTablas = Frame()
            self.FrameTablas.config(width="600", height="400")
            self.FrameTablas.config(bg="snow")
            self.FrameTablas.pack()

            self.Texto = Label(self.FrameTablas, text="Tytus", fg="gray1", font=("Times New Roman", 20))
            self.Texto.configure(bg="snow")
            self.Texto.pack(padx=0, pady=0)

            self.TablasBox = ttk.Combobox(self.FrameTablas, state="readonly")
            self.TablasBox["values"] = ["Tabla1", "Tabla2", "Tabla3"]
            self.TablasBox.pack()

            self.Boton = Button(self.FrameTablas, text="Seleccione una tabla")
            self.Boton.configure(bg="DarkGoldenrod2")
            self.Boton.pack()

            self.BotonRegresar = Button(self.FrameTablas, text="Regresar", command=self.AccederPestañaBases)
            self.BotonRegresar.configure(bg="DarkGoldenrod2")
            self.BotonRegresar.pack()
        else:
            messagebox.showinfo(message="Debe seleccionar una base de\ndatos para poder continuar",
                                title="BD no seleccionada")

