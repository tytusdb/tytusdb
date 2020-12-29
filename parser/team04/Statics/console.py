from tkinter import *
from tkinter.ttk import *


class Console:
    console = None

    @staticmethod
    def create(parent):
        Console.console = Text(parent)
        Console.console.pack(fill="both", expand=False)

    @staticmethod
    def add(text):
        Console.console.insert(END, text)
        Console.console.insert(END, "\n")

    @staticmethod
    def clear():
        Console.console.delete('1.0', END)
