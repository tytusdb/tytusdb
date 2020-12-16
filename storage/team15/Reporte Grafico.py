
from tkinter import *
from HashMode import*
from ListaBaseDatos import*




class Databases_Window:
    def __init__(self, window, settings_frame, database):
        self.window = window
        self.database= database

        self.settings_frame = settings_frame
        if database == "":
            self.settings_frame = self.Default_frame()

        self.nav_var_databases(window)

        '''    BOTON PARA ACTUALIZAR LA PAGINA     '''
        Button(self.new_frame(window, 0, 0, 20, 10), text="↻", width=0, anchor="c", font=("Arial Black", 12)
               , command=self.update_databases(), foreground="blue").pack()


        '''    BOTON PARA CREAR NUEVA BASE DE DATOS     '''
        Button(self.new_frame(window, 0, 0, 320, 60), text=" ✚ ", width=0, anchor="c", font=("Arial Black", 12), command=self.command_create_database(), foreground="green").pack()
        Label(self.window, text="CREATE A NEW DATABASE ", font=("Arial Black", 12)).place(x=380, y=65)

        '''    BOTON PARA CARGAR BASES DE DATOS     '''
        Button(self.new_frame(window, 0, 0, 320, 120), text=" ⇧ ", width=0, anchor="c", font=("Arial Black", 12), foreground="blue").pack()
        Label(self.window, text="UPLOAD DATABASE ", font=("Arial Black", 12)).place(x=380, y=130)


        Label(self.window, text="DATABASES: ", font=("Arial Black", 9)).place(x=20, y=65)


        window.geometry("800x500")
        window.resizable(False, False)
        window.title("TytusStorage")
        window.mainloop()



    '''
        VENTANA EMERGENTE PARA ADVERTIR DE ALGO MAL HECHO EN RENOMBRAR LA BASE DE DATOS
    '''
    def Warning_Window_Alter_Database(self, text, database):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text=text, font=("Arial Black", 11)).pack()
        Button(self.new_frame(temp, 0, 0, 120, 60), text="Aceptar", font=("Arial", 12), command=self._Warning_Window_Alter_Database(temp, database)).pack()
        print("Entreeee problema")
        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 100, x, y))
        temp.resizable(0,0)
        temp.title("WARNING ALTERDATABASE")

    def _Warning_Window_Alter_Database(self, temp, database):
        return lambda : self._warning_window_alter_database(temp, database)

    def _warning_window_alter_database(self, temp, database):
        temp.destroy()
        self._command_alter_database(database)



    '''
        VENTANA EMERGENTE PARA ADVERTIR DE ALGO MAL HECHO EN CREAR UNA NUEVA BASE DE DATOS
    '''
    def Warning_Window_Create_Database(self, text):
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text=text, font=("Arial Black", 11)).pack()
        Button(self.new_frame(temp, 0, 0, 120, 60), text="Aceptar", font=("Arial", 12),
               command=self._Warning_Window_Create_Database(temp)).pack()
        print("Entreeee problema")
        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 100, x, y))
        temp.resizable(0, 0)
        temp.title("WARNING CREATEDATABASE")

    def _Warning_Window_Create_Database(self, temp):
        return lambda : self._warning_window_create_database(temp)

    def _warning_window_create_database(self, temp):
        temp.destroy()
        self._command_create_database()



    '''
        Iplementacion de apartado para visualizacion de las bases de datos 
        registradas
    '''
    def show_databases(self, frame):
        self.frame1 = frame
        for i in showDatabases():
            Button(frame, text="• " + str(i), width=30, anchor="w", command=self.command_button_databases(i)).pack()

    def command_button_databases(self, database):
        return lambda: self._command_button_databases(database)

    def _command_button_databases(self, database):
        Databases_Window(self.window, self.Settings_Frame(database), database)



    '''
        FRAME POR DEFECTO PARA QUE EL USUARIO SELECCIONE UNA BASE DE DATOS
    '''
    def Default_frame(self):
        tmp = self.new_frame(self.window, 470, 273, 300, 200)
        Frame(tmp, width=470, height=273).pack()
        Label(self.new_frame(tmp, 0, 0, 20, 20), text="Select a database to start managing",
              font=("Arial Black", 12)).pack()
        return tmp



    '''
        FRAME PARA GESTIONAR LA BASE DE DATOS SELECCIONADA
    '''
    def Settings_Frame(self, database):
        temp = self.new_frame(self.window, 470, 273, 300, 200)
        Frame(temp, width=470, height=273).pack()

        Label(self.new_frame(temp, 0, 0, 20, 10), text="DATABASE NAME: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 150, 10), text=str(database), font=("Arial", 9)).pack()

        Label(self.new_frame(temp, 0, 0, 20, 140), text="SETTINGS: ", font=("Arial Black", 8)).pack()

        Label(self.new_frame(temp, 0, 0, 80, 180), text="RENAME DATABASE", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 20, 170), text=" ✎ ", font=("", 14), foreground="brown", command=self.command_alter_database(database)).pack()

        Label(self.new_frame(temp, 0, 0, 80, 230), text="DROP DATABASE", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 20, 220), text=" ✘ ", font=("", 14), foreground="red", command=self.command_delete_database(database)).pack()

        Label(self.new_frame(temp, 0, 0, 350, 80), text="SHOW TABLES", font=("Arial Black", 8)).pack()
        Button(self.new_frame(temp, 0, 0, 290, 70), text=" ☄ ", font=("", 14), foreground="blue",  command=self.show_tables(database)).pack()

        Label(self.new_frame(temp, 0, 0, 20, 70), text="DETAILS: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 100, 70), text="Tables: ", font=("Arial", 9)).pack()
        Label(self.new_frame(temp, 0, 0, 160, 70), text=" 10 ", font=("Arial", 9)).pack()


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
        Label(self.new_frame(temp, 0,0, 10, 10), text="Are you sure to delete this database?", font=("Arial", 14)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43), text="Database selected: ", font=("Arial Black", 8)).pack()
        Label(self.new_frame(temp, 0, 0, 140, 43), text=str(database), font=("Arial", 9)).pack()
        Button(self.new_frame(temp, 0,0, 80, 80), text="Aceptar", font=("Arial", 12), command=self.DropDatabase(temp, database)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 80), text="Cancelar", font=("Arial", 12), command=self.Cancel(temp, database)).pack()

        x = (temp.winfo_screenwidth() // 2) - (temp.winfo_width() // 2) - 200
        y = (temp.winfo_screenheight() // 2) - (temp.winfo_height() // 2) - 100
        temp.geometry('{}x{}+{}+{}'.format(350, 130, x, y))
        temp.title("DropDatabase")
        temp.resizable(0, 0)
        temp.mainloop()

    def DropDatabase(self, temp,  database):
        return lambda : self._DropDatabase(temp, database)



    '''
        ACEPTAR ELIMINAR LA BASE DE DATOS ACTUAL
    '''
    def _DropDatabase(self, temp, database):
        if database != "":
            temp.destroy()
            dropDatabase(database)
            Databases_Window(self.window, self.Default_frame(), database)



    '''
        CANCELAR LA ACCION DE LA VENTANA EMERGENTE
    '''
    def Cancel(self, temp, database):
        return lambda: self._Cancel(temp, database)

    def _Cancel(self, temp, database):
        temp.destroy()
        #Databases_Window(self.window, self.Default_frame(), database)



    '''
        MOSTRAR VENTANA EMERGENTE PARA MODIFICAR EL NOMBRE DE LA BASE DE DATOS
    '''
    def command_alter_database(self, database):
        return lambda: self._command_alter_database(database)

    def _command_alter_database(self, database):
        Entrada = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text="Enter new database name",font=("Arial Black", 11)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43), text="Name: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 40, 10, 70, 43), width=35, font=("Arial", 10), textvariable=Entrada).pack()
        Button(self.new_frame(temp, 0, 0, 80, 80), text="Aceptar", font=("Arial", 12), command=self.AlterDatabase(temp, Entrada, database)).pack()
        Button(self.new_frame(temp, 0, 0, 170, 80), text="Cancelar", font=("Arial", 12),command=self.Cancel(temp, database)).pack()

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
        return lambda : self._AlterDatabase(tmp, entrada, database)

    def _AlterDatabase(self, tmp, entrada, database):
        if str(entrada.get()) != "":
            temp = storage.Buscar(entrada.get())
            if temp:
                text = "This database already exists"
                tmp.destroy()
                self.Warning_Window_Alter_Database(text, database)
            else:
                alterDatabase(database, entrada.get())
                tmp.destroy()
                Databases_Window(self.window, self.Default_frame(), database)
        else:
            text= "Please write the name of the database"
            tmp.destroy()
            self.Warning_Window_Alter_Database(text, database)


    '''
        VENTANA EMERGENTE PARA CREAR LA BASE DE DATOS
    '''
    def _command_create_database(self):
        Entrada = StringVar()
        temp = Toplevel()
        Label(self.new_frame(temp, 0, 0, 10, 10), text="Enter new database name", font=("Arial Black", 11)).pack()
        Label(self.new_frame(temp, 0, 0, 10, 43), text="Name: ", font=("Arial Black", 8)).pack()
        Entry(self.new_frame(temp, 40, 10, 70, 43), width=35, font=("Arial", 10), textvariable=Entrada).pack()
        Button(self.new_frame(temp, 0, 0, 80, 80), text="Aceptar", font=("Arial", 12)
               , command=self.Create_Database(temp, Entrada)).pack()
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
        return lambda : self._Create_Database(tmp, name)

    def _Create_Database(self,tmp, name):
        if str(name.get()) != "":
            temp = storage.Buscar(name.get())
            if temp:
                text = "This database already exists"
                tmp.destroy()
                self.Warning_Window_Create_Database(text)
            else:
                print("ESTOY CREANDO: "+str(name.get()))
                createDatabase(name.get())
                tmp.destroy()
                Databases_Window(self.window, self.Default_frame(), "")
        else:
            text="Please write the name of the database"
            tmp.destroy()
            self.Warning_Window_Create_Database(text)




    '''
        MOSTRAR VENTANA DE CON LISTADO DE TABLAS
    '''
    def show_tables(self, database):
        return lambda: Tables_Window(database, "", "")



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
        can.bind("<Configure>", lambda e: can.configure(scrollregion=can.bbox("all")))
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
    def __init__(self, database, table_name, directorio):
        window = Toplevel()

        self.database=database
        self.table_name=table_name
        self.window=window
        self.directorio=directorio

        '''  BARRA DE NAVEGACION DE TABLAS DISPONIBLES   '''
        self.nav_var_tables(window, database)

        '''  SCROLL PARA DIRECCIONAR LA IMAGEN DE LA ESTRUCTURA HASH   '''
        Frame1 = LabelFrame(window)
        can = Canvas(Frame1, width=430, height=380)
        Scrollbar_x = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scrollbar_y = Scrollbar(Frame1, orient="horizontal", command=can.xview)
        Scrollbar_y.pack(side="bottom", fill="x")
        Scrollbar_x.pack(side="right", fill="y")
        can.pack(expand=True, fill="both")
        can.configure(yscrollcommand=Scrollbar_x.set, xscrollcommand=Scrollbar_y.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(scrollregion=can.bbox("all")))
        Frame1.place(x=300, y=70)

        ''' AGREGARA LA IMAGEN DE LA ESTRUCTURA HASH'''
        photo = PhotoImage(file=self.directorio)
        Label(frame, image=photo).pack()


        '''  ESPECIFICAR NOMBRE DE LA BASE DE DATOS   '''
        self.Title_BD = Label(self.window, text="BASE DE DATOS: ").place(x=70, y=10)
        Label(self.window, text=self.database).place(x=70, y=35)

        '''  ESPECIFICAR NOMBRE DE LA BASE DE DATOS   '''
        self.Title_Tables = Label(self.window, text="TABLA: ").place(x=430, y=10)
        Label(self.window, text=self.table_name).place(x=480, y=35)


        ''' BOTON DE ACTUALIZAR PAGINA '''
        Button(self.new_frame(window, 0, 0, 20, 10), text="↻", width=0, anchor="c", font=("Arial Black", 12),
               command=self.update_tables()).pack()

        window.geometry("800x500")
        window.resizable(False, False)
        window.title("TytusStorage/Tables")
        window.mainloop()



    '''  MOSTRAR LISTA DE TABLAS DE UNA BASE DE DATOS SELECCIONADA   '''
    def show_tables(self, frame, database):
        for i in showTables(database):
            Button(frame, text="• "+ str(i) , width=30, anchor="w",
                   command=self.command_button_tables(i)).pack()

    '''  DEFINIR LA ACCION DE CADA BOTON PARA MOSTRAR LA IMAGEN DE LA ESTRUCTURA HASH   '''
    def command_button_tables(self, table):
        return lambda: self.update_Image(table)

    '''  ACTUALIZAR LA IMAGEN PARA VISUALIZACION DEL USUARIO   '''
    def update_Image(self,table):
        temp = storage.Devolver(self.database, table)

        indice = 0
        print('Contenido de la tabla:', temp.nombre)
        for i in temp.vector:
            if i is None:
                print('Indice:', indice, 'Contenido:', i)
            else:
                print('Indice:', indice, 'Contenido:', end=' ')
                for j in i:
                    print('{Primaria:'+ str(j.primaria) + '}', end=' ')
                print('')
            indice += 1


        temp.Grafico()
        self.window.destroy()
        Tables_Window(self.database, table, "hash.png")

    '''  BOTON DE ACTUALIZAR PARA LIMPIAR LA IMAGEN EN PANTALLA   '''
    def update_tables(self):
        return lambda: self._update_tables()

    def _update_tables(self):
        self.window.destroy()
        Tables_Window(self.database,"","")

    '''
        BARRA DE NAVEGACION PARA LAS TABLAS
    '''

    def nav_var_tables(self, window, database):
        Frame1 = LabelFrame(window)
        can = Canvas(Frame1, width=230, height=400)
        can.pack(side=LEFT)
        Scroll = Scrollbar(Frame1, orient="vertical", command=can.yview)
        Scroll.pack(side=RIGHT, fill="y")
        can.configure(yscrollcommand=Scroll.set)
        frame = Frame(can)
        can.create_window((False, False), window=frame, anchor="nw")
        can.bind("<Configure>", lambda e: can.configure(scrollregion=can.bbox("all")))
        Frame1.place(x=20, y=70)
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
    def __init__(self, database, table_name, directorio):
        window = Toplevel()

        self.database = database
        self.table_name = table_name
        self.window = window
        self.directorio = directorio
        pass




if __name__ == '__main__':


    '''showDatabases()
    showTables("BD_Principal")'''

    '''print(createDatabase("BD_Principal"))
    print(createDatabase("BD_Secundaria"))
    input("stop")
    print(showDatabases())'''

    '''print(createTable("BD_Principal", "Tabla 1 BD", 4))
    input("stop")
    print(createTable("BD_Principal", "Tabla 2 BD", 5))'''


    '''print(createTable("BD_Principal", "Tabla 1 BD", 4))
    print(insert("BD_Principal", "Tabla 1 BD", ["Carros", "Aviones", "Barcos", "Naves"]))'''

    '''print(createTable("BD_Principal", "Tabla 1 BD", 4))

    print(insert("BD_Principal", "Tabla 1 BD", ["Carros1", "Aviones1", "Barcos1", "Naves1"]))
    print(insert("BD_Principal", "Tabla 1 BD", ["Carros2", "Aviones2", "Barcos2", "Naves2"]))
    print(insert("BD_Principal", "Tabla 1 BD", ["Carros3", "Aviones3", "Barcos3", "Naves3"]))
    print(insert("BD_Principal", "Tabla 1 BD", ["Carros4", "Aviones4", "Barcos4", "Naves4"]))'''

    #print(createDatabase("BD_Secundaria"))
    print(extractTable("BD_Principal", "Tabla 1 BD"))
    #input("stop")
    print(showTables("BD_Principal"))
    print(showTables("BD_Secundaria"))
    '''print(createDatabase("BD_3"))
    print(createDatabase("BD_4"))
    print(createDatabase("BD_5"))
    print(createDatabase("BD_6"))
    print(createDatabase("BD_7"))'''


    #Databases_Window(Tk(), "", "")




