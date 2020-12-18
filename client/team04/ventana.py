import tkinter as tk
from tkinter import Menu, Tk, Text, DISABLED, RAISED,Frame, FLAT, Button, Scrollbar, Canvas, END
from tkinter import messagebox as MessageBox
from tkinter import ttk

class TextLineNumbers(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
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

class CustomText(Text):
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

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

class Campo(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.vsb = Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)
        self.vsb.pack(side="right", fill="y")

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()

class Arbol(Frame):
    
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            background = "silver",
            foreground = "black",
            fieldbackground = "silver"
            )
        self.file_image = tk.PhotoImage(file="file.png")
        self.file_image = self.file_image.subsample(35)
        self.folder_image = tk.PhotoImage(file="folder.png")
        self.folder_image = self.folder_image.subsample(38)

        self.treeview = ttk.Treeview(self)
        self.treeview.heading("#0", text="Navegador")
        item = self.treeview.insert("", END, text="Bases de datos")
        subitem = self.treeview.insert(item, END, text="Amazon",image=self.folder_image)
        self.treeview.insert(subitem, END, text="Empleado",image=self.file_image)
        self.treeview.insert(subitem, END, text="Cliente",image=self.file_image)
        self.treeview.insert(subitem, END, text="Producto",image=self.file_image)
        subitem = self.treeview.insert(item, END, text="Aurora",image=self.folder_image)
        self.treeview.pack(side="top", fill="both", expand=True)
        self.pack(side="top", fill="both", expand=True)

def abrirDoc():
    MessageBox.showinfo(title="Aviso",message="Hizo clic en abrir documento")

def CrearVentana():
    raiz = Tk()
    raiz.title("TytuSQL") #Cambiar el nombre de la ventana
    raiz.iconbitmap('icon.ico')
    raiz.rowconfigure(0, minsize=800, weight=1)
    raiz.columnconfigure(1, minsize=800, weight=1)
    
    ########### menu ############
    #Se crea la barra
    barraDeMenu=Menu(raiz, tearoff=0,relief=FLAT, font=("Verdana", 12),activebackground='red')
    #Se crean los menus que se deseen
    archivo=Menu(barraDeMenu, tearoff=0)
    #Crear las opciones de la opción del menú
    archivo.add_command(label="Nueva ventana", command=CrearVentana)
    archivo.add_command(label="Abrir un documento",command=abrirDoc)
    archivo.add_command(label="Abrir un modelo")
    archivo.add_separator()
    archivo.add_command(label="Nueva Query")
    archivo.add_command(label="Guardar como...")
    archivo.add_command(label="Guardar")
    archivo.add_separator()
    archivo.add_command(label="Salir")
    #creando el Editar
    editar=Menu(barraDeMenu, tearoff=0)
    #agregando su lista
    editar.add_command(label="Cortar")
    editar.add_command(label="Pegar")
    editar.add_command(label="Copiar")
    editar.add_separator()
    editar.add_command(label="Seleccionar todo")
    editar.add_command(label="Formato")
    editar.add_command(label="Preferencias")
    #se agrega Tools
    tools=Menu(barraDeMenu, tearoff=0)
    #se agrega su lista
    tools.add_command(label="Configuración")
    tools.add_command(label="Utilidades")
    #se agrega ayuda
    ayuda=Menu(barraDeMenu, tearoff=0)
    #lista de ayuda
    ayuda.add_command(label="Documentación de TytuSQL")
    ayuda.add_command(label="Acerca de TytuSQL")
    #Se agrgan los menús a la barra
    barraDeMenu.add_cascade(label="Archivo",menu=archivo)
    barraDeMenu.add_cascade(label="Editar",menu=editar)
    barraDeMenu.add_cascade(label="Herramientas",menu=tools)
    barraDeMenu.add_cascade(label="Ayuda",menu=ayuda)
    #Se indica que la barra de menú debe estar en la ventana
    raiz.config(menu=barraDeMenu, background='silver')

    FrameIzquiero = Frame(raiz, relief=RAISED, bd=2)
    FrameIzquiero.pack(side="left", fill="both")
    Arbol(FrameIzquiero)

    # Posicionarla en la ventana..

    Button(raiz, text="Enviar Consulta").pack(side="top",fill="both")
    consola = Text(raiz)
    consola.pack(side="bottom",fill="both")
    consola.insert(1.0,"Consola de Salida")
    consola.config(state=DISABLED)
    Campo(raiz).pack(side="right", fill="both", expand=True)
    
    ###### CREAMOS EL PANEL PARA LAS PESTAÑAS ########
    raiz.mainloop()

def main():
    CrearVentana()

if __name__ == "__main__":
    main()
