from tkinter import *
from tkinter import ttk
import random
from grammar import parse


root = Tk() 
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("TytusDB - Query Tools") 

global selected
selected = False

# ACTIONS
def analizar(txt):
    print("analizando...")
    print(txt)
    salida_table()
    parse(txt)

def analizar_select(e):
    global selected
    if my_text.selection_get():
        selected = my_text.selection_get()
        print(selected)
        parse(selected)

toolbar_frame = Frame(root)
toolbar_frame.pack(fill = X)

text_frame = Frame(root)
text_frame.pack(pady=5)



# VERTICAL SCROLL BAR
text_scroll = Scrollbar(text_frame)
text_scroll.pack(side = RIGHT, fill = Y)
# HORIZONTAL SCROLL BAR
hor_scroll = Scrollbar(text_frame, orient = 'horizontal')
hor_scroll.pack(side = BOTTOM, fill = X)



my_text_h = int(h * 0.028)
my_text = Text(text_frame, width=w, height=my_text_h, selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap = "none", xscrollcommand = hor_scroll.set)
my_text.pack()

text_scroll.config(command = my_text.yview)
hor_scroll.config(command = my_text.xview)

#MENU
my_menu = Menu(root)
root.config(menu = my_menu)

file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Archivo", menu = file_menu)
file_menu.add_command(label = "Analizar", command = lambda: analizar(my_text.get("1.0",'end-1c')))
file_menu.add_command(label = "Analizar Query" , command = lambda: analizar_select(False))
file_menu.add_command(label = "Save")
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

reportes_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Reportes", menu = reportes_menu)
reportes_menu.add_command(label = "New")
reportes_menu.add_command(label = "Open")
reportes_menu.add_command(label = "Save")

analizar_button = Button(toolbar_frame)
photoCompila = PhotoImage(file="iconos/all.png")
analizar_button.config(image=photoCompila, width="50", height="50", activebackground="black",command = lambda: analizar(my_text.get("1.0",'end-1c')))
analizar_button.grid(row = 0, column = 0, sticky = W)

analizar_step_step = Button(toolbar_frame)
photoCompila1 = PhotoImage(file="iconos/select.png")
analizar_step_step.config(image=photoCompila1, width="50", height="50", activebackground="black",command = lambda: analizar_select(False))
analizar_step_step.grid(row = 0, column = 1, sticky = W)

def salida_table():
    global salida_frame
    try:
        global salida_frame
        salida_frame.destroy()
    except:
        pass
    salida_frame = LabelFrame(root, text = "Salida")
    salida_frame.pack(fill = X)

    for widget in salida_frame.winfo_children():
        widget.destroy()

    global random_numero
    random_numero = random.randint(5,10)

    prueba_columna = []

    i = 1
    while i < random_numero:
        prueba_columna.append(i)
        i += 1

    print(prueba_columna)
    
    my_tree = ttk.Treeview(salida_frame, columns=prueba_columna)

    my_tree.pack(side=LEFT)
    my_tree.place(x=0,y=0)

    for record in prueba_columna:
        # print(record-1)
        if record == 1:
            my_tree.column("#"+str(record-1), stretch=False, width=40)
            my_tree.heading("#"+str(record-1),text = " ")
        else:
            my_tree.column("#"+str(record-1), stretch=False, width=100)
            my_tree.heading("#"+str(record-1),text = "Label"+str(record-1))

    yscrollbar = ttk.Scrollbar(salida_frame, orient = "vertical", command=my_tree.yview)
    yscrollbar.pack(side = RIGHT, fill = Y)

    xscrollbar = ttk.Scrollbar(salida_frame, orient="horizontal", command = my_tree.xview)
    xscrollbar.pack(side=BOTTOM, fill = X)

    my_tree.configure(yscrollcommand=yscrollbar.set, xscrollcommand = xscrollbar.set)


    data = []

    j = 1
    while j < 50:
        data.append(["Usuario"+str(j),"Password"+str(j),j])
        j += 1


    count = 1
    for record in data:
        my_tree.insert(parent = '', index = 'end', iid=count, text = str(count), values = (record[0],record[1],record[2]))
        count += 1
        
    

    my_tree.pack(fill = X)


root.mainloop() 