from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from tkinter import scrolledtext
import tkinter as tk
from analyzer import *


class CustomText_follow_line_and_column_in_text(tk.scrolledtext.ScrolledText):
    def __init__(self, *args, **kwargs):
        tk.scrolledtext.ScrolledText.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        cmd = (self._orig,) + args        
        try:
            result = self.tk.call(cmd)
        except Exception:
            return None

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "delete") or 
            args[0:3] == ("mark", "set", "insert")):
            self.event_generate("<<CursorChange>>", when="tail")

        return result     

def _on_change(event):
        line, column = text.index("insert").split(".") # Row starts at 1 and column starts at 0
        message.set("Line: " + line + " Column: " + str(int(column)+1))


route = "" # will store the file path

def new():
    global route
    message.set("New file")
    route = ""
    text.delete(1.0, "end")
    root.title("Tytus")

def open_():
    global route
    message.set("Open file")
    route = FileDialog.askopenfilename(
        initialdir='.', 
        title="Open a file")

    if route != "":
        file_ = open(route, 'r')
        content = file_.read()
        text.delete(1.0,'end')
        text.insert('insert', content)
        file_.close()
        root.title(route + " - Tytus")

def save():
    message.set("Save file")
    if route != "":
        content = text.get(1.0,'end-1c')
        file_ = open(route, 'w+')
        file_.write(content)
        file_.close()
        message.set("File saved successfully")
    else:
        save_as()

def save_as():
    global route
    message.set("Save file as")

    file_ = FileDialog.asksaveasfile(title="Save file", 
        mode="w")

    if file_ is not None:
        route = file_.name
        contenido = text.get(1.0,'end-1c')
        file_ = open(route, 'w+')
        file_.write(contenido)
        file_.close()
        message.set("File saved correctly")
    else:
        message.set("Saved canceled")
        route = ""

def compile():
    #clean console
    console.configure(state="normal")
    console.delete(1.0, "end")
    console.configure(state="disabled")
    #read input text
    input_text = text.get(1.0,'end-1c')
    #parse input text
    analyzer_ = analyzer()
    analyzer_result_ = analyzer_.analyze(input_text)
    #print to console
    console.configure(state="normal")
    console.insert(1.0, analyzer_result_.Printed_Error_Table)
    console.configure(state="disabled")


# Root configuration
root = Tk()
root.title("Tytus")

# Superior menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open_)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="File")

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Compile", command=compile)
menubar.add_cascade(menu=filemenu, label="Analysis")

# Text
text = CustomText_follow_line_and_column_in_text()
text.pack(fill="both", expand=1)
text.configure(bg="#000000", fg="#FFFFFF", insertbackground='#FFFFFF')
text.config(bd=0, padx=6, pady=4, font=("consoles",12))
text.bind("<<CursorChange>>", _on_change)

# Console
console = scrolledtext.ScrolledText(root, width=100, height=20)
console.pack(fill="both", expand=1)
console.configure(bg="#434B4D", fg="#FFFFFF", insertbackground='#FFFFFF')
console.config(bd=0, padx=6, pady=4, font=("consoles",12))
console.configure(state="disabled")

# Lower monitor
message = StringVar()
message.set("Welcome to Tytus")
monitor = Label(root, textvar=message, justify='left')
monitor.pack(side="left")

root.config(menu=menubar)
# App loop
root.mainloop()