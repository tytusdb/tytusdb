from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from tkinter import scrolledtext
import tkinter as tk
import Tytus_GUI


prints = []
prints_c3d = []
prints_c3d_optimized = []


class print_data:

    def __init__(self, type_print: str, data_type: str, print_: str):
        self.type_print = type_print
        self.data_type = data_type
        self.print_ = print_


#0 -> console, prints
#1 -> console_c3d, prints_c3d
#2 -> console_c3d_optimized, prints_c3d_optimized

def print_error(data_type: str, print_: str, console_number: int):
    print_data_("#FF0000", "error", data_type, print_, console_number)

def print_warning(data_type: str, print_: str, console_number: int):
    print_data_("#FFFF00", "warning", data_type, print_, console_number)

def print_success(data_type: str, print_: str, console_number: int):
    print_data_("#00FF00", "success", data_type, print_, console_number)

def print_text(data_type: str, print_: str, console_number: int):
    print_data_("FFFFFF", "text", data_type, print_, console_number)

def print_table(data_type, print_: str, console_number: int):
    print_data_("FFFFFF", "table", data_type, print_, console_number)


#Tytus_GUI.console.tag_add("tag name", "initial_line.initial_column", "end_line.end_column")
#       Always initial position line starts at 1, end position line starts at 1
#       Always initial position column starts at 0, end position column starts at 1
#Tytus_GUI.console.insert("line.column", "text")
#       line starts at 1, column starts at 0


def print_data_(hexadecimal_color_foreground: str, type_print: str, data_type: str, print_: str, console_number: int):

    selected_prints =  None
    selected_console = None
    if console_number == 0:
        selected_prints= prints
        selected_console= Tytus_GUI.console
    elif console_number == 1:
        selected_prints= prints_c3d
        selected_console= Tytus_GUI.console_c3d
    elif console_number == 2:
        selected_prints= prints_c3d_optimized
        selected_console= Tytus_GUI.console_c3d_optimized

    if selected_prints!= None and selected_console!= None:
    
        # We save the print
        selected_prints.append( print_data(type_print,data_type,print_) )

        if type_print != "table":
            print_ = data_type + ">>    " + print_  

        text_console_before = selected_console.get(1.0,'end-1c')
        number_of_lines_before = 0
        if(text_console_before!=""):
            number_of_lines_before = len(text_console_before.split("\n"))
    
        # We add printing
        if text_console_before!="":
            print_ = "\n" + print_
        selected_console.configure(state="normal")
        selected_console.insert(str(number_of_lines_before + 1) + ".0", print_)
        selected_console.configure(state="disabled")
    
        text_console_after = selected_console.get(1.0,'end-1c')
        number_of_lines_after = 0
        if(text_console_after!=""):
            number_of_lines_after = len(text_console_after.split("\n"))
    
        positions = get_printed_line_and_column(text_console_before,  text_console_after, (number_of_lines_before + 1), number_of_lines_after)

        # We create a tag
        selected_console.tag_config(type_print,foreground=hexadecimal_color_foreground)
    
        # We apply the tag to a fragment of the text using indexes
        selected_console.tag_add(type_print, str(positions[0]) + "." + str(positions[1]), str(positions[2]) + "." + str(positions[3]))


#0 -> console
#1 -> console_c3d
#2 -> console_c3d_optimized

def print_error_table(data_type: str, print_: str, console_number: int):
    print_report("#FFFFFF", "#FF0000", "error_table", data_type, print_, console_number)

def print_symbol_table(data_type: str, print_: str, console_number: int):
    print_report("#FFFFFF", "#0000FF", "symbol_table", data_type, print_, console_number)

def print_messages(data_type: str, print_: str, console_number: int):
    print_report("#000000", "#FFFFFF", "message", data_type, print_, console_number)

def print_querys(data_type: str, print_: str, console_number: int):
    print_report("#FFFFFF", "#00FF00", "query", data_type, print_, console_number)

def print_optimization_table(data_type: str, print_: str, console_number: int):
    print_report("#FFFFFF", "#00BB2D", "optimization_table", data_type, print_, console_number)


def print_report(hexadecimal_color_foreground: str, hexadecimal_color_background: str, type_print: str, data_type: str, print_: str, console_number: int):

    selected_console = None
    if console_number == 0:
        selected_console= Tytus_GUI.console
    elif console_number == 1:
        selected_console= Tytus_GUI.console_c3d
    elif console_number == 2:
        selected_console= Tytus_GUI.console_c3d_optimized

    if selected_console!= None:
    
        text_console_before = selected_console.get(1.0,'end-1c')
        number_of_lines_before = 0
        if(text_console_before!=""):
            number_of_lines_before = len(text_console_before.split("\n"))
    
        # We save the print
        if text_console_before!="":
            print_ = "\n" + print_
        selected_console.configure(state="normal")
        selected_console.insert(str(number_of_lines_before + 1) + ".0", print_)
        selected_console.configure(state="disabled")
    
        text_console_after = selected_console.get(1.0,'end-1c')
        number_of_lines_after = 0
        if(text_console_after!=""):
            number_of_lines_after = len(text_console_after.split("\n"))
    
        positions = get_printed_line_and_column(text_console_before,  text_console_after, (number_of_lines_before + 1), number_of_lines_after)

        # We create a tag
        selected_console.tag_config(type_print,foreground=hexadecimal_color_foreground,background=hexadecimal_color_background)
    
        # We apply the tag to a fragment of the text using indexes
        selected_console.tag_add(type_print, str(positions[0]) + "." + str(positions[1]), str(positions[2]) + "." + str(positions[3]))


def get_printed_line_and_column(text_before: str, text_after: str, initial_line: int, end_line: int):#the line count starts at 1

    if initial_line==0:
        initial_line = 1
    if end_line==0:
        end_line = 1
    
    text_split = text_after.split("\n")
    end_column = len(text_split[(len(text_split)-1)])
    if end_column==0:
        end_column = 1
    positions = [initial_line, 0, end_line, end_column]
    return positions