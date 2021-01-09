import gramatica2 as g
from storageManager import jsonMode
from Expresion.variablesestaticas import variables
from tkinter import *

class CodigoIntermedio():
    def __init__(self,entorno):
        self.entorno=entorno
        jsonMode.dropAll()

        variables.consola.delete("1.0", "end")
        variables.consola.configure(state='normal')

    def ejecutarsql(self, stringinstr):
        'ejecucion del bloque'
        instr=g.parse(stringinstr)
        for inst in instr:
            return inst.ejecutar(self.entorno)

    def getSym(self):
        f = open('tsAux', 'a+')
        f.write(self.entorno.mostrarSimbolos())
        f.close()




