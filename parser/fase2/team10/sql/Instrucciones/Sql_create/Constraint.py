from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Constraint(Instruccion):
    def __init__(self, nombre, tipo,lista_constraint, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.nombre = nombre
        self.tipo = tipo
        self.lista_constraint=lista_constraint
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)