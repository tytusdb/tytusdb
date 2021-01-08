from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as FiledDialog
from tkinter import ttk
from tkinter import messagebox

import Instruccion as INST
from io import open
import Gramatica as Gram
#Parte de Importaciones para el analisis etc
import interprete as Inter
import Ast2 as ast
from Instruccion import *
from intermedio import main
import Sentenciac3d as Op




# ------------------------------------------- VENTANA PRINCIPAL ------------------------------------------------------ #
class Aplicacion:

# ruta del fichero
    ruta = ""
# ----------------------------------------- FUNCIONES MENU ARCHIVO --------------------------------------------------- #
    def nuevo(self):

        global ruta
        ruta = ""
        # Borra desde el primer caracter hasta el final del texto.
        self.entrada.delete(1.0, "end")
        self.consola.delete(1.0, "end")
        self.consola2.delete(1.0,"end")

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

    def ejecutarMain(self):
        main()
        if len(Lista) > 0:
            self.consola.insert('insert', Lista[0])
        else:
            return


    def enviarDatos(self):
        contenido = self.entrada.get(1.0, "end-1c")

        self.consola.insert('insert', contenido)
        Inter.inicializarEjecucionAscendente(contenido)



    def enviarC3d(self):
        if Op.c3d !=False:
            contenido = Op.c3d.pop()
            #print("<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ESTE SOY")
            #print(contenido)
            self.consola2.insert('insert', contenido)




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
            #print(nueva)
            Inter.inicializarEjecucionAscendenteSel(cadena)

            if len(Lista) >0:
                self.consola.insert('insert', Lista[0])
            else:
                return
        except:
            cadena2 = self.entrada.get(1.0, "end-1c")
            nuevaV = str(cadena2).upper()
            #print(nuevaV)
            Inter.inicializarEjecucionAscendenteSel(cadena2)

            if len(Lista) >0:
                self.consola.insert('insert', Lista[0])
            else:
                return




    def reporte_gramatical_(self):     
        try:
           Gram.reporte_gramatical()
        except:
            print("error en el reporte gramatical :(")


    def reporte_optimizacion_(self):
        Op.reporte_optimizacion()



    def reporte_AST_(self):
        Gram.reporte_AST_GLOB()



    def Traducir_Codigo_(self):
        Gram.traducir_AST_GLOB()
        self.enviarC3d()


    def Ejecucion(self):
        Gram.Ejecucion()
        if len(Lista) > 0:
            self.consola.insert('insert', Lista[0])
        else:
            return

        if len(Lista) > 0:
            self.consola.insert('insert', Lista[0])
        else:
            return


    def graficaTabla(self):
        INST.tabla_simbolos()

    def Errores(self):
        Inter.reporte_errores()

    def Graficar(self):
        print("graficando arbol")

    def __init__(self):
        self.miVentana = Tk()
        self.miVentana.title("TytusDB G16")
        self.miVentana.config(bd=3)
        self.miVentana.state('zoomed')

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

        self.menuAnalizar.add_command(label="Interpretar", command=self.Seleccionar)
        self.menuAnalizar.add_command(label="Ejecucion", command=self.Ejecucion)
        self.menuAnalizar.add_command(label="Graficar Arbol", command=self.reporte_AST_)
        self.menuAnalizar.add_command(label="Traducir", command=self.Traducir_Codigo_)

        self.menuReportes = Menu(self.barraMenu, tearoff=0)
        self.menuReportes.add_command(label="Reporte Errores", command=self.Errores)
        self.menuReportes.add_command(label="Tabla de Simbolos", command=self.graficaTabla)
        self.menuReportes.add_command(label="Reporte Gramatical", command=self.reporte_gramatical_)
        self.menuReportes.add_command(label="Reporte Optimizacion", command=self.reporte_optimizacion_)

        self.menu3D = Menu(self.barraMenu, tearoff=0)
        # self.menu3D.add_command(label="Generar", command=self.Errores)
        self.menu3D.add_command(label="Ejecutar", command=self.ejecutarMain)


        self.barraMenu.add_cascade(menu=self.menuArchivo, label="Archivo")
        self.barraMenu.add_cascade(menu=self.menuAnalizar, label="Run")
        self.barraMenu.add_cascade(menu=self.menuReportes, label="Reportes")
        self.barraMenu.add_cascade(menu=self.menu3D, label="Codigo Intermedio")


        # Consola salida c3d

        self.consola2 = scrolledtext.ScrolledText(self.miVentana,width=88,height=26, selectbackground="white",
                      selectforeground="black", undo=True, foreground="white",background="black")

        # fill desde la raiz y se expande = True/1
        self.consola2.pack(side=RIGHT, fill=Y)
        self.consola2.place(x=750, y=0)
        # Borde de 0px, padding X = 10px, padding Y = 5 y fuente
        self.consola2.config(bd=0, padx=10, pady=5, font=("Consolas", 11))



        # Area de texto
        self.entrada = scrolledtext.ScrolledText(self.miVentana,width=88,height=26,selectbackground="black")
        # fill desde la raiz y se expande = True/1
        self.entrada.pack(side=RIGHT, fill=Y)
        self.entrada.place(x=0, y=0)
        # Borde de 0px, padding X = 10px, padding Y = 5 y fuente
        self.entrada.config(bd=0, padx=10, pady=5, font=("Consolas", 11))





        # Consola salida
        self.consola = scrolledtext.ScrolledText(self.miVentana,width=183, height=15,selectbackground="black",background="yellow")
        self.consola.pack( fill=X)
        self.consola.place(x=0, y=510)
        # Borde de 0px, padding X = 10px, padding Y = 5 y fuente
        self.consola.config(bd=0, padx=10, pady=5, font=("Consolas", 11))








        # Loop ventana
        self.miVentana.config(menu=self.barraMenu)
        self.miVentana.mainloop()

principal = Aplicacion()
