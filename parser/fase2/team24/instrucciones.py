class instruccion:
    '''Clase abstracta'''

class create_db(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

    def report_ast(self):
        ast= str(id(self)) + "[shape = rect, slide = 4, skew = .4, label = \" Create_BD \" ]\n"
        ast+= self.nombre.report_ast()+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.nombre))+ "\n"
        return ast
        

class show_db(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

    def report_ast(self):
        ast= str(id(self)) + "[shape = rect, slide = 4, skew = .4, label = \" Show_DB \" ]\n"
        ast+= self.nombre.report_ast()+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.nombre))+ "\n"
        return ast

class alter_db(instruccion):
    def __init__(self,antigua, nueva):
        self.antigua = antigua
        self.nueva = nueva

    def report_ast(self):
        ast= str(id(self)) + "[shape = rect, slide = 4, skew = .4, label = \" Alter_DB \" ]\n"
        ast+= self.antigua.report_ast()+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.antigua))+ "\n"
        ast+= self.nueva.report_ast()+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.nueva))+ "\n"
        return ast

class show_db_like(instruccion):
    def __init__(self,nombre,like):
        self.nombre = nombre
        self.like = like

    def report_ast(self):
        ast= str(id(self)) + "[shape = rect, slide = 4, skew = .4, label = \" Show_DB \" ]\n"
        ast+= self.nombre.report_ast()+ "\n"
        ast+= self.like.report_ast()+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.nombre))+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.like))+ "\n"
        return ast

class drop_db(instruccion):
    def __init__(self,nombre):
        self.nombre = nombre

    def report_ast(self):
        ast= str(id(self)) + "[shape = rect, slide = 4, skew = .4, label = \" Show_DB \" ]\n"
        ast+= self.nombre.report_ast()+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.nombre))+ "\n"
        return ast

class create_table(instruccion):
    def __init__(self,db,nombre,columnas):
        self.nombre = nombre
        self.db = db
        self.columnas = columnas

    def report_ast(self):
        ast= str(id(self)) + "[shape = rect, slide = 4, skew = .4, label = \" Create_table \" ]\n"
        ast+= self.nombre.report_ast()+ "\n"
        ast+= self.db.report_ast()+ "\n"
        ast+= self.columnas.report_ast()+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.nombre))+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.db))+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.columnas))+ "\n"
        return ast

class create_table_herencia(instruccion):
    def __init__(self,db,nombre,columnas,herencia):
        self.nombre = nombre
        self.db = db
        self.columnas = columnas
        self.herencia =  herencia

    def report_ast(self):
        ast= str(id(self)) + "[shape = rect, slide = 4, skew = .4, label = \" Create_table \" ]\n"
        ast+= self.nombre.report_ast()+ "\n"
        ast+= self.db.report_ast()+ "\n"
        ast+= self.columnas.report_ast()+ "\n"
        ast+= self.herencia.report_ast()+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.nombre))+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.db))+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.columnas))+ "\n"
        ast+= str(id(self))+ "->"+str(id(self.herencia))+ "\n"
        return ast

class drop_table(instruccion):
    def __init__(self,db,nombre):
        self.db = db
        self.nombre = nombre

class alter_table(instruccion):
    def __init__(self,db,nombre, tipo):
        self.db = db
        self.nombre = nombre
        self.tipo = tipo

class alter_add_column(instruccion):
    def __init__(self, db,antigua, nueva):
        self.db = db
        self.antigua = antigua
        self.nueva = nueva

class update(instruccion):
    def __init__(self, id, cond_set, cond_where):
        self.id= id
        self.cond_set = cond_set
        self.cond_where = cond_where

class insert(instruccion):
    def __init__ (self,id,values):
        self.id = id
        self.values = values


class ListaInstrucciones(instruccion):
    lst = []

    def __init__(self, lst: []):
        self.lst = lst


    def ast_inicio(self):
        contenido = " digraph G { \n"
        contenido += self.report_ast()
        contenido += "}"
        return contenido

    def report_ast(self):
        concatenar = ""
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "LISTA_INSTRUCCIONES" + "\"]\n"

        for elemento in self.lst:
            concatenar += elemento.report_ast()
            concatenar += str(id(self)) + " -> " + str(id(elemento)) + "\n"
        return concatenar

    def agregar(self, nuevo: Instruccion):
        self.lst.append(nuevo)


