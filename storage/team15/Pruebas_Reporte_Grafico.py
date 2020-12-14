import tkinter as tk
from tkinter import *
from tkinter import ttk

# create_table

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns =columns
        self.list_tuples = []

    def get_Name_Table(self):
        return self.name


# create_database

class Database:
    def __init__(self, name):
        self.name = name
        self.index_tables = 0
        self.list_table = []

    # get database name
    def get_Name_Database(self):
        return self.name

    def get_Index_Table(self):
        return self.index_tables

    # add new table
    def _add_table(self, name_table, columns):
        self.list_table.append(Table(name_table, columns))
        self.index_tables += 1

    # get Tables
    def get_Tables(self):
        return self.list_table



class List_Database:
    def __init__(self):
        self.database = []

    def add_database(self, name):
        self.database.append(Database(name))

    def add_table(self, name_database, name_table, columns):
        for i in self.database:
            if i.get_Name_Database() == name_database:
                i._add_table(name_table, columns)

    def show_database(self):
        for i in self.database:
            print("NAME DATABASE: " + str(i.get_Name_Database()))

    def show_tables(self, name_database):
        for i in self.database:
            if i.get_Name_Database() == name_database:
                print("NAME DATABASE: " + str(i.get_Name_Database()))
                for j in i.get_Tables():
                    print("NAME TABLE: " + str(j.get_Name_Table()))


# View Databases

class Database_Window:
    def __init__(self, databases, window):
        self.databases = databases
        self.window = window

        window.title("Bases de Datos")
        window.geometry("520x480")
        Label(self.window, text="BASES DE DATOS", font=("Algerian", 26)).place(x=60, y=10)
        self.fill_databases()

    def show_tables(self, name, database):
        if database.get_Index_Table() == 0:
            return lambda: print("No hay tablas")
        else:
            return lambda: Tables_Window(self.databases, name, tk.Tk())


    def fill_databases(self):
        width = 20
        height = 80
        for i in self.databases.database:
            button = Button(self.window, text="Ver tablas", width=10, font=("Arial Black", 10), bg="light gray")
            button.config(command=self.show_tables(i.get_Name_Database(), i))
            button.place(x=width, y=height)
            Label(self.window, text=i.get_Name_Database(), font=("Algerian", 14)).place(x=width + 120, y=height)
            height += 40
        self.window.mainloop()


#View Tables

class Tables_Window:
    def __init__(self, databases, database_selected, window):
        self.databases = databases
        self.window = window

        window.title("Tablas")
        window.geometry("450x350")
        Label(self.window, text="Database: "+database_selected, font=("Algerian", 20)).place(x=20, y=10)
        Label(self.window, text="Tablas_________", font=("Arial Black", 10)).place(x=140, y=50)
        self.fill_tables(database_selected)

    def show_tuplas(self, name):
        return lambda: print("tuplas de "+str(name))

    def fill_tables(self, database_name):
        width = 20
        height = 80

        for i in self.databases.database:
            if database_name == str(i.get_Name_Database()):
                for j in i.get_Tables():
                    button = Button(self.window, text="ver tuplas", width=10, font=("Arial Black", 10), bg="light gray")
                    button.config(command=self.show_tuplas(j.get_Name_Table()))
                    button.place(x=width, y=height)
                    Label(self.window, text=j.get_Name_Table(), font=("Algerian", 14)).place(x=width + 120, y=height)
                    height += 40

                self.window.mainloop()



if __name__ == '__main__':

    list = List_Database()

    # add databases
    list.add_database("Proyecto_EDD")
    list.add_database("Base 2")
    list.add_database("Base 3")
    list.add_database("Othello")


    # add tables
    list.add_table("Proyecto_EDD", "Arbol AVL", 5)
    list.add_table("Proyecto_EDD", "Arbol B", 5)
    list.add_table("Proyecto_EDD", "Arbol B+", 5)
    list.add_table("Proyecto_EDD", "ISAM", 5)
    list.add_table("Proyecto_EDD", "Tablas Hash", 5)


    list.add_table("Base 2", "Table 4", 4)
    list.add_table("Base 2", "Table 5", 5)
    list.add_table("Base 2", "Table 6", 6)

    # show
    list.show_database()
    print()
    list.show_tables("Base 1")
    print()
    list.show_tables("Base 2")

    # graphic
    Database_Window(list, tk.Tk())





