from tkinter import Tk, Text, BOTH, W, N, E, S, Menu
from tkinter.ttk import Frame, Button, Label, Style




class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("TytusDB")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="TytusDB")
        lbl.grid(sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4,
            padx=5, sticky=E+W+S+N)


def main():

    root = Tk()
    root.geometry("350x300+300+300")
    app = Example()

    # *************************** BARRA DE MENÚ ***************************    
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo")
    filemenu.add_command(label="Abrir")
    filemenu.add_command(label="Salir", command=root.quit)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Documentación")
    helpmenu.add_command(label="Acerca de...")
    servermenu = Menu(menubar, tearoff=0)
    servermenu.add_command(label="Nueva conexión")
    servermenu.add_command(label="Quitar conexión")
    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Servidor", menu=servermenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)
    root.config(menu=menubar)
    # *********************************************************************

    root.mainloop()


if __name__ == '__main__':
    main()