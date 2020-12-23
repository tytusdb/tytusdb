import tkinter as tk
import tkinter.filedialog
import tkinter.scrolledtext
import lex 


def open_file_func():
    read_file = tk.filedialog.askopenfile(mode="r")
    entrada_box.insert(tk.INSERT, read_file.read())

def parse_entrada():
    txt_entrada = entrada_box.get(1.0, tk.END+"-1c")
    parse_result = lex.parse(str(txt_entrada))
    label2 = tk.Label(ventana, text=str(parse_result)).grid(row=10, column=0)


#ventana Pricipal
ventana = tk.Tk()
ventana.geometry(newGeometry='1500x750')
ventana.title('Compiladores 2 SQLParser')

#Main Menu Bar
main_menu = tk.Menu(ventana)
ventana.config(menu=main_menu)

#Submenu File
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file_func)

#Input Area
entrada_box = tk.scrolledtext.ScrolledText(ventana, width=180, height=30)
entrada_box.grid(row=0, column=0)

#Buttons Area
parse_button = tk.Button(ventana, text="Parse", command=parse_entrada).grid(row=1, column=0)

#Cosole Area


main_menu.add_cascade(label='File', menu=file_menu)

ventana.mainloop()