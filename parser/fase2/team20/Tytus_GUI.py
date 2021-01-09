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

from Tytus_GUI_console import print_error, print_symbol_table, print_error_table, print_messages, print_querys, print_optimization_table
import Tytus_GUI_console

from graphviz import Source
import webbrowser

from prettytable import PrettyTable

from execution.executeOptimization import *
from execution.executeOptimization_result import *
from C3D import up

def update_line_and_column(text_: tk.Text):
    line, column = text_.index("insert").split(".") # Row starts at 1 and column starts at 0
    message.set("Line: " + str(line) + " Column: " + str(int(column)+1))

route = "" # will store the file path
dotAST = ""
dotAST += "digraph ASTTytus{ \n rankdir = TD\n node[shape = \"box\"]\n"
dotAST += "\n }"
content_grammar_report = ""

path_c3d = "C3D.py"

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

def translate_to_C3D():
    #clear console
    console.configure(state="normal")
    console.delete(1.0, "end")
    console.configure(state="disabled")
    Tytus_GUI_console.prints = []
    #clear text editor text_c3d
    text_c3d.delete(1.0, "end")
    #clear console_c3d
    console_c3d.configure(state="normal")
    console_c3d.delete(1.0, "end")
    console_c3d.configure(state="disabled")
    Tytus_GUI_console.prints_c3d = []
    #clear text editor text_c3d_optimized
    text_c3d_optimized.delete(1.0, "end")
    #clear console_c3d_optimized
    console_c3d_optimized.configure(state="normal")
    console_c3d_optimized.delete(1.0, "end")
    console_c3d_optimized.configure(state="disabled")
    Tytus_GUI_console.prints_c3d_optimized = []
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
    print_c3d_(result_execute.c3d)


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
                print_error("Unknown Error", "AST graphic not generated", 0)
                #print(e)

def generate_grammar_report(content_grammar_report_: str):
    try:
        file_grammar_report = open("bnf.md", "w")
        file_grammar_report.write(content_grammar_report_)
        file_grammar_report.close()
        generate_grammar_report_view(content_grammar_report_)
    except Exception as e:
        print_error("Unknown Error", "Grammar report file not generated", 0)
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
        print_error("Unknown Error", "Grammar report view not generated", 0)
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
    print_error_table("Error Table", print_, 0)

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
    print_error_table("Error Table", print_, 0)

def print_symbol_table_(printSymbolTable: str):
    print_symbol_table("Symbol Table", printSymbolTable, 0)

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
    print_messages("Message", print_, 0)

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
    print_querys("Query", print_, 0)

def print_c3d_(c3d):
    text_c3d.insert("1.0", c3d)


def optimize_C3D():
    #clear console_c3d
    console_c3d.configure(state="normal")
    console_c3d.delete(1.0, "end")
    console_c3d.configure(state="disabled")
    Tytus_GUI_console.prints_c3d = []
    #clear text editor text_c3d_optimized
    text_c3d_optimized.delete(1.0, "end")
    #clear console_c3d_optimized
    console_c3d_optimized.configure(state="normal")
    console_c3d_optimized.delete(1.0, "end")
    console_c3d_optimized.configure(state="disabled")
    Tytus_GUI_console.prints_c3d_optimized = []
    #get input text
    Input_text = text_c3d.get(1.0,'end-1c')
    #eanalyze text and xecute Optimization
    executeOptimization_ = executeOptimization()
    executeOptimization_result_ = executeOptimization_.optimize(Input_text)
    #process results and display reports
    print_c3d_optimized_(executeOptimization_result_.c3d_optimized)
    print_optimization_table_(executeOptimization_result_.print_optimization_table)

def print_c3d_optimized_(c3d):
    text_c3d_optimized.insert("1.0", c3d)

def print_optimization_table_(print_):
    print_optimization_table("Optimization Table", print_, 1)


def compile_C3D():
    #clear console_c3d_optimized
    console_c3d_optimized.configure(state="normal")
    console_c3d_optimized.delete(1.0, "end")
    console_c3d_optimized.configure(state="disabled")
    Tytus_GUI_console.prints_c3d_optimized = []
    #get input text
    Input_text = text_c3d_optimized.get(1.0,'end-1c')    
    #compile c3d
    compile_C3D_aux(Input_text)
    #result_compile = compile(Input_text)
    #process results and display reports
    #process_results_compile_and_display_reports(result_compile)
    

def compile_C3D_aux(c3d_optimized):
    global path_c3d
    try:
        up()
        #exec(compile(c3d_optimized, path_c3d, 'exec'))
    except Exception as e:
        print_error("UNKNOWN ERROR", "Error running optimized c3d, "+str(e),2)
        #print(e)


# Root configuration
root = Tk()
root.title("Tytus")
try:
    root.iconbitmap("Tytus.ico")
except Exception as e:
    i=0#print(e)

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
filemenu.add_command(label="Translate to C3D", command=translate_to_C3D)
filemenu.add_command(label="Optimize C3D", command=optimize_C3D)
filemenu.add_command(label="Compile C3D", command=compile_C3D)
menubar.add_cascade(menu=filemenu, label="Analysis")

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Generate AST Report", command=lambda:generate_report(0))
filemenu.add_command(label="Generate Grammar Report", command=lambda:generate_report(1))
menubar.add_cascade(menu=filemenu, label="Reports")

width_text = 50
height_text = 14

#Labels
frame_labels = tk.Frame(root)
frame_labels.pack(ipadx=10, ipady=10, expand=False, side="top", fill="both")

label_text = Label(frame_labels, width=width_text, text="Input Text")
label_text.pack(fill="both", expand=1)
label_text.pack(side ="left")
label_text.config(bd=0, padx=6, pady=4, font=("consolas",12))
label_text_c3d = Label(frame_labels, width=width_text, text="C3D")
label_text_c3d.pack(fill="both", expand=1)
label_text_c3d.pack(side ="left")
label_text_c3d.config(bd=0, padx=6, pady=4, font=("consolas",12))
label_text_c3d_optimized = Label(frame_labels, width=width_text, text="Optimized C3D")
label_text_c3d_optimized.pack(fill="both", expand=1)
label_text_c3d_optimized.pack(side ="left")
label_text_c3d_optimized.config(bd=0, padx=6, pady=4, font=("consolas",12))

#Text editors
frame_1 = tk.Frame(root)
frame_1.pack(ipadx=10, ipady=10, expand=True, side="top", fill="both")

frame_11 = tk.Frame(frame_1)
frame_11.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")
text_xscrollbar = Scrollbar(frame_11, orient=HORIZONTAL)
text_xscrollbar.pack(side=BOTTOM, fill=X)
text = scrolledtext.ScrolledText(frame_11, width=width_text, height=height_text, wrap=NONE, xscrollcommand=text_xscrollbar.set)
text.pack(fill="both", expand=1)
text.configure(bg="#000000", fg="#FFFFFF", insertbackground='#FFFFFF')
text.config(bd=0, padx=6, pady=4, font=("consolas",12))
text.pack(side ="left")
text.bindtags(('Text','post-class-bindings_text', '.', 'all'))
text.bind_class("post-class-bindings_text", "<KeyPress>", lambda e: update_line_and_column(text))
text.bind_class("post-class-bindings_text", "<Button-1>", lambda e: update_line_and_column(text))
text_xscrollbar.config(command=text.xview)

frame_12 = tk.Frame(frame_1)
frame_12.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")
text_c3d_xscrollbar = Scrollbar(frame_12, orient=HORIZONTAL)
text_c3d_xscrollbar.pack(side=BOTTOM, fill=X)
text_c3d = scrolledtext.ScrolledText(frame_12, width=width_text, height=height_text, wrap=NONE, xscrollcommand=text_c3d_xscrollbar.set)
text_c3d.pack(fill="both", expand=1)
text_c3d.configure(bg="#000000", fg="#FFFFFF", insertbackground='#FFFFFF')
text_c3d.config(bd=0, padx=6, pady=4, font=("consolas",12))
text_c3d.pack(side ="left")
text_c3d.bindtags(('Text','post-class-bindings_text_c3d', '.', 'all'))
text_c3d.bind_class("post-class-bindings_text_c3d", "<KeyPress>", lambda e: update_line_and_column(text_c3d))
text_c3d.bind_class("post-class-bindings_text_c3d", "<Button-1>", lambda e: update_line_and_column(text_c3d))
text_c3d_xscrollbar.config(command=text_c3d.xview)

frame_13 = tk.Frame(frame_1)
frame_13.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")
text_c3d_optimized_xscrollbar = Scrollbar(frame_13, orient=HORIZONTAL)
text_c3d_optimized_xscrollbar.pack(side=BOTTOM, fill=X)
text_c3d_optimized = scrolledtext.ScrolledText(frame_13, width=width_text, height=height_text, wrap=NONE, xscrollcommand=text_c3d_optimized_xscrollbar.set)
text_c3d_optimized.pack(fill="both", expand=1)
text_c3d_optimized.configure(bg="#000000", fg="#FFFFFF", insertbackground='#FFFFFF')
text_c3d_optimized.config(bd=0, padx=6, pady=4, font=("consolas",12))
text_c3d_optimized.pack(side ="left")
text_c3d_optimized.bindtags(('Text','post-class-bindings_text_c3d_optimized', '.', 'all'))
text_c3d_optimized.bind_class("post-class-bindings_text_c3d_optimized", "<KeyPress>", lambda e: update_line_and_column(text_c3d_optimized))
text_c3d_optimized.bind_class("post-class-bindings_text_c3d_optimized", "<Button-1>", lambda e: update_line_and_column(text_c3d_optimized))
text_c3d_optimized_xscrollbar.config(command=text_c3d_optimized.xview)

#Consoles
frame_2 = tk.Frame(root)
frame_2.pack(ipadx=10, ipady=10, expand=True, side="top", fill="both")

frame_21 = tk.Frame(frame_2)
frame_21.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")
console_xscrollbar = Scrollbar(frame_21, orient=HORIZONTAL)
console_xscrollbar.pack(side=BOTTOM, fill=X)
console = scrolledtext.ScrolledText(frame_21, width=width_text, height=height_text, wrap=NONE, xscrollcommand=console_xscrollbar.set)
console.pack(fill="both", expand=1)
console.configure(bg="#434B4D", fg="#FFFFFF", insertbackground='#FFFFFF')
console.config(bd=0, padx=6, pady=4, font=("consolas",12))
console.configure(state="disabled")
console.pack(side ="left")
console_xscrollbar.config(command=console.xview)

frame_22 = tk.Frame(frame_2)
frame_22.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")
console_c3d_xscrollbar = Scrollbar(frame_22, orient=HORIZONTAL)
console_c3d_xscrollbar.pack(side=BOTTOM, fill=X)
console_c3d = scrolledtext.ScrolledText(frame_22, width=width_text, height=height_text, wrap=NONE, xscrollcommand=console_c3d_xscrollbar.set)
console_c3d.pack(fill="both", expand=1)
console_c3d.configure(bg="#434B4D", fg="#FFFFFF", insertbackground='#FFFFFF')
console_c3d.config(bd=0, padx=6, pady=4, font=("consolas",12))
console_c3d.configure(state="disabled")
console_c3d.pack(side ="left")
console_c3d_xscrollbar.config(command=console_c3d.xview)

frame_23 = tk.Frame(frame_2)
frame_23.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")
console_c3d_optimized_xscrollbar = Scrollbar(frame_23, orient=HORIZONTAL)
console_c3d_optimized_xscrollbar.pack(side=BOTTOM, fill=X)
console_c3d_optimized = scrolledtext.ScrolledText(frame_23, width=width_text, height=height_text, wrap=NONE, xscrollcommand=console_c3d_optimized_xscrollbar.set)
console_c3d_optimized.pack(fill="both", expand=1)
console_c3d_optimized.configure(bg="#434B4D", fg="#FFFFFF", insertbackground='#FFFFFF')
console_c3d_optimized.config(bd=0, padx=6, pady=4, font=("consolas",12))
console_c3d_optimized.configure(state="disabled")
console_c3d_optimized.pack(side ="left")
console_c3d_optimized_xscrollbar.config(command=console_c3d_optimized.xview)

# Lower monitor
message = StringVar()
message.set("Welcome to Tytus")
monitor = Label(root, textvar=message, justify='left')
monitor.pack(side="left")

root.config(menu=menubar)
# App loop
#root.mainloop()