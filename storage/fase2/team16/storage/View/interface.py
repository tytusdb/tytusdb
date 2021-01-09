# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from tkinter import Label, Frame, Button, Tk, TOP, BOTTOM, RIGHT, LEFT, END, BOTH, CENTER, X, Y, W, SW, ALL, \
    Scrollbar, Listbox, Grid, Entry, filedialog, messagebox, Toplevel, Canvas
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from .controller import Controller, Enums


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
        self.master.iconbitmap('storage/View/img/logo.ico')
        self.master.deiconify()
        self.centrar()
        if self.val == 1:
            self.main()
        elif self.val == 2:
            self.funciones()
        elif self.val == 3:
            self.reportes()
        elif self.val == 4:
            self.blockchain()
        elif self.val == 5:
            self.grafos()

    def centrar(self):
        if self.val == 1:
            ancho = 500
            alto = 560
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
        image = Image.open('storage/View/img/function.png')
        background_image = ImageTk.PhotoImage(image.resize((1060, 680)))
        background_label = Label(v2, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        v2.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(v2, self.master))
        app2 = GUI(master=v2, val=2)
        app2.mainloop()

    def ventanaReporte(self):
        v3 = Toplevel()
        self.master.iconify()
        v3['bg'] = "#0f1319"
        v3.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(v3, self.master))
        app3 = GUI(master=v3, val=3)
        app3.mainloop()
    
    def ventanaBlockhchain(self):
        v4 = Toplevel()
        self.master.iconify()
        v4['bg'] = "#0f1319"
        v4.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(v4, self.master))
        app4 = GUI(master=v4, val=4)
        app4.mainloop()
    
    def ventanaGrafos(self):
        v5 = Toplevel()
        self.master.iconify()
        v5['bg'] = "#0f1319"
        v5.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(v5, self.master))
        app5 = GUI(master=v5, val=5)
        app5.mainloop()

    @staticmethod
    def on_closing(win, root):
        if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
            win.destroy()
            root.deiconify()

    def _on_mousewheel(self, event):
        try:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        except:
            pass

    # region Menú principal
    def main(self):
        btnF = Button(text="FUNCIONES", bg="#33868a", bd=0, activebackground="#225b5e",
                      font="Arial 18", pady=12, width=14, command=lambda: self.ventanaFunciones())
        btnF.pack(side=TOP, pady=(127, 25))

        btnR = Button(text="REPORTES", bg="#33868a", bd=0, activebackground="#225b5e",
                      font="Arial 18", pady=12, width=14, command=lambda: self.ventanaReporte())
        btnR.pack(side=TOP, pady=(0, 25))

        btnB = Button(text="BLOCKCHAIN", bg="#33868a", bd=0, activebackground="#225b5e",
                      font="Arial 18", pady=12, width=14, command=lambda: self.ventanaBlockhchain())
        btnB.pack(side=TOP, pady=(0, 25))

        btnB = Button(text="GRAFOS", bg="#33868a", bd=0, activebackground="#225b5e",
                      font="Arial 18", pady=12, width=14, command=lambda: self.ventanaGrafos())
        btnB.pack(side=TOP, pady=(0, 25))

        btnS = Button(text="SALIR", bg="#bf4040", bd=0, activebackground="#924040",
                      font="Arial 18", pady=0, width=14, command=lambda: self.master.destroy())
        btnS.pack(side=TOP, pady=(0, 0))
        
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
                             command=lambda: self.simpleDialog(["database", "mode", "encoding"], self.actions[1]))
        btnCreateDB.grid(row=2, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnAlterMode = Button(self.master,
                             text=self.actions[24],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=16,
                             command=lambda: self.simpleDialog(["database", "mode"], self.actions[24]))
        btnAlterMode.grid(row=3, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnshowDBS = Button(self.master,
                            text=self.actions[2],
                            bg="#abb2b9", font=("Courier New", 14),
                            borderwidth=0.5, pady=6, width=16,
                            command=lambda: self.controller.execute(None, self.actions[2]))
        btnshowDBS.grid(row=4, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnAlterDB = Button(self.master,
                            text=self.actions[3],
                            bg="#abb2b9", font=("Courier New", 14),
                            borderwidth=0.5, pady=6, width=16,
                            command=lambda: self.simpleDialog(["databaseOld", "databaseNew"], self.actions[3]))
        btnAlterDB.grid(row=5, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnDropDB = Button(self.master,
                           text=self.actions[4],
                           bg="#abb2b9", font=("Courier New", 14),
                           borderwidth=0.5, pady=6, width=16,
                           command=lambda: self.simpleDialog(["database"], self.actions[4]))
        btnDropDB.grid(row=6, column=0, sticky=W, padx=(70, 0), pady=(0, 25))

        btnFormat = Button(self.master,
                           text=self.actions[23],
                           bg="#abb2b9", font=("Courier New", 14),
                           borderwidth=0.5, pady=6, width=16,
                           command=lambda: self.controller.execute(None, self.actions[23]))
        btnFormat.grid(row=7, column=0, sticky=W, padx=(70, 0), pady=(0, 25))
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

        btnAlterTBMode = Button(self.master,
                             text=self.actions[25],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=15,
                             command=lambda: self.simpleDialog(["database", "table", "mode"], self.actions[25]))
        btnAlterTBMode.grid(row=6, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

        btnTBCompress = Button(self.master,
                             text=self.actions[26],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=15,
                             command=lambda: self.simpleDialog(["database", "table", "level"], self.actions[26]))
        btnTBCompress.grid(row=7, column=1, sticky=W, padx=(10, 0), pady=(0, 25))

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
                                   command=lambda: self.simpleDialog(["database", "table", "column", "lower", "upper"],
                                                                     self.actions[8]))
        btnExtractRangeTb.grid(row=6, column=2, sticky=W, padx=(5, 0), pady=(0, 25))

        btnDecompressTb = Button(self.master,
                                   text=self.actions[27],
                                   bg="#abb2b9", font=("Courier New", 14),
                                   borderwidth=0.5, pady=6, width=15,
                                   command=lambda: self.simpleDialog(["database", "table"],
                                                                     self.actions[27]))
        btnDecompressTb.grid(row=7, column=2, sticky=W, padx=(5, 0), pady=(0, 25))
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
    def reportes(self):
        self.titulo3 = Label(self.master, text="Reporte bases de datos", bg="#0f1319", fg="#45c2c5",
                             font=("Century Gothic", 42), pady=12)
        self.titulo3.pack(fill=X)

        self.scrollbarY = Scrollbar(self.master)
        self.scrollbarY.pack(side=RIGHT, fill=Y)

        self.scrollbarX = Scrollbar(self.master, orient='horizontal')
        self.scrollbarX.pack(side=BOTTOM, fill=X)

        self.listbox = Listbox(self.master, height=21, width=20,
                               bg="#0f1319", bd=0, fg='#ffffff', font=("Century Gothic", 12))
        self.listbox.place(x=65, y=122)

        self.listbox.bind("<<ListboxSelect>>", self.displayDBData)

        self.tableList = Combobox(self.master, state="readonly", width=30, font=("Century Gothic", 12))
        self.tableList.place(x=435, y=120)
        self.tableList.set('Seleccione tabla...')
        self.tableList.bind("<<ComboboxSelected>>", self.displayTableData)

        self.tuplelist = Combobox(self.master, state="readonly", width=30, font=("Century Gothic", 12))
        self.tuplelist.place(x=770, y=120)
        self.tuplelist.set('Seleccione tupla...')
        self.tuplelist.bind("<<ComboboxSelected>>", self.displayTupleData)

        self.canvas = Canvas(self.master, width=740, height=415, bg="#0f1319", highlightthickness=0)
        self.canvas.place(x=320, y=170)
        # self.canvas.config(xscrollcommand=self.scrollbarX.set, yscrollcommand=self.scrollbarY.set)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.scrollbarY.config(command=self.canvas.yview)
        self.scrollbarX.config(command=self.canvas.xview)

        self.desplegarDB()

    # Mostrar lista de base de datos
    def desplegarDB(self):
        try:
            dblist = self.controller.execute(None, self.actions[2])
            if dblist:
                for db in dblist:
                    self.listbox.insert(END, str(db))
                png = self.controller.reportDB()
                bg_DB = ImageTk.PhotoImage(Image.open(png))
                self.image_on_canvas = self.canvas.create_image(370, 207, anchor=CENTER, image=bg_DB)
                self.master.mainloop()
            else:
                messagebox.showwarning('Operación imposible','No se encuentran bases de datos\ndisponibles para desplegar el reporte.')
        except:
            None

    # Mostrar lista de tablas
    def displayDBData(self, event):
        try:
            selection = event.widget.curselection()
            data = ""
            tmp = []
            if selection:
                self.tableList.set('Seleccione tabla...')
                self.tuplelist.set('Seleccione tupla...')
                index = selection[0]
                data = event.widget.get(index)
                self.titulo3.configure(text=data)
                tmp.append(data)
                dbList = self.controller.execute(tmp, self.actions[6])
                self.tableList["values"] = dbList
                png = self.controller.reportTBL(data)
                bg_TBL = ImageTk.PhotoImage(Image.open(png))
                self.canvas.itemconfig(self.image_on_canvas, image=bg_TBL)
                self.canvas.config(xscrollcommand=self.scrollbarX.set, yscrollcommand=self.scrollbarY.set)
                self.canvas.config(scrollregion=self.canvas.bbox(ALL))
                self.master.mainloop()
        except:
            None

    # Mostrar AVL de tabla
    def displayTableData(self, event):
        try:
            self.tuplelist.set('Seleccione tupla...')
            db = str(self.titulo3["text"])
            tb = str(self.tableList.get())
            tp = self.controller.getIndexes(db, tb)
            tmp = []
            for i in tp:
                txt = ",".join(str(x) for x in i)
                tmp.append(txt)
            self.tuplelist["values"] = tmp
            png = self.controller.reportMode(db, tb)
            bg_AVL = ImageTk.PhotoImage(Image.open(png))
            self.canvas.itemconfig(self.image_on_canvas, image=bg_AVL)
            self.canvas.config(xscrollcommand=self.scrollbarX.set, yscrollcommand=self.scrollbarY.set)
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))
            self.master.mainloop()
        except:
            None

    # Mostrar tupla
    def displayTupleData(self, event):
        try:
            tp = str(self.tuplelist.get())
            png = self.controller.reportTPL(tp)  # le envío el índice del árbol (tp)
            bg_TPL = ImageTk.PhotoImage(Image.open(png))
            self.canvas.itemconfig(self.image_on_canvas, image=bg_TPL)
            self.canvas.config(xscrollcommand=self.scrollbarX.set, yscrollcommand=self.scrollbarY.set)
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))
            self.master.mainloop()
        except:
            None

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
                dialog.destroy()
                return messagebox.showerror("Oops", "Existen campos vacíos")
        response = self.controller.execute(self.parametros, action)
        if response in range(1, 8):
            self.parametros.clear()
            dialog.destroy()
            return messagebox.showerror("Error número: " + str(response),
                                        "Ocurrió un error en la operación.\nAsegúrese de introducir datos correctos")
        elif action == self.actions[28] or action == self.actions[29]:
            if response:
                g = 'graphDSD' if action == self.actions[28] else 'graphDF'
                dialog.destroy()
                self.displayGraph(g)
            else:
                dialog.destroy()
                return messagebox.showerror("Error " + str(response),
                                        "Ocurrió un error en la operación.\nAsegúrese de introducir datos correctos")
        else:
            dialog.destroy()


#*******************************************Blockchain*******************************************#
    def blockchain(self):
        self.titulo4 = Label(self.master, text="Blockchain", bg="#0f1319", fg="#45c2c5",
                             font=("Century Gothic", 42), pady=12)
        self.titulo4.pack(fill=X)

        self.scrollbarY = Scrollbar(self.master)
        self.scrollbarY.pack(side=RIGHT, fill=Y)

        self.scrollbarX = Scrollbar(self.master, orient='horizontal')
        self.scrollbarX.pack(side=BOTTOM, fill=X)

        self.dblst = Combobox(self.master, state="readonly", width=35, font=("Century Gothic", 15))
        self.dblst.place(x=120, y=135)
        self.dblst.set('Seleccione base de datos...')
        self.dblst.bind("<<ComboboxSelected>>", self.displayTableList)

        self.tablelst = Combobox(self.master, state="readonly", width=35, font=("Century Gothic", 15))
        self.tablelst.place(x=620, y=135)
        self.tablelst.set('Seleccione tabla...')
        self.tablelst.bind("<<ComboboxSelected>>", self.displayBlockchain)

        self.canvas = Canvas(self.master, width=1000, height=300, bg="#0f1319", highlightthickness=0)
        self.canvas.place(x=72, y=200)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.scrollbarY.config(command=self.canvas.yview)
        self.scrollbarX.config(command=self.canvas.xview)

        self.display_availableDBS()
    
    # Mostrar lista de base de datos con tablas seguras
    def display_availableDBS(self):
        try:
            dblist = self.controller.getDBS_Security()
            if dblist:
                self.dblst["values"] = dblist
            else:
                messagebox.showwarning('Operación imposible','Debe existir al menos una tabla en modo\nseguro para generar el Blockchain.')
        except:
            None
    
    # Mostrar valores en lista de tablas
    def displayTableList(self, event):
        try:
            self.tablelst.set('Seleccione tabla...')
            tblist = self.controller.getTBS_Security(self.dblst.get())
            self.tablelst["values"] = tblist
            if self.canvas.find_all():
                self.canvas.delete(self.image_on_canvas)
            self.master.mainloop()
        except:
            None
    
    # Mostrar grafica
    def displayBlockchain(self, event):
        try:
            database = str(self.dblst.get())
            table = str(self.tablelst.get())
            png = self.controller.graphBlockchain(database, table)
            bg = ImageTk.PhotoImage(Image.open(png))
            if self.canvas.find_all():
                self.canvas.itemconfig(self.image_on_canvas, image=bg)
            else:
                self.image_on_canvas = self.canvas.create_image(370, 170, anchor=W, image=bg)
            self.canvas.config(xscrollcommand=self.scrollbarX.set, yscrollcommand=self.scrollbarY.set)
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))
            self.master.mainloop()
        except:
            None

#*******************************************Grafos*******************************************#
    def grafos(self):
        self.titulo5 = Label(self.master, text="Grafos", bg="#0f1319", fg="#45c2c5",
                             font=("Century Gothic", 42), pady=12)
        self.titulo5.pack(fill=X)

        self.scrollbarY = Scrollbar(self.master)
        self.scrollbarY.pack(side=RIGHT, fill=Y)

        self.scrollbarX = Scrollbar(self.master, orient='horizontal')
        self.scrollbarX.pack(side=BOTTOM, fill=X)

        btnDSD = Button(self.master,
                             text=self.actions[28],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=25,
                             command=lambda: self.simpleDialog(["database"], self.actions[28]))
        btnDSD.place(x=220, y=110)

        btnDF = Button(self.master,
                             text=self.actions[29],
                             bg="#abb2b9", font=("Courier New", 14),
                             borderwidth=0.5, pady=6, width=25,
                             command=lambda: self.simpleDialog(["database", "table"], self.actions[29]))
        btnDF.place(x=660, y=110)    

        self.canvas = Canvas(self.master, width=1000, height=435, bg="#0f1319", highlightthickness=0)
        self.canvas.place(x=72, y=175)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.scrollbarY.config(command=self.canvas.yview)
        self.scrollbarX.config(command=self.canvas.xview)

    # Mostrar grafica
    def displayGraph(self, fname):
        try:
            png = self.controller.getGraph(fname)
            bg = ImageTk.PhotoImage(Image.open(png))
            if self.canvas.find_all():
                self.canvas.itemconfig(self.image_on_canvas, image=bg)
            else:
                self.image_on_canvas = self.canvas.create_image(370, 170, anchor=W, image=bg)
            self.canvas.config(xscrollcommand=self.scrollbarX.set, yscrollcommand=self.scrollbarY.set)
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))
            self.master.mainloop()
        except:
            None



def run():
    v1 = Tk()
    image = Image.open('storage/View/img/main.png')
    background_image = ImageTk.PhotoImage(image.resize((560, 560)))
    background_label = Label(v1, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    app = GUI(master=v1, val=1)
    app.mainloop()