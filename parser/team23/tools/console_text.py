contenido_consola = "PS C:\\Users\\Grupo 23> "

def limpiar_consola():    
    global contenido_consola
    contenido_consola = "PS C:\\Users\\Grupo 23> "

def add_text(text):
    global contenido_consola
    contenido_consola = contenido_consola + str(text)

def get_contenido():
    global contenido_consola
    return contenido_consola

use_actual_db = ""

def update_use_db(id_db):
    global use_actual_db
    use_actual_db = id_db

def get_actual_use():
    global use_actual_db
    return use_actual_db