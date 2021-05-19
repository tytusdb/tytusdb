# HASH Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team


from tkinter import *
from storage.Hash.storage import HashMode as h


def Mostrar():
    Databases_Window(Tk(), "", "")


class Databases_Window:
    def __init__(self, window, settings_frame, database):
        self.window = window
        self.database = database

        self.settings_frame = settings_frame
        if database == "":
            self.settings_frame = self.Default_frame()

        self.nav_var_databases(window)

        '''    BOTON PARA ACTUALIZAR LA PAGINA     '''
        Button(self.new_frame(window, 0, 0, 20, 10), text="↻", width=0, anchor="c", font=(
            "Arial Black", 12), command=self.update_databases(), foreground="blue").pack()

        '''    BOTON PARA CREAR NUEVA BASE DE DATOS     '''
        Button(self.new_frame(window, 0, 0, 320, 40), text=" ✚ ", width=0, anchor="c", font=(
            "Arial Black", 12), command=self.command_create_database(), foreground="green").pack()
        Label(self.window, text="CREATE A NEW DATABASE ",
              font=("Arial Black", 12)).place(x=380, y=45)

        '''    BOTON PARA CARGAR BASES DE DATOS     '''
        Button(self.new_frame(window, 0, 0, 320, 100), text=" ⇧ ", width=0, anchor="c", font=(
            "Arial Black", 12), command=self.command_cargar_csv(""), foreground="blue").pack()
        Label(self.window, text="UPLOAD DATABASE ",
              font=("Arial Black", 12)).place(x=380, y=110)

        Label(self.window, text="DATABASES: ", font=(
            "Arial Black", 9)).place(x=20, y=65)

        '''  SCROLL PARA DIRECCIONAR LA IMAGEN DE LA ESTRUCTURA HASH   '''
        Frame1 = LabelFrame(window)
        can = Canvas(Frame1, width=450, height=70)
        Scrollbar_x = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scrollbar_y = Scrollbar(Frame1, orient="horizontal", command=can.xview)
        Scrollbar_y.pack(side="bottom", fill="x")
        Scrollbar_x.pack(side="right", fill="y")
        can.pack(expand=True, fill="both")
        can.configure(yscrollcommand=Scrollbar_x.set,
                      xscrollcommand=Scrollbar_y.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=300, y=383)

        ''' AGREGARA LA IMAGEN DE LAS BASES DE DATOS'''
        h._storage.graficar()
        photo = PhotoImage(file="dbs.png")
        Label(frame, image=photo).pack()

        window.geometry("800x500")
        window.resizable(False, False)
        window.title("TytusStorage")
        window.mainloop()

    '''
        VENTANA EMERGENTE PARA ADVERTIR DE ALGO MAL HECHO EN RENOMBRAR LA BASE DE DATOS
    '''

    def Warning_Window_Alter_Database(self, text, database):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text=text, font=("Arial Black", 11)).pack()
        Button(self.new_frame(temp, 0, 0, 120, 60), text="Aceptar", font=(
            "Arial", 12), command=self._Warning_Window_Alter_Database(temp, database)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 100, x, y))
        temp.resizable(0, 0)
        temp.title("WARNING ALTERDATABASE")

    def _Warning_Window_Alter_Database(self, temp, database):
        return lambda: self._warning_window_alter_database(temp, database)

    def _warning_window_alter_database(self, temp, database):
        temp.destroy()
        self._command_alter_database(database)

    '''
        VENTANA EMERGENTE PARA ADVERTIR DE ALGO MAL HECHO EN CREAR UNA NUEVA BASE DE DATOS
    '''

    def Warning_Window_Create_Database(self, text):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text=text, font=("Arial Black", 11)).pack()
        Button(self.new_frame(temp, 0, 0, 120, 60), text="Aceptar", font=("Arial", 12),
               command=self._Warning_Window_Create_Database(temp)).pack()
        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 100, x, y))
        temp.resizable(0, 0)
        temp.title("WARNING CREATEDATABASE")

    def _Warning_Window_Create_Database(self, temp):
        return lambda: self._warning_window_create_database(temp)

    def _warning_window_create_database(self, temp):
        temp.destroy()
        self._command_create_database()

    '''
        Iplementacion de apartado para visualizacion de las bases de datos 
        registradas
    '''

    def show_databases(self, frame):
        self.frame1 = frame
        for i in h.showDatabases():
            Button(frame, text="• " + str(i), width=30, anchor="w",
                   command=self.command_button_databases(i)).pack()

    def command_button_databases(self, database):
        return lambda: self._command_button_databases(database)

    def _command_button_databases(self, database):
        Databases_Window(self.window, self.Settings_Frame(database), database)

    '''
        FRAME POR DEFECTO PARA QUE EL USUARIO SELECCIONE UNA BASE DE DATOS
    '''

    def Default_frame(self):
        tmp = self.new_frame(self.window, 470, 273, 300, 160)
        Frame(tmp, width=470, height=200).pack()
        Label(self.new_frame(tmp, 0, 0, 20, 20), text="Select a database to start managing",
              font=("Arial Black", 12)).pack()
        return tmp

    '''
        FRAME PARA GESTIONAR LA BASE DE DATOS SELECCIONADA
    '''

    def Settings_Frame(self, database):
        temp = self.new_frame(self.window, 470, 273, 300, 160)
        Frame(temp, width=470, height=200).pack()

        Label(self.new_frame(temp, 0, 0, 20, 10),
              text="DATABASE NAME: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 150, 10),
              text=str(database), font=("Arial", 9)).pack()

        Label(self.new_frame(temp, 0, 0, 20, 110),
              text="SETTINGS: ", font=("Arial Black", 8)).pack()

        Label(self.new_frame(temp, 0, 0, 80, 150),
              text="RENAME DATABASE", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 20, 140), text=" ✎ ", font=(
            "", 14), foreground="brown", command=self.command_alter_database(database)).pack()

        Label(self.new_frame(temp, 0, 0, 330, 150),
              text="DROP DATABASE", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 270, 140), text=" ✘ ", font=(
            "", 14), foreground="red", command=self.command_delete_database(database)).pack()

        Label(self.new_frame(temp, 0, 0, 330, 55),
              text="SHOW TABLES", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 270, 45), text=" ☄ ", font=(
            "", 14), foreground="blue",  command=self.show_tables(database)).pack()

        Label(self.new_frame(temp, 0, 0, 20, 50),
              text="DETAILS: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 100, 50),
              text="Tables: ", font=("Arial", 9)).pack()
        Label(self.new_frame(temp, 0, 0, 160, 50), text=str(
            len(h.showTables(database))), font=("Arial", 9)).pack()

    '''
        ACCION DE MOSTRAR VENTANA EMERGENTE PARA DECIDIR SI ELIMINAR LA BASE DE DATOS
    '''

    def command_delete_database(self, database):
        return lambda: self._command_delete_database(database)

    ''''
        VENTANA EMERGENTE PARA CONFIRMAR SI SE ELIMINA LA BASE DE DATOS
    '''

    def _command_delete_database(self, database):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="Are you sure to delete this database?", font=("Arial", 14)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Database selected: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 140, 43),
              text=str(database), font=("Arial", 9)).pack()
        Button(self.new_frame(temp, 0, 0, 80, 80), text="Aceptar", font=(
            "Arial", 12), command=self.DropDatabase(temp, database)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 80), text="Cancelar", font=(
            "Arial", 12), command=self.Cancel(temp, database)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 130, x, y))
        temp.title("DropDatabase")
        temp.resizable(0, 0)
        temp.mainloop()

    def DropDatabase(self, temp,  database):
        return lambda: self._DropDatabase(temp, database)

    '''
        ACEPTAR ELIMINAR LA BASE DE DATOS ACTUAL
    '''

    def _DropDatabase(self, temp, database):
        if database != "":
            temp.destroy()
            h.dropDatabase(database)
            Databases_Window(self.window, self.Default_frame(), database)

    '''
        CANCELAR LA ACCION DE LA VENTANA EMERGENTE
    '''

    def Cancel(self, temp, database):
        return lambda: self._Cancel(temp, database)

    def _Cancel(self, temp, database):
        temp.destroy()

    '''
        MOSTRAR VENTANA EMERGENTE PARA MODIFICAR EL NOMBRE DE LA BASE DE DATOS
    '''

    def command_alter_database(self, database):
        return lambda: self._command_alter_database(database)

    def _command_alter_database(self, database):
        Entrada = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="Enter new database name", font=("Arial Black", 11)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Name: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 40, 10, 70, 43), width=35,
              font=("Arial", 10), textvariable=Entrada).pack()
        Button(self.new_frame(temp, 0, 0, 80, 80), text="Aceptar", font=(
            "Arial", 12), command=self.AlterDatabase(temp, Entrada, database)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 80), text="Cancelar", font=(
            "Arial", 12), command=self.Cancel(temp, database)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 130, x, y))
        temp.title("RenameDatabase")
        temp.resizable(0, 0)
        temp.mainloop()

    '''
        ACEPTAR EL CAMBIO DE NOMBRE DE LA BASE DE DATOS ACTUAL
    '''

    def AlterDatabase(self, tmp, entrada, database):
        return lambda: self._AlterDatabase(tmp, entrada, database)

    def _AlterDatabase(self, tmp, entrada, database):
        if str(entrada.get()) != "":
            temp = h._storage.Buscar(entrada.get())
            if temp:
                text = "This database already exists"
                tmp.destroy()
                self.Warning_Window_Alter_Database(text, database)
            else:
                h.alterDatabase(database, entrada.get())
                tmp.destroy()
                Databases_Window(self.window, self.Default_frame(), database)
        else:
            text = "Please write the name of the database"
            tmp.destroy()
            self.Warning_Window_Alter_Database(text, database)

    '''
        VENTANA EMERGENTE PARA CREAR LA BASE DE DATOS
    '''

    def _command_create_database(self):
        Entrada = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="Enter new database name", font=("Arial Black", 11)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Name: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 40, 10, 70, 43), width=35,
              font=("Arial", 10), textvariable=Entrada).pack()
        Button(self.new_frame(temp, 0, 0, 80, 80), text="Aceptar", font=(
            "Arial", 12), command=self.Create_Database(temp, Entrada)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 80), text="Cancelar", font=("Arial", 12),
               command=self.Cancel(temp, "")).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 130, x, y))
        temp.title("CreateDatabase")
        temp.resizable(0, 0)
        temp.mainloop()

    def command_create_database(self):
        return lambda: self._command_create_database()

    def Create_Database(self, tmp, name):
        return lambda: self._Create_Database(tmp, name)

    def _Create_Database(self, tmp, name):
        if str(name.get()) != "":
            temp = h._storage.Buscar(name.get())
            if temp:
                text = "This database already exists"
                tmp.destroy()
                self.Warning_Window_Create_Database(text)
            else:
                h.createDatabase(name.get())
                tmp.destroy()
                Databases_Window(self.window, self.Default_frame(), "")
        else:
            text = "Please write the name of the database"
            tmp.destroy()
            self.Warning_Window_Create_Database(text)

    '''
         CARGAR ARCHIVO CSV   
    '''

    def command_cargar_csv(self, database):
        return lambda: self._command_cargar_csv("", database, "", "", "")

    def _command_cargar_csv(self, win, database, table, list_tables, list_csv):
        temp = ""
        if win == "":
            temp = Toplevel()
        else:
            temp = win
            tab = list_tables

        Label(self.new_frame(temp, 0, 0, 10, 5),
              text="DATABASES: ", font=("Arial Black", 9)).pack()
        Label(self.new_frame(temp, 0, 0, 240, 5),
              text="TABLES: ", font=("Arial Black", 9)).pack()

        Frame_details = self.new_frame(temp, 470, 273, 470, 30)
        Frame(Frame_details, width=200, height=150).pack()
        Label(self.new_frame(Frame_details, 0, 0, 10, 10),
              text="DATABASE: ", font=("Arial Black", 10)).pack()
        Label(self.new_frame(Frame_details, 0, 0, 10, 40),
              text=str(database), font=("Arial", 11)).pack()
        Label(self.new_frame(Frame_details, 0, 0, 10, 90),
              text="TABLE:   ", font=("Arial Black", 10)).pack()
        Label(self.new_frame(Frame_details, 0, 0, 10, 120),
              text=str(table), font=("Arial", 11)).pack()

        Frame1 = LabelFrame(temp)
        can = Canvas(Frame1, width=190, height=150)
        can.pack(side=LEFT)
        Scroll = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scroll.pack(side=RIGHT, fill="y")
        can.configure(yscrollcommand=Scroll.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=10, y=30)
        for i in h.showDatabases():
            Button(frame, text="• " + str(i), width=25, anchor="w",
                   command=self.view_tables(temp, i)).pack()

        temp.geometry("685x330")
        temp.title("UPLOAD CSV")
        temp.resizable(0, 0)

    def view_tables(self, temp, database):
        return lambda: self._view_tables(temp, database)

    def _view_tables(self, temp, database):
        Frame1 = LabelFrame(temp)
        can = Canvas(Frame1, width=190, height=150)
        can.pack(side=LEFT)
        Scroll = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scroll.pack(side=RIGHT, fill="y")
        can.configure(yscrollcommand=Scroll.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=240, y=30)
        for i in h.showTables(database):
            Button(frame, text="• " + str(i), width=25, anchor="w",
                   command=self.send_database_table(temp, database, i, "")).pack()
        self._command_cargar_csv(temp, database, "", "", "")

    def send_database_table(self, tmp, database, table, list_table):
        return lambda: self._command_cargar_csv(tmp, database, table, list_table, self.send_csv(tmp, database, table))

    def send_csv(self, tmp, database, table):
        path = StringVar()
        Frame_details = self.new_frame(tmp, 470, 273, 10, 200)
        Frame(Frame_details, width=660, height=110).pack()
        Label(self.new_frame(Frame_details, 0, 0, 10, 10),
              text="Enter the path of a CSV file", font=("Arial Black", 10)).pack()
        Entry(self.new_frame(Frame_details, 0, 0, 10, 40),
              textvariable=path, font=("Arial", 11), width=75).pack()
        Button(self.new_frame(Frame_details, 0, 0, 570, 70), text="Upload", anchor="w",
               command=self._send_csv(Frame_details, database, table, path)).pack()

    def _send_csv(self, tmp, database, table, path):
        return lambda: self._send_csv_(tmp, database, table, path)

    def _send_csv_(self, tmp, database, table, path):
        try:
            print(h.loadCSV(str(path.get()), database, table))
            tmp.destroy()
            self.successfully()
        except:
            tmp.destroy()

    def successfully(self):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="The file was uploaded successfully", font=("Arial Black", 11)).pack()
        Button(self.new_frame(temp, 0, 0, 120, 60), text="Aceptar",
               font=("Arial", 12), command=self._successfully(temp)).pack()
        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 100, x, y))
        temp.resizable(0, 0)
        temp.title("Successfully")

    def _successfully(self, tmp):
        return lambda: tmp.destroy()

    def unsatisfactory(self):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="The file was uploaded unsatisfactory", font=("Arial Black", 11)).pack()
        Button(self.new_frame(temp, 0, 0, 120, 60), text="Aceptar",
               font=("Arial", 12), command=self._successfully(temp)).pack()
        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 100, x, y))
        temp.resizable(0, 0)
        temp.title("Unsatisfactory")

    '''
        MOSTRAR VENTANA DE CON LISTADO DE TABLAS
    '''

    def show_tables(self, database):
        return lambda: Tables_Window("", database, "", "", "")

    '''
        BOTON DE ACTUALIZACION DE LA PAGINA
    '''

    def update_databases(self):
        return lambda: Databases_Window(self.window, "", "")

    '''
        BARRA DE NAVEGACION PARA LAS BASES DE DATOS
    '''

    def nav_var_databases(self, window):
        Frame1 = LabelFrame(window)
        can = Canvas(Frame1, width=230, height=380)
        can.pack(side=LEFT)
        Scroll = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scroll.pack(side=RIGHT, fill="y")
        can.configure(yscrollcommand=Scroll.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=20, y=90)
        self.show_databases(frame)

    '''
        Crear frame para cada wiggles que se pone en la ventana principal
    '''

    def new_frame(self, window, width, height, x, y):
        Frame1 = LabelFrame(window)
        can = Canvas(Frame1, width=width, height=height)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        Frame1.place(x=x, y=y)
        return Frame1


class Tables_Window:
    def __init__(self, win,   database, table_name, settings_frame, tuplas_settings):
        if win == "":
            self.window = Toplevel()
            self.settings_frame = self.Default_Frame()
            self.tuplas_setting_frame = self.Tuplas_Default_Frame()
        else:
            self.window = win
            self.settings_frame = settings_frame
            self.tuplas_setting_frame = tuplas_settings

        self.database = database
        self.table_name = table_name
        window = self.window

        '''    BOTON PARA CREAR UNA NUEVA TABLA     '''
        Button(self.new_frame(window, 0, 0, 250, 20), text=" ✚ ", width=0, anchor="c", font=(
            "Arial Black", 12), command=self.command_create_table(database), foreground="green").pack()
        Label(self.window, text="CREATE A NEW TABLE ",
              font=("Arial Black", 10)).place(x=300, y=25)

        Label(self.window, text="TABLES: ", font=(
            "Arial Black", 9)).place(x=20, y=65)

        '''  BARRA DE NAVEGACION DE TABLAS DISPONIBLES   '''
        self.nav_var_tables(window, database)

        '''  SCROLL PARA DIRECCIONAR LA IMAGEN DE LAS TABLAS   '''
        Frame1 = LabelFrame(self.window)
        can = Canvas(Frame1, width=430, height=70)
        Scrollbar_x = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scrollbar_y = Scrollbar(Frame1, orient="horizontal", command=can.xview)
        Scrollbar_y.pack(side="bottom", fill="x")
        Scrollbar_x.pack(side="right", fill="y")
        can.pack(expand=True, fill="both")
        can.configure(yscrollcommand=Scrollbar_x.set,
                      xscrollcommand=Scrollbar_y.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=300, y=383)

        ''' AGREGARA LA IMAGEN DE LAS TABLAS'''
        tmp = h._storage.Buscar(database)
        tmp.graficar()
        photo = PhotoImage(file="tablas.png")
        Label(frame, image=photo).pack()

        '''  ESPECIFICAR NOMBRE DE LA BASE DE DATOS   '''
        self.Title_BD = Label(self.window, text="BASE DE DATOS: ", font=(
            "Arial Black", 9)).place(x=70, y=10)
        Label(self.window, text=self.database).place(x=70, y=30)

        ''' BOTON DE ACTUALIZAR PAGINA '''
        Button(self.new_frame(window, 0, 0, 20, 10), text="↻", width=0, anchor="c", font=("Arial Black", 12),
               command=self.update_tables()).pack()

        window.geometry("800x500")
        window.resizable(False, False)
        window.title("TytusStorage/Tables")
        window.mainloop()

    '''  
        MOSTRAR LISTA DE TABLAS DE UNA BASE DE DATOS SELECCIONADA   
    '''

    def show_tables(self, frame, database):
        for i in h.showTables(database):
            Button(frame, text="• " + str(i), width=30, anchor="w",
                   command=self.command_button_tables(database, i)).pack()

    def command_button_tables(self, database, table):
        return lambda: self._command_button_tables(database, table)

    def _command_button_tables(self, database, table):
        Tables_Window(self.window, self.database, table, self.Settings_Frame(
            database, table), self.Tuples_Settings_Frame(database, table))

    '''
        VENTANA EMERGENTE PARA ADVERTIR DE ALGO MAL HECHO EN CREAR UNA TABLA
    '''

    def Warning_Window_Create_Table(self, text, database):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text=text, font=("Arial Black", 9)).pack()
        Button(self.new_frame(temp, 0, 0, 120, 60), text="Aceptar", font=("Arial", 12),
               command=self._Warning_Window_Create_Table(temp, database)).pack()
        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 100, x, y))
        temp.resizable(0, 0)
        temp.title("WARNING CREATETABLE")

    def _Warning_Window_Create_Table(self, temp, database):
        return lambda: self._warning_window_create_table(temp, database)

    def _warning_window_create_table(self, temp, database):
        temp.destroy()
        self._command_create_table(database)

    '''
        VENTANA EMERGENTE PARA ADVERTIR DE ALGO MAL HECHO EN CREAR UNA TABLA
    '''

    def Warning_Window_Alter_Table(self, text, database, table):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text=text, font=("Arial Black", 9)).pack()
        Button(self.new_frame(temp, 0, 0, 120, 60), text="Aceptar", font=("Arial", 12),
               command=self._Warning_Window_Alter_Table(temp, database, table)).pack()
        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 100, x, y))
        temp.resizable(0, 0)
        temp.title("WARNING CREATETABLE")

    def _Warning_Window_Alter_Table(self, temp, database, table):
        return lambda: self._warning_window_alter_table(temp, database, table)

    def _warning_window_alter_table(self, temp, database, table):
        temp.destroy()
        self._command_alter_table(database, table)

    '''
        VENTANA EMERGENTE PARA CREAR LA BASE DE DATOS
    '''

    def _command_create_table(self, database):
        Entrada = StringVar()
        Columns = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="Enter new table name", font=("Arial Black", 11)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Name: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 40, 10, 70, 43), width=35,
              font=("Arial", 10), textvariable=Entrada).pack()
        Label(self.new_frame(temp, 0, 0, 10, 73),
              text="No. Columns: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 5, 10, 110, 73), width=10,
              font=("Arial", 10), textvariable=Columns).pack()

        Button(self.new_frame(temp, 0, 0, 80, 110), text="Aceptar", font=("Arial", 12),
               command=self.create_table(temp, database, Entrada, Columns)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 110), text="Cancelar",
               font=("Arial", 12), command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 160, x, y))
        temp.title("CreateTable")
        temp.resizable(0, 0)
        temp.mainloop()

    def command_create_table(self, database):
        return lambda: self._command_create_table(database)

    def create_table(self, temp, database, entrada, columns):
        return lambda: self._create_table(temp, database, entrada, columns)

    def _create_table(self, temp, database, entrada, columns):
        if entrada.get() != "":
            dato = self.Convert_Number(columns.get())
            if dato:
                if int(columns.get()) > 0:
                    print(h.createTable(database, entrada.get(), int(columns.get())))
                    temp.destroy()
                    Tables_Window(self.window, self.database, "",
                                  self.Default_Frame(), self.Tuplas_Default_Frame())
                else:
                    text = "Please enter a number greater than zero"
                    temp.destroy()
                    self.Warning_Window_Create_Table(text, database)
            else:
                text = "Please enter a valid number of columns"
                temp.destroy()
                self.Warning_Window_Create_Table(text, database)
        else:
            text = "Please enter the name of the table"
            temp.destroy()
            self.Warning_Window_Create_Table(text, database)

    '''  VERIFICAR SI LA ENTRADA INGRESADA ES UN NUMERO   '''

    def Convert_Number(self, dato):
        try:
            dato = int(dato)
            return True
        except:
            return False

    '''
        CANCELAR LA ACCION DE LA VENTANA EMERGENTE
    '''

    def Cancel(self, temp):
        return lambda: temp.destroy()

    '''
        FRAME POR DEFAULT PARA ESCOGER UNA TABLA
    '''

    def Default_Frame(self):
        temp = self.new_frame(self.window, 470, 200, 300, 100)
        Frame(temp, width=470, height=270).pack()
        Label(self.new_frame(temp, 0, 0, 20, 20),
              text="Please select a table", font=("Arial Black", 8)).pack()

    def Tuplas_Default_Frame(self):
        temp = self.new_frame(self.window, 470, 200, 480, 10)
        Frame(temp, width=290, height=80).pack()
        Label(self.new_frame(temp, 0, 0, 20, 20),
              text="Please select a table", font=("Arial Black", 8)).pack()

    '''
        FRAME PARA GESTIONAR LA TABLA SELECCIONADA
    '''

    def Settings_Frame(self, database, table):
        temp = self.new_frame(self.window, 470, 200, 300, 100)
        Frame(temp, width=470, height=270).pack()

        Label(self.new_frame(temp, 0, 0, 80, 30),
              text="ALTER COLUMN", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 20, 20), text=" ✎ ", font=(
            "", 14), foreground="brown", command=self.command_alter_add_column(database, table)).pack()

        Label(self.new_frame(temp, 0, 0, 330, 180),
              text="DROP COLUMN", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 270, 170), text=" ✘ ", font=(
            "", 14), foreground="red", command=self.command_alter_drop_column(database, table)).pack()

        Label(self.new_frame(temp, 0, 0, 80, 80),
              text="ALTER ADD PK", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 20, 70), text="  ¶  ", font=(
            "", 14), foreground="orange", command=self.command_alter_add_PK(database, table)).pack()

        Label(self.new_frame(temp, 0, 0, 330, 80),
              text="ALTER ADD FK", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 270, 70), text="  ¶  ",
               font=("", 14), foreground="blue").pack()

        Label(self.new_frame(temp, 0, 0, 80, 130),
              text="ALTER ADD INDEX", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 20, 120), text=" ✎ ",
               font=("", 14), foreground="brown").pack()

        Label(self.new_frame(temp, 0, 0, 330, 130),
              text="ALTER DROP PK", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 270, 120), text=" ☒ ", font=(
            "", 14), foreground="red", command=self.command_alter_drop_PK(database, table)).pack()

        Label(self.new_frame(temp, 0, 0, 80, 180),
              text="EXTRACT RANGE TABLE", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 20, 170), text=" № ", font=(
            "", 14), foreground="black", command=self.command_extract_range_table(database, table)).pack()

        Label(self.new_frame(temp, 0, 0, 330, 30),
              text="EXTRACT TABLE", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 270, 20), text=" ★ ", font=(
            "", 14), foreground="yellow", command=self.command_extract_table(database, table)).pack()

        Label(self.new_frame(temp, 0, 0, 80, 230),
              text="RENAME TABLE", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 20, 220), text=" ✎ ", font=(
            "", 14), foreground="brown", command=self.command_alter_table(database, table)).pack()

        Label(self.new_frame(temp, 0, 0, 330, 230),
              text="DROP TABLE", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 270, 220), text=" ✘ ", font=(
            "", 14), foreground="red", command=self.command_delete_table(database, table)).pack()

    '''
        VENTANA PARA VER DETALLES DE TUPLAS
    '''

    def Tuples_Settings_Frame(self, database, table):
        temp = self.new_frame(self.window, 470, 200, 480, 10)
        Frame(temp, width=290, height=80).pack()

        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="TABLE NAME:", font=("Arial Black", 7)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 40),
              text=str(table), font=("Arial", 7)).pack()

        Label(self.new_frame(temp, 0, 0, 210, 30),
              text="SHOW TUPLES", font=("Arial Black", 7)).pack()
        Button(self.new_frame(temp, 0, 0, 150, 20), text=" ☄ ", font=(
            "", 14), foreground="blue", command=self.show_Tuples(database, table)).pack()

    def show_Tuples(self, database, table):
        return lambda: Tuples_Window("", database, table, "")

    ''''
        VENTANA EMERGENTE PARA CONFIRMAR SI SE ELIMINA LA TABLA
    '''

    def command_delete_table(self, database, table):
        return lambda: self._command_delete_table(database, table)

    def _command_delete_table(self, database, table):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text="Are you sure to delete this table?",
              font=("Arial", 14)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Table selected: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 140, 43),
              text=str(table), font=("Arial", 9)).pack()
        Button(self.new_frame(temp, 0, 0, 80, 80), text="Aceptar", font=("Arial", 12),
               command=self.DropDatabase(temp, database, table)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 80), text="Cancelar", font=("Arial", 12),
               command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 130, x, y))
        temp.title("DropDatabase")
        temp.resizable(0, 0)
        temp.mainloop()

    def DropDatabase(self, temp, database, table):
        return lambda: self._DropDatabase(temp, database, table)

    def _DropDatabase(self, temp, database, table):
        h.dropTable(database, table)
        temp.destroy()
        Tables_Window(self.window, self.database, "",
                      self.Default_Frame(), self.Tuplas_Default_Frame())

    '''
        MOSTRAR VENTANA EMERGENTE PARA MODIFICAR EL NOMBRE DE LA TABLA
    '''

    def command_alter_table(self, database, table):
        return lambda: self._command_alter_table(database, table)

    def _command_alter_table(self, database, table):
        Entrada = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="Enter new table name", font=("Arial Black", 11)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Name: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 40, 10, 70, 43), width=35,
              font=("Arial", 10), textvariable=Entrada).pack()
        Button(self.new_frame(temp, 0, 0, 80, 80), text="Aceptar", font=("Arial", 12),
               command=self.AlterTable(temp, Entrada, database, table)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 80), text="Cancelar", font=("Arial", 12),
               command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 130, x, y))
        temp.title("RenameTable")
        temp.resizable(0, 0)
        temp.mainloop()

    '''
        ACEPTAR EL CAMBIO DE NOMBRE DE LA TABLA ACTUAL
    '''

    def AlterTable(self, tmp, entrada, database, table):
        return lambda: self._AlterTable(tmp, entrada, database, table)

    def _AlterTable(self, tmp, entrada, database, table):
        if entrada.get() != "":
            h.alterTable(database, table, entrada.get())
            tmp.destroy()
            Tables_Window(self.window, self.database, "",
                          self.Default_Frame(), self.Tuplas_Default_Frame())
        else:
            text = "Please enter the name of the table"
            tmp.destroy()
            self.Warning_Window_Alter_Table(text, database, table)

    '''
        AGREGAR UNA COLUMNA A LA TABLA
    '''

    def command_alter_add_column(self, database, table):
        return lambda: self.Alter_Add_Column(database, table)

    def Alter_Add_Column(self, database, table):
        default = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="Enter any value....", font=("Arial Black", 11)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 60),
              text="Default: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 5, 10, 110, 60), width=30,
              font=("Arial", 10), textvariable=default).pack()
        Button(self.new_frame(temp, 0, 0, 80, 120), text="Aceptar", font=(
            "Arial", 12), command=self.alter_add_column(temp, database, table, default)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 120), text="Cancelar",
               font=("Arial", 12), command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 160, x, y))
        temp.title("ALTERADDTABLE")
        temp.resizable(0, 0)
        temp.mainloop()

    def alter_add_column(self, temp, database, table, default):
        return lambda: self._alter_add_column(temp, database, table, default)

    def _alter_add_column(self, temp, database, table, default):
        h.alterAddColumn(database, table, default)
        temp.destroy()

    '''
        ELIMINAR COLUMNAS DE LA TABLA
    '''

    def command_alter_drop_column(self, database, table):
        return lambda: self._command_alter_drop_column(database, table)

    def _command_alter_drop_column(self, database, table):
        Columns = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="Please enter the column number to drop", font=("Arial Black", 11)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Name: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 40, 10, 70, 43),
              text=str(table), font=("Arial", 10)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 73),
              text="No. Columns: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 5, 10, 110, 73), width=10,
              font=("Arial", 10), textvariable=Columns).pack()

        Button(self.new_frame(temp, 0, 0, 80, 110), text="Aceptar", font=("Arial", 12),
               command=self.alter_drop_columns(temp, database, table, Columns)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 110), text="Cancelar",
               font=("Arial", 12), command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 160, x, y))
        temp.resizable(0, 0)
        temp.title("ALTERDROPCOLUMN")

    def alter_drop_columns(self, temp, database, table, columns):
        return lambda: self._alter_drop_columns(temp, database, table, columns)

    def _alter_drop_columns(self, temp, database, table, columns):
        try:
            print(h.alterDropColumn(database, table, int(columns.get())))
            temp.destroy()
        except:
            temp.destroy()

    '''
        AGREGA LAS COLUMNAS QUE SERAN LLAVES PRIMARIAS
    '''

    def command_alter_add_PK(self, database, table):
        return lambda: self._command_alter_add_PK(database, table)

    def _command_alter_add_PK(self, database, table):
        Columns = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text="Enter the column numbers separated by commas",
              font=("Arial Black", 10)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Name: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 40, 10, 70, 43),
              text=str(table), font=("Arial", 10)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 73),
              text="No. Columns: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 5, 10, 110, 73), width=10,
              font=("Arial", 10), textvariable=Columns).pack()

        Button(self.new_frame(temp, 0, 0, 80, 110), text="Aceptar", font=(
            "Arial", 12), command=self.alter_add_PK(temp, database, table, Columns)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 110), text="Cancelar",
               font=("Arial", 12), command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 160, x, y))
        temp.resizable(0, 0)
        temp.title("ALTERADDPK")

    def alter_add_PK(self, temp, database, table, columns):
        return lambda: self._alter_add_PK(temp, database, table, columns)

    def _alter_add_PK(self, temp, database, table, columns):
        try:
            list = []
            for i in columns.get().split(","):
                list.append(int(i))
            print(h.alterAddPK(database, table, list))
            temp.destroy()
        except:
            temp.destroy()

    '''
        ELIMINAR LLAVES PRIMARIAS
    '''

    def command_alter_drop_PK(self, database, table):
        return lambda: self._command_alter_drop_PK(database, table)

    def _command_alter_drop_PK(self, database, table):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text="Are you sure you delete the primary key?",
              font=("Arial Black", 10)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Name: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 40, 10, 70, 43),
              text=str(table), font=("Arial", 10)).pack()

        Button(self.new_frame(temp, 0, 0, 120, 110), text="Aceptar", font=(
            "Arial", 12), command=self.alter_drop_PK(temp, database, table)).pack()
        Button(self.new_frame(temp, 0, 0, 210, 110), text="Cancelar",
               font=("Arial", 12), command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(480, 160, x, y))
        temp.resizable(0, 0)
        temp.title("ALTERDROPPK")

    def alter_drop_PK(self, temp, database, table):
        return lambda: self._alter_drop_PK(temp, database, table)

    def _alter_drop_PK(self, temp, database, table):
        print(h.alterDropPK(database, table))
        temp.destroy()

    '''
        EXTRAER TABLA SELECCIONADA
    '''

    def command_extract_table(self, database, table):
        return lambda: self._command_extract_table(database, table)

    def _command_extract_table(self, database, table):
        temp = Toplevel()
        Label(self.new_frame(temp, 100, 30, 20, 10),
              text="TABLE NAME: ", font=("Arial Black", 10)).pack()
        Label(self.new_frame(temp, 100, 30, 150, 10),
              text=str(table), font=("Arial", 11)).pack()
        Frame1 = LabelFrame(temp)
        can = Canvas(Frame1, width=430, height=150)
        Scrollbar_x = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scrollbar_y = Scrollbar(Frame1, orient="horizontal", command=can.xview)
        Scrollbar_y.pack(side="bottom", fill="x")
        Scrollbar_x.pack(side="right", fill="y")
        can.pack(expand=True, fill="both")
        can.configure(yscrollcommand=Scrollbar_x.set,
                      xscrollcommand=Scrollbar_y.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=20, y=50)
        height = 0
        for i in h.extractTable(database, table):
            Label(frame, text=str(i), font=("Arial", 10)).pack()
            height += 30

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(500, 250, x, y))
        temp.resizable(0, 0)
        temp.title("EXRACTTABLE")

    '''
        EXTRAER EL RANGO DE LA TABLA
    '''

    def command_extract_range_table(self, database, table):
        return lambda: self._command_extract_range_table(database, table)

    def _command_extract_range_table(self, database, table):
        lower = StringVar()
        upper = StringVar()
        Columns = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="Enter the requested parameters", font=("Arial Black", 11)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Lower: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 50, 10, 70, 43), width=35,
              font=("Arial", 10), textvariable=lower).pack()
        Label(self.new_frame(temp, 0, 0, 10, 73),
              text="Upper: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 50, 10, 70, 73), width=35,
              font=("Arial", 10), textvariable=upper).pack()
        Label(self.new_frame(temp, 0, 0, 10, 100),
              text="No. Columns: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 5, 10, 110, 100), width=10,
              font=("Arial", 10), textvariable=Columns).pack()
        Button(self.new_frame(temp, 0, 0, 80, 130), text="Aceptar", font=("Arial", 12),
               command=self.extract_range_table(temp, database, table, lower, upper, Columns)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 130), text="Cancelar", font=("Arial", 12),
               command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 180, x, y))
        temp.title("EXTRACTRANGETABLE")
        temp.resizable(0, 0)
        temp.mainloop()

    def extract_range_table(self, temp, database, table, lower, upper, columns):
        return lambda: self._extract_range_table(temp, database, table, lower, upper, columns)

    def _extract_range_table(self, temp, database, table, lower, upper, columns):
        col = self.Casteo(columns.get())
        up = self.Casteo(upper.get())
        low = self.Casteo(lower.get())
        if col:
            columns = int(columns.get())
        if up:
            upper = int(upper.get())
        if low:
            lower = int(lower.get())

        text = h.extractRangeTable(database, table, columns, lower, upper)
        temp.destroy()
        self.show_row(text, table)

    def show_row(self, text, table):
        temp = Toplevel()
        Label(self.new_frame(temp, 100, 30, 20, 10),
              text="TABLE: ", font=("Arial Black", 10)).pack()
        Label(self.new_frame(temp, 100, 30, 100, 10),
              text=str(table), font=("Arial", 11)).pack()
        Frame1 = LabelFrame(temp)
        can = Canvas(Frame1, width=430, height=20)
        Scrollbar_x = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scrollbar_y = Scrollbar(Frame1, orient="horizontal", command=can.xview)
        Scrollbar_y.pack(side="bottom", fill="x")
        Scrollbar_x.pack(side="right", fill="y")
        can.pack(expand=True, fill="both")
        can.configure(yscrollcommand=Scrollbar_x.set,
                      xscrollcommand=Scrollbar_y.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=20, y=50)

        for z in text:
            Label(frame, text=str(z), font=("Arial", 10)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(500, 140, x, y))
        temp.resizable(0, 0)
        temp.title("EXRACTRANGETABLE")

    '''  CASTEO DE DATOS INGRESADOS   '''

    def Casteo(self, dato):
        try:
            x = int(dato)
            return True
        except:
            return False

    '''  BOTON DE ACTUALIZAR PARA LIMPIAR LA IMAGEN EN PANTALLA   '''

    def update_tables(self):
        return lambda: Tables_Window(self.window, self.database, "", self.Default_Frame(), self.Tuplas_Default_Frame())

    '''
        BARRA DE NAVEGACION PARA LAS TABLAS
    '''

    def nav_var_tables(self, window, database):
        Frame1 = LabelFrame(window)
        can = Canvas(Frame1, width=230, height=380)
        can.pack(side=LEFT)
        Scroll = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scroll.pack(side=RIGHT, fill="y")
        can.configure(yscrollcommand=Scroll.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=20, y=90)
        self.show_tables(frame, database)

    '''  CREACION DE FRAMES PARA QUE NO SE REPITAN LOS WIDGETS AL MOMENTO DE ACTUALIZAR LA PAGINA  '''

    def new_frame(self, window, width, height, x, y):
        Frame1 = LabelFrame(window)
        can = Canvas(Frame1, width=width, height=height)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        Frame1.place(x=x, y=y)
        return Frame1


class Tuples_Window:
    def __init__(self, win,  database, table, settings_frame):
        if win == "":
            self.window = Toplevel()
            self.settings_frame = self.Default_Frame()
        else:
            self.window = win
            self.settings_frame = settings_frame

        self.database = database
        self.table = table
        window = self.window

        Label(self.window, text="DATABASE: "+str(database),
              font=("Arial Black", 8)).place(x=70, y=10)
        Label(self.window, text="TABLE: " + str(table),
              font=("Arial Black", 8)).place(x=70, y=35)
        Label(self.window, text="TUPLE | PRIMARY KEY",
              font=("Arial Black", 8)).place(x=20, y=125)

        '''    BOTON PARA CREAR NUEVA BASE DE DATOS     '''
        Button(self.new_frame(window, 0, 0, 90, 70), text=" ✚ ", width=0, anchor="c", font=("Arial Black", 12),
               command=self.command_create_tuple(database, table), foreground="green").pack()
        Label(self.window, text="INSERT A NEW TUPLE ",
              font=("Arial Black", 8)).place(x=140, y=80)

        ''' BOTON DE ACTUALIZAR PAGINA '''
        Button(self.new_frame(window, 0, 0, 20, 10), text="↻", width=0, anchor="c", font=("Arial Black", 12),
               command=self.update_tables()).pack()

        '''  MOSTRAR BARRA DE NAVEGACION EN TUPLAS   '''
        self.nav_var_tables(window, database, table)

        '''  OPCIONES PARA TUPLA SELECCIONADA    '''

        '''  FRAME PARA MOSTRAR ESTRUCTURA HASH QUE ALMACENA LOS REGISTROS   '''
        Frame1 = LabelFrame(self.window)
        can = Canvas(Frame1, width=430, height=320)
        Scrollbar_x = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scrollbar_y = Scrollbar(Frame1, orient="horizontal", command=can.xview)
        Scrollbar_y.pack(side="bottom", fill="x")
        Scrollbar_x.pack(side="right", fill="y")
        can.pack(expand=True, fill="both")
        can.configure(yscrollcommand=Scrollbar_x.set,
                      xscrollcommand=Scrollbar_y.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=300, y=150)

        ''' AGREGARA LA IMAGEN DE LAS TABLAS'''
        tmp = h._storage.Cargar(database, table)
        tmp.Grafico()
        photo = PhotoImage(file="hash.png")
        Label(frame, image=photo).pack()

        window.geometry("800x500")
        window.resizable(False, False)
        window.title("TytusStorage/Tables/Tuples")
        window.mainloop()

    '''
        FRAME POR DEFECTO
    '''

    def Default_Frame(self):
        temp = self.new_frame(self.window, 470, 200, 300, 10)
        Frame(temp, width=470, height=130).pack()
        Label(self.new_frame(temp, 0, 0, 20, 20),
              text="Please select a tuple for start work", font=("Arial Black", 10)).pack()

    '''
        FRAME DE OPCCIONES PARA TUPLA SELECCIONADA
    '''

    def Settings_Frame(self, database, table, pk):
        temp = self.new_frame(self.window, 470, 200, 300, 10)
        Frame(temp, width=470, height=130).pack()

        Label(self.new_frame(temp, 0, 0, 10, 10),
              text="PRIMARY KEY:", font=("Arial Black", 7)).pack()
        Label(self.new_frame(temp, 0, 0, 90, 10), text=str(
            pk.primaria), font=("Arial Black", 7)).pack()

        Label(self.new_frame(temp, 0, 0, 70, 90),
              text="EXTRACT ROW", font=("Arial Black", 7)).pack()
        Button(self.new_frame(temp, 0, 0, 10, 80), text=" ★ ", font=(
            "", 14), foreground="yellow", command=self.command_extract_row(database, table, pk)).pack()

        Label(self.new_frame(temp, 0, 0, 255, 90),
              text="UPDATE", font=("Arial Black", 7)).pack()
        Button(self.new_frame(temp, 0, 0, 195, 80), text=" ⇧ ", font=(
            "", 14), foreground="blue", command=self.command_update(database, table, pk)).pack()

        Label(self.new_frame(temp, 0, 0, 390, 20),
              text="TRUNCATE", font=("Arial Black", 7)).pack()
        Button(self.new_frame(temp, 0, 0, 330, 10), text=" ✎ ", font=(
            "", 14), foreground="brown", command=self.command_truncate(database, table)).pack()

        Label(self.new_frame(temp, 0, 0, 410, 90),
              text="DELETE", font=("Arial Black", 7)).pack()
        Button(self.new_frame(temp, 0, 0, 350, 80), text=" ✘ ", font=(
            "", 14), foreground="red", command=self.command_delete(database, table, pk)).pack()

    '''  BOTON DE ACTUALIZAR PARA LIMPIAR LA IMAGEN EN PANTALLA   '''

    def update_tables(self):
        return lambda: Tuples_Window(self.window, self.database, self.table, self.Default_Frame())

    '''
        MOSTRAR TUPLAS
    '''

    def show_tuples(self, frame, database, table):
        tmp = h._storage.Cargar(database, table)
        for i in tmp.vector:
            if i is None:
                pass
            else:
                for j in i:
                    Button(frame, text="• " + str(j.primaria), width=30, anchor="w",
                           command=self._show_tuples(database, table, j)).pack()

    def _show_tuples(self, database, table, pk):
        return lambda: Tuples_Window(self.window, self.database, self.table, self.Settings_Frame(database, table, pk))

    '''
        CREAR UNA TUPLA
    '''

    def command_create_tuple(self, database, table):
        return lambda: self._command_create_tuple(database, table)

    def _command_create_tuple(self, database, table):
        Entrada = StringVar()
        tmp = h._storage.Cargar(database, table)
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text="TABLE: " +
              str(table), font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 230, 10), text="COLUMNS: " +
              str(tmp.columnas), font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 45),
              text="Enter the tuple separated by commas", font=("Arial Black", 9)).pack()

        Label(self.new_frame(temp, 0, 0, 10, 80),
              text="Tuple: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 40, 10, 70, 80), width=35,
              font=("Arial", 10), textvariable=Entrada).pack()

        Button(self.new_frame(temp, 0, 0, 80, 110), text="Aceptar", font=("Arial", 12),
               command=self.insert_tuple(temp, database, table, Entrada)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 110), text="Cancelar", font=("Arial", 12),
               command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 160, x, y))
        temp.title("CreateTable")
        temp.resizable(0, 0)
        temp.mainloop()

    def insert_tuple(self, tmp, database, table, tuple):
        return lambda: self._insert_tuple(tmp, database, table, tuple)

    def _insert_tuple(self, tmp, database, table, tuple):
        try:
            list = []
            for i in tuple.get().split(","):
                temp = self.casteo(i)
                if temp:
                    list.append(int(i))
                else:
                    list.append(str(i))
            print(h.insert(database, table, list))
            tmp.destroy()
            Tuples_Window(self.window, self.database,
                          self.table, self.Default_Frame())
        except:
            tmp.destroy()
            Tuples_Window(self.window, self.database,
                          self.table, self.Default_Frame())

    '''
        EXTRAER UNA TUPLA
    '''

    def command_extract_row(self, database, table, pk):
        return lambda: self._command_extract_row(database, table, pk)

    def _command_extract_row(self, database, table, pk):
        temp = Toplevel()
        Label(self.new_frame(temp, 100, 30, 20, 10),
              text="PRIMARY KEY: ", font=("Arial Black", 10)).pack()
        Label(self.new_frame(temp, 100, 30, 150, 10),
              text=str(pk.primaria), font=("Arial", 11)).pack()
        Frame1 = LabelFrame(temp)
        can = Canvas(Frame1, width=430, height=20)
        Scrollbar_x = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scrollbar_y = Scrollbar(Frame1, orient="horizontal", command=can.xview)
        Scrollbar_y.pack(side="bottom", fill="x")
        Scrollbar_x.pack(side="right", fill="y")
        can.pack(expand=True, fill="both")
        can.configure(yscrollcommand=Scrollbar_x.set,
                      xscrollcommand=Scrollbar_y.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=20, y=50)
        Label(frame, text=str(pk.datos), font=("Arial", 10)).pack()
        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(500, 140, x, y))
        temp.resizable(0, 0)
        temp.title("EXRACTROW")

    '''
        ELIMINAR TODOS LOS DATOS DE LA TABLA
    '''

    def command_truncate(self, database, table):
        return lambda: self._command_truncate(database, table)

    def _command_truncate(self, database, table):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text="Are you sure you want tol delete all the data?",
              font=("Arial", 14)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Table selected: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 140, 43),
              text=str(table), font=("Arial", 9)).pack()
        Button(self.new_frame(temp, 0, 0, 80, 80), text="Aceptar", font=("Arial", 12),
               command=self.truncate(temp, database, table)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 80), text="Cancelar", font=("Arial", 12),
               command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 130, x, y))
        temp.title("TRUNCATE")
        temp.resizable(0, 0)
        temp.mainloop()

    def truncate(self, tmp, database, table):
        return lambda: self._truncate(tmp, database, table)

    def _truncate(self, tmp, database, table):
        h.truncate(database, table)
        tmp.destroy()
        Tuples_Window(self.window, self.database,
                      self.table, self.Default_Frame())

    '''
        ACTUALIZAR UNA TUPLA
    '''

    def command_update(self, database, table, pk):
        return lambda: self._command_update(database, table, pk)

    def _command_update(self, database, table, pk):
        Entrada = StringVar()
        tmp = h._storage.Cargar(database, table)
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text="TABLE: " +
              str(table), font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 230, 10), text="COLUMNS: " +
              str(tmp.columnas), font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 45), text="Enter the tuple separated by commas",
              font=("Arial Black", 9)).pack()

        Label(self.new_frame(temp, 0, 0, 10, 80),
              text="Tuple: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 40, 10, 70, 80), width=35,
              font=("Arial", 10), textvariable=Entrada).pack()

        Button(self.new_frame(temp, 0, 0, 80, 110), text="Aceptar", font=(
            "Arial", 12), command=self.update_tuple(temp, database, table, pk, Entrada)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 110), text="Cancelar", font=("Arial", 12),
               command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 160, x, y))
        temp.title("UPDATE TUPLE")
        temp.resizable(0, 0)
        temp.mainloop()

    def update_tuple(self, tmp, database, table, pk, entrada):
        return lambda: self._update_tuple(tmp, database, table, pk, entrada)

    def _update_tuple(self, tmp, database, table, pk, entrada):
        list = {}
        try:
            for i in entrada.get().split(";"):
                aux = i.split(",")
                temp = self.casteo(aux[1])
                if temp:
                    list[int(aux[0])] = int(aux[1])
                else:
                    list[int(aux[0])] = str(aux[1])
            print(str(list))
            print(h.update(database, table, list, [pk.primaria]))
            tmp.destroy()
            Tuples_Window(self.window, self.database,
                          self.table, self.Default_Frame())
        except:
            tmp.destroy()
            Tuples_Window(self.window, self.database,
                          self.table, self.Default_Frame())

    '''  CASTEAR DATOS DE ENTRADA   '''

    def casteo(self, dato):
        try:
            x = int(dato)
            return True
        except:
            return False

    '''
        ELIMINAR TUPLA
    '''

    def command_delete(self, database, table, pk):
        return lambda: self._command_delete(database, table, pk)

    def _command_delete(self, database, table, pk):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text="Are you sure you want to delete this tuple?",
              font=("Arial", 14)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43),
              text="Primary Key: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 140, 43), text=str(
            pk.primaria), font=("Arial", 9)).pack()
        Button(self.new_frame(temp, 0, 0, 80, 80), text="Aceptar", font=("Arial", 12),
               command=self.delete_tuple(temp, database, table, pk)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 80), text="Cancelar", font=("Arial", 12),
               command=self.Cancel(temp)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 130, x, y))
        temp.title("TRUNCATE")
        temp.resizable(0, 0)
        temp.mainloop()

    def delete_tuple(self, tmp, database, table, pk):
        return lambda: self._delete_tuple(tmp, database, table, pk)

    def _delete_tuple(self, tmp, database, table, pk):
        print(h.delete(database, table, [pk.primaria]))
        tmp.destroy()
        Tuples_Window(self.window, self.database,
                      self.table, self.Default_Frame())

    '''
        CANCELAR LA ACCION DE LA VENTANA EMERGENTE
    '''

    def Cancel(self, temp):
        return lambda: temp.destroy()

    '''
        BARRA DE NAVEGACION PARA LAS TUPLAS
    '''

    def nav_var_tables(self, window, database, table):
        Frame1 = LabelFrame(window)
        can = Canvas(Frame1, width=230, height=320)
        can.pack(side=LEFT)
        Scroll = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scroll.pack(side=RIGHT, fill="y")
        can.configure(yscrollcommand=Scroll.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(
            scrollregion=can.bbox("all")))
        Frame1.place(x=20, y=150)
        self.show_tuples(frame, database, table)

    '''  CREACION DE FRAMES PARA QUE NO SE REPITAN LOS WIDGETS AL MOMENTO DE ACTUALIZAR LA PAGINA  '''

    def new_frame(self, window, width, height, x, y):
        Frame1 = LabelFrame(window)
        can = Canvas(Frame1, width=width, height=height)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        Frame1.place(x=x, y=y)
        return Frame1
