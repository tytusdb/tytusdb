#interfaz2
from storage import storage as storage
from storage import Serializable as Serializable
from storage.avl.DataAccessLayer import reports as avl_graph
from storage.b import Estructura_ArbolB as b_graph
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import os

def show_data_bases():
    data_bases = storage.showDatabases()
    tree_window = Toplevel(main_window)
    main_window.iconify()
    tree_window.geometry('715x580+200+75')
    tree_window.title('Bases de datos')
    main_tree = Frame(tree_window)
    main_tree.pack(fill=BOTH, expand=1)
    main_tree.configure(background='black')
    canvas_tree = Canvas(tree_window, width=650, height=470)
    canvas_tree.place(x=20, y=75)
    scroll = Scrollbar(main_tree, orient=VERTICAL, command=canvas_tree.yview)
    scroll.pack(side=RIGHT, fill=Y)
    canvas_tree.configure(yscrollcommand=scroll.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
    scroll_tree = Scrollbar(main_tree, orient=HORIZONTAL, command=canvas_tree.xview)
    scroll_tree.pack(side=BOTTOM, fill=X)
    canvas_tree.configure(xscrollcommand=scroll_tree.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
    frame_tree = Frame(canvas_tree)
    canvas_tree.create_window((0, 0), width=10000, height=5000, window=frame_tree, anchor='nw')
    xview = 10
    yview = 5
    contador = 0
    names = []
    for x in data_bases:
        names.append(x)
        Button(frame_tree, text=x, font='Helvetica 8 bold italic', fg='white', bg='black',command= 
        lambda database=x: show_tables(tree_window, database) ,width=15,padx=15, pady=5).place(x=xview, y=yview)
        xview += 160
        contador += 1
        if contador == 4:
            contador = 0
            xview = 10
            yview += 40

    Button(main_tree, text='Regresar', font='Helvetica 10 bold italic',command=lambda:
    close_table_window(tree_window, main_window), bg='red', width=15, pady=3).place(x=20, y=15)
  
def show_tables(parent_window, database):
    tables = storage.showTables(database)
    parent_window.iconify()
    table_window = Toplevel(parent_window)
    parent_window.iconify()
    table_window.geometry('720x580+200+75')
    table_window.title(database)
    main_tree = Frame(table_window)
    main_tree.pack(fill=BOTH, expand=1)
    main_tree.configure(background='black')
    canvas_tree = Canvas(table_window, width=650, height=470)
    canvas_tree.place(x=25, y=75)
    scroll = Scrollbar(main_tree, orient=VERTICAL, command=canvas_tree.yview)
    scroll.pack(side=RIGHT, fill=Y)
    canvas_tree.configure(yscrollcommand=scroll.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))

    scroll_tree = Scrollbar(main_tree, orient=HORIZONTAL, command=canvas_tree.xview)
    scroll_tree.pack(side=BOTTOM, fill=X)
    canvas_tree.configure(xscrollcommand=scroll_tree.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
    frame_tree = Frame(canvas_tree)
    
    canvas_tree.create_window((0, 0), width=10000, height=5000, window=frame_tree, anchor='nw')
    yview = 5
    xview = 10
    contador = 0
    names = []
    for x in tables:
        names.append(x)
        Button(frame_tree, text=x, font='Helvetica 8 bold italic', fg='white', bg='black'
        ,command=lambda table=x: extract_table(database, table, table_window),width=15,padx=15, pady=5).place(x=xview, y=yview)
        xview += 160
        contador += 1
        if contador == 4:
            contador = 0
            xview = 10
            yview += 40
    Button(table_window, text='Regresar', font='Helvetica 10 bold italic',command=lambda:
    close_table_window(table_window, parent_window), bg='red', width=15, pady=3).place(x=25, y=15)
    
def rows_picture(database, table, canvas, frame):
    storage.checkData()
    try:
        print('entre')
        data = Serializable.Read('./Data/',"Data")
        db = data.get(database)
        dataTable = Serializable.Read('./Data/',"DataTables")
        tab = dataTable.get(database+"_"+table)
        if db:
            if tab:
                if tab[1] == 'avl':
                    res = storage.avl.extractTable(database, table)
                    try:
                        avl_graph.graphAVL(database, table)
                        canvas.image = PhotoImage(file=f'./tmp/grafo-avl.png')
                        Label(frame, image=canvas.image).place(x=50, y=50)
                    except:
                        return res
                elif tab[1] == 'b':
                    res = storage.b.extractTable(database, table)
                    try:
                        table_aux = Serializable.Read(f'./Data/B/', database+'-'+table+'-b')
                        table_aux.graficar()  
                        canvas.image = PhotoImage(file='salida.png')
                        Label(frame, image=canvas.image).place(x=50, y=50)
                    except:
                        return res
                elif tab[1] == 'bplus':
                    res = storage.bplus.extractTable(database, table)
                    try:
                        table_aux = Serializable.Read(f'./Data/BPlusMode/{database}/{table}/', table)
                        table_aux.graficar(database, table)
                        canvas.image = PhotoImage(file=f'./Data/BPlusMode/{database}/{table}/{table}.png')
                        Label(frame, image=canvas.image).place(x=50, y=50)
                    except:
                        pass
                        return res
                elif tab[1] == 'dict':
                    res = storage.dict.extractTable(database, table)
                elif tab[1] == 'isam':
                    res = storage.isam.extractTable(database, table)
                    try:
                        storage.isam.chart(database, table)
                        canvas.image = PhotoImage(file='isam.png')
                        Label(frame, image=canvas.image).place(x=50, y=50)
                    except:
                        return res
                elif tab[1] == 'json':
                    res = storage.json.extractTable(database, table)
                elif tab[1] == 'hash':
                    res = storage.hash.extractTable(database, table)
                    try:
                        table_aux = Serializable.Read(f'./Data/hash/{database}/', table)  
                        table_aux.Grafico()
                        canvas.image = PhotoImage(file='hash.png')
                        Label(frame, image=canvas.image).place(x=50, y=50)
                    except:
                        return res
                return res
        return None
    except:
        print('error')
        return None
    print('')


def extract_table(database, table, parent_window):
    table_window = Toplevel(parent_window)
    parent_window.iconify()
    table_window.geometry('950x580+200+75')
    table_window.title(database+' :' + table)
    main_tree = Frame(table_window)
    main_tree.pack(fill=BOTH, expand=1)
    main_tree.configure(background='black')
    canvas_tree = Canvas(table_window, width=850, height=445)
    canvas_tree.place(x=25, y=75)
    scroll = Scrollbar(main_tree, orient=VERTICAL, command=canvas_tree.yview)
    scroll.pack(side=RIGHT, fill=Y)
    canvas_tree.configure(yscrollcommand=scroll.set)
    #canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_buttons.bbox('all')))
    scroll_tree = Scrollbar(main_tree, orient=HORIZONTAL, command=canvas_tree.xview)
    scroll_tree.pack(side=BOTTOM, fill=X)
    canvas_tree.configure(xscrollcommand=scroll_tree.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
    frame_tree = Frame(canvas_tree)
    canvas_tree.create_window((0, 0), width=20000, height=5000, window=frame_tree, anchor='nw')
    datos = rows_picture(database, table, canvas_tree, frame_tree)
    Button(table_window, text='Regresar', font='Helvetica 10 bold italic',
    command=lambda: close_table_window(table_window, parent_window), bg='red', width=15, pady=1.5).place(x=25, y=15)
    canvas_image = Canvas(table_window)
    canvas_image.image = PhotoImage(file='lock_red.png')
    Button(table_window, image=canvas_image.image, command=lambda: safe_mode(database, table, table_window)).place(x=837,y=15)
    variable = StringVar(table_window)
    variable.set(datos[0])
    box = OptionMenu(table_window, variable, *datos)
    box.place(x=175, y=15)

def close_table_window(window, parent):
    window.destroy()
    parent.deiconify()

def safe_mode(database, table, window):
    try:
        storage.block.blockchain().graficar(database, table)
        table_window = Toplevel(window)
        table_window.geometry('950x610+200+75')
        table_window.title('Safe Mode')
        main_tree = Frame(table_window)
        main_tree.pack(fill=BOTH, expand=1)
        main_tree.configure(background='black')
        canvas_tree = Canvas(table_window, width=850, height=500)
        canvas_tree.place(x=25, y=75)
        scroll = Scrollbar(main_tree, orient=VERTICAL, command=canvas_tree.yview)
        scroll.pack(side=RIGHT, fill=Y)
        canvas_tree.configure(yscrollcommand=scroll.set)
        canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
        scroll_tree = Scrollbar(main_tree, orient=HORIZONTAL, command=canvas_tree.xview)
        scroll_tree.pack(side=BOTTOM, fill=X)
        canvas_tree.configure(xscrollcommand=scroll_tree.set)
        canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
        frame_tree = Frame(canvas_tree)
        canvas_tree.create_window((0, 0), width=50000, height=1000, window=frame_tree, anchor='nw')
        canvas_tree.image = PhotoImage(file='tupla.png')
        Label(frame_tree, image=canvas_tree.image).place(x=50, y=50)
        canvas_image = Canvas(table_window)
        canvas_image.image = PhotoImage(file='unlock.png')
        Button(table_window,image=canvas_image.image,command=lambda:no_safe(table_window)).place(x=837, y=15)
    except:
        messagebox.showinfo(title='Safe Mode', message='No posee registros en el modo seguro')

def no_safe(window):
    window.destroy()

main_window = tkinter.Tk()
main_window.geometry('610x310+300+100')
main_window.title('Tytus EDD: Fase 2')
main_window.configure(background='black')
main_canvas = Canvas(main_window, width=580, height=280).place(x=15, y=10)
tkinter.Label(main_canvas, text='Tytus Database', font='Helvetica 30 bold italic',padx=10, pady=5).place(x=150, y=20)
tkinter.Button(main_canvas, text='Reportes', font='Helvetica 16 bold italic', width=20, height=2, borderwidth= 5, fg='white',
command=show_data_bases,background='black').place(x=175, y=150)
main_window.mainloop()