from tkinter import Label, Frame, Button, Tk, TOP, BOTTOM, RIGHT, LEFT, END, BOTH, CENTER, X, Y, W, SW, Scrollbar, \
    Listbox, \
    Grid, Entry, filedialog, messagebox, Toplevel
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from controller import Controller, Enums


class GUI(Frame):

    def __init__(self, master=None, val=0):
        super().__init__(master)
        self.master = master
        self.val = val
        self.parametros = []
        self.actions = Enums.actions
        self.controller = Controller()
        self.initComp()

    def initComp(self):
        self.master.title("EDD - TytusDB")
        self.master.iconbitmap('View/img/logo.ico')
        self.master.deiconify()
        self.centrar()
        if self.val == 1:
            self.main()
        elif self.val == 2:
            self.funciones()
        elif self.val == 3:
            self.reportes(self.controller)

    def centrar(self):
        if self.val == 1:
            ancho = 500
            alto = 500
        elif self.val == 2:
            ancho = 1045
            alto = 660
        else:
            ancho = 1150
            alto = 650
        x_ventana = self.winfo_screenwidth() // 2 - ancho // 2
        y_ventana = self.winfo_screenheight() // 2 - alto // 2
        posicion = str(ancho) + "x" + str(alto) + "+" + str(x_ventana) + "+" + str(y_ventana - 35)
        self.master.resizable(width=False, height=False)
        self.master.geometry(posicion)

    def ventanaFunciones(self):
        v2 = Toplevel()
        self.master.iconify()
        image = Image.open('View/img/function.png')
        background_image = ImageTk.PhotoImage(image.resize((1060, 680)))
        background_label = Label(v2, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        v2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(v2, self.master))
        app2 = GUI(master=v2, val=2)
        app2.mainloop()

    def ventanaReporte(self):
        v3 = Tk()
        self.master.iconify()
        v3['bg'] = "#0f1319"
        v3.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(v3, self.master))
        app3 = GUI(master=v3, val=3)
        app3.mainloop()

    @staticmethod
    def on_closing(win, root):
        if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
            win.destroy()
            root.deiconify()

    # region Menú principal
    def main(self):
        btnF = Button(text="FUNCIONES", bg="#33868a", bd=0, activebackground="#225b5e",
                      font="Arial 18", pady=12, width=14, command=lambda: self.ventanaFunciones())
        btnF.pack(side=TOP, pady=(150, 25))

        btnR = Button(text="REPORTES", bg="#33868a", bd=0, activebackground="#225b5e",
                      font="Arial 18", pady=12, width=14, command=lambda: self.ventanaReporte())
        btnR.pack(side=TOP, pady=(0, 25))

        btnS = Button(text="SALIR", bg="#bf4040", bd=0, activebackground="#924040",
                      font="Arial 18", pady=0, width=14, command=exit)
        btnS.pack(side=TOP, pady=(0, 25))

    # endregion

    # region Ventana de funciones
    def funciones(self):
        lbl1 = Label(self.master, text="Bases de datos", font=("Century Gothic", 21), bg="#0f1319", fg="#ffffff")
        lbl1.grid(row=1, column=0, padx=(60, 85), pady=(100, 25))

        lbl2 = Label(self.master, text="Tablas", font=("Century Gothic", 21), bg="#0f1319", fg="#ffffff")
        lbl2.grid(row=1, column=1, padx=(5, 0), columnspan=2, pady=(100, 25))

        lbl3 = Label(self.master, text="Tuplas", font=("Century Gothic", 21), bg="#0f1319", fg="#ffffff")
        lbl3.grid(row=1, column=3, padx=(130, 150), pady=(100, 25))

        # region Bases de datos
        btnCreateDB = Button(self.master,
                             text=self.actions[1],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=16,
                             command=lambda: self.simpleDialog(["database"], self.actions[1]))
        btnCreateDB.grid(row=2, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnshowDBS = Button(self.master,
                            text=self.actions[2],
                            bg="#abb2b9", font=("Courier New", 14),
                            borderwidth=0.5, pady=6, width=16,
                            command=lambda: self.controller.execute(None, self.actions[2]))
        btnshowDBS.grid(row=3, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnAlterDB = Button(self.master,
                            text=self.actions[3],
                            bg="#abb2b9", font=("Courier New", 14),
                            borderwidth=0.5, pady=6, width=16,
                            command=lambda: self.simpleDialog(["databaseOld", "databaseNew"], self.actions[3]))
        btnAlterDB.grid(row=4, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnDropDB = Button(self.master,
                           text=self.actions[4],
                           bg="#abb2b9", font=("Courier New", 14),
                           borderwidth=0.5, pady=6, width=16,
                           command=lambda: self.simpleDialog(["database"], self.actions[4]))
        btnDropDB.grid(row=5, column=0, sticky=W, padx=(70, 0), pady=(0, 25))
        # endregion

        # region Tablas
        btnCreateTb = Button(self.master,
                             text=self.actions[5],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=15,
                             command=lambda: self.simpleDialog(["database", "tableName", "numberColumns"],
                                                               self.actions[5]))
        btnCreateTb.grid(row=2, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnDefinePK = Button(self.master,
                             text=self.actions[9],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=15,
                             command=lambda: self.simpleDialog(["database", "table", "columns"], self.actions[9]))
        btnDefinePK.grid(row=3, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnDropPK = Button(self.master,
                           text=self.actions[10],
                           bg="#abb2b9", font=("Courier New", 14),
                           borderwidth=0.5, pady=6, width=15,
                           command=lambda: self.simpleDialog(["database", "table"], self.actions[10]))
        btnDropPK.grid(row=4, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnShowTb = Button(self.master,
                           text=self.actions[6],
                           bg="#abb2b9", font=("Courier New", 14),
                           borderwidth=0.5, pady=6, width=15,
                           command=lambda: self.simpleDialog(["database"], self.actions[6]))
        btnShowTb.grid(row=5, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnAlterTb = Button(self.master,
                            text=self.actions[13],
                            bg="#abb2b9", font=("Courier New", 14),
                            borderwidth=0.5, pady=6, width=15,
                            command=lambda: self.simpleDialog(["database", "tableOld", "tableNew"], self.actions[13]))
        btnAlterTb.grid(row=6, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnDropTb = Button(self.master,
                           text=self.actions[16],
                           bg="#abb2b9", font=("Courier New", 14),
                           borderwidth=0.5, pady=6, width=15,
                           command=lambda: self.simpleDialog(["database", "tableName"], self.actions[16]))
        btnDropTb.grid(row=2, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        btnAlterAdd = Button(self.master,
                             text=self.actions[14],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=15,
                             command=lambda: self.simpleDialog(["database", "tableName", "default"],
                                                               self.actions[14]))
        btnAlterAdd.grid(row=3, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        btnAlterDrop = Button(self.master,
                              text=self.actions[15],
                              bg="#abb2b9", font=("Courier New", 14),
                              borderwidth=0.5, pady=6, width=15,
                              command=lambda: self.simpleDialog(["database", "tableName", "columnNumber"],
                                                                self.actions[15]))
        btnAlterDrop.grid(row=4, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        btnExtractTb = Button(self.master,
                              text=self.actions[7],
                              bg="#abb2b9", font=("Courier New", 14),
                              borderwidth=0.5, pady=6, width=15,
                              command=lambda: self.simpleDialog(["database", "table"], self.actions[7]))
        btnExtractTb.grid(row=5, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        btnExtractRangeTb = Button(self.master,
                                   text=self.actions[8],
                                   bg="#abb2b9", font=("Courier New", 14),
                                   borderwidth=0.5, pady=6, width=15,
                                   command=lambda: self.simpleDialog(["database", "table", "lower", "upper"],
                                                                     self.actions[8]))
        btnExtractRangeTb.grid(row=6, column=2, sticky=W, padx=(5, 0), pady=(0, 25))
        # endregion

        # region Tuplas:
        btnInsertTp = Button(self.master,
                             text=self.actions[17],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=12,
                             command=lambda: self.simpleDialog(["database", "table", "register"], self.actions[17]))
        btnInsertTp.grid(row=2, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        btnLoadfile = Button(self.master,
                             text=self.actions[18],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=12,
                             command=lambda: self.simpleDialog(["file", "database", "table"], self.actions[18]))
        btnLoadfile.grid(row=3, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        btnExtractTp = Button(self.master,
                              text=self.actions[19],
                              bg="#abb2b9", font=("Courier New", 14),
                              borderwidth=0.5, pady=6, width=12,
                              command=lambda: self.simpleDialog(["database", "table", "id"], self.actions[19]))
        btnExtractTp.grid(row=4, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        btnUpdateTp = Button(self.master,
                             text=self.actions[20],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=12,
                             command=lambda: self.simpleDialog(["database", "table", "register", "columns"],
                                                               self.actions[20]))
        btnUpdateTp.grid(row=5, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        btnDeleteTp = Button(self.master,
                             text=self.actions[21],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=12,
                             command=lambda: self.simpleDialog(["database", "tableName", "columns"], self.actions[21]))
        btnDeleteTp.grid(row=6, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        btnTruncateTp = Button(self.master,
                               text=self.actions[22],
                               bg="#abb2b9", font=("Courier New", 14),
                               borderwidth=0.5, pady=6, width=12,
                               command=lambda: self.simpleDialog(["database", "tableName"], self.actions[22]))
        btnTruncateTp.grid(row=7, column=3, sticky=W, padx=(110, 0), pady=(0, 25))

        # endregion

    # endregion

    # region Ventana de reporte
    def reportes(self, controller):
        self.controller = controller

        self.titulo3 = Label(self.master, text="Árbol AVL", bg="#0f1319", fg="#45c2c5",
                             font=("Century Gothic", 42), pady=12)
        self.titulo3.pack(fill=X)

        self.scrollbar = Scrollbar(self.master)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.master, yscrollcommand=self.scrollbar.set, height=21, width=20,
                               bg="#0f1319", bd=0, fg='#ffffff', font=("Century Gothic", 12))
        self.listbox.pack(side=LEFT, padx=(60, 0))
        self.scrollbar.config(command=self.listbox.yview)

        self.panel = Label(self.master, bg="#ffffff", height=25, width=110)
        self.panel.pack(side=TOP, pady=(100, 0))

        self.desplegarDB(controller)
        self.listbox.bind("<<ListboxSelect>>", self.displayData)

        self.tableList = Combobox(self.master, state="readonly")
        self.tableList.place(x=450, y=130)
        self.tableList.bind("<<ComboboxSelected>>", self.displayTableData)

        self.tuplelist = Combobox(self.master, state="readonly")
        self.tuplelist.place(x=850, y=130)
        self.tuplelist.bind("<<ComboboxSelected>>", self.tupleMode)

        self.opcion = 0

    # endregion

    # region Digitador
    def simpleDialog(self, args, action):
        self.parametros.clear()
        tmp = []
        dialog = Tk()
        dialog['bg'] = "#0f1319"
        dialog.title(action)
        dialog.resizable(False, False)
        dialog.update()
        dialog.deiconify()
        dim = len(args)
        for i in range(dim):
            Label(dialog, text=args[i] + ":", bg="#0f1319", fg="#ffffff", font=("Century Gothic", 12)
                  ).grid(row=i, padx=(12, 1), pady=(2, 2), sticky=SW)

        if args[0] == "file":
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
        tmp[0].focus_set()
        dialog.bind('<Return>', lambda event=None: self.ejecutar(dialog, tmp, action))
        dialog.bind('<Escape>', lambda event=None: dialog.destroy())
        submit = Button(dialog, text="OK", bg="#45c2c5", bd=0, pady=6, width=10,
                        command=lambda: self.ejecutar(dialog, tmp, action))
        submit.grid(row=dim + 1, columnspan=2, pady=(8, 10))
        dialog.mainloop()

    # endregion

    def cargarArchivo(self, btn):
        filename = filedialog.askopenfilename(filetypes=[("csv files", "*.csv")])
        if filename:
            self.parametros.append(filename)
            btn.configure(text=filename[filename.rfind('/') + 1:])

    def ejecutar(self, dialog, args, action):
        for arg in args:
            if arg.get():
                self.parametros.append(arg.get())
            else:
                return messagebox.showerror("Oops", "Existen campos vacíos")
        response = self.controller.execute(self.parametros, action)
        if response in range(1, 7):
            return messagebox.showerror("Error número: " + str(response),
                                        "Ocurrió un error en la operación.\nAsegúrese de introducir datos correctos")
        messagebox.showinfo("Siuu", "Proceso realizado con éxito")
        dialog.destroy()

    def desplegarDB(self, controller):
        dbList = controller.execute(None, "Show DB")
        for i in dbList:
            self.listbox.insert(END, str(i))

    def displayData(self, event):
        selection = event.widget.curselection()
        data = ""
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            self.titulo3.configure(text=data)
        dbList = self.controller.execute(None, "Show DB")
        for db in dbList:
            if db == str(data):
                self.tableList["values"] = self.controller.execute([db], "Show Tables")
                if len(self.tableList["values"]) > 0:
                    self.tableList.current(0)
                break

    def displayTableData(self, event):
        db =str(self.titulo3["text"])
        tb =  str(self.tableList.get())
        tp = self.controller.execute([db, tb], "Extract Table")
        self.tuplelist["values"] = tp
        # graficar tabla

    def tupleMode(self, event):
            # graficar la tupla


def run():
    v1 = Tk()
    image = Image.open('View/img/main.png')
    background_image = ImageTk.PhotoImage(image.resize((500, 500)))
    background_label = Label(v1, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    app = GUI(master=v1, val=1)
    app.mainloop()


#run()
