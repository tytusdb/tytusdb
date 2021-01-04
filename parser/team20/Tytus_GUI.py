from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from tkinter import scrolledtext
import tkinter as tk

from grammar import analyze
from grammar_result import *
from execution.execute import *
from execution.execute_result import *

from execution.AST.error import *

from Tytus_GUI_console import print_error, print_symbol_table, print_error_table, print_messages, print_querys
import Tytus_GUI_console

from graphviz import Source
import webbrowser

from prettytable import PrettyTable


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
dotAST = ""
dotAST += "digraph ASTTytus{ \n rankdir = TD\n node[shape = \"box\"]\n"
dotAST += "\n }"
content_grammar_report = ""

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
    #clear console
    console.configure(state="normal")
    console.delete(1.0, "end")
    console.configure(state="disabled")
    Tytus_GUI_console.prints = []
    #get input text
    Input_text = text.get(1.0,'end-1c')    
    #analyze text
    result_analyze = analyze(Input_text)
    #run analysis results
    exec = Execute(result_analyze.noderoot)
    result_execute = exec.execute()
    #process results and display reports
    process_results_and_display_reports(result_analyze, result_execute)

def process_results_and_display_reports(result_analyze, result_execute):
    #generate_ast_tree(result_execute.dotAST, result_execute.errors)
    global dotAST
    dotAST = result_execute.dotAST
    #generate_grammar_report(result_analyze.grammarreport)
    global content_grammar_report
    content_grammar_report = result_analyze.grammarreport
    #print_error_table_(result_analyze.grammarerrors, result_execute.errors)
    print_alternative_error_table_()
    print_symbol_table_(result_execute.printSymbolTable)
    #print_messages_(result_execute.messages)
    #print_querys_(result_execute.querys)

def generate_report(report_number: int):
    if report_number == 0:
        errors_ = []
        global dotAST
        generate_ast_tree(dotAST, errors_)
    elif report_number == 1:
        global content_grammar_report
        generate_grammar_report(content_grammar_report)

def generate_ast_tree(dot: str, errors):
    file_used_by_another = True
    i = 0
    error_file_used_by_another_part_one = "Command '['dot', '-Tpdf', '-O', 'AST_Report_" + str(i) + "']' "
    error_file_used_by_another_part_two = "returned non-zero exit status 1. "
    error_file_used_by_another_part_three = "[stderr: b'Error: Could not open \"AST_Report_" + str(i) + ".pdf\" for writing : Permission denied\\r\\n']"
    error_file_used_by_another = error_file_used_by_another_part_one + error_file_used_by_another_part_two + error_file_used_by_another_part_three
    
    while file_used_by_another==True:
        error_file_used_by_another_part_one = "Command '['dot', '-Tpdf', '-O', 'AST_Report_" + str(i) + "']' "
        error_file_used_by_another_part_three = "[stderr: b'Error: Could not open \"AST_Report_" + str(i) + ".pdf\" for writing : Permission denied\\r\\n']"
        error_file_used_by_another = error_file_used_by_another_part_one + error_file_used_by_another_part_two + error_file_used_by_another_part_three
        try:
            src = Source(dot)
            src.render('AST_Report_' + str(i), view=True)
            file_used_by_another = False
        except Exception as e:
            if str(e) == error_file_used_by_another:
                file_used_by_another = True
                i += 1
            else:
                file_used_by_another = False
                errors.append( Error("Unknown", "AST graphic not generated", 0, 0) )
                print_error("Unknown Error", "AST graphic not generated")
                #print(e)

def generate_grammar_report(content_grammar_report_: str):
    try:
        file_grammar_report = open("bnf.md", "w")
        file_grammar_report.write(content_grammar_report_)
        file_grammar_report.close()
        generate_grammar_report_view(content_grammar_report_)
    except Exception as e:
        print_error("Unknown Error", "Grammar report file not generated")
        #print(e)

def generate_grammar_report_view(content_grammar_report_: str):
    try:    
        grammar_report_html = "<!DOCTYPE html>\n"
        grammar_report_html += "<html lang=\"es-ES\">\n"
        grammar_report_html += "   <head>\n"
        grammar_report_html += "       <meta charset=\"utf-8\">"
        grammar_report_html += "       <title>bnf.md</title>\n"
        grammar_report_html += "   </head>\n"
        grammar_report_html += "   <body>\n"
        grammar_report_split = content_grammar_report_.split("\n")
        i = 0
        while i < len(grammar_report_split):
            grammar_report_html += "       <p>" + grammar_report_split[i] + "</p>"
            i += 1
        grammar_report_html += "   </body>"
        grammar_report_html += "</html>"
        file_grammar_report_html = open("bnf.md.html", "w")
        file_grammar_report_html.write(grammar_report_html)
        file_grammar_report_html.close()
        webbrowser.open("bnf.md.html", new=2, autoraise=True)
    except Exception as e:
        print_error("Unknown Error", "Grammar report view not generated")
        #print(e)

def print_error_table_(grammarerrors,executionerrors):
    errors_ = grammarerrors + executionerrors
    print_ = "ERROR TABLE"
    if len(errors_)>0:
        print_ += "\n"
    i = 0
    while i<len(errors_):
        if(i!=0):
            print_ += "\n"
        print_ += errors_[i].toString()
        i += 1
    print_error_table("Error Table", print_)

def print_alternative_error_table_():
    x = PrettyTable(["Number", "Type", "Description"])
    i = 0
    j = 1
    while i < len(Tytus_GUI_console.prints):        
        if ("ERROR" in str(Tytus_GUI_console.prints[i].data_type).upper()) == True:
            x.add_row([j, str(Tytus_GUI_console.prints[i].data_type), str(Tytus_GUI_console.prints[i].print_)])
            j += 1
        i += 1
    print_ = x.get_string(title="Error Table")
    print_error_table("Error Table", print_)

def print_symbol_table_(printSymbolTable: str):
    print_symbol_table("Symbol Table", printSymbolTable)

def print_messages_(messages):
    print_ = "MESSAGES"
    if len(messages)>0:
        print_ += "\n"
    i = 0
    while i<len(messages):
        if(i!=0):
            print_ += "\n"
        print_ += messages[i]
        i += 1
    print_messages("Message", print_)

def print_querys_(querys):
    print_ = "QUERYS"
    if len(querys)>0:
        print_ += "\n"
    i = 0
    while i<len(querys):
        if(i!=0):
            print_ += "\n"
        print_ += querys[i].toString()
        i += 1
    print_querys("Query", print_)


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

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Generate AST Report", command=lambda:generate_report(0))
filemenu.add_command(label="Generate Grammar Report", command=lambda:generate_report(1))
menubar.add_cascade(menu=filemenu, label="Reports")

# Text
text = CustomText_follow_line_and_column_in_text()
text.pack(fill="both", expand=1)
text.configure(bg="#000000", fg="#FFFFFF", insertbackground='#FFFFFF')
text.config(bd=0, padx=6, pady=4, font=("consolas",12))
text.bind("<<CursorChange>>", _on_change)

# Console
console = scrolledtext.ScrolledText(root, width=100, height=20)
console.pack(fill="both", expand=1)
console.configure(bg="#434B4D", fg="#FFFFFF", insertbackground='#FFFFFF')
console.config(bd=0, padx=6, pady=4, font=("consolas",12))
console.configure(state="disabled")
# Lower monitor
message = StringVar()
message.set("Welcome to Tytus")
monitor = Label(root, textvar=message, justify='left')
monitor.pack(side="left")

root.config(menu=menubar)
# App loop
#root.mainloop()