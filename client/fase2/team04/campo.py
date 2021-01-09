import tkinter as tk
from tkinter import Menu, Tk, Text, DISABLED, RAISED,Frame, FLAT, Button, Scrollbar, Canvas, END
from tkinter import messagebox as MessageBox
from tkinter import ttk
import tkinter.simpledialog
from tkinter import *
from tkinter import font as tkFont
#Metodo para enumerar las lineas
class TextLineNumbers(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

#Metodo para el campo de texto
class CustomText(Text):
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or 
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result 

#Frame que une todo
class Campo(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        
        # clone the text widget font and use it as a basis for some tag
        bold_font = tkFont.Font(self.text, self.text.cget("font"))
        bold_font.configure(weight="bold")
        self.text.tag_configure("bold", font=bold_font)
        self.text.tag_configure("reserve", foreground="blue", underline=False)

    def _on_change(self, event):
        self.linenumbers.redraw()


#Clase para crear usuario
class MyDialog(tkinter.simpledialog.Dialog):

    def body(self, master):

        Label(master, text="Username:").grid(row=0)
        Label(master, text="Password:").grid(row=1)
        self.result = []
        self.accept = False
        self.e1 = Entry(master)
        self.e2 = Entry(master, show="*")

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        self.accept = True
        self.result = [first, second]