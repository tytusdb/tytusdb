from tkinter import Tk, Text, BOTH, W, N, E, S, Menu
from tkinter.ttk import Frame, Button, Label, Style




class Example(Frame):

    def __init__(self):
        super().__init__()

        #Creacion de ventana

        self.master.title("TytusDB")
        self.pack(fill=BOTH, expand=True)


        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        self.lbl = Label(self, text="TytusDB")
        self.lbl.grid(sticky=W, pady=4, padx=5)

        #self.tab = self.LabelFrame(
        #self, text='Aquí se realizará la operación'
        #)


        # *************************** BARRA DE MENÚ ***************************
        menubar = Menu(self.master)
        self.master.filemenu = Menu(menubar, tearoff=0)
        self.master.filemenu.add_command(label="Nuevo")
        self.master.filemenu.add_command(label="Abrir")
        self.master.filemenu.add_command(label="Salir", command=self.master.quit)
        self.master.helpmenu = Menu(menubar, tearoff=0)
        self.master.helpmenu.add_command(label="Documentación")
        self.master.helpmenu.add_command(label="Acerca de...")
        self.master.servermenu = Menu(menubar, tearoff=0)
        self.master.servermenu.add_command(label="Nueva conexión")
        self.master.servermenu.add_command(label="Quitar conexión")
        self.master.herramientasMenu = Menu(menubar, tearoff=0)
        self.master.herramientasMenu.add_command(label="Query Tool", command=self.addQueryTool)
        menubar.add_cascade(label="Archivo", menu=self.master.filemenu)
        menubar.add_cascade(label="Servidor", menu=self.master.servermenu)
        menubar.add_cascade(label="Herramientas", menu=self.master.herramientasMenu)
        menubar.add_cascade(label="Ayuda", menu=self.master.helpmenu)
        self.master.config(menu=menubar);
        # *********************************************************************

    #Metodo agregar QueryTool
    def addQueryTool( self ):
        self.area = Text(self)
        self.area.grid(row=1, column=0, columnspan=2, rowspan=4,
                       padx=5, sticky=E + W + S + N)
        #self.lbl.configure(text="Cambia")

def main():
    root = Tk()
    app = Example()
    root.geometry("350x300+300+300")
    root.mainloop()




if __name__ == '__main__':
    main()