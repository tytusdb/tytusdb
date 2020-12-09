contenido_consola = "PS C:\\Users\\Luis Fer> "

def limpiar_consola():    
    global contenido_consola
    contenido_consola = "PS C:\\Users\\Luis Fer> "

def add_text(text):
    global contenido_consola
    contenido_consola = contenido_consola + str(text)
    

def get_contenido():
    global contenido_consola
    return contenido_consola