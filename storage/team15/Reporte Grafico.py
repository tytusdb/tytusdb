
from tkinter import *
from TytusStorage import*
from ListaBaseDatos import*




class Databases_Window:
    def __init__(self, window):
        self.window = window

        self.nav_var_databases(window)

        Button(self.new_frame(window, 0, 0, 20, 10), text="↻", width=0, anchor="c", font=("Arial Black", 12)
               , command=self.update_databases()).pack()

        Label(self.window, text="BASE DE DATOS: ").place(x=70, y=20)


        #window.geometry("800x500")
        window.geometry("350x500")
        window.resizable(False, False)
        window.title("TytusStorage")
        window.mainloop()

    '''
        Iplementacion de apartado para visualizacion de las bases de datos 
        registradas
    '''

    def show_databases(self, frame):
        self.frame1=frame
        for i in storage.lista_bases_datos:
            Button(frame, text="• "+str(i.Name), width=30, anchor="w", command=self.command_button_databases(i)).pack()


    def command_button_databases(self, database):
        return lambda: self.show_tables(database)

    '''
        Mostrar ventana de tablas
    '''

    def show_tables(self, database):
        print("Hola: "+database.Name)
        #self.window.destroy()
        Tables_Window(database, "", "")


    '''
        Boton de actualizacion de la pagina
    '''
    def update_databases(self):
        return lambda: Databases_Window(self.window)

    '''
        Barra de navegacion para las bases de datos
    '''

    def nav_var_databases(self, window):
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
        self.show_databases(frame)

    '''
        Crear frame para cada wiggles que se pone en la ventana principal
    '''

    def new_frame(self,window, width, height, x, y):
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
        Label(self.window, text=self.database.Name).place(x=70, y=35)

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
        for i in database.list_table:
            Button(frame, text="• "+ str(i.nombre) , width=30, anchor="w",
                   command=self.command_button_tables(i)).pack()

    '''  DEFINIR LA ACCION DE CADA BOTON PARA MOSTRAR LA IMAGEN DE LA ESTRUCTURA HASH   '''
    def command_button_tables(self, table):
        return lambda: self.update_Image(table)

    '''  ACTUALIZAR LA IMAGEN PARA VISUALIZACION DEL USUARIO   '''
    def update_Image(self,table):
        table.Grafico()
        self.window.destroy()
        Tables_Window(self.database, table.nombre, "hash.png")

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




if __name__ == '__main__':
    createDatabase(5, "BD_Principal")
    print()
    createDatabase(5, "BD_Secundaria")
    print()
    createDatabase(5, "BD_Secundaria_1")
    print()
    createDatabase(5, "BD_Secundaria_2")
    print()

    createTable("BD_Principal", "Tabla 1 BD", 2)
    createTable("BD_Principal", "Tabla 2 BD", 3)
    createTable("BD_Principal", "Tabla 3 BD", 3)
    createTable("BD_Principal", "Tabla 5 BD", 11)
    createTable("BD_Principal", "Tabla 6 BD", 8)
    createTable("BD_Principal", "Tabla 7 BD", 9)
    createTable("BD_Principal", "Tabla 8 BD", 10)
    createTable("BD_Principal", "Tabla 9 BD", 11)
    createTable("BD_Principal", "Tabla 10 BD", 8)
    createTable("BD_Principal", "Tabla 11 BD", 9)
    createTable("BD_Principal", "Tabla 12 BD", 10)
    createTable("BD_Principal", "Tabla 13 BD", 11)
    createTable("BD_Principal", "Tabla 14 BD", 8)
    createTable("BD_Principal", "Tabla 15 BD", 9)
    createTable("BD_Principal", "Tabla 16 BD", 10)
    createTable("BD_Principal", "Tabla 17 BD", 11)
    createTable("BD_Principal", "Tabla 18 BD", 8)
    createTable("BD_Principal", "Tabla 19 BD", 9)
    createTable("BD_Principal", "Tabla 20 BD", 10)
    createTable("BD_Principal", "Tabla 21 BD", 11)
    createTable("BD_Principal", "Tabla 22 BD", 8)
    createTable("BD_Principal", "Tabla 23 BD", 9)
    createTable("BD_Principal", "Tabla 24 BD", 10)
    createTable("BD_Principal", "Tabla 25 BD", 11)

    insert("BD_Principal", "Tabla 1 BD", ["Hola","Adios"])
    insert("BD_Principal", "Tabla 2 BD", ["Mundo", "Planeta", "Satelite"])
    insert("BD_Principal", "Tabla 3 BD", ["Pez", "Gato", "Perro"])

    showDatabases()
    showTables("BD_Principal")



    Databases_Window(Tk())




