import re
from sys import path
from os.path import dirname as dir
from typing import Generator

path.append(dir(path[0]))
from optimization.optGrammar import optimize
from optimization.abstract.optimize import OptimizedInstruction

listaInstruccion = list()

def optimizedCode(text):
    global listaInstruccion
    listaInstruccion = optimize(text)

    #Intentamos optimizar cada instruccion
    for ins in listaInstruccion:
        if isinstance(ins, OptimizedInstruction):
            ins.optimize()

    generator = OptimizedGenerator()
    #Agregamos al nuevo doc
    for ins in listaInstruccion:
        if isinstance(ins, OptimizedInstruction):
            ins.addToCode(generator)
            ins.toReport(generator)
        elif isinstance(ins, str):
            generator.addToCode(ins)

    generator.makeCode()
    generator.makeReport()

class OptimizedGenerator:
    """
    Clase encargada de generar codigo optimizado
    """
    def __init__(self) -> None:
        self.report = list()
        self.code = list()

    def addToCode(self, text):
        self.code.append(text+'\n')

    def toReport(self, text):
        self.report.append(text +'\n')

    def genCode(self) -> str:
        string = ''
        string+="from goto import with_goto\n"
        string+="from interpreter import execution\n"
        string+="from c3d.stack import Stack\n"
        for line in self.code:
            string += line

        return string

    def genReport(self) -> str:
        report = '<table><tr><th>Instrucción Optimizada</th><th>Regla</th><th>Linea</th></td>'
        for line in self.report:
            report += line
        report += '</table>'
        return report

    def makeCode(self):
        code = self.genCode()
        with open('codigoOptimizado.py','w') as file:
            file.write(code)
            file.close()

    def makeReport(self):
        report = self.genReport()
        with open('reporteOptimizado.html','w') as file:
            file.write(report)
            file.close()

optimizedCode('''
from goto import with_goto
from interpreter import execution
from c3d.stack import Stack

stack = Stack()
RETURN=[None]

@with_goto
def ptest():
	x =  0
	t0 = 4 * 4 
	t1 = 8 / 5
	t2 = t1 / 1
	t3 = t2 * 0
	t4 = t0 + t3
	x =  t4
	label .L0

@with_goto
def principal():
    pass


def funcionIntermedia():
	execution(stack.pop())
principal()
''')
