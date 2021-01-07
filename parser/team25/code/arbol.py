
from useDB.instanciaDB import DB_ACTUAL
from reporteErrores.errorReport import ErrorReport
from reporteErrores.instance import listaErrores , listaShowConsola
import os
from astSelect import matriz
path = 'data/Reportes/'

class Arbol:
    def __init__(self  , instrucciones):
        self.instrucciones = instrucciones
    
    def ejecutar(self):
        #es el primer ejecutar que se llama
        listaShowConsola.clear()
        ts = [] #por el momento , pero deberia de ser otro tipo de tabla de simbolos
        for instruccion in self.instrucciones:
            nodoSintetizado = instruccion.ejecutar(ts)
            #print(DB_ACTUAL.getName())
            if isinstance(nodoSintetizado , ErrorReport):
                listaErrores.addError(nodoSintetizado)
                print(nodoSintetizado.description)
            else:
                if isinstance( nodoSintetizado, matriz):
                    listaShowConsola.append(nodoSintetizado.getTablaToString()+'\n')
                    print("instruccion OK")# SUBIR ESTE ARCHIVOOOOOOOOOOOOOOOOOOOOOOOOO

    
    def dibujar(self)->str:# no se como se inicia a graficar :v 
        g = "digraph g {" +'\n'
        g+='style = filled;'+'\n'
        g+='bgcolor = black;'+'\n'
        g+='node[fillcolor = black , fontcolor = white ,style = filled , penwidth = 1.1 , color = gold1 , shape = invhouse];'+'\n'
        g+='edge[arrowhead = "empty" color = "white"];'+'\n'+'\n'+'\n'
        identificador = str(hash(self))
        g+=identificador + "[ label = \"Init\"];"
        
        for instruccion in self.instrucciones:
            g+= '\n' + identificador + "->" + str(hash(instruccion))
            g+= instruccion.dibujar()

        
        
        g+='\n'+"}"
        return g
    
    def reporteAst(self):
        archivo = open(path+'dot.txt' ,'w')# w es escritura, si no existe lo crea
        archivo.write(self.dibujar())
        archivo.close()
        os.system(f'dot -Tsvg data/Reportes/dot.txt -o data/Reportes/arbol.svg')
        os.system('cd data/Reportes & arbol.svg')
        # os.system(f'dot -Tpdf data/Reportes/dot.txt -o data/Reportes/arbol.pdf')
        # os.system('cd data/Reportes & arbol.pdf')