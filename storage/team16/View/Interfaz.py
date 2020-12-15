import sys
import os
sys.path.append(os.path.abspath('.'))

from tkinter import Label, Frame, Button, Tk, TOP, BOTTOM, RIGHT, LEFT, END, BOTH, CENTER, X, Y, W, SW, Scrollbar, \
    Listbox, \
    Grid, Entry, filedialog, messagebox, Toplevel
from PIL import Image, ImageTk
from controller import Controller


class GUI(Frame):

    def __init__(self, master=None, val=0):
        super().__init__(master)
        self.master = master
        self.val = val
        self.parametros = []
        self.initComp()
        self.controlador = Controller()

    def initComp(self):
        self.master.title("EDD - TytusDB")
        self.master.iconbitmap('img/logo.ico')
        self.master.deiconify()
        self.centrar()
        if self.val == 1:
            self.agregarComp()
        elif self.val == 2:
            self.agregarComp2()
        elif self.val == 3:
            self.agregarComp3()

    def ventanaFunciones(self):
        self.master.iconify()
        v2 = Toplevel()
        image = Image.open('img/function.png')
        background_image = ImageTk.PhotoImage(image.resize((1070, 600)))
        background_label = Label(v2, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        v2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(v2, self.master))
        app2 = GUI(master=v2, val=2)
        app2.mainloop()

    def ventanaReporte(self):
        self.master.iconify()
        v3 = Tk()
        v3['bg'] = "#0f1319"
        v3.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(v3, self.master))
        app3 = GUI(master=v3, val=3)
        app3.mainloop()

    @staticmethod
    def on_closing(win, root):
        if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
            win.destroy()
            root.deiconify()

    def centrar(self):
        if self.val == 1:
            ancho = 500
            alto = 500
        elif self.val == 2:
            ancho = 1045
            alto = 590
        else:
            ancho = 1150
            alto = 650
        x_ventana = self.winfo_screenwidth() // 2 - ancho // 2
        y_ventana = self.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(x_ventana) + "+" + str(y_ventana - 35)
        self.master.resizable(width=False, height=False)
        self.master.geometry(posicion)

    # Menu principal
    def agregarComp(self):
        self.btn2 = Button(self.master, text="FUNCIONES", bg="#33868a", activebackground="#225b5e",
                           bd=0, font="Arial 18", pady=12, width=14, command=lambda: self.ventanaFunciones())
        self.btn2.pack(side=TOP, pady=(150, 25))

        self.btn3 = Button(self.master, text="REPORTES", bg="#33868a", activebackground="#225b5e", font="Arial 18",
                           bd=0, pady=12, width=14, command=lambda: self.ventanaReporte())
        self.btn3.pack(side=TOP, pady=(0, 25))

        self.btnSalir = Button(self.master, text="SALIR", bg="#bf4040", activebackground="#924040", font="Arial 18",
                               bd=0, pady=0, width=14, command=exit)
        self.btnSalir.pack(side=TOP, pady=(0, 25))

    # Ventana de funciones
    def agregarComp2(self):
        lbl1 = Label(self.master, text="Bases de datos", font=("Century Gothic", 21), bg="#0f1319", fg="#ffffff")
        lbl1.grid(row=1, column=0, padx=(60, 85), pady=(100, 25))

        lbl2 = Label(self.master, text="Tablas", font=("Century Gothic", 21), bg="#0f1319", fg="#ffffff")
        lbl2.grid(row=1, column=1, padx=(8, 0), columnspan=2, pady=(100, 25))

        lbl3 = Label(self.master, text="Tuplas", font=("Century Gothic", 21), bg="#0f1319", fg="#ffffff")
        lbl3.grid(row=1, column=3, padx=(130, 150), pady=(100, 25))

        # Bases de datos
        btnCreateDB = Button(self.master,
                             text="Create database",
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=16,
                             command=lambda: self.simpleDialog(["database"], "Create DB"))
        btnCreateDB.grid(row=2, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnshowDBS = Button(self.master,
                            text="Show databases",
                            bg="#abb2b9", font=("Courier New", 14),
                            borderwidth=0.5, pady=6, width=16,
                            command=lambda: self.controlador.ejectutarFuncion("Show DB", None))
        btnshowDBS.grid(row=3, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnAlterDB = Button(self.master,
                            text="Alter database",
                            bg="#abb2b9", font=("Courier New", 14),
                            borderwidth=0.5, pady=6, width=16,
                            command=lambda: self.simpleDialog(["databaseOld", "databaseNew"], "Alter database"))
        btnAlterDB.grid(row=4, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnDropDB = Button(self.master,
                           text="Drop database",
                           bg="#abb2b9", font=("Courier New", 14),
                           borderwidth=0.5, pady=6, width=16,
                           command=lambda: self.simpleDialog(["database"], "Drop DB"))
        btnDropDB.grid(row=5, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnLoadfile = Button(self.master,
                             text="Load CSV",
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=16,
                             command=lambda: self.simpleDialog(["file", "database", "table"], "Load file"))
        btnLoadfile.grid(row=6, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        # Tablas
        btnCreateTb = Button(self.master,
                             text="Create table",
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=15,
                             command=lambda: self.simpleDialog(["database", "tableName", "numberColumns"],
                                                               "Create table"))
        btnCreateTb.grid(row=2, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnDefinePK = Button(self.master,
                             text="Define PK",
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=15,
                             command=lambda: self.simpleDialog(["database", "table", "columns"], "Define PK"))
        btnDefinePK.grid(row=3, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnDefineFK = Button(self.master,
                             text="Define FK",
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=15,
                             command=lambda: self.simpleDialog(["database", "table", "references"], "Define FK"))
        btnDefineFK.grid(row=4, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnShowTb = Button(self.master,
                           text="Show tables",
                           bg="#abb2b9", font=("Courier New", 14),
                           borderwidth=0.5, pady=6, width=15,
                           command=lambda: self.simpleDialog(["database"], "Show tables"))
        btnShowTb.grid(row=5, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnAlterTb = Button(self.master,
                            text="Alter table",
                            bg="#abb2b9", font=("Courier New", 14),
                            borderwidth=0.5, pady=6, width=15,
                            command=lambda: self.simpleDialog(["database", "tableOld", "tableNew"], "Alter table"))
        btnAlterTb.grid(row=6, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnDropTb = Button(self.master,
                           text="Drop table",
                           bg="#abb2b9", font=("Courier New", 14),
                           borderwidth=0.5, pady=6, width=15,
                           command=lambda: self.simpleDialog(["database", "tableName"], "Drop table"))
        btnDropTb.grid(row=2, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        btnAlterAdd = Button(self.master,
                             text="Alter add",
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=15,
                             command=lambda: self.simpleDialog(["database", "tableName", "columnName"], "Alter add"))
        btnAlterAdd.grid(row=3, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        btnAlterDrop = Button(self.master,
                              text="Alter drop",
                              bg="#abb2b9", font=("Courier New", 14),
                              borderwidth=0.5, pady=6, width=15,
                              command=lambda: self.simpleDialog(["database", "tableName", "columnNumber"],
                                                                "Alter drop"))
        btnAlterDrop.grid(row=4, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        btnExtractTb = Button(self.master,
                              text="Extract table",
                              bg="#abb2b9", font=("Courier New", 14),
                              borderwidth=0.5, pady=6, width=15,
                              command=lambda: self.simpleDialog(["database", "table"], "Extract table"))
        btnExtractTb.grid(row=5, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        btnExtractRangeTb = Button(self.master,
                                   text="Extract range",
                                   bg="#abb2b9", font=("Courier New", 14),
                                   borderwidth=0.5, pady=6, width=15,
                                   command=lambda: self.simpleDialog(["database", "table", "lower", "upper"],
                                                                     "Extract range table"))
        btnExtractRangeTb.grid(row=6, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        # Tuplas:
        btnInsertTp = Button(self.master,
                             text="Insert",
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=12,
                             command=lambda: self.simpleDialog(["database", "table", "columns"], "Insertar"))
        btnInsertTp.grid(row=2, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        btnUpdateTp = Button(self.master,
                             text="Update",
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=12,
                             command=lambda: self.simpleDialog(["database", "table", "id", "columnNumber", "value"],
                                                               "Actualizar valor"))
        btnUpdateTp.grid(row=3, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        btnDeleteTp = Button(self.master,
                             text="Delete",
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=12,
                             command=lambda: self.simpleDialog(["database", "tableName", "id"], "Eliminar registro"))
        btnDeleteTp.grid(row=4, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        btnTruncateTp = Button(self.master,
                               text="Truncate",
                               bg="#abb2b9", font=("Courier New", 14),
                               borderwidth=0.5, pady=6, width=12,
                               command=lambda: self.simpleDialog(["database", "tableName"], "Vaciar tabla"))
        btnTruncateTp.grid(row=5, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        btnExtractTp = Button(self.master,
                              text="Extract",
                              bg="#abb2b9", font=("Courier New", 14),
                              borderwidth=0.5, pady=6, width=12,
                              command=lambda: self.simpleDialog(["database", "table", "id"], "Extraer tupla"))
        btnExtractTp.grid(row=6, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

    # Digitador
    def simpleDialog(self, params, fun):
        self.parametros.clear()
        tmp = []
        dialog = Tk()
        dialog['bg'] = "#0f1319"
        dialog.title(fun)
        dim = len(params)
        for i in range(dim):
            Label(dialog, text=params[i] + ":", bg="#0f1319", fg="#ffffff", font=("Century Gothic", 12)
                  ).grid(row=i, padx=(12, 1), pady=(2, 2), sticky=SW)
        if params[0] == "file":
            btnFile = Button(dialog, text="Examinar...", command=lambda: self.cargarArchivo(btnFile))
            btnFile.grid(row=0, column=1, pady=(15, 2), padx=(0, 18), sticky="ew")
            for j in range(dim - 1):
                entry = Entry(dialog)
                entry.grid(row=j + 1, column=1, padx=(0, 18))
                tmp.append(entry)
        else:
            for j in range(dim):
                entry = Entry(dialog)
                entry.grid(row=j, column=1, padx=(0, 18))
                tmp.append(entry)

        submit = Button(dialog, text="OK", bg="#45c2c5",
                        borderwidth=0.5, pady=6, width=10,
                        command=lambda: self.ejecutar(tmp, dialog, fun))
        submit.grid(row=dim + 1, columnspan=2, pady=(8, 10))
        dialog.mainloop()

    def cargarArchivo(self, btn):
        filename = filedialog.askopenfilename(filetypes=[("csv files", "*.csv")])
        if filename:
            self.parametros.append(filename)
            btn.configure(text=filename[filename.rfind('/') + 1:])

    def ejecutar(self, params, dialog, fun):
        for param in params:
            self.parametros.append(param.get())
        dialog.destroy()
        retorno = self.controlador.ejectutarFuncion(fun, self.parametros)
        if retorno == 1 or retorno == 2 or retorno == 3:
            messagebox.showerror("Error número: " + str(retorno),
                                 "Ocurrió un error en la operación.\nAsegúrese de introducir datos correctos")

    # Ventana de reporte
    def agregarComp3(self):
        self.titulo3 = Label(self.master, text="Árbol AVL", bg="#0f1319", fg="#45c2c5", font=("Century Gothic", 42),
                             pady=12)
        self.titulo3.pack(fill=X)

        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.master, yscrollcommand=self.scrollbar.set, height=21, width=20, bg="#ecf0f1",
                               font=("Century Gothic", 12))
        self.listbox.pack(side=LEFT, padx=(60, 0))
        self.scrollbar.config(command=self.listbox.yview)

        self.panel = Label(self.master, bg="#ecf0f1", height=31, width=110)
        self.panel.pack(side=TOP, pady=(40, 0))

        self.desplegarDB()
        self.listbox.bind("<<ListboxSelect>>", self.displayData)

    def desplegarDB(self):
        for i in range(1, 26, 1):
            self.listbox.insert(END, "Base de datos " + str(i))

    def displayData(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            self.titulo3.configure(text=data)


def run():
    v1 = Tk()
    image = Image.open('img/main.png')
    background_image = ImageTk.PhotoImage(image.resize((500, 500)))
    background_label = Label(v1, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    app = GUI(master=v1, val=1)
    app.mainloop()


run()
