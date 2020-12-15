import tkinter as tk
import gramaticaASC as g
import Graficar as graficando
from Graficar import*
import principal as principal

from tkinter import filedialog
from tkinter import StringVar
from tkinter.constants import END, INSERT


#################################### CLASE TextLineNumbers ####################################
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)
################################## FIN CLASE TextLineNumbers ##################################


###################################### CLASE CustomText #######################################
class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        try:
            result = self.tk.call(cmd)
        except Exception:
            return None

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or 
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result
#################################### FIN CLASE CustomText #####################################       


######################################## CLASE Example ########################################
class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)


    def _on_change(self, event):
        
        self.linenumbers.redraw()
        global fila
        global colum

        filaString = "Fila: " + str(self.text.index(tk.INSERT).split(".")[0])
        fila.set(filaString)

        columnString = "Columna: " + str(self.text.index(tk.INSERT).split(".")[1] )
        colum.set(columnString)

    def insert_text(self, text):
        self.text.insert(INSERT, text)
###################################### FIN CLASE Example ######################################


if __name__ == "__main__":

########################################## FUNCIONES ##########################################
    #FUNCIÓN PARA CREAR UN NUEVO ARCHIVO
    def __funcion_nuevo():
        print('Creando...') 


# FUNCIÓN PRIVADA PARA ABRIR UN ARCHIVO DE TEXTO
    def __funcion_abrir():
    
        input = filedialog.askopenfilename(initialdir="/")
        f = open(input, "r", encoding="utf8")
        input2 = f.read()
        my_editor.text.delete('1.0',END)
        my_editor.text.insert(INSERT, input2)


    # FUNCIÓN PARA GUARDAR UN NUEVO ARCHIVO
    def __funcion_guardar():
        print('Guardando...') 


    # FUNCIÓN PARA GUARDAR COMO
    def __funcion_guardar_como():
        print('Guardando como...') 


    # FUNCIÓN PARA DETENER EL PROGRAMA
    def __funcion_cerrar():
        print('Cerrando...')


    # FUNCIÓN PRIVADA PARA ANALIZAR EL ARCHIVO DE ENTRADA
    def __funcion_analizar():
    
        entrada = my_editor.text.get('1.0',END)
        arbol = g.parse(entrada)
        raiz = graficando.analizador(entrada)
        principal.interpretar_sentencias(arbol)
        
        if arbol is not None:
            consola.configure(state=tk.NORMAL)
            consola.delete('1.0',END)
            consola.insert(INSERT, 'Archivo analizado con éxito \n')
            #consola.insert(INSERT, str(recorrerNodo(raiz)))
            GraficarAST(raiz)
            consola.configure(state=tk.DISABLED)
            
        else:
            consola.configure(state=tk.NORMAL)
            consola.delete('1.0',END)
            consola.insert(INSERT, 'Se detectaron errores en el archivo de entrada')
            consola.configure(state=tk.DISABLED)

######################################## FIN FUNCIONES ########################################


######################### CONFIGURANDO LOS PARÁMETROS PARA LA VENTANA #########################
    root = tk.Tk()
    root.config(width=1366, height=728)
    root.title("[G13]OLC2 TytusDB Query tool ")


    # VENTANA PRINCIPAL
    frame = tk.Frame(root)
    frame.place(x=0, y=0, width=1366, height=500)


############################### BARRA DE MENÚS DE LA APLICACIÓN ###############################
    top = frame.winfo_toplevel()

    #DECLARACIÓN DE LA BARRA DE MENÚ
    menubar = tk.Menu(top,font='Helvetica 25 bold')


### MENÚ ARCHIVO
    menu_archivo = tk.Menu(menubar, tearoff=0)

    #SUB MENÚS PARA EL MENÚ ARCHIVO
    menu_archivo.add_command(label="Nuevo", command=__funcion_nuevo)
    menu_archivo.add_command(label="Abrir", command=__funcion_abrir)
    menu_archivo.add_command(label="Guardar", command=__funcion_guardar)
    menu_archivo.add_command(label="Guardar como", command=__funcion_guardar_como)
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=__funcion_cerrar)

    #CREACIÓN DEL MENÚ ARCHIVO INCRUSTANDO LOS SUBMENÚS
    menubar.add_cascade(label="Archivo", menu=menu_archivo)
    
    
### MENÚ ANALIZAR
    menu_analizar = tk.Menu(menubar, tearoff=0)

    #SUB MENÚS PARA EL MENÚ ANALIZAR
    menu_analizar.add_command(label="Analizar Entrada", command=__funcion_analizar)

    #CREACIÓN DEL MENÚ ANALIZAR INCRUSTANDO LOS SUBMENÚS
    menubar.add_cascade(label="Analizar", menu=menu_analizar)


    #SE AGREGA LA BARRA DE MENÚ A LA RAÍZ
    root.config(menu=menubar)


### MENÚ REPORTES
    menu_reporte = tk.Menu(menubar, tearoff=0)

    #SUB MENÚS PARA EL MENÚ ANALIZAR
    menu_reporte.add_command(label="AST", command=__funcion_analizar)
    menu_reporte.add_separator()
    menu_reporte.add_command(label="Errores Léxicos", command=__funcion_analizar)
    menu_reporte.add_command(label="Errores Sintácticos", command=__funcion_analizar)
    menu_reporte.add_command(label="Errores Semánticos", command=__funcion_analizar)
    

    #CREACIÓN DEL MENÚ ANALIZAR INCRUSTANDO LOS SUBMENÚS
    menubar.add_cascade(label="Reportes", menu=menu_reporte)


    #SE AGREGA LA BARRA DE MENÚ A LA RAÍZ
    root.config(menu=menubar)


####################################### EDITOR DE TEXTO #######################################

    # EDITOR DE TEXTO
    my_editor =  Example(frame)
    my_editor.pack(side="top", fill="both", expand=True)


    #ETIQUETAS PARA LA FILA Y COLUMNA ACTUAL

    fila = StringVar()
    colum = StringVar()

    filaL = tk.Label(frame, textvariable=fila)
    filaL.place(x=100,y=550,width=100,height=25)
    filaL.pack()

    columnaL = tk.Label(frame, textvariable=colum)
    columnaL.place(x=100,y=590, width=100,height=25)
    columnaL.pack()


######################################### CONSOLA #############################################

    consola = tk.Text(root,bg='black',fg='white',state=tk.DISABLED)
    consola.place(x=30,y=505,width=1330, height=140)
    

    root.mainloop()