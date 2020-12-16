import Storage
import tkinter
from tkinter import *
from tkinter import messagebox


def show_data_bases():
    data_bases = Storage.showDatabases()
    tree_window = Toplevel(main_window)
    main_window.iconify()
    tree_window.geometry('800x600')
    tree_window.title('Bases de datos')
    main_tree = Frame(tree_window)
    main_tree.pack(fill=BOTH, expand=1)
    canvas_tree = Canvas(main_tree, width=800, height=600)
    canvas_tree.place(x=0, y=0)
    scroll = Scrollbar(main_tree, orient=VERTICAL, command=canvas_tree.yview)
    scroll.pack(side=RIGHT, fill=Y)
    canvas_tree.configure(yscrollcommand=scroll.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
    scroll_tree = Scrollbar(main_tree, orient=HORIZONTAL, command=canvas_tree.xview)
    scroll_tree.pack(side=BOTTOM, fill=X)
    canvas_tree.configure(xscrollcommand=scroll_tree.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
    frame_tree = Frame(canvas_tree)
    canvas_tree.create_window((100, 0), width=1000, height=1000, window=frame_tree, anchor='nw')
    canvas_tree.image = PhotoImage(file='C:/Users/Marcos/Desktop/Data/DataBases.png')
    Button(frame_tree, image=canvas_tree.image).pack()
    Label(frame_tree, bg='#C4D3CB', width=200, height=200).place(x=0, y=0)
    Label(frame_tree, image=canvas_tree.image).place(x=150, y=20)
    Button(canvas_tree, text='Regresar', padx=20, pady=5, font='Helvetica 8 bold italic', bg='#FF6666',command=lambda: close_table_window(tree_window, main_window)).place(x=0, y=0)
    y = 200
    n = 0
    top = 600
    for x in data_bases:
        Button(frame_tree, text=x, font='Helvetica 8 bold italic', bg='#CCFF99', padx=15, pady=3).place(x=y, y=top)
        n += 1
        y += 80
        if n == 5:
            n = 0
            y = 200
            top += 30

def show_functions():
        main_window.iconify()
        function_window = Toplevel(main_window)
        function_window.title('Funciones de las bases de datos')
        function_window.geometry('600x600')
        #function_canvas = Canvas(function_window, width=600, height=600)
        #function_canvas.image = PhotoImage(file='fondo_bases.png')
        #tkinter.Label(function_window, image=function_canvas.image).place(x=0, y=0)
        Button(function_window, text='Regresar', padx=20, pady=5, font='Helvetica 8 bold italic', bg='#FF6666',command=lambda: close_table_window(function_window, main_window)).place(x=0, y=0)
        tkinter.Label(function_window,text='Create Database',font='Helvetica 10 bold italic', width=20).place(x=10, y=50)
        database_name = Entry(function_window,width=20)
        database_name.place(x=150,y=50)
        tkinter.Button(function_window, text='Create',font='Helvetica 10 bold italic', width=10, command= lambda : create_database(database_name.get(),database_name)).place(x=250, y=45)
        tkinter.Label(function_window, text='Alter Database', font='Helvetica 10 bold italic', width=20).place(x=10, y=100)
        alter_data_base = Entry(function_window, width=20)
        alter_data_base.place(x=150, y=100)
        tkinter.Button(function_window, text='Alter', font='Helvetica 10 bold italic', width=10, command=lambda: alter_database(alter_data_base.get(), alter_data_base)).place(x=250, y=95)


def create_database(database,database_name):
    if database:
        result = Storage.createDatabase(database)
        if result == 0:
            messagebox.showinfo(title='Create Database', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Create Database', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Create Database', message='Base de datos existente')
        database_name.delete(0,END)
    else:
        messagebox.showinfo(title='Create Database', message='No escribio un nombre')
        print('No qlon')

def alter_database(info, alter_data_base):
    if info:
        print(info)
        new_name = info.split(',')
        result = Storage.alterDatabase(new_name[0], new_name[1])
        if result == 0:
            messagebox.showinfo(title='Create Database', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Create Database', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Create Database', message=new_name[0] + ' no existe')
        elif result == 3:
            messagebox.showinfo(title='Create Database', message=new_name[1] + ' ya existe')
        alter_data_base.delete(0, END)
    else:
        messagebox.showinfo(title='Create Database', message='No escribio un nombre')

def close_table_window(window, parent):
        window.destroy()
        parent.deiconify()




main_window = tkinter.Tk()
main_window.geometry('600x500')
main_window.title('Tytus EDD: Fase 1')
#imagen = PhotoImage(file='imagenEDD.png')
#tkinter.Label(main_window, image=imagen).place(x=0, y=0)
tkinter.Label(main_window, text='Estructuras de datos: Grupo 18', font='Helvetica 16 bold italic', bg='#99CCFF',padx=10, pady=5).place(x=200, y=20)
tkinter.Button(main_window, text='Reportes', font='Helvetica 16 bold italic', bg='#CCFF99', width=20, height=2, command=show_data_bases).place(x=10, y=100)
tkinter.Button(main_window, text='Funciones', font='Helvetica 16 bold italic',bg='#CCFF99',width=20, height=2, command=show_functions).place(x=10, y=200)
main_window.mainloop()