import os
import webbrowser
def graphAST(self):
        
        dot = "digraph ASTTytus{ \n rankdir = TD\n node[shape = \"box\"]\n"
        dot += "S[label=\"S\"]\n"
        for node in self.nodes:
            dot += node.graphAST('','S')
        dot += "\n }"
        try:
            archivodot = open("ast.dot", "w")
            archivodot.write(dot)
            archivodot.close()
            cmd = 'dot \"' + 'ast.dot\" -o \"' +  "ast.pdf\" -Tpdf"
            print("Comando DOT : " + cmd)
            os.system(cmd)
            webbrowser.open_new_tab('ast.pdf')
            #print(dot)
        except Exception as e:
            self.messagebox('Error reporte', str(e))