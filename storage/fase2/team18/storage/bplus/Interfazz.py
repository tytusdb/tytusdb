# B+ Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from . import BPlusMode as Storage
from . import BplusTree
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import os

def show_data_bases():
    data_bases = Storage.showDatabases()
    database_tree = Storage.serializable.Read('./Data/BPlusMode/', 'Databases')
    database_tree.graph("Databases")
    tree_window = Toplevel(main_window)
    main_window.iconify()
    tree_window.geometry('950x580+200+75')
    tree_window.title('Bases de datos')
    main_tree = Frame(tree_window)
    main_tree.pack(fill=BOTH, expand=1)
    main_tree.configure(background='black')
    canvas_tree = Canvas(tree_window, width=750, height=470)
    canvas_tree.place(x=170, y=75)
    scroll = Scrollbar(main_tree, orient=VERTICAL, command=canvas_tree.yview)
    scroll.pack(side=RIGHT, fill=Y)
    canvas_tree.configure(yscrollcommand=scroll.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_buttons.bbox('all')))
    scroll_tree = Scrollbar(main_tree, orient=HORIZONTAL, command=canvas_tree.xview)
    scroll_tree.pack(side=BOTTOM, fill=X)
    canvas_tree.configure(xscrollcommand=scroll_tree.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
    frame_tree = Frame(canvas_tree)
    canvas_tree.create_window((0, 0), width=10000, height=5000, window=frame_tree, anchor='nw')
    canvas_tree.image = PhotoImage(file='./Data/BPlusMode/DataBases.png')
    #Label(frame_tree, width=2000, height=200).place(x=0, y=0)
    Label(frame_tree, image=canvas_tree.image).place(x=50, y=50)


    canvas_buttons = Canvas(tree_window, background='red',width=130, height=470)
    canvas_buttons.place(x=25, y=75)
    scroll_buttons = Scrollbar(main_tree, orient=VERTICAL, command=canvas_buttons.yview)
    scroll_buttons.pack(side=LEFT, fill=Y)
    canvas_buttons.configure(yscrollcommand=scroll_buttons.set)
    canvas_buttons.bind('<Configure>', lambda e: canvas_buttons.configure(scrollregion=canvas_buttons.bbox('all')))
    buttons_frame = Frame(canvas_buttons)
    canvas_buttons.create_window((15,0), width=130, height=5000, window=buttons_frame, anchor='nw')
    yview = 5
    names = []
    for x in data_bases:
        names.append(x)
        Button(buttons_frame, text=x, font='Helvetica 8 bold italic', fg='white', bg='black',command= lambda database=x: show_tables(tree_window, database) ,width=15,padx=15, pady=5).place(x=0, y=yview)
        yview += 35
    Button(main_tree, text='Regresar', font='Helvetica 10 bold italic', command=lambda: close_table_window(tree_window, main_window), bg='red', width=15, pady=3).place(x=25, y=15)
    Button(main_tree, text='Create', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda: create_database_window(tree_window)).place(x=170, y=15)
    Button(main_tree, text='Alter', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda: alter_database_window(tree_window, names)).place(x=270, y=15)
    Button(main_tree, text='Drop', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda: drop_database_window(tree_window, names)).place(x=370, y=15)
    Button(main_tree, text='Show Tables', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda: show_tables_window(tree_window, names)).place(x=470, y=15)

def show_tables(parent_window, database):
    tables = Storage.showTables(database)
    db = Storage.serializable.Read(f"./Data/BPlusMode/{database}/", database)
    db.graph(database)
    parent_window.iconify()
    table_window = Toplevel(parent_window)
    parent_window.iconify()
    table_window.geometry('950x580+200+75')
    table_window.title(database)
    main_tree = Frame(table_window)
    main_tree.pack(fill=BOTH, expand=1)
    main_tree.configure(background='black')
    canvas_tree = Canvas(table_window, width=750, height=470)
    canvas_tree.place(x=170, y=75)
    scroll = Scrollbar(main_tree, orient=VERTICAL, command=canvas_tree.yview)
    scroll.pack(side=RIGHT, fill=Y)
    canvas_tree.configure(yscrollcommand=scroll.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_buttons.bbox('all')))
    scroll_tree = Scrollbar(main_tree, orient=HORIZONTAL, command=canvas_tree.xview)
    scroll_tree.pack(side=BOTTOM, fill=X)
    canvas_tree.configure(xscrollcommand=scroll_tree.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
    frame_tree = Frame(canvas_tree)
    canvas_tree.create_window((0, 0), width=10000, height=5000, window=frame_tree, anchor='nw')
    canvas_tree.image = PhotoImage(file=f'./Data/BPlusMode/{database}/{database}.png')
    Label(frame_tree, image=canvas_tree.image).place(x=150, y=50)
    canvas_buttons = Canvas(table_window, width=120, height=470)
    canvas_buttons.place(x=25, y=75)
    scroll_buttons = Scrollbar(main_tree, orient=VERTICAL, command=canvas_buttons.yview)
    scroll_buttons.pack(side=LEFT, fill=Y)
    canvas_buttons.configure(yscrollcommand=scroll_buttons.set)
    canvas_buttons.bind('<Configure>', lambda e: canvas_buttons.configure(scrollregion=canvas_buttons.bbox('all')))
    buttons_frame = Frame(canvas_buttons)
    canvas_buttons.create_window((15, 0), width=120, height=6000, window=buttons_frame, anchor='nw')
    yview = 5
    names = []
    for x in tables:
        names.append(x)
        Button(buttons_frame, text=x, font='Helvetica 8 bold italic', fg='white', bg='black', command=lambda table=x: extract_table(database, table, table_window),width=15,padx=15, pady=5).place(x=0, y=yview)
        yview += 35
    Button(table_window, text='Regresar', font='Helvetica 10 bold italic',command=lambda:
    close_table_window(table_window, parent_window), bg='red', width=15, pady=3).place(x=25, y=15)
    Button(table_window, text='Create', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    create_table_window(parent_window, table_window, database)).place(x=170, y=15)
    Button(main_tree, text='Extract', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    extract_table_window(database, names)).place(x=270, y=15)
    Button(main_tree, text='Extract Range', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3,command=lambda:
    extract_range_table_window(database, names)).place(x=370, y=15)
    Button(main_tree, text='Alter', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3,command=lambda:
    alter_table_window(parent_window,table_window,database, names)).place(x=520, y=15)
    Button(main_tree, text='Drop', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    drop_table_window(parent_window, table_window, database, names)).place(x=620, y=15)

def extract_table(database, table, parent_window):
    rows = Storage.extractTable(database, table)
    keys = get_keys(database, table)
    table_window = Toplevel(parent_window)
    parent_window.iconify()
    table_window.geometry('950x580+200+75')
    table_window.title(database+' :' + table)
    main_tree = Frame(table_window)
    main_tree.pack(fill=BOTH, expand=1)
    main_tree.configure(background='black')
    canvas_tree = Canvas(table_window, width=750, height=445)
    canvas_tree.place(x=170, y=100)
    scroll = Scrollbar(main_tree, orient=VERTICAL, command=canvas_tree.yview)
    scroll.pack(side=RIGHT, fill=Y)
    canvas_tree.configure(yscrollcommand=scroll.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_buttons.bbox('all')))
    scroll_tree = Scrollbar(main_tree, orient=HORIZONTAL, command=canvas_tree.xview)
    scroll_tree.pack(side=BOTTOM, fill=X)
    canvas_tree.configure(xscrollcommand=scroll_tree.set)
    canvas_tree.bind('<Configure>', lambda e: canvas_tree.configure(scrollregion=canvas_tree.bbox('all')))
    frame_tree = Frame(canvas_tree)
    canvas_tree.create_window((0, 0), width=10000, height=5000, window=frame_tree, anchor='nw')
    canvas_tree.image = PhotoImage(file=f'./Data/BPlusMode/{database}/{table}/{table}.png')
    Label(frame_tree, image=canvas_tree.image).place(x=50, y=50)

    canvas_buttons = Canvas(table_window, width=120, height=433)
    canvas_buttons.place(x=25, y=110)
    scroll_buttons = Scrollbar(main_tree, orient=VERTICAL, command=canvas_buttons.yview)
    scroll_buttons.pack(side=LEFT, fill=Y)
    canvas_buttons.configure(yscrollcommand=scroll_buttons.set)
    canvas_buttons.bind('<Configure>', lambda e: canvas_buttons.configure(scrollregion=canvas_buttons.bbox('all')))
    buttons_frame = Frame(canvas_buttons)
    canvas_buttons.create_window((15, 0), width=120, height=5000, window=buttons_frame, anchor='nw')
    Button(table_window, text='Regresar', font='Helvetica 10 bold italic',command=lambda: close_table_window(table_window, parent_window), bg='red', width=15, pady=1.5).place(x=25, y=15)
    yview = 5
    names = []
    for x in range(0,len(list(keys))):
        Button(buttons_frame, text=keys[x], font='Helvetica 8 bold italic',  fg='white', bg='black',command=lambda info=rows[x], key=keys[x]: table_graph(info, key, table, database), width=15, padx=15, pady=5).place(x=0, y=yview)
        yview += 35
    Button(table_window, text='AddPK', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    alter_addPK_window(parent_window, table_window, database, table)).place(x=170, y=15)
    Button(table_window, text='DropPK', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    alter_dropPK(parent_window, table_window,database, table)).place(x=270, y=15)
    Button(table_window, text='Add Column', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3,command=lambda:
    alter_addColumn_window(parent_window, table_window,database, table)).place(x=380, y=15)
    Button(table_window, text='Drop Column', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    alter_dropColumn_window(parent_window, table_window, database, table)).place(x=520, y=15)
    Button(table_window, text='Insert', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    insert_row_window(parent_window, table_window, database, table)).place(x=660, y=15)
    Button(table_window, text='Load CSV', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    load_csv_window(parent_window, table_window, database, table)).place(x=750, y=15)
    Button(table_window, text='Extract', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    extract_row_window(database, table)).place(x=170, y=60)
    Button(table_window, text='Update', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    update_window(parent_window, table_window, database, table)).place(x=270, y=60)
    Button(table_window, text='Delete', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    delete_window(parent_window, table_window, database, table)).place(x=380, y=60)
    Button(table_window, text='Truncate', font='Helvetica 10 bold italic', bg='white', padx=20, pady=3, command=lambda:
    truncate_table(parent_window, table_window, database, table)).place(x=480, y=60)
    tkinter.Label(table_window, bg='yellow', text='Columnas: '+getColumn(database, table)[0], font='Helvetica 10 bold italic',width=10, padx=20, pady=3).place(x=25, y=50)
    tkinter.Label(table_window, bg='yellow', text='PK: '+",".join(str(x) for x in getColumn(database, table)[1]), font='Helvetica 10 bold italic',width=10, padx=20, pady=3).place(x=25, y=80)


def getColumn(database, table):
    Storage.checkData()
    # Get the databases tree
    dataBaseTree = Storage.serializable.Read('./Data/BPlusMode/', "Databases")
    # Get the dbNode
    databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database)
    # If DB exist
    if databaseNode:
        tablesTree = Storage.serializable.Read(f"./Data/BPlusMode/{database}/", database)
        if tablesTree.search(tablesTree.getRoot(), table):
            table_aux = Storage.serializable.Read(f'./Data/BPlusMode/{database}/{table}/', table)
            if len(table_aux.PKey):
                pk = table_aux.PKey
            else:
                pk = ['PK Oculta']
            return [str(table_aux.columns),pk]
        else:
            return ['0',['PK Oculta']]
    else:
        return ['0',['PK Oculta']]

def get_keys(database, table):
    Storage.checkData()
    # Get the databases tree
    dataBaseTree = Storage.serializable.Read('./Data/BPlusMode/', "Databases")
    # Get the dbNode
    databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database)
    # If DB exist
    if databaseNode:
        tablesTree = Storage.serializable.Read(f"./Data/BPlusMode/{database}/", database)
        if tablesTree.search(tablesTree.getRoot(), table):
            table_aux = Storage.serializable.Read(f'./Data/BPlusMode/{database}/{table}/', table)
            table_aux.graficar(database, table)
            return list(table_aux.lista())
        else:
            return None
    else:
        return None

def table_graph(tupla, key, table, database):
    f = open(f'Data/BPlusMode/{database}/{table}/tupla.dot', 'w', encoding='utf-8')
    f.write("digraph dibujo{\n")
    f.write('graph [ordering="out"];')
    f.write('rankdir=TB;\n')
    f.write('node [shape = box];\n')
    data = ""
    for x in tupla:
        data += """<td>""" + str(x) + """</td>"""
    tabla = """<<table cellspacing='0' cellpadding='20' border='0' cellborder='1'>
                <tr>""" + data + """</tr>        
            </table> >"""
    f.write('table [label = ' + tabla + ',  fontsize="30", shape = plaintext ];\n')
    f.write('}')
    f.close()
    Storage.os.system(f'dot -Tpng Data/BPlusMode/{database}/{table}/tupla.dot -o ./Data/BPlusMode/{database}/{table}/tupla.png')
    info_window = Toplevel()

    info_window.title('Llave: ' + key)
    info_window.geometry('700x200+300+100')
    tupla_frame = Frame(info_window)
    tupla_frame.pack(fill=BOTH, expand=1)
    tupla_canvas = Canvas(info_window, width=700, height=300)
    tupla_canvas.place(x=0,y=0)
    scroll = Scrollbar(info_window, orient=HORIZONTAL, command=tupla_canvas.xview)
    scroll.pack(side=BOTTOM, fill=X)
    tupla_canvas.configure(xscrollcommand=scroll.set)
    tupla_canvas.bind('<Configure>', lambda e: tupla_canvas.configure(scrollregion=tupla_canvas.bbox('all')))
    photo_frame = Frame(tupla_canvas)
    tupla_canvas.create_window((0, 0), width=3000, height=300, window=photo_frame, anchor='nw')
    tupla_canvas.image = PhotoImage(file=f'./Data/BPlusMode/{database}/{table}/tupla.png')
    Label(photo_frame,image=tupla_canvas.image).place(x=0,y=0)

def close_table_window(window, parent):
    window.destroy()
    parent.deiconify()

#--------------Functions----------------------------

def upload_csv(entry):
    file = filedialog.askopenfilename(filetypes=[('CSV files','*.csv')])
    if file:
        entry.insert(END,file)

def create_database_window(parent):
    create_window = Toplevel()
    create_window.geometry('400x200+200+100')
    create_window.title('Create Database')
    tkinter.Label(create_window, text='Create Database', font='Helvetica 10 bold italic', width=20).place(x=5, y=70)
    database_name = Entry(create_window, width=25)
    database_name.place(x=140, y=70)
    tkinter.Button(create_window, text='Create', font='Helvetica 10 bold italic', width=10, command=lambda: create_database(database_name.get(), database_name, create_window,parent)).place(x=300, y=65)

def create_database(database,database_name, window, parent):
   if database:
        result = Storage.createDatabase(database)
        if result == 0:
            messagebox.showinfo(title='Create Database', message='Operacion exitosa')
            window.destroy()
            parent.destroy()
            show_data_bases()
        elif result == 1:
            messagebox.showinfo(title='Create Database', message='Error en la operacion')
            database_name.delete(0, END)
        elif result == 2:
            messagebox.showinfo(title='Create Database', message='Base de datos existente')
            database_name.delete(0, END)
   else:
        messagebox.showinfo(title='Create Database', message='No lleno el campo de texto')

def alter_database_window(parent, names):
    if names:
        window = Toplevel()
        window.geometry('500x200+200+100')
        window.title('Alter Database')
        variable = StringVar(window)
        variable.set(names[0])
        tkinter.Label(window, text='Alter Database', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
        box = OptionMenu(window, variable, *names)
        box.place(x=165, y=65)
        Label(window, text='New Name', font='Helvetica 10 bold italic', width=20).place(x=250, y= 50)
        new_data_base = Entry(window, width=20)
        new_data_base.place(x=275, y=70)
        tkinter.Button(window, text='Alter', font='Helvetica 10 bold italic', width=10,command=lambda:
        alter_database(variable.get(), new_data_base.get(),new_data_base, window, parent)).place(x=390, y=70)

def alter_database(old, new, entry1, window, parent):
    if old and new:
        result = Storage.alterDatabase(old, new)
        if result == 0:
            messagebox.showinfo(title='Alter Database', message='Operacion exitosa')
            window.destroy()
            parent.destroy()
            show_data_bases()
        elif result == 1:
            messagebox.showinfo(title='Alter Database', message='Error en la operacion')
            entry1.delete(0, END)
        elif result == 2:
            messagebox.showinfo(title='Alter Database', message=old + ' no existe')
            entry1.delete(0, END)
        elif result == 3:
            messagebox.showinfo(title='Alter Database', message=new + ' ya existe')
            entry1.delete(0, END)
    else:
        messagebox.showinfo(title='Alter Database', message='No lleno los campos de texto')
        entry1.delete(0, END)

def show_tables_window(parent, names):
    if names:
        window = Toplevel()
        window.geometry('500x200+200+100')
        window.title('Show Tables')
        variable = StringVar(window)
        variable.set(names[0])
        Label(window, text='Show Tables', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
        box = OptionMenu(window, variable, *names)
        box.place(x=165, y=65)
        Button(window, text='Show', font='Helvetica 10 bold italic', width=10, command=lambda:
        function_show_tables(variable.get(), window, parent)).place(x=290, y=70)

def drop_database_window(parent, names):
    if names:
        window = Toplevel()
        window.geometry('500x200+200+100')
        window.title('Drop Database')
        variable = StringVar(window)
        variable.set(names[0])
        tkinter.Label(window, text='Drop Database', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
        box = OptionMenu(window, variable, *names)
        box.place(x=165, y=65)
        tkinter.Button(window, text='Drop', font='Helvetica 10 bold italic', width=10, command=lambda:
        drop_database(variable.get(), window, parent)).place(x=285, y=65)

def drop_database(database, window, parent):
    if database:
        result = Storage.dropDatabase(database)
        if result == 2:
            messagebox.showinfo(title='Drop Database', message=database + ' no existe')
        elif result == 1:
            messagebox.showinfo(title='Drop Database', message="Error en la operacion")
        elif result == 0:
            messagebox.showinfo(title='Drop Database', message="Operacion exitosa")
            window.destroy()
            parent.destroy()
            show_data_bases()
    else:
        messagebox.showinfo(title='Drop Database', message='No lleno el campo de texto')

#------------------Tables------------------------

def create_table_window(grandParent,parent, database):
    window = Toplevel()
    window.geometry('500x200+200+100')
    window.title('Create Table')
    Label(window, text='Create Table', font='Helvetica 10 bold italic', width=20).place(x=50, y=70)
    Label(window, text='Name', font='Helvetica 10 bold italic', width=20).place(x=130, y=50)
    Label(window, text='Columns', font='Helvetica 10 bold italic', width=10).place(x=260, y=50)
    table = Entry(window, width=20)
    table.place(x=180, y=70)
    columns = Entry(window, width=10)
    columns.place(x=275, y=70)
    tkinter.Button(window, text='Create', font='Helvetica 10 bold italic', width=10, command=lambda:
    create_data_table(database, table.get(), columns.get(), columns,table, window, parent, grandParent)).place(x=345, y=65)

def create_data_table(database,table,columns, entry1, entry2, window, parent, grandParent):
    if database and table and columns:
        if isNumber(columns):
            result = Storage.createTable(database,table,int(columns))
            if result == 3:
                messagebox.showinfo(title='Create table', message=table + ' ya existe')
                entry1.delete(0, END)
                entry2.delete(0, END)
            elif result == 2:
                messagebox.showinfo(title='Create table', message=database + ' no existe')
                entry1.delete(0, END)
                entry2.delete(0, END)
            elif result == 1:
                messagebox.showinfo(title='Create table', message="Error en la operacion")
                entry1.delete(0, END)
                entry2.delete(0, END)
            elif result == 0:
                messagebox.showinfo(title='Create table', message="Operacion exitosa")
                window.destroy()
                refresh_tables(grandParent, parent, database)
        else:
            messagebox.showinfo(title='Create table', message="No escribio un numero de columnas")
            entry1.delete(0, END)
    else:
        messagebox.showinfo(title='Create table', message='No lleno el campo de texto')
        entry1.delete(0, END)
        entry2.delete(0, END)

def refresh_tables(parent, actual, database):
    actual.destroy()
    show_tables(parent,database)

def isNumber(entry):
    result = Storage.re.search(r'[0-9]+|[\s]',entry)
    return result

def function_show_tables(database,window, parent):
    if database:
        messagebox.showinfo(title='Show tables', message=f'{database}: {Storage.showTables(database)}')

def extract_table_window(database, names):
    if names:
        window = Toplevel()
        window.geometry('500x200+200+100')
        window.title('Extract Table')
        variable = StringVar(window)
        variable.set(names[0])
        Label(window, text='Show Tables', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
        box = OptionMenu(window, variable, *names)
        box.place(x=165, y=65)
        Button(window, text='Extract', font='Helvetica 10 bold italic', width=10, command=lambda:
        extract_table_function(database,variable.get())).place(x=270, y=65)

def extract_table_function(database, table):
    if database and table:
        result = Storage.extractTable(database, table)
        if result is not None:
            messagebox.showinfo(title='Extract table', message='Operacion exitosa: ' + str(result))
        else:
            messagebox.showinfo(title='Extract table', message='Base de datos o tabla no exsitentes: '+ str(result))
    else:
        messagebox.showinfo(title='Create Database', message='No se llenaron los campos de texto')

def extract_range_table_window(database, names):
    if names:
        window = Toplevel()
        window.geometry('600x200+200+100')
        window.title('Extract Range')
        variable = StringVar(window)
        variable.set(names[0])
        box = OptionMenu(window, variable, *names)
        box.place(x=140, y=60)
        Label(window, text='Extract Range', font='Helvetica 10 bold italic', width=15).place(x=10, y=70)
        Label(window, text='Column', font='Helvetica 10 bold italic', width=10).place(x=200, y=50)
        Label(window, text='Lower', font='Helvetica 10 bold italic', width=10).place(x=270, y=50)
        Label(window, text='Upper', font='Helvetica 10 bold italic', width=10).place(x=340, y=50)
        column = Entry(window, width=10)
        column.place(x=220, y=70)
        lower = Entry(window, width=10)
        lower.place(x=280, y=70)
        upper = Entry(window, width=10)
        upper.place(x=340, y=70)
        tkinter.Button(window, text='Create', font='Helvetica 10 bold italic', width=10, command=lambda:
        extract_range_table(database, variable.get(), column.get(), lower.get(), upper.get(),column, lower, upper)).place(x=410,y=65)

def extract_range_table(database, table, columnNumber, lower, upper, entry1, entry2, entry3):
    if database and table and columnNumber and lower and upper:
        if isNumber(columnNumber):
            result = Storage.extractRangeTable(database, table, int(columnNumber), lower, upper)
            if result is not None:
                messagebox.showinfo(title='Extract range table', message='Extract completado: ' + str(result))
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
            else:
                messagebox.showinfo(title='Extract range table', message='Datos no existentes: '+ str(result))
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
        else:
            messagebox.showinfo(title='Extract range table', message='No escribio un numero de columnas')
            entry1.delete(0, END)
    else:
        messagebox.showinfo(title='Extract range table', message='No se llenaron los campos de texto')

def alter_table_window(grandParent, parent, database, names):
    if names:
        window = Toplevel()
        window.geometry('500x200+200+100')
        window.title('Alter Table')
        variable = StringVar(window)
        variable.set(names[0])
        tkinter.Label(window, text='Alter Table', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
        box = OptionMenu(window, variable, *names)
        box.place(x=165, y=65)
        Label(window, text='New Name', font='Helvetica 10 bold italic', width=20).place(x=250, y=50)
        new_table = Entry(window, width=20)
        new_table.place(x=275, y=70)
        tkinter.Button(window, text='Alter', font='Helvetica 10 bold italic', width=10, command=lambda:
        alter_table(grandParent, parent, window, database, variable.get(), new_table.get(), new_table)).place(x=390, y=70)

def drop_table_window(grandParent, parent, database, names):
    if names:
        window = Toplevel()
        window.geometry('500x200+200+100')
        window.title('Drop Table')
        variable = StringVar(window)
        variable.set(names[0])
        tkinter.Label(window, text='Drop Table', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
        box = OptionMenu(window, variable, *names)
        box.place(x=165, y=65)
        tkinter.Button(window, text='Drop', font='Helvetica 10 bold italic', width=10, command=lambda:
        drop_table(grandParent, parent, window, database, variable.get())).place(x=285, y=65)

def drop_table(grandParent, parent, actual, database, table):
    if database and table:
        result = Storage.dropTable(database, table)
        if result == 0:
            messagebox.showinfo(title='Alter DropPK', message='Operacion exitosa')
            actual.destroy()
            refresh_tables(grandParent, parent, database)
        elif result == 1:
            messagebox.showinfo(title='Alter DropPK', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Alter DropPK', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Alter DropPK', message='Tabla no existente')
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')
#--------ROWS----------------

def alter_addPK_window(grandParent, parent, database, table):
    window = Toplevel()
    window.geometry('500x200+200+100')
    window.title('Add PK')
    tkinter.Label(window, text='Add Pk', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
    Label(window, text='PK', font='Helvetica 10 bold italic', width=20).place(x=140, y=50)
    columns = Entry(window, width=20)
    columns.place(x=165, y=70)
    tkinter.Button(window, text='Add', font='Helvetica 10 bold italic', width=10, command=lambda:
    alter_addPK(grandParent, parent, window, database, table, columns.get(), columns)).place(x=275, y=65)

def alter_addPK(grandParent, parent, actual,database, table, columns, entry1):
    if database and table and columns:
        pk = []
        separate = columns.split(',')
        for x in separate:
            if not isNumber(x):
                messagebox.showinfo(title='Alter AddPK', message='No ingreso algun numero de columna')
                entry1.delete(0, END)
                return
            pk.append(int(x))
        result = Storage.alterAddPK(database, table, pk)
        if result == 0:
            messagebox.showinfo(title='Alter AddPK', message='Operacion exitosa')
            actual.destroy()
            refresh_rows(grandParent,parent,database,table)
        elif result == 1:
            messagebox.showinfo(title='Alter AddPK', message='Error en la operacion')
            entry1.delete(0, END)
        elif result == 2:
            messagebox.showinfo(title='Alter AddPK', message='Base de datos no existente')
            entry1.delete(0, END)
        elif result == 3:
            messagebox.showinfo(title='Alter AddPK', message='Tabla no existente')
            entry1.delete(0, END)
        elif result == 4:
            messagebox.showinfo(title='Alter AddPK', message='Llave primaria existente')
            entry1.delete(0, END)
        elif result == 5:
            messagebox.showinfo(title='Alter AddPK', message='Columnas fuera de limites')
            entry1.delete(0, END)
    else:
        messagebox.showinfo(title='Alter AddPK', message='No se llenaron los campos de texto')

def refresh_rows(parent, actual, database, table):
    actual.destroy()
    extract_table(database, table, parent)

def alter_dropPK(grandParent, parent,database, table):
    if database and table:
        result = Storage.alterDropPK(database, table)
        if result == 0:
            messagebox.showinfo(title='Alter DropPK', message='Operacion exitosa')
            refresh_rows(grandParent, parent, database, table)
        elif result == 1:
            messagebox.showinfo(title='Alter DropPK', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Alter DropPK', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Alter DropPK', message='Tabla no existente')
        elif result == 4:
            messagebox.showinfo(title='Alter DropPK', message='Llave primaria no existente')
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')

def alter_table(grandParent, parent, actual, database, tableOld, tableNew, entry1):
    if database and tableOld and tableNew:
        result = Storage.alterTable(database, tableOld, tableNew)
        if result == 0:
            messagebox.showinfo(title='Alter DropPK', message='Operacion exitosa')
            actual.destroy()
            refresh_tables(grandParent, parent, database)
        elif result == 1:
            messagebox.showinfo(title='Alter DropPK', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Alter DropPK', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Alter DropPK', message=tableOld+ ' no existente')
        elif result == 4:
            messagebox.showinfo(title='Alter DropPK', message=tableNew+' nueva ya existe')
            entry1.delete(0, END)
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')

def alter_addColumn_window(grandParent, parent, database, table):
    window = Toplevel()
    window.geometry('500x200+200+100')
    window.title('Add Column')
    tkinter.Label(window, text='Add Column', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
    Label(window, text='Default', font='Helvetica 10 bold italic', width=20).place(x=140, y=50)
    default = Entry(window, width=20)
    default.place(x=165, y=70)
    tkinter.Button(window, text='Add', font='Helvetica 10 bold italic', width=10, command=lambda:
    alter_addColumn(grandParent, parent, window, database, table, default.get(), default)).place(x=275, y=65)

def alter_addColumn(grandParent, parent, window, database, table, default, entry1):
    if database and table and default:
        result = Storage.alterAddColumn(database, table, default)
        if result == 0:
            messagebox.showinfo(title='Add Column', message='Operacion exitosa')
            window.destroy()
            refresh_rows(grandParent, parent, database, table)
        elif result == 1:
            messagebox.showinfo(title='Add Column', message='Error en la operacion')
            entry1.delete(0, END)
        elif result == 2:
            messagebox.showinfo(title='Add Column', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Add Column', message=table + ' no existente')
    else:
        messagebox.showinfo(title='Add Column', message='No se llenaron los campos de texto')

def alter_dropColumn_window(grandParent, parent, database, table):
    window = Toplevel()
    window.geometry('500x200+200+100')
    window.title('Drop Column')
    tkinter.Label(window, text='Drop Column', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
    Label(window, text='Column', font='Helvetica 10 bold italic', width=20).place(x=140, y=50)
    columns = Entry(window, width=20)
    columns.place(x=165, y=70)
    tkinter.Button(window, text='Drop', font='Helvetica 10 bold italic', width=10, command=lambda:
    alter_dropColumn(grandParent, parent, window, database, table, columns.get(), columns)).place(x=275, y=65)

def alter_dropColumn(grandParent, parent, window, database, table, columnNumber, entry1):
    if database and table and columnNumber:
        if isNumber(columnNumber):
            result = Storage.alterDropColumn(database, table, int(columnNumber))
            if result == 0:
                messagebox.showinfo(title='Alter Drop Column', message='Operacion exitosa')
                window.destroy()
                refresh_rows(grandParent, parent, database, table)
            elif result == 1:
                messagebox.showinfo(title='Alter Drop Column', message='Error en la operacion')
                entry1.delete(0, END)
            elif result == 2:
                messagebox.showinfo(title='Alter Drop Column', message='Base de datos no existente')
            elif result == 3:
                messagebox.showinfo(title='Alter Drop Column', message=table + ' no existente')
            elif result == 4:
                messagebox.showinfo(title='Alter Drop Column', message='Llave no puede eliminarse o la tabla se queda sin columnas')
            elif result == 5:
                messagebox.showinfo(title='Alter Drop Column', message='Columna fuera de limites')
                entry1.delete(0, END)
        else:
            messagebox.showinfo(title='Alter Drop Column', message='No ingreso un numero de columnas')
            entry1.delete(0, END)
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')

def insert_row_window(grandParent, parent, database, table):
    window = Toplevel()
    window.geometry('500x200+200+100')
    window.title('Insert')
    tkinter.Label(window, text='Insert', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
    Label(window, text='List', font='Helvetica 10 bold italic', width=20).place(x=140, y=50)
    register = Entry(window, width=20)
    register.place(x=165, y=70)
    tkinter.Button(window, text='Insert', font='Helvetica 10 bold italic', width=10, command=lambda:
    insert_row(grandParent, parent, window, database, table, register.get(), register)).place(x=275, y=65)

def insert_row(grandParent, parent, window, database, table, register, entry1):
    if database and table and register:
        data = register.split(',')
        result = Storage.insert(database, table, data)
        if result == 0:
            messagebox.showinfo(title='Insert', message='Operacion exitosa')
            window.destroy()
            refresh_rows(grandParent, parent, database, table)
        elif result == 1:
            messagebox.showinfo(title='Insert', message='Error en la operacion')
            entry1.delete(0, END)
        elif result == 2:
            messagebox.showinfo(title='Insert', message='Base de datos no existente')
            entry1.delete(0, END)
        elif result == 3:
            messagebox.showinfo(title='Insert', message='Tabla no existente')
            entry1.delete(0, END)
        elif result == 4:
            messagebox.showinfo(title='Insert', message='Llave primaria duplicada')
            entry1.delete(0, END)
        elif result == 5:
            messagebox.showinfo(title='Insert', message='Columna fuera de limites')
            entry1.delete(0, END)
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')

def load_csv_window(grandParent, parent, database, table):
    window = Toplevel()
    window.geometry('400x200+200+100')
    window.title('Load')
    tkinter.Label(window, text='Load CSV', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
    Label(window, text='File  path', font='Helvetica 10 bold italic', width=20).place(x=140, y=50)
    file = Entry(window, width=20)
    file.place(x=165, y=70)
    tkinter.Button(window, text='Insert', font='Helvetica 10 bold italic', width=10, command=lambda:
    load_csv(grandParent, parent, window, database, table, file.get(), file)).place(x=200, y=120)
    tkinter.Button(window, text='Upload', font='Helvetica 10 bold italic', width=10, command=lambda:
    upload_csv(file)).place(x=120, y=120)

def load_csv(grandParent, parent, window , database, table, filepath, entry1):
    if filepath and database and table:
        try:
            result = Storage.loadCSV(filepath,database, table)
            messagebox.showinfo(title='Load CSV', message=result)
            window.destroy()
            refresh_rows(grandParent, parent, database, table)
        except:
            messagebox.showinfo(title='Load CSV', message='Ocurrio un error')
            entry1.delete(0, END)
    else:
        messagebox.showinfo(title='Load CSV', message='No se llenaron los campos de texto')
        entry1.delete(0, END)

def extract_row_window(database, table):
    window = Toplevel()
    window.geometry('500x200+200+100')
    window.title('Extract Row')
    tkinter.Label(window, text='Extract Row', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
    Label(window, text='List', font='Helvetica 10 bold italic', width=20).place(x=140, y=50)
    columns = Entry(window, width=20)
    columns.place(x=165, y=70)
    tkinter.Button(window, text='Extract', font='Helvetica 10 bold italic', width=10, command=lambda:
    extract_row(database, table, columns.get(), columns)).place(x=275, y=65)

def extract_row(database, table, columns, entry1):
    if database and table and columns:
        separate = columns.split(',')
        result = Storage.extractRow(database, table, separate)
        messagebox.showinfo(title='Extract Row', message='Resultado: '+str(result))
    else:
        messagebox.showinfo(title='Extract Row', message='No se llenaron los campos de texto')
        entry1.delete(0, END)

def update_window(grandParent, parent, database, table):
    window = Toplevel()
    window.geometry('500x200+200+100')
    window.title('Update')
    Label(window, text='Update', font='Helvetica 10 bold italic', width=20).place(x=50, y=70)
    Label(window, text='Dictionary', font='Helvetica 10 bold italic', width=20).place(x=130, y=50)
    Label(window, text='Columns', font='Helvetica 10 bold italic', width=10).place(x=290, y=50)
    register = Entry(window, width=20)
    register.place(x=180, y=70)
    columns = Entry(window, width=10)
    columns.place(x=300, y=70)
    tkinter.Button(window, text='Update', font='Helvetica 10 bold italic', width=10, command=lambda:
    update(grandParent, parent, window, database, table, register.get(),columns.get(),register, columns)).place(x=370,y=65)

def update(grandParent, parent, window, database, table, register, columns, entry1, entry2):
    if database and table and register and columns:
        dictionary = {}
        separate_register = register.split(',')
        separate = columns.split(',')
        for x in separate_register:
            data = x.split(':')
            if not isNumber(data[0]):
                messagebox.showinfo(title='Extract Row', message='No ingreso correctamente las claves')
                entry1.delete(0, END)
                return
            key = int(data[0])
            dictionary[key] = data[1]
        result = Storage.update(database, table, dictionary, separate)
        if result == 0:
            messagebox.showinfo(title='Update', message='Operacion exitosa')
            window.destroy()
            refresh_rows(grandParent, parent, database, table)
        elif result == 1:
            messagebox.showinfo(title='Update', message='Error en la operacion')
            entry1.delete(0, END)
            entry2.delete(0, END)
        elif result == 2:
            messagebox.showinfo(title='Update', message='Base de datos no existente')
            entry1.delete(0, END)
            entry2.delete(0, END)
        elif result == 3:
            messagebox.showinfo(title='Update', message='Tabla no existente')
            entry1.delete(0, END)
            entry2.delete(0, END)
        elif result == 4:
            messagebox.showinfo(title='Update', message='Llave primaria no existe')
            entry1.delete(0, END)
            entry2.delete(0, END)
    else:
        messagebox.showinfo(title='Extract Row', message='No se llenaron los campos de texto')
        entry1.delete(0, END)
        entry2.delete(0, END)

def delete_window(grandParent, parent, database, table):
    window = Toplevel()
    window.geometry('500x200+200+100')
    window.title('Delete')
    tkinter.Label(window, text='Delete', font='Helvetica 10 bold italic', width=20).place(x=25, y=70)
    Label(window, text='List', font='Helvetica 10 bold italic', width=20).place(x=140, y=50)
    columns = Entry(window, width=20)
    columns.place(x=165, y=70)
    tkinter.Button(window, text='Delete', font='Helvetica 10 bold italic', width=10, command=lambda:
    delete(grandParent, parent, window,database, table, columns.get(), columns)).place(x=275, y=65)

def delete(grandParent, parent, window, database, table, columns, entry1):
    if database and table and columns:
        separate = columns.split(',')
        result = Storage.delete(database, table, separate)
        if result == 0:
            messagebox.showinfo(title='Update', message='Operacion exitosa')
            window.destroy()
            refresh_rows(grandParent, parent, database, table)
        elif result == 1:
            messagebox.showinfo(title='Update', message='Error en la operacion')
            entry1.delete(0, END)
        elif result == 2:
            messagebox.showinfo(title='Update', message='Base de datos no existente')
            entry1.delete(0, END)
        elif result == 3:
            messagebox.showinfo(title='Update', message='Tabla no existente')
            entry1.delete(0, END)
        elif result == 4:
            messagebox.showinfo(title='Update', message='Llave primaria no existe')
            entry1.delete(0, END)
    else:
        messagebox.showinfo(title='Update', message='No lleno todos los campos')
        entry1.delete(0, END)

def truncate_table(grandParent, parent ,database, table):
    pregunta = messagebox.askyesno(message='Esta seguro?')
    if pregunta:
        if database and table:
            result = Storage.truncate(database, table)
            if result == 0:
                messagebox.showinfo(title='Update', message='Operacion exitosa')
                refresh_rows(grandParent, parent, database, table)
            elif result == 1:
                messagebox.showinfo(title='Update', message='Error en la operacion')
            elif result == 2:
                messagebox.showinfo(title='Update', message='Base de datos no existente')
            elif result == 3:
                messagebox.showinfo(title='Update', message='Tabla no existente')
        else:
            messagebox.showinfo(title='Update', message='No lleno todos los campos')

main_window = tkinter.Tk()
main_window.geometry('610x310+300+100')
main_window.title('Tytus EDD: Fase 1')
main_window.configure(background='black')
main_canvas = Canvas(main_window, width=580, height=280).place(x=15, y=10)
tkinter.Label(main_canvas, text='Tytus Database', font='Helvetica 30 bold italic',padx=10, pady=5).place(x=150, y=20)
tkinter.Button(main_canvas, text='Reportes', font='Helvetica 16 bold italic', width=20, height=2, borderwidth= 5, fg='white', background='black',command=show_data_bases).place(x=175, y=150)
    
def start():
    main_window.mainloop()