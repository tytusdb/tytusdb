
from graphviz import Digraph
from graphviz import Source
import os
import webbrowser

class Nodo():

    c=0
    b=""
    root=0
    def __init__(self):
        self.c=0
    #def __init__(self,produccion,reglas,hijos):
        #self.produccion = produccion
        #self.reglas = reglas
        #self.hijos = hijos
    def start(self):  

       
        self.b  = """
        digraph G{
        edge [dir=forward]
        node [shape=plaintext]

        0 [label="Raiz"]
        
        """
        print(" nodo ea ",self.b )
        f = open ('AST.txt', "w")
        print("table: ")
        f.write(self.b)
        f.close()

        f = open ('var.txt', "w")        
        f.write("1")
        f.close()


    def agregar(self,node):
        f = open ('AST.txt', "a+")
        f.write(node)
        f.close()    

       
    def ending(self): 
      #  f = open("var.txt", "r")
      #  var=f.read()
     #   self.c=int(var)
      #  f.close()
      #self.b +=  """0-> """+str(self.c)
       # self.b +=  """ [label=""]  }"""


        self.b +=  """0->1 [label=""]  }"""

        f = open ('AST.txt', "a+")
        f.write(self.b)
        f.close()  


        f = open("AST.txt", "r")
        var=str(f.read())
        print(" nodo ea ",var )
        f = open ('AST.dot','w')
        f.write(var)
        f.close()


        os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz 2.44.1\bin'
           #os.system("dot -Tpng "+s+" -o AST.png")
          #os.system("C:/Graph/Graphviz2.44.1/bin/dot -c -Tpng AST.dot -o AST.ps")

        #os.system("C:/Graph/Graphviz2.44.1/bin/dot  -Tps AST.dot -o AST.ps")
        os.system("C:/Graph/Graphviz2.44.1/bin/dot  -Tpng  AST.dot -o AST.png")
    

        page = "<html>" + '\n' + "<head>" + '\n' + "<title>Grafo AST</title>" + '\n' + "</head>" + '\n'
        page = page + "<body>" + '\n' + "<center><Font size=16 >" + "Grafo AST" + "</Font></center>" + '\n'
        page = page + "<hr ><center>" + '\n'

      

        page = page +' <img src="AST.png" > '

        page = page + '\n' + "</center></body>" + '\n' + "</html>"

        f = open ('AST.html','w')
        f.write(page)
        f.close()
        webbrowser.open_new_tab('AST.html')




    def addencabezado(self,raiz,node):
        b =  ""
        try: 
                b +=  """ """+str(node)+"""
                [label="tipo:""" +raiz+""" "] """
              
        except:
                    pass

        f = open ('AST.txt', "a+")
        f.write(b)
        f.close()  


    def apuntar(self,raiz,hijo): 
        b =  ""
        try: 
              
                b +=  """ """+str(raiz)+""" -> """+str(hijo)
                b +=  """ [label=""] """
        except:
                    pass

        f = open ('AST.txt', "a+")
        f.write(b)
        f.close()  

      


    def append(self,tipo,valor): 

        f = open("var.txt", "r")
        var=f.read()
        c=int(var)
        f.close()


        print("graphiz bb")
       
        Raiz=c
        root=Raiz
        b =  """ """+str(c)+"""         
           [label="Primitivo"]"""
        print("112el944444")         

        c= c+1
        Left=str(c)
        print("112ello")          

        b +=  str(c)
        print("kkkk")          

        b +=  """   [label="Tipo:""" +str(tipo)+""" "] """
        print("zzzzccc ")          

        c= c+1
        Rigth=c
        b +=  """ """+str(c)+"""
         [label="Valor:""" +str(valor)+""" "] """
        b +=  """ """+str(Raiz)+"""-> """+Left
        b +=  """ [label=""] """
        print("11fffff")          

        b +=  """ """+str(Raiz)+"""-> """+str(Rigth)
        b +=  """ [label=""] """
        print("11vvvvvv")          

        f = open ('AST.txt', "a+")
        f.write(b)
        f.close()  
        c= c+1
        f = open ('var.txt', "w")        
        f.write(str(c))
        f.close()
        return root


    def graficar(self,entorno,tree):      

      

        self.contenido = "digraph G {\n"
        self.contenido += "node [style=filled];\n"
        self.contenido += "S->ni [color=\"0.002 0.782 0.999\"];\n"
        self.contenido += ""
        self.contenido += ""

       
        self.contenido += "S [color=\"0.449 0.447 1.000\"];\n"
        self.contenido += "ni [color=\"0.201 0.753 1.000\", label=\"Etiquetas\"];\n"
        self.contenido += "}"

       
        temp = """
        digraph G{
        edge [dir=forward]
        node [shape=plaintext]

        0 [label="0 (None)"]
        0 -> 5 [label="root"]
        1 [label="1 (Hello)"]
        2 [label="2 (how)"]
        2 -> 1 [label="advmod"]
        3 [label="3 (are)"]
        4 [label="4 (you)"]
        5 [label="5 (doing)"]
        5 -> 3 [label="aux"]
        5 -> 2 [label="advmod"]
        5 -> 4 [label="nsubj"]
        }
        """

        f = open ('AST.dot','w')
        f.write(temp)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz 2.44.1\bin'
           #os.system("dot -Tpng "+s+" -o AST.png")
          #os.system("C:/Graph/Graphviz2.44.1/bin/dot -c -Tpng AST.dot -o AST.ps")

        #os.system("C:/Graph/Graphviz2.44.1/bin/dot  -Tps AST.dot -o AST.ps")
        os.system("C:/Graph/Graphviz2.44.1/bin/dot  -Tpng  AST.dot -o AST.png")


       # os.system("DEL /F /A AST.dot")

        #f = open ('AST.dot','w')
       # f.write(self.contenido)
       # f.close()    