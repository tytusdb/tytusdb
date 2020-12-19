import Storage
import BplusTree
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import os

def show_data_bases():
    data_bases = Storage.showDatabases()
    database_tree = Storage.serializable.Read('./Data/', 'Databases')
    database_tree.graph("Databases")
    tree_window = Toplevel(main_window)
    main_window.iconify()
    tree_window.geometry('950x580+200+75')
    tree_window.title('Bases de datos')
    main_tree = Frame(tree_window)
    main_tree.pack(fill=BOTH, expand=1)
    main_tree.configure(background='black')
    canvas_tree = Canvas(tree_window, width=750, height=530)
    canvas_tree.place(x=170, y=15)
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
    canvas_tree.image = PhotoImage(file='./Data/DataBases.png')
    #Label(frame_tree, width=2000, height=200).place(x=0, y=0)
    Label(frame_tree, image=canvas_tree.image).place(x=50, y=50)


    canvas_buttons = Canvas(tree_window, background='red',width=130, height=530)
    canvas_buttons.place(x=25, y=15)
    scroll_buttons = Scrollbar(main_tree, orient=VERTICAL, command=canvas_buttons.yview)
    scroll_buttons.pack(side=LEFT, fill=Y)
    canvas_buttons.configure(yscrollcommand=scroll_buttons.set)
    canvas_buttons.bind('<Configure>', lambda e: canvas_buttons.configure(scrollregion=canvas_buttons.bbox('all')))
    buttons_frame = Frame(canvas_buttons)
    canvas_buttons.create_window((15,0), width=130, height=5000, window=buttons_frame, anchor='nw')
    Button(buttons_frame, text='Regresar', font='Helvetica 8 bold italic', command=lambda : close_table_window(tree_window,main_window), bg='red', padx=15, pady=3).place(x=0, y=0)
    yview = 30
    for x in data_bases:
        Button(buttons_frame, text=x, font='Helvetica 8 bold italic', fg='white', bg='black',command= lambda database = x : show_tables(tree_window, database) ,padx=15, pady=5).place(x=0, y=yview)
        yview += 35


def show_tables(parent_window, database):
    tables = Storage.showTables(database)
    db = Storage.serializable.Read(f"./Data/{database}/", database)
    db.graph(database)
    parent_window.iconify()
    table_window = Toplevel(parent_window)
    parent_window.iconify()
    table_window.geometry('950x580+200+75')
    table_window.title(database)
    main_tree = Frame(table_window)
    main_tree.pack(fill=BOTH, expand=1)
    main_tree.configure(background='black')
    canvas_tree = Canvas(table_window, width=750, height=530)
    canvas_tree.place(x=170, y=15)
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
    canvas_tree.image = PhotoImage(file=f'./Data/{database}/{database}.png')
    Label(frame_tree, image=canvas_tree.image).place(x=150, y=50)
    canvas_buttons = Canvas(table_window, width=120, height=530)
    canvas_buttons.place(x=25, y=15)
    scroll_buttons = Scrollbar(main_tree, orient=VERTICAL, command=canvas_buttons.yview)
    scroll_buttons.pack(side=LEFT, fill=Y)
    canvas_buttons.configure(yscrollcommand=scroll_buttons.set)
    canvas_buttons.bind('<Configure>', lambda e: canvas_buttons.configure(scrollregion=canvas_buttons.bbox('all')))
    buttons_frame = Frame(canvas_buttons)
    canvas_buttons.create_window((15, 0), width=120, height=6000, window=buttons_frame, anchor='nw')
    Button(buttons_frame, text='Regresar', font='Helvetica 8 bold italic', command=lambda: close_table_window(table_window, parent_window), bg='red', padx=15, pady=3).place(x=0, y=0)
    yview = 30
    for x in tables:
        Button(buttons_frame, text=x, font='Helvetica 8 bold italic', fg='white', bg='black', command=lambda table=x: extract_table(database, table, table_window),padx=15, pady=5).place(x=0, y=yview)
        yview += 35

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
    canvas_tree = Canvas(table_window, width=750, height=530)
    canvas_tree.place(x=170, y=15)
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
    canvas_tree.image = PhotoImage(file=f'./Data/{database}/{table}/{table}.png')
    #Label(frame_tree, width=2000, height=200).place(x=0, y=0)
    Label(frame_tree, image=canvas_tree.image).place(x=50, y=50)

    canvas_buttons = Canvas(table_window, width=120, height=530)
    canvas_buttons.place(x=25, y=15)
    scroll_buttons = Scrollbar(main_tree, orient=VERTICAL, command=canvas_buttons.yview)
    scroll_buttons.pack(side=LEFT, fill=Y)
    canvas_buttons.configure(yscrollcommand=scroll_buttons.set)
    canvas_buttons.bind('<Configure>', lambda e: canvas_buttons.configure(scrollregion=canvas_buttons.bbox('all')))
    buttons_frame = Frame(canvas_buttons)
    canvas_buttons.create_window((15, 0), width=120, height=5000, window=buttons_frame, anchor='nw')
    Button(buttons_frame, text='Regresar', font='Helvetica 8 bold italic',command=lambda: close_table_window(table_window, parent_window), bg='red', padx=15, pady=3).place(x=0, y=0)
    yview = 30
    print(rows)
    for x in range(0,len(list(keys))):
        Button(buttons_frame, text=keys[x], font='Helvetica 8 bold italic',  fg='white', bg='black',command=lambda info=rows[x], key=keys[x]: table_graph(info, key, table, database), padx=15, pady=5).place(x=0, y=yview)
        yview += 35

def get_keys(database, table):
    Storage.checkData()
    # Get the databases tree
    dataBaseTree = Storage.serializable.Read('./Data/', "Databases")
    # Get the dbNode
    databaseNode = dataBaseTree.search(dataBaseTree.getRoot(), database)
    # If DB exist
    if databaseNode:
        tablesTree = Storage.serializable.Read(f"./Data/{database}/", database)
        if tablesTree.search(tablesTree.getRoot(), table):
            table_aux = Storage.serializable.Read(f'./Data/{database}/{table}/', table)
            table_aux.graficar(database, table)
            return list(table_aux.lista())
        else:
            return None
    else:
        return None

def table_graph(tupla, key, table, database):
    f = open(f'Data/{database}/{table}/tupla.dot', 'w', encoding='utf-8')
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
    Storage.os.system(f'dot -Tpng Data/{database}/{table}/tupla.dot -o ./Data/{database}/{table}/tupla.png')
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
    tupla_canvas.image = PhotoImage(file=f'./Data/{database}/{table}/tupla.png')
    Label(photo_frame,image=tupla_canvas.image).place(x=0,y=0)

def close_table_window(window, parent):
    window.destroy()
    parent.deiconify()

#--------------Functions----------------------------
def show_functions():
        main_window.iconify()
        function_window = Toplevel(main_window)
        function_window.title('Funciones de las bases de datos')
        function_window.geometry('675x620+300+50')

        main_frame = Frame(function_window)
        main_frame.pack(fill=BOTH, expand=1)

        main_canvas = Canvas(function_window, width=655, height=600)
        main_canvas.place(x=0, y=0)

        scroll = Scrollbar(main_frame, orient=VERTICAL, command=main_canvas.yview)
        scroll.pack(side=RIGHT, fill=Y)
        main_canvas.configure(yscrollcommand=scroll.set)
        main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox('all')))

        funtion_frame = Frame(main_canvas)
        Button(function_window, text='Regresar', padx=20, pady=5, font='Helvetica 8 bold italic', fg='black',bg='red', command=lambda: close_table_window(function_window, main_window)).place(x=10, y=5)

        funtion_frame.configure(bg='black')
        main_canvas.create_window((10, 10), width=655, height=2000, window=funtion_frame, anchor='nw')

        database_canvas = Canvas(funtion_frame, width=630, height=300)
        database_canvas.configure(bg='white')
        database_canvas.place(x=10, y=40)

        tkinter.Label(database_canvas, text='Database Functions',font='Helvetica 16 bold italic').place(x=225, y=10)
        tkinter.Label(database_canvas,text='Create Database',font='Helvetica 10 bold italic', width=20).place(x=110, y=70)
        database_name = Entry(database_canvas, width=20)
        database_name.place(x=250,y=70)
        tkinter.Button(database_canvas, text='Create',font='Helvetica 10 bold italic', width=10, command= lambda : create_database(database_name.get(),database_name)).place(x=320, y=65)

        tkinter.Label(database_canvas, text='Alter Database', font='Helvetica 10 bold italic', width=20).place(x=100, y=120)
        old_data_base = Entry(database_canvas, width=20)
        old_data_base.place(x=250, y=120)
        new_data_base = Entry(database_canvas, width=20)
        new_data_base.place(x=320, y=120)
        tkinter.Button(database_canvas, text='Alter', font='Helvetica 10 bold italic', width=10, command=lambda: alter_database(old_data_base.get(), new_data_base.get(),old_data_base,new_data_base)).place(x=390, y=115)

        tkinter.Label(database_canvas, text='Show Databases', font='Helvetica 10 bold italic', width=20).place(x=100,y=170)
        tkinter.Button(database_canvas, text='Show', font='Helvetica 10 bold italic', width=10, command=function_show_databases).place(x=250, y=165)

        tkinter.Label(database_canvas, text='Drop Database', font='Helvetica 10 bold italic', width=20).place(x=100,y=220)
        drop_data_base = Entry(database_canvas, width=20)
        drop_data_base.place(x=250, y=220)
        tkinter.Button(database_canvas, text='Drop', font='Helvetica 10 bold italic', width=10, command=lambda: drop_database(drop_data_base.get(), drop_data_base)).place(x=390, y=215)

        tables_canvas = Canvas(funtion_frame, width=630, height=700)
        tables_canvas.configure(bg='white')
        tables_canvas.place(x=10, y=360)

        tkinter.Label(tables_canvas, text='Table Functions', font='Helvetica 16 bold italic').place(x=225 ,y=10)
        tkinter.Label(tables_canvas, text='Create Table', font='Helvetica 10 bold italic', width=20).place(x=10, y=70)
        data_base = Entry(tables_canvas, width=12)
        data_base.place(x=150, y=70)
        table_name = Entry(tables_canvas, width=12)
        table_name.place(x=225, y=70)
        columns = Entry(tables_canvas, width=12)
        columns.place(x=300, y=70)
        tkinter.Button(tables_canvas, text='Create', font='Helvetica 10 bold italic', width=10,command=lambda: create_data_table(data_base.get(), table_name.get(), columns.get(), data_base, table_name, columns)).place(x=360, y=65)

        tkinter.Label(tables_canvas, text='Show tables', font='Helvetica 10 bold italic', width=20).place(x=10,y=120)
        show_table = Entry(tables_canvas, width=20)
        show_table.place(x=150, y=120)
        tkinter.Button(tables_canvas, text='Show', font='Helvetica 10 bold italic', width=10,command=lambda: function_show_tables(show_table.get(), show_table)).place(x=250, y=115)

        tkinter.Label(tables_canvas, text='Extract Table', font='Helvetica 10 bold italic', width=20).place(x=10, y=170)
        data_base_name = Entry(tables_canvas, width=20)
        data_base_name.place(x=150, y=170)
        table_name_extract = Entry(tables_canvas, width=20)
        table_name_extract.place(x=225, y=170)
        tkinter.Button(tables_canvas, text='Extract', font='Helvetica 10 bold italic', width=10, command=lambda: extract_table_function(data_base_name.get(), table_name_extract.get(),data_base_name,table_name_extract)).place(x=300, y=165)

        tkinter.Label(tables_canvas, text='Extract Range Table', font='Helvetica 10 bold italic', width=20).place(x=10, y=220)
        database_range_name = Entry(tables_canvas, width=15)
        database_range_name.place(x=170, y=220)
        table_range_name = Entry(tables_canvas, width=15)
        table_range_name.place(x=245, y=220)
        column_range = Entry(tables_canvas, width=15)
        column_range.place(x=320, y=220)
        lower_range = Entry(tables_canvas, width=15)
        lower_range.place(x=395, y=220)
        upper_range = Entry(tables_canvas, width=15)
        upper_range.place(x=470, y=220)
        tkinter.Button(tables_canvas, text='Extract', font='Helvetica 10 bold italic', width=10, command=lambda: extract_range_table(database_range_name.get(), table_range_name.get(),
                    column_range.get(), lower_range.get(), upper_range.get(), database_range_name, table_range_name, column_range, lower_range, upper_range)).place(x=535, y=215)

        tkinter.Label(tables_canvas, text='Alter AddPK', font='Helvetica 10 bold italic', width=20).place(x=10, y=270)
        data_base_pk = Entry(tables_canvas, width=20)
        data_base_pk.place(x=150, y=270)
        table_name_pk = Entry(tables_canvas, width=20)
        table_name_pk.place(x=225, y=270)
        column_pk = Entry(tables_canvas, width=20)
        column_pk.place(x=300, y=270)
        tkinter.Button(tables_canvas, text='Alter', font='Helvetica 10 bold italic', width=10, command=lambda:
        alter_addPK(data_base_pk.get(), table_name_pk.get(), column_pk.get(), data_base_pk, table_name_pk, column_pk)).place(x=375, y=265)

        tkinter.Label(tables_canvas, text='Alter DropPK', font='Helvetica 10 bold italic', width=20).place(x=10, y=320)
        database_drop_pk = Entry(tables_canvas, width=20)
        database_drop_pk.place(x=150, y=320)
        table_drop_pk = Entry(tables_canvas, width=20)
        table_drop_pk.place(x=225, y=320)
        tkinter.Button(tables_canvas, text='Alter', font='Helvetica 10 bold italic', width=10,command=lambda:
        alter_dropPK(database_drop_pk.get(), table_drop_pk.get(), database_drop_pk, table_drop_pk)).place(x=300, y=315)

        tkinter.Label(tables_canvas, text='Alter AddFK', font='Helvetica 10 bold italic', width=20).place(x=10, y=370)
        database_fk = Entry(tables_canvas, width=20)
        database_fk.place(x=150, y=370)
        table_fk = Entry(tables_canvas, width=20)
        table_fk.place(x=225, y=370)
        references = Entry(tables_canvas, width=20)
        references.place(x=300, y=370)
        tkinter.Button(tables_canvas, text='Alter', font='Helvetica 10 bold italic', width=10).place(x=390, y=365)

        tkinter.Label(tables_canvas, text='Alter AddIndex', font='Helvetica 10 bold italic', width=20).place(x=10, y=420)
        database_index = Entry(tables_canvas, width=20)
        database_index.place(x=150, y=420)
        table_index = Entry(tables_canvas, width=20)
        table_index.place(x=225, y=420)
        references_index = Entry(tables_canvas, width=20)
        references_index.place(x=300, y=420)
        tkinter.Button(tables_canvas, text='Alter', font='Helvetica 10 bold italic', width=10).place(x=390, y=415)

        tkinter.Label(tables_canvas, text='Alter Table', font='Helvetica 10 bold italic', width=20).place(x=10, y=470)
        database_alter = Entry(tables_canvas, width=20)
        database_alter.place(x=150, y=470)
        table_old = Entry(tables_canvas, width=20)
        table_old.place(x=225, y=470)
        table_new = Entry(tables_canvas, width=20)
        table_new.place(x=300, y=470)
        tkinter.Button(tables_canvas, text='Alter', font='Helvetica 10 bold italic', width=10, command=lambda:
        alter_table(database_alter.get(), table_old.get(), table_new.get(), database_alter, table_old, table_new)).place(x=375, y=465)

        tkinter.Label(tables_canvas, text='Alter AddColumn', font='Helvetica 10 bold italic', width=20).place(x=10, y=520)
        database_add_column = Entry(tables_canvas, width=20)
        database_add_column.place(x=150, y=520)
        table_add_column = Entry(tables_canvas, width=20)
        table_add_column.place(x=225, y=520)
        default = Entry(tables_canvas, width=20)
        default.place(x=300, y=520)
        tkinter.Button(tables_canvas, text='Alter', font='Helvetica 10 bold italic', width=10, command=lambda:
        alter_addColumn(database_add_column.get(), table_add_column.get(), default.get(),database_add_column, table_add_column, default)).place(x=375, y=515)

        tkinter.Label(tables_canvas, text='Alter DropColumn', font='Helvetica 10 bold italic', width=20).place(x=10, y=570)
        database_drop_column = Entry(tables_canvas, width=20)
        database_drop_column.place(x=150, y=570)
        table_drop_column = Entry(tables_canvas, width=20)
        table_drop_column.place(x=225, y=570)
        column_number = Entry(tables_canvas, width=20)
        column_number.place(x=300, y=570)
        tkinter.Button(tables_canvas, text='Alter', font='Helvetica 10 bold italic', width=10,command=lambda:
        alter_dropColumn(database_drop_column.get(), table_drop_column.get(), column_number.get(), database_drop_column, table_drop_column, column_number)).place(x=375, y=565)
        # -------------------------------
        tkinter.Label(tables_canvas, text='Drop Table', font='Helvetica 10 bold italic', width=20).place(x=10,y=620)
        database_drop_table = Entry(tables_canvas, width=20)
        database_drop_table.place(x=150, y=620)
        table_drop = Entry(tables_canvas, width=20)
        table_drop.place(x=225, y=620)
        tkinter.Button(tables_canvas, text='Alter', font='Helvetica 10 bold italic', width=10,command=lambda:
        drop_table(database_drop_table.get(), table_drop.get(), database_drop_table,table_drop)).place(x=300, y=615)
        # -------------------------------
        row_canvas = Canvas(funtion_frame, width=630, height=700)
        row_canvas.configure(bg='white')
        row_canvas.place(x=10, y=1080)

        tkinter.Label(row_canvas, text='Row Functions', font='Helvetica 16 bold italic').place(x=225, y=10)
        tkinter.Label(row_canvas, text='Insert', font='Helvetica 10 bold italic', width=20).place(x=10, y=70)
        database_insert = Entry(row_canvas, width=12)
        database_insert.place(x=150, y=70)
        table_insert = Entry(row_canvas, width=12)
        table_insert.place(x=225, y=70)
        register = Entry(row_canvas, width=15)
        register.place(x=300, y=70)
        tkinter.Button(row_canvas, text='Insert', font='Helvetica 10 bold italic', width=10,command=lambda:
        insert_row(database_insert.get(), table_insert.get(), register.get(), database_insert, table_insert, register)).place(x=395, y=65)

        tkinter.Label(row_canvas, text='LoadCSV', font='Helvetica 10 bold italic', width=20).place(x=10, y=120)
        file_load = Entry(row_canvas, width=12)
        file_load.place(x=150, y=120)
        database_load = Entry(row_canvas, width=12)
        database_load.place(x=225, y=120)
        table_load = Entry(row_canvas, width=15)
        table_load.place(x=300, y=120)
        tkinter.Button(row_canvas, text='Upload', font='Helvetica 10 bold italic', width=10, command=lambda: upload_csv(file_load)).place(x=150, y=145)
        tkinter.Button(row_canvas, text='Load', font='Helvetica 10 bold italic', width=10,command=lambda:
        load_csv(file_load.get(),database_load.get(), table_load.get(),file_load,database_load, table_load)).place(x=395, y=115)

        tkinter.Label(row_canvas, text='Extract Row', font='Helvetica 10 bold italic', width=20).place(x=10, y=180)
        database_row = Entry(row_canvas, width=12)
        database_row.place(x=150, y=180)
        table_row = Entry(row_canvas, width=12)
        table_row.place(x=225, y=180)
        row_columns = Entry(row_canvas, width=15)
        row_columns.place(x=300, y=180)
        tkinter.Button(row_canvas, text='Extract', font='Helvetica 10 bold italic', width=10, command=lambda:
        extract_row(database_row.get(), table_row.get(), row_columns.get(),database_row, table_row, row_columns)).place(x=395, y=175)

        tkinter.Label(row_canvas, text='Update', font='Helvetica 10 bold italic', width=20).place(x=10, y=240)
        database_update = Entry(row_canvas, width=12)
        database_update.place(x=150, y=240)
        table_update = Entry(row_canvas, width=12)
        table_update.place(x=225, y=240)
        register_dic = Entry(row_canvas, width=15)
        register_dic.place(x=300, y=240)
        column_update = Entry(row_canvas, width=15)
        column_update.place(x=395, y=240)
        tkinter.Button(row_canvas, text='Update', font='Helvetica 10 bold italic', width=10, command=lambda:
        update(database_update.get(), table_update.get(), register_dic.get(), column_update.get(), database_update, table_update, register_dic, column_update)).place(x=495, y=235)
        # ----------------- -----------
        tkinter.Label(row_canvas, text='Delete', font='Helvetica 10 bold italic', width=20).place(x=10, y=300)
        database_delete = Entry(row_canvas, width=12)
        database_delete.place(x=150, y=300)
        table_delete = Entry(row_canvas, width=12)
        table_delete.place(x=225, y=300)
        column_delete = Entry(row_canvas, width=15)
        column_delete.place(x=300, y=300)
        tkinter.Button(row_canvas, text='Delete', font='Helvetica 10 bold italic', width=10, command=lambda:
        delete(database_delete.get(), table_delete.get(), column_delete.get(),database_delete, table_delete, column_delete)).place(x=400, y=295)

        tkinter.Label(row_canvas, text='Truncate', font='Helvetica 10 bold italic', width=20).place(x=10, y=360)
        database_truncate = Entry(row_canvas, width=12)
        database_truncate.place(x=150, y=360)
        table_truncate = Entry(row_canvas, width=12)
        table_truncate.place(x=225, y=360)
        tkinter.Button(row_canvas, text='Truncate', font='Helvetica 10 bold italic', width=10, command=lambda:
        truncate_table(database_truncate.get(), table_truncate.get(),database_truncate, table_truncate)).place(x=320, y=355)

def upload_csv(entry):
    file = filedialog.askopenfilename(filetypes=[('CSV files','*.csv')])
    if file:
        entry.insert(END,file)

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
        messagebox.showinfo(title='Create Database', message='No lleno el campo de texto')

def alter_database(old,new, entry1, entry2):
    if old and new:
        result = Storage.alterDatabase(old, new)
        if result == 0:
            messagebox.showinfo(title='Alter Database', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Alter Database', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Alter Database', message=old + ' no existe')
        elif result == 3:
            messagebox.showinfo(title='Alter Database', message=new + ' ya existe')
    else:
        messagebox.showinfo(title='Alter Database', message='No lleno los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)

def function_show_databases():
    messagebox.showinfo(title='Available Databases', message=f'Databases: {Storage.showDatabases()}')

def drop_database(database, entry):
    if database:
        result = Storage.dropDatabase(database)
        if result == 2:
            messagebox.showinfo(title='Drop Database', message=database + ' no existe')
        elif result == 1:
            messagebox.showinfo(title='Drop Database', message="Error en la operacion")
        elif result == 0:
            messagebox.showinfo(title='Drop Database', message="Operacion exitosa")
        entry.delete(0, END)
    else:
        messagebox.showinfo(title='Drop Database', message='No lleno el campo de texto')

def create_data_table(database,table,columns, entry1, entry2, entry3):
    if database and table and columns:
        if isNumber(columns):
            result = Storage.createTable(database,table,int(columns))
            if result == 3:
                messagebox.showinfo(title='Create table', message=table + ' ya existe')
            elif result == 2:
                messagebox.showinfo(title='Create table', message=database + ' no existe')
            elif result == 1:
                messagebox.showinfo(title='Create table', message="Error en la operacion")
            elif result == 0:
                messagebox.showinfo(title='Create table', message="Operacion exitosa")
        else:
            messagebox.showinfo(title='Create table', message="No escribio un numero de columnas")
    else:
        messagebox.showinfo(title='Create table', message='No lleno el campo de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def isNumber(entry):
    result = Storage.re.search(r'[0-9]+|[\s]',entry)
    return result

def function_show_tables(database,entry):
    if entry:
        messagebox.showinfo(title='Show tables', message=f'{database}: {Storage.showTables(database)}')
        entry.delete(0, END)
    else:
        messagebox.showinfo(title='Show tables', message=f'{database}: {Storage.showTables(database)}')

def extract_table_function(database, table, entry1, entry2):
    if database and table:
        result = Storage.extractTable(database, table)
        if result is not None:
            messagebox.showinfo(title='Extract table', message='Operacion exitosa: ' + str(result))
        else:
            messagebox.showinfo(title='Extract table', message='Base de datos o tabla no exsitentes: '+ str(result))
    else:
        messagebox.showinfo(title='Create Database', message='No se llenaron los campos de texto')

    entry1.delete(0, END)
    entry2.delete(0, END)

def extract_range_table(database, table, columnNumber, lower, upper, entry1, entry2, entry3, entry4, entry5):
    if database and table and columnNumber and lower and upper:
        if isNumber(columnNumber):
            result = Storage.extractRangeTable(database, table, int(columnNumber), lower, upper)
            if result is not None:
                messagebox.showinfo(title='Extract range table', message='Extract completado: ' + str(result))
            else:
                messagebox.showinfo(title='Extract range table', message='Datos no existentes: '+ str(result))
        else:
            messagebox.showinfo(title='Extract range table', message='No escribio un numero de columnas')
            entry3.delete(0, END)
    else:
        messagebox.showinfo(title='Extract range table', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def alter_addPK(database, table, columns, entry1, entry2, entry3):
    if database and table and columns:
        pk = []
        separate = columns.split(',')
        for x in separate:
            if not isNumber(x):
                messagebox.showinfo(title='Alter AddPK', message='No ingreso algun numero de columna')
                entry3.delete(0, END)
                return
            pk.append(int(x))
        result = Storage.alterAddPK(database, table, pk)
        if result == 0:
            messagebox.showinfo(title='Alter AddPK', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Alter AddPK', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Alter AddPK', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Alter AddPK', message='Tabla no existente')
        elif result == 4:
            messagebox.showinfo(title='Alter AddPK', message='Llave primaria existente')
        elif result == 5:
            messagebox.showinfo(title='Alter AddPK', message='Columnas fuera de limites')
    else:
        messagebox.showinfo(title='Alter AddPK', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def alter_dropPK(database, table, entry1, entry2):
    if database and table:
        result = Storage.alterDropPK(database, table)
        if result == 0:
            messagebox.showinfo(title='Alter DropPK', message='Operacion exitosa')
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
    entry1.delete(0, END)
    entry2.delete(0, END)

def alter_table(database, tableOld, tableNew, entry1, entry2, entry3):
    if database and tableOld and tableNew:
        result = Storage.alterTable(database, tableOld, tableNew)
        if result == 0:
            messagebox.showinfo(title='Alter DropPK', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Alter DropPK', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Alter DropPK', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Alter DropPK', message=tableOld+ ' no existente')
        elif result == 4:
            messagebox.showinfo(title='Alter DropPK', message=tableNew+' nueva ya existe')
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def alter_addColumn(database, table, default, entry1, entry2, entry3):
    if database and table and default:
        result = Storage.alterAddColumn(database, table, default)
        if result == 0:
            messagebox.showinfo(title='Alter DropPK', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Alter DropPK', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Alter DropPK', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Alter DropPK', message=table + ' no existente')
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def alter_dropColumn(database, table, columnNumber, entry1, entry2, entry3):
    if database and table and columnNumber:
        if isNumber(columnNumber):
            result = Storage.alterDropColumn(database, table, int(columnNumber))
            if result == 0:
                messagebox.showinfo(title='Alter Drop Column', message='Operacion exitosa')
            elif result == 1:
                messagebox.showinfo(title='Alter Drop Column', message='Error en la operacion')
            elif result == 2:
                messagebox.showinfo(title='Alter Drop Column', message='Base de datos no existente')
            elif result == 3:
                messagebox.showinfo(title='Alter Drop Column', message=table + ' no existente')
            elif result == 4:
                messagebox.showinfo(title='Alter Drop Column', message='Llave no puede eliminarse o la tabla se queda sin columnas')
            elif result == 5:
                messagebox.showinfo(title='Alter Drop Column', message='Columna fuera de limites')
        else:
            messagebox.showinfo(title='Alter Drop Column', message='No ingreso un numero de columnas')
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def drop_table(database, table, entry1, entry2):
    if database and table:
        result = Storage.dropTable(database, table)
        if result == 0:
            messagebox.showinfo(title='Alter DropPK', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Alter DropPK', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Alter DropPK', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Alter DropPK', message='Tabla no existente')
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)

def insert_row(database, table, register, entry1, entry2, entry3):
    if database and table and register:
        data = register.split(',')
        result = Storage.insert(database, table, data)
        if result == 0:
            messagebox.showinfo(title='Insert', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Insert', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Insert', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Insert', message='Tabla no existente')
        elif result == 4:
            messagebox.showinfo(title='Insert', message='Llave primaria duplicada')
        elif result == 5:
            messagebox.showinfo(title='Insert', message='Columna fuera de limites')
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def load_csv(filepath, database, table, entry1, entry2, entry3):
    if filepath and database and table:
        try:
            result = Storage.loadCSV(filepath,database, table)
            messagebox.showinfo(title='Load CSV', message=result)
        except:
            messagebox.showinfo(title='Load CSV', message='Ocurrio un error')
    else:
        messagebox.showinfo(title='Alter DropPK', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def extract_row(database, table, columns, entry1, entry2, entry3):
    if database and table and columns:
        pk = []
        separate = columns.split(',')
        for x in separate:
            if not isNumber(x):
                messagebox.showinfo(title='Extract Row', message='No ingreso algun numero de columna')
                entry3.delete(0, END)
                return
            pk.append(int(x))
        result = Storage.extractRow(database, table, pk)
        messagebox.showinfo(title='Extract Row', message='Resultado: '+str(result))
    else:
        messagebox.showinfo(title='Extract Row', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def update(database, table, register, columns, entry1, entry2, entry3, entry4):
    if database and table and register and columns:
        pk = []
        dictionary = {}
        separate_register = register.split(',')
        separate = columns.split(',')
        for x in separate_register:
            data = x.split(':')
            if not isNumber(data[0]):
                messagebox.showinfo(title='Extract Row', message='No ingreso correctamente las claves')
                entry3.delete(0, END)
                return
            key = int(data[0])
            dictionary[key] = data[1]
        for x in separate:
            if not isNumber(x):
                messagebox.showinfo(title='Extract Row', message='No ingreso algun numero de columna')
                entry3.delete(0, END)
                return
            pk.append(int(x))
        result = Storage.update(database, table, dictionary, pk)
        if result == 0:
            messagebox.showinfo(title='Update', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Update', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Update', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Update', message='Tabla no existente')
        elif result == 4:
            messagebox.showinfo(title='Update', message='Llave primaria no existe')
    else:
        messagebox.showinfo(title='Extract Row', message='No se llenaron los campos de texto')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

def delete(database, table, columns, entry1, entry2, entry3):
    if database and table and columns:
        pk = []
        separate = columns.split(',')
        for x in separate:
            if not isNumber(x):
                messagebox.showinfo(title='Extract Row', message='No ingreso algun numero de columna')
                entry3.delete(0, END)
                return
            pk.append(int(x))
        result = Storage.delete(database, table, pk)
        if result == 0:
            messagebox.showinfo(title='Update', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Update', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Update', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Update', message='Tabla no existente')
        elif result == 4:
            messagebox.showinfo(title='Update', message='Llave primaria no existe')
    else:
        messagebox.showinfo(title='Update', message='No lleno todos los campos')
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def truncate_table(database, table, entry1, entry2):
    if database and table:
        result = Storage.truncate(database, table)
        if result == 0:
            messagebox.showinfo(title='Update', message='Operacion exitosa')
        elif result == 1:
            messagebox.showinfo(title='Update', message='Error en la operacion')
        elif result == 2:
            messagebox.showinfo(title='Update', message='Base de datos no existente')
        elif result == 3:
            messagebox.showinfo(title='Update', message='Tabla no existente')
    else:
        messagebox.showinfo(title='Update', message='No lleno todos los campos')
        entry1.delete(0, END)
        entry2.delete(0, END)

main_window = tkinter.Tk()
main_window.geometry('610x310+300+100')
main_window.title('Tytus EDD: Fase 1')
main_window.configure(background='black')
main_canvas = Canvas(main_window, width=580, height=280).place(x=15, y=10)
#Label(main_window, width=600, height =500, bg = 'white').place(x=0, y=0)
tkinter.Label(main_canvas, text='Tytus Database', font='Helvetica 30 bold italic',padx=10, pady=5).place(x=150, y=20)
tkinter.Button(main_canvas, text='Reportes', font='Helvetica 16 bold italic', width=20, height=2, borderwidth= 5, fg='white', background='black',command=show_data_bases).place(x=15, y=150)
tkinter.Button(main_canvas, text='Funciones', font='Helvetica 16 bold italic', width=20, height=2, borderwidth= 5, fg='white', background='black', command=show_functions).place(x=300, y=150)
main_window.mainloop()