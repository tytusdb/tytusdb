
import PLSQLParser as analisar
from InstruccionesPL.TablaSimbolosPL import ArbolPL as objArbol
from InstruccionesPL.TablaSimbolosPL import TablaPL as tb
from reportes.reportetabla import *
from InstruccionesPL import Optimizacion 

def ejecucionesPL():
    f = open("entrada.txt", "r")
    input = f.read()
    #print(input)
    Instrus = analisar.getParser(input) 
    initTraduccion = objArbol.ArbolPL(Instrus)
    print('Fin de analisis')
    #guardar lo traducido
    #guardar la lista de tripletas
    tablita = tb.TablaPL(None)
    result = ''
    for i in initTraduccion.getInstrucciones():
        result = i.ejecutar(tablita, initTraduccion)
      
    print(result)
    crear_tabla(initTraduccion)
ejecucionesPL()