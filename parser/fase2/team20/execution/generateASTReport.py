import os
import webbrowser
import graphviz

from .AST.error import * 

import sys
sys.path.append("../")
from console import print_error

def graphAST(self):
        
    dot = "digraph ASTTytus{ \n rankdir = TD\n node[shape = \"box\"]\n"

    dotaux = ""
    try:
        if self.nodes != None:
            for node in self.nodes:
                dotaux += node.graphAST('','S')
    except Exception as e:
        print_error("AST Error",e,0)
        print(e)
        self.errors.append( Error("Unknown", "Wrong generated AST", 0, 0) )
        print_error("Unknown Error", "Wrong generated AST", 0)
        #print(e)

    if dotaux != "":
        dot += "S[label=\"S\"]\n"
        dot += dotaux

    dot += "\n }"

    #print(dot)
    
    return dot