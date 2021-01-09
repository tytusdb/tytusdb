
try:
    import Tytus_GUI_console
except Exception as e:
    i=0#print(e)

def print_error(data_type: str, print_: str, console_number: int):
    try:
        Tytus_GUI_console.print_error(data_type, print_, console_number)
    except Exception as e:
        i=0#print(e)

def print_warning(data_type: str, print_: str, console_number: int):
    try:
        Tytus_GUI_console.print_warning(data_type, print_, console_number)
    except Exception as e:
        i=0#print(e)

def print_success(data_type: str, print_: str, console_number: int):
    try:
        Tytus_GUI_console.print_success(data_type, print_, console_number)
    except Exception as e:
        i=0#print(e)
    
def print_text(data_type: str, print_: str, console_number: int):
    try:
        Tytus_GUI_console.print_text(data_type, print_, console_number)
    except Exception as e:
        i=0#print(e)

def print_table(data_type: str, print_: str, console_number: int):
    try:
        Tytus_GUI_console.print_table(data_type, print_, console_number) 
    except Exception as e:
        i=0#print(e)