import os
import nodo as grammer
from subprocess import check_call

class graficaArbol():

    def __init__(self, listArbols):
        self.listArbol = listArbols


    def ejecutarGrafica(self):
        file = open("graficaArbol.txt", "w")
        encabezado = 'digraph lista{ rankdir=TB;node[shape = box, style = filled, color = white]; '
        file.write(encabezado+ os.linesep)
        contenido  =  self.recorrido(self.listArbol)
        file.write(contenido)
        file.write("}")
        file.close()

        check_call(['dot','-Tpng','graficaArbol.txt','-o','graficaArbol.png'])
    
    def recorrido(self, listaarbol):
        node = listaarbol
        var = node.id
        print(var)
        varid = id(node)
        #creamos el nodo
        var3 = 'nodo'+str(varid)+'[ label=\"'+var+'\"];'+ os.linesep
        for elementos in node.listDirecciones:
            var3 +=self.recorrido(elementos) + os.linesep
            varid2= id(elementos)
            var3 +='\"nodo'+str(varid)+'\"->\"nodo'+str(varid2)+'\"'+os.linesep

        return var3 

class graficaArbolDes():
    
    def _init_(self, listArbols):
        self.listArbol = listArbols


    def ejecutarGrafica(self):
        file = open("graficaArbolDes.txt", "w")
        encabezado = 'digraph lista{ rankdir=TB;node[shape = box, style = filled, color = white]; '
        file.write(encabezado+ os.linesep)
        contenido  =  self.recorrido(self.listArbol)
        file.write(contenido)
        file.write("}")
        file.close()

        check_call(['dot','-Tpng','graficaArbolDes.txt','-o','graficaArbolDes.png'])
    
    def recorrido(self, listaarbol):
        node = listaarbol
        var = node.id
        print(var)
        varid = id(node)
        #creamos el nodo
        var3 = 'nodo'+str(varid)+'[ label=\"'+var+'\"];'+ os.linesep
        for elementos in node.listDirecciones:
            var3 +=self.recorrido(elementos) + os.linesep
            varid2= id(elementos)
            var3 +='\"nodo'+str(varid)+'\"->\"nodo'+str(varid2)+'\"'+os.linesep

        return var3

        
class graficaGramatical():
    def __init__(self, listGramatical):
        self.listGramatical = listGramatical

    def ejecutarGrafica(self):
        file = open("graficaGramatical.txt", "w")        
        file.write('digraph G {'+ os.linesep)
        file.write('node [shape=plaintext]'+ os.linesep)
        file.write(' a [label=<<table border="0" cellborder="1" cellspacing="0">'+ os.linesep)
        file.write('<tr><td><b>\"Regla\"</b></td><td>\"Producciones\"</td></tr>'+os.linesep)
        for instus in self.listGramatical:
            col1 = instus.instruccion
            col2 =''
            for aux in instus.listDetalle:
                col2 +=aux +'<br/>'
            file.write('<tr><td><b>\"'+col1+'\"</b></td><td>\"'+col2+'\"</td></tr>' + os.linesep)

        file.write("</table>>];"+os.linesep)
        file.write("}")
        file.close()

        check_call(['dot','-Tpng','graficaGramatical.txt','-o','graficaGramatical.png'])

class graficaGramaticalbnf():
    def __init__(self, listGramatical):
        self.listGramatical = listGramatical

    def ejecutarGrafica(self):
        file = open("graficaGramaticalbnf.txt", "w")        
        file.write('digraph G {'+ os.linesep)
        file.write('node [shape=plaintext]'+ os.linesep)
        file.write(' a [label=<<table border="0" cellborder="1" cellspacing="0">'+ os.linesep)
        file.write('<tr><td><b>\"Regla\"</b></td><td>\"Producciones\"</td></tr>'+os.linesep)
        for instus in self.listGramatical:
            col1 = instus.instruccion
            col2 =''
            for aux in instus.listDetalle:
                col2 +=aux +'<br/>'
            file.write('<tr><td><b>\"'+col1+'\"</b></td><td>\"'+col2+'\"</td></tr>' + os.linesep)

        file.write("</table>>];"+os.linesep)
        file.write("}")
        file.close()

        check_call(['dot','-Tpng','graficaGramaticalbnf.txt','-o','graficaGramaticalbnf.png'])