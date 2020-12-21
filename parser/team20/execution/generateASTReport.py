import os
import webbrowser
import graphviz

from AST.error import * 

import sys
sys.path.append("../")
from console import print_error

def graphAST(self):
        
    dot = "digraph ASTTytus{ \n rankdir = TD\n node[shape = \"box\"]\n"
    dot += "S[label=\"S\"]\n"
        
    try:
        for node in self.nodes:
            dot += node.graphAST('','S')
        # archivodot = open("ast.dot", "w")
        # archivodot.write(dot)
        # archivodot.close()
        # cmd = 'dot \"' + 'ast.dot\" -o \"' +  "ast.pdf\" -Tpdf"
        # print("Comando DOT : " + cmd)
        # os.system(cmd)
        # webbrowser.open_new_tab('ast.pdf')
    except Exception as e:
        self.errors.append( Error("Unknown", "Wrong generated AST", 0, 0) )
        print_error("Unknown Error", "Wrong generated AST")
        #print(e)
        
    dot += "\n }"        
    #print(dot)

    return dot